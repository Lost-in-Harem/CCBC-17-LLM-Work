from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field

sys.dont_write_bytecode = True

from build_summary import (  # noqa: E402
    ROUNDS,
    collect_records,
    feeder_pool_round,
    parse_feeders,
    read_frontmatter,
)

USABLE_FEEDER_STATUSES = {"candidate", "accepted"}
ACTIONABLE_STATUSES = {"pending", "working", "rejected"}


@dataclass
class ResolvedDependencies:
    keys: list[str] = field(default_factory=list)
    issues: list[str] = field(default_factory=list)
    scope_unknown: bool = False


@dataclass
class MenuEntry:
    record: dict[str, str]
    notes: list[str] = field(default_factory=list)
    next_action: str = ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Print a read-only menu of Puzzle Hunt Nodes that are ready, "
            "awaiting verification, or waiting for dependencies."
        )
    )
    parser.add_argument(
        "--round",
        dest="round_id",
        help="Show only Nodes in one Round while still resolving cross-Round feeders.",
    )
    return parser.parse_args()


def record_key(record: dict[str, str]) -> str:
    return f"{record['round']}/{record['node_id']}"


def task_path(record: dict[str, str]) -> str:
    return f"{record['round']}/{record['directory']}"


def start_command(record: dict[str, str]) -> str:
    return (
        "$work-on-node "
        f"rounds/{record['round']}/nodes/{record['directory']}"
    )


def section_text(body: str, heading: str) -> str:
    if heading not in body:
        return ""
    remainder = body.split(heading, 1)[1].strip()
    if "\n## " in remainder:
        remainder = remainder.split("\n## ", 1)[0].strip()
    return " ".join(remainder.split())


def next_action(record: dict[str, str]) -> str:
    if record["status"] == "pending":
        return ""
    solution = (
        ROUNDS
        / record["round"]
        / "nodes"
        / record["directory"]
        / "solution.md"
    )
    if not solution.is_file():
        return ""
    try:
        _, body = read_frontmatter(solution)
    except (OSError, UnicodeError, ValueError):
        return ""
    return section_text(body, "## Next action")


def resolve_dependencies(
    record: dict[str, str],
    records_by_key: dict[str, dict[str, str]],
    round_ids: set[str],
) -> ResolvedDependencies:
    result = ResolvedDependencies()
    feeders = parse_feeders(record["feeders"])
    if feeders == ["unknown"]:
        result.scope_unknown = True
        return result

    own_key = record_key(record)
    seen: set[str] = set()
    for feeder in feeders:
        pool_round = feeder_pool_round(feeder, record["round"])
        if pool_round is not None:
            if pool_round not in round_ids:
                result.issues.append(
                    f"{feeder}: unknown Round"
                )
                continue
            keys = sorted(
                key
                for key, candidate in records_by_key.items()
                if candidate["round"] == pool_round
                and candidate["round_feeder"] == "yes"
                and key != own_key
            )
            if not keys:
                result.issues.append(
                    f"{feeder}: feeder pool is empty"
                )
                continue
        else:
            keys = [
                feeder
                if "/" in feeder
                else f"{record['round']}/{feeder}"
            ]

        for key in keys:
            if key in seen:
                continue
            seen.add(key)
            if key not in records_by_key:
                result.issues.append(f"{key}: Node is missing")
            else:
                result.keys.append(key)
    return result


def can_reach(
    start: str,
    destination: str,
    graph: dict[str, set[str]],
) -> bool:
    pending = [start]
    visited: set[str] = set()
    while pending:
        current = pending.pop()
        if current == destination:
            return True
        if current in visited:
            continue
        visited.add(current)
        pending.extend(graph.get(current, set()) - visited)
    return False


def compact(value: str, limit: int = 160) -> str:
    text = " ".join((value or "").split())
    if len(text) > limit:
        return text[: limit - 3] + "..."
    return text


