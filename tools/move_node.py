from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

sys.dont_write_bytecode = True

from build_summary import (  # noqa: E402
    ROOT,
    ROUNDS,
    collect_records,
    feeder_pool_round,
    parse_feeders,
    read_frontmatter,
)

LOCK = ROOT / ".move-node.lock"


class MoveError(RuntimeError):
    """A safe, user-facing move failure."""


@dataclass
class DocumentChange:
    original_path: Path
    final_path: Path
    original_text: str
    new_text: str
    label: str


@dataclass
class MovePlan:
    source_dir: Path
    destination_dir: Path
    source_record: dict[str, str]
    destination_round: str
    destination_id: str
    changes: list[DocumentChange]
    feeder_changes: list[tuple[str, str, str]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    body_mentions: list[str] = field(default_factory=list)


def safe_component(value: str) -> bool:
    invalid_characters = '<>:"/\\|?*'
    return (
        bool(value)
        and value not in {".", ".."}
        and not value.startswith("_")
        and not value.endswith((".", " "))
        and Path(value).name == value
        and not any(character in value for character in invalid_characters)
    )


def node_reference(value: str) -> tuple[str, str]:
    normalized = value.strip().replace("\\", "/")
    parts = normalized.split("/")
    if len(parts) != 2 or not all(safe_component(part) for part in parts):
        raise argparse.ArgumentTypeError(
            "Node must be written as one safe round/node path"
        )
    return parts[0], parts[1]


def shared_source(value: str) -> str:
    candidate = value.strip().replace("\\", "/")
    path = PurePosixPath(candidate)
    if (
        not candidate
        or path.is_absolute()
        or ".." in path.parts
    ):
        raise argparse.ArgumentTypeError(
            "source must be a non-empty safe relative path under Round shared/"
        )
    return candidate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Safely move or rename one Node, update structured feeder "
            "references, and rebuild SUMMARY.md."
        )
    )
    parser.add_argument("source", type=node_reference, metavar="ROUND/NODE")
    parser.add_argument(
        "destination",
        type=node_reference,
        metavar="ROUND/NODE",
    )
    source_group = parser.add_mutually_exclusive_group()
    source_group.add_argument(
        "--new-source",
        type=shared_source,
        help=(
            "Bind the moved Node to this shared source in the destination "
            "Round. The directory must already exist."
        ),
    )
    source_group.add_argument(
        "--clear-source",
        action="store_true",
        help="Clear the moved Node's shared source.",
    )
    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the complete plan without changing files.",
    )
    action_group.add_argument(
        "--yes",
        action="store_true",
        help="Apply the displayed plan without the interactive confirmation.",
    )
    return parser.parse_args()


def record_key(record: dict[str, str]) -> str:
    return f"{record['round']}/{record['node_id']}"


def record_path(record: dict[str, str]) -> str:
    return f"{record['round']}/{record['directory']}"


def solution_path(record: dict[str, str]) -> Path:
    return (
        ROUNDS
        / record["round"]
        / "nodes"
        / record["directory"]
        / "solution.md"
    )


def ensure_within(path: Path, parent: Path, label: str) -> None:
    try:
        path.resolve().relative_to(parent.resolve())
    except ValueError as error:
        raise MoveError(f"{label} escapes the repository: {path}") from error


def update_frontmatter(text: str, updates: dict[str, str]) -> str:
    newline = "\r\n" if "\r\n" in text else "\n"
    final_newline = text.endswith(("\n", "\r"))
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise MoveError(
            "solution.md is missing its opening frontmatter delimiter")

    closing_index: int | None = None
    found: set[str] = set()
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break
        key, separator, _ = line.partition(":")
        normalized = key.strip().lower()
        if separator and normalized in updates:
            if normalized in found:
                raise MoveError(
                    f"solution.md contains duplicate {normalized!r} fields"
                )
            found.add(normalized)
            original_key = key.strip() or normalized
            value = updates[normalized]
            lines[index] = (
                f"{original_key}: {value}" if value else f"{original_key}:"
            )

    if closing_index is None:
        raise MoveError(
            "solution.md is missing its closing frontmatter delimiter")
    for key, value in updates.items():
        if key in found:
            continue
        line = f"{key}: {value}" if value else f"{key}:"
        lines.insert(closing_index, line)
        closing_index += 1

    result = newline.join(lines)
    if final_newline:
        result += newline
    return result