def classify(
    records: list[dict[str, str]],
    round_ids: set[str],
    visible_round: str | None = None,
) -> tuple[list[MenuEntry], list[MenuEntry], list[MenuEntry], int]:
    records_by_key = {record_key(record): record for record in records}
    dependencies = {
        key: resolve_dependencies(record, records_by_key, round_ids)
        for key, record in records_by_key.items()
    }
    graph = {
        key: set(resolved.keys)
        for key, resolved in dependencies.items()
    }

    ready: list[MenuEntry] = []
    verify: list[MenuEntry] = []
    waiting: list[MenuEntry] = []
    accepted = 0

    for record in sorted(records, key=lambda item: task_path(item).casefold()):
        if visible_round and record["round"] != visible_round:
            continue
        status = record["status"]
        action = next_action(record)
        if status == "accepted":
            accepted += 1
            continue
        if status == "candidate":
            notes: list[str] = []
            if record["confidence"]:
                notes.append(f"confidence: {record['confidence']}")
            verify.append(MenuEntry(record, notes, action))
            continue
        if status == "blocked":
            notes = ["status is blocked"]
            if action:
                notes.append(f"next: {compact(action)}")
            waiting.append(MenuEntry(record, notes, action))
            continue

        resolved = dependencies[record_key(record)]
        blocking = list(resolved.issues)
        cycle_notes: list[str] = []
        tentative: list[str] = []
        for feeder_key in resolved.keys:
            feeder = records_by_key[feeder_key]
            feeder_status = feeder["status"]
            if feeder_status in USABLE_FEEDER_STATUSES:
                if feeder_status == "candidate":
                    confidence = feeder["confidence"] or "unknown confidence"
                    tentative.append(
                        f"{feeder_key} (candidate, {confidence})"
                    )
                continue
            if can_reach(feeder_key, record_key(record), graph):
                cycle_notes.append(
                    f"{feeder_key} ({feeder_status})"
                )
            else:
                blocking.append(
                    f"{feeder_key} ({feeder_status or 'invalid status'})"
                )

        notes = []
        if resolved.scope_unknown:
            notes.append(
                "feeder scope is unknown; determine it from this Node")
        if tentative:
            notes.append("tentative feeders: " + ", ".join(tentative))
        if cycle_notes:
            notes.append(
                "cyclic unresolved feeders are non-blocking: "
                + ", ".join(cycle_notes)
            )

        if status not in ACTIONABLE_STATUSES:
            blocking.append(f"unsupported task status {status!r}")
        if blocking:
            notes.insert(0, "waiting for: " + ", ".join(blocking))
            if action:
                notes.append(f"next: {compact(action)}")
            waiting.append(MenuEntry(record, notes, action))
        else:
            if action:
                notes.append(f"next: {compact(action)}")
            ready.append(MenuEntry(record, notes, action))

    return ready, verify, waiting, accepted


def print_entry(entry: MenuEntry, mode: str) -> None:
    record = entry.record
    label = task_path(record)
    title = compact(record["title"], 80) or label
    print(f"- {label} [{record['status']}] - {title}")
    if record["summary"]:
        print(f"  Summary: {compact(record['summary'])}")
    for note in entry.notes:
        print(f"  Note: {note}")
    if mode == "verify":
        print(
            "  Verify: open a fresh task with VERIFY_TASK_PROMPT.md for "
            f"rounds/{record['round']}/nodes/{record['directory']}"
        )
    elif mode == "ready":
        print(f"  Start: {start_command(record)}")


def print_group(title: str, entries: list[MenuEntry], mode: str) -> None:
    print(f"\n## {title} ({len(entries)})")
    if not entries:
        print("\n(none)")
        return
    print()
    for entry in entries:
        print_entry(entry, mode)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    args = parse_args()
    records, round_titles, errors, warnings = collect_records()
    if errors:
        print("Task menu validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 2

    if args.round_id:
        if args.round_id not in round_titles:
            print(f"Unknown Round: {args.round_id}", file=sys.stderr)
            return 2
    ready, verify, waiting, accepted = classify(
        records,
        set(round_titles),
        args.round_id,
    )
    print("# Puzzle Hunt task menu")
    if args.round_id:
        print(f"\nRound filter: {args.round_id}")
    print_group("Ready to work", ready, "ready")
    print_group("Candidates to verify", verify, "verify")
    print_group("Waiting or blocked", waiting, "waiting")
    print(f"\nAccepted Nodes hidden: {accepted}")

    visible_warnings = warnings
    if args.round_id:
        prefix = f"{args.round_id}/"
        visible_warnings = [
            warning for warning in warnings if warning.startswith(prefix)
        ]
    if visible_warnings:
        print(f"\n## Repository warnings ({len(visible_warnings)})")
        print()
        for warning in visible_warnings:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