def direct_feeder_key(token: str, current_round: str) -> str | None:
    if token == "unknown" or feeder_pool_round(token, current_round) is not None:
        return None
    if "/" in token:
        return token
    return f"{current_round}/{token}"


def rewrite_feeders(
    record: dict[str, str],
    *,
    moved_record: dict[str, str],
    destination_round: str,
    destination_id: str,
) -> list[str]:
    tokens = parse_feeders(record["feeders"])
    old_round = moved_record["round"]
    old_key = record_key(moved_record)
    is_moved = record is moved_record
    rewritten: list[str] = []

    for original in tokens:
        token = original
        if is_moved and old_round != destination_round:
            if token == "all-round-feeders":
                token = f"{old_round}/all-round-feeders"
            elif token != "unknown" and "/" not in token:
                token = f"{old_round}/{token}"

        if not is_moved and direct_feeder_key(
            token, record["round"]
        ) == old_key:
            if "/" not in token and record["round"] == destination_round:
                token = destination_id
            else:
                token = f"{destination_round}/{destination_id}"
        rewritten.append(token)
    return rewritten


def validate_virtual_records(
    records: list[dict[str, str]],
    round_ids: set[str],
) -> list[str]:
    errors: list[str] = []
    records_by_key: dict[str, dict[str, str]] = {}
    for record in records:
        key = record_key(record)
        if key in records_by_key:
            errors.append(f"duplicate proposed Node key {key!r}")
        records_by_key[key] = record

    for record in records:
        own_key = record_key(record)
        feeders = parse_feeders(record["feeders"])
        if feeders == ["unknown"] or not feeders:
            continue
        seen: set[str] = set()
        for feeder in feeders:
            pool_round = feeder_pool_round(feeder, record["round"])
            if pool_round is not None:
                if pool_round not in round_ids:
                    continue
                keys = sorted(
                    key
                    for key, candidate in records_by_key.items()
                    if candidate["round"] == pool_round
                    and candidate["round_feeder"] == "yes"
                    and key != own_key
                )
            else:
                key = direct_feeder_key(feeder, record["round"])
                keys = [key] if key is not None else []

            for key in keys:
                if key == own_key:
                    errors.append(
                        f"{own_key}: proposed feeder refers to itself")
                elif key in seen:
                    errors.append(
                        f"{own_key}: proposed move creates duplicate feeder "
                        f"{key!r}"
                    )
                seen.add(key)
    return errors


def find_body_mentions(
    records: list[dict[str, str]],
    old_key: str,
    old_directory_path: str,
) -> list[str]:
    mentions: list[str] = []
    for record in records:
        path = solution_path(record)
        if not path.is_file():
            continue
        try:
            _, body = read_frontmatter(path)
        except (OSError, UnicodeError, ValueError):
            continue
        if old_key in body or old_directory_path in body:
            mentions.append(record_path(record))
    return sorted(mentions, key=str.casefold)


def pool_consumers(
    records: list[dict[str, str]],
    pool_round: str,
    moved_record: dict[str, str],
) -> list[str]:
    result: list[str] = []
    for record in records:
        if record is moved_record:
            continue
        if any(
            feeder_pool_round(token, record["round"]) == pool_round
            for token in parse_feeders(record["feeders"])
        ):
            result.append(record_path(record))
    return sorted(result, key=str.casefold)


def destination_references(
    records: list[dict[str, str]],
    destination_key: str,
    moved_record: dict[str, str],
) -> list[str]:
    result: list[str] = []
    for record in records:
        if record is moved_record:
            continue
        if any(
            direct_feeder_key(token, record["round"]) == destination_key
            for token in parse_feeders(record["feeders"])
        ):
            result.append(record_path(record))
    return sorted(result, key=str.casefold)


def make_plan(args: argparse.Namespace) -> MovePlan:
    records, round_titles, errors, _ = collect_records()
    if errors:
        details = "\n".join(f"- {error}" for error in errors)
        raise MoveError(
            "The repository has validation errors; fix them before moving:\n"
            + details
        )

    source_round, source_directory = args.source
    destination_round, destination_id = args.destination
    moved_record = next(
        (
            record
            for record in records
            if record["round"] == source_round
            and record["directory"] == source_directory
        ),
        None,
    )
    if moved_record is None:
        raise MoveError(
            f"Source Node not found: {source_round}/{source_directory}")
    if destination_round not in round_titles:
        raise MoveError(
            f"Destination Round does not exist: {destination_round}"
        )

    source_dir = ROUNDS / source_round / "nodes" / source_directory
    destination_parent = ROUNDS / destination_round / "nodes"
    destination_dir = destination_parent / destination_id
    ensure_within(source_dir, ROUNDS, "Source")
    ensure_within(destination_parent, ROUNDS, "Destination parent")
    if not source_dir.is_dir():
        raise MoveError(f"Source directory does not exist: {source_dir}")
    if not destination_parent.is_dir():
        raise MoveError(
            f"Destination Round has no nodes directory: {destination_parent}"
        )
    if destination_dir.exists():
        raise MoveError(f"Destination already exists: {destination_dir}")
    if source_dir.resolve() == destination_dir.resolve():
        raise MoveError("Source and destination are the same")

    source_solution = source_dir / "solution.md"
    if not source_solution.is_file():
        raise MoveError(f"Source Node has no solution.md: {source_solution}")

    old_key = record_key(moved_record)
    destination_key = f"{destination_round}/{destination_id}"
    if any(
        record_key(record) == destination_key
        for record in records
        if record is not moved_record
    ):
        raise MoveError(
            f"Another Node already uses destination key {destination_key!r}"
        )

    current_source = moved_record["source"]
    new_source = current_source
    if args.clear_source:
        new_source = ""
    elif args.new_source is not None:
        new_source = args.new_source
    elif source_round != destination_round and current_source:
        raise MoveError(
            f"{old_key} declares shared source {current_source!r}. "
            "For a cross-Round move, pass --new-source SOURCE after creating "
            "the destination shared directory, or pass --clear-source."
        )
    if new_source:
        shared_dir = (
            ROUNDS
            / destination_round
            / "shared"
            / Path(new_source.replace("/", os.sep))
        )
        ensure_within(shared_dir, ROUNDS / destination_round / "shared",
                      "Shared source")
        if not shared_dir.is_dir():
            raise MoveError(
                f"Destination shared source does not exist: {shared_dir}"
            )

    proposed_records: list[dict[str, str]] = []
    rewritten_by_identity: dict[int, str] = {}
    feeder_changes: list[tuple[str, str, str]] = []
    for record in records:
        rewritten = rewrite_feeders(
            record,
            moved_record=moved_record,
            destination_round=destination_round,
            destination_id=destination_id,
        )
        feeder_text = ", ".join(rewritten)
        rewritten_by_identity[id(record)] = feeder_text
        if feeder_text != record["feeders"]:
            feeder_changes.append(
                (record_path(record), record["feeders"], feeder_text)
            )

        proposed = dict(record)
        proposed["feeders"] = feeder_text
        if record is moved_record:
            proposed["round"] = destination_round
            proposed["node_id"] = destination_id
            proposed["directory"] = destination_id
            proposed["source"] = new_source
            proposed["round_title"] = round_titles[destination_round]
        proposed_records.append(proposed)

    virtual_errors = validate_virtual_records(
        proposed_records, set(round_titles)
    )
    if virtual_errors:
        details = "\n".join(f"- {error}" for error in virtual_errors)
        raise MoveError(
            "The proposed move would create invalid feeder relationships:\n"
            + details
        )

    changes: list[DocumentChange] = []
    for record in records:
        updates: dict[str, str] = {}
        if record is moved_record:
            updates.update(
                {
                    "node_id": destination_id,
                    "round": destination_round,
                    "source": new_source,
                }
            )
        new_feeders = rewritten_by_identity[id(record)]
        if new_feeders != record["feeders"]:
            updates["feeders"] = new_feeders
        if not updates:
            continue

        original_path = solution_path(record)
        original_text = original_path.read_text(encoding="utf-8-sig")
        new_text = update_frontmatter(original_text, updates)
        final_path = (
            destination_dir / "solution.md"
            if record is moved_record
            else original_path
        )
        changes.append(
            DocumentChange(
                original_path,
                final_path,
                original_text,
                new_text,
                record_path(record),
            )
        )

    warnings: list[str] = []
    if source_round != destination_round and moved_record["parent"]:
        warnings.append(
            f"parent remains {moved_record['parent']!r}; verify that this "
            "Round-local relationship still makes sense"
        )
    if source_round != destination_round and moved_record["round_feeder"] == "yes":
        old_consumers = pool_consumers(records, source_round, moved_record)
        new_consumers = pool_consumers(
            records, destination_round, moved_record)
        old_text = ", ".join(old_consumers) if old_consumers else "none"
        new_text = ", ".join(new_consumers) if new_consumers else "none"
        warnings.append(
            f"{old_key} leaves the {source_round!r} feeder pool; consumers: "
            f"{old_text}"
        )
        warnings.append(
            f"{destination_key} enters the {destination_round!r} feeder pool; "
            f"consumers: {new_text}"
        )

    future_references = destination_references(
        records, destination_key, moved_record
    )
    if future_references:
        warnings.append(
            "existing references to the previously missing destination key "
            f"will become active in: {', '.join(future_references)}"
        )

    old_directory_path = (
        f"rounds/{source_round}/nodes/{source_directory}"
    )
    body_mentions = find_body_mentions(
        records, old_key, old_directory_path
    )
    return MovePlan(
        source_dir=source_dir,
        destination_dir=destination_dir,
        source_record=moved_record,
        destination_round=destination_round,
        destination_id=destination_id,
        changes=changes,
        feeder_changes=feeder_changes,
        warnings=warnings,
        body_mentions=body_mentions,
    )


def print_plan(plan: MovePlan) -> None:
    source = record_path(plan.source_record)
    destination = f"{plan.destination_round}/{plan.destination_id}"
    print("# Node move plan")
    print(f"\n- Move: {source} -> {destination}")
    print(f"- Directory: {plan.source_dir} -> {plan.destination_dir}")
    print(f"- solution.md files changed: {len(plan.changes)}")

    print(f"\n## Structured feeder rewrites ({len(plan.feeder_changes)})")
    if not plan.feeder_changes:
        print("\n(none)")
    else:
        print()
        for label, before, after in plan.feeder_changes:
            print(f"- {label}: {before or '(empty)'} -> {after or '(empty)'}")

    print(f"\n## Warnings ({len(plan.warnings)})")
    if not plan.warnings:
        print("\n(none)")
    else:
        print()
        for warning in plan.warnings:
            print(f"- {warning}")

    print(
        "\n## Unstructured solution-body mentions "
        f"({len(plan.body_mentions)})"
    )
    if not plan.body_mentions:
        print("\n(none)")
    else:
        print()
        for label in plan.body_mentions:
            print(f"- {label}")
        print(
            "\nThese prose mentions are not modified automatically; review "
            "them after the move."
        )
    print(
        "\nStop any Agent currently writing the moved Node or the listed "
        "consumer Nodes before applying this plan."
    )


def write_atomic(path: Path, text: str) -> None:
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            prefix=f".{path.name}.move.",
            suffix=".tmp",
            dir=path.parent,
            delete=False,
        ) as stream:
            stream.write(text)
            temporary_name = stream.name
        os.replace(temporary_name, path)
        temporary_name = None
    finally:
        if temporary_name:
            try:
                Path(temporary_name).unlink()
            except FileNotFoundError:
                pass


def acquire_lock() -> None:
    try:
        descriptor = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as error:
        raise MoveError(
            f"Move lock already exists: {LOCK}. Verify no move is active "
            "before removing a stale lock."
        ) from error
    with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
        stream.write(f"{os.getpid()}\n")


def release_lock() -> None:
    try:
        LOCK.unlink()
    except FileNotFoundError:
        pass


def run_summary() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / "tools" / "build_summary.py")],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def verify_unchanged(plan: MovePlan) -> None:
    if not plan.source_dir.is_dir():
        raise MoveError("Source directory changed after the plan was created")
    if plan.destination_dir.exists():
        raise MoveError("Destination appeared after the plan was created")
    for change in plan.changes:
        try:
            current = change.original_path.read_text(encoding="utf-8-sig")
        except OSError as error:
            raise MoveError(
                f"Could not re-read {change.original_path}: {error}"
            ) from error
        if current != change.original_text:
            raise MoveError(
                f"{change.original_path} changed after the plan was created"
            )


def rollback(plan: MovePlan, moved: bool) -> list[str]:
    errors: list[str] = []
    if moved:
        for change in plan.changes:
            try:
                write_atomic(change.final_path, change.original_text)
            except OSError as error:
                errors.append(f"restore {change.final_path}: {error}")
        try:
            if plan.source_dir.exists():
                errors.append(
                    f"original path was recreated: {plan.source_dir}"
                )
            else:
                plan.destination_dir.rename(plan.source_dir)
        except OSError as error:
            errors.append(f"restore directory: {error}")
    summary = run_summary()
    if summary.returncode:
        errors.append(
            "restore SUMMARY.md: "
            + (summary.stderr.strip() or summary.stdout.strip())
        )
    return errors


def apply_plan(plan: MovePlan) -> None:
    acquire_lock()
    moved = False
    try:
        verify_unchanged(plan)
        try:
            plan.source_dir.rename(plan.destination_dir)
            moved = True
            for change in plan.changes:
                write_atomic(change.final_path, change.new_text)
            summary = run_summary()
            if summary.returncode:
                details = summary.stderr.strip() or summary.stdout.strip()
                raise MoveError(
                    "Summary validation failed after the move:\n" + details
                )
        except Exception as error:
            rollback_errors = rollback(plan, moved)
            if rollback_errors:
                details = "\n".join(f"- {item}" for item in rollback_errors)
                raise MoveError(
                    f"Move failed: {error}\nRollback also had errors:\n"
                    + details
                ) from error
            raise MoveError(
                f"Move failed and was rolled back: {error}") from error

        if summary.stdout.strip():
            print(summary.stdout.strip())
        if summary.stderr.strip():
            print(summary.stderr.strip(), file=sys.stderr)
    finally:
        release_lock()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    args = parse_args()
    try:
        plan = make_plan(args)
        print_plan(plan)
        if args.dry_run:
            print("\nDry run only; no files changed.")
            return 0
        if not args.yes:
            try:
                response = input("\nType MOVE to apply this plan: ")
            except EOFError:
                response = ""
            if response.strip() != "MOVE":
                print("Cancelled; no files changed.")
                return 1
        apply_plan(plan)
    except (MoveError, OSError, UnicodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    destination = f"{plan.destination_round}/{plan.destination_id}"
    print(f"Moved Node to {plan.destination_dir}")
    print(
        "Start with: "
        f"$work-on-node rounds/{plan.destination_round}/nodes/"
        f"{plan.destination_id}"
    )
    print(f"Inspect with: python tools/inspect_node.py {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
