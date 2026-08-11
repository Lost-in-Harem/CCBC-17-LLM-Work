from __future__ import annotations

import argparse
import mimetypes
import os
import sys
import wave
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_summary import (
    ROOT,
    ROUNDS,
    collect_records,
    feeder_pool_round,
    parse_feeders,
    read_frontmatter,
)

sys.dont_write_bytecode = True


try:
    from PIL import Image
except ImportError:  # Optional dependency.
    Image = None

try:
    from pypdf import PdfReader
except ImportError:  # Optional dependency.
    PdfReader = None

MAX_LISTED_FILES = 80


class AssetReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        del tag
        for name, value in attrs:
            if not value:
                continue
            if name.lower() in {"src", "href", "poster", "data"}:
                self.references.append(value)
            elif name.lower() == "srcset":
                self.references.extend(
                    item.strip().split()[0]
                    for item in value.split(",")
                    if item.strip()
                )


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print a read-only context brief for one Puzzle Hunt Node."
    )
    parser.add_argument("node", type=node_reference, metavar="ROUND/NODE")
    parser.add_argument(
        "--all-files",
        action="store_true",
        help="List every input file instead of the first 80.",
    )
    return parser.parse_args()


def human_size(size: int) -> str:
    value = float(size)
    for unit in ("B", "KiB", "MiB", "GiB"):
        if value < 1024 or unit == "GiB":
            if unit == "B":
                return f"{int(value)} {unit}"
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} GiB"


def files_under(directory: Path) -> list[Path]:
    if not directory.is_dir():
        return []
    return sorted(
        (
            path
            for path in directory.rglob("*")
            if path.is_file() and path.name != ".gitkeep"
        ),
        key=lambda path: path.relative_to(directory).as_posix().lower(),
    )


def describe_file(path: Path) -> str:
    details = [human_size(path.stat().st_size)]
    mime_type, _ = mimetypes.guess_type(path.name)
    if mime_type:
        details.append(mime_type)

    if Image is not None and mime_type and mime_type.startswith("image/"):
        try:
            with Image.open(path) as image:
                details.append(f"{image.width}×{image.height}")
                frames = getattr(image, "n_frames", 1)
                if frames > 1:
                    details.append(f"{frames} frames")
        except (OSError, ValueError):
            details.append("image metadata unreadable")
    elif PdfReader is not None and path.suffix.lower() == ".pdf":
        try:
            details.append(f"{len(PdfReader(str(path)).pages)} pages")
        except Exception:  # pypdf uses several version-specific read errors.
            details.append("PDF metadata unreadable")
    elif path.suffix.lower() == ".wav":
        try:
            with wave.open(str(path), "rb") as audio:
                duration = audio.getnframes() / max(audio.getframerate(), 1)
                details.append(
                    f"{duration:.1f}s, {audio.getnchannels()} channel(s)"
                )
        except (EOFError, OSError, wave.Error):
            details.append("WAV metadata unreadable")

    return ", ".join(details)


def missing_html_assets(html_file: Path, input_root: Path) -> list[str]:
    try:
        text = html_file.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return [f"could not read {html_file.name}"]

    parser = AssetReferenceParser()
    parser.feed(text)
    missing: list[str] = []
    for reference in parser.references:
        parsed = urlsplit(reference.strip())
        if (
            parsed.scheme
            or parsed.netloc
            or not parsed.path
            or parsed.path.startswith("#")
        ):
            continue
        relative = Path(unquote(parsed.path).lstrip("/"))
        base = input_root if parsed.path.startswith("/") else html_file.parent
        candidate = base / relative
        if not candidate.exists():
            missing.append(
                f"{html_file.name} references missing local asset {reference!r}"
            )
    return missing


def section_text(body: str, heading: str) -> str:
    if heading not in body:
        return ""
    remainder = body.split(heading, 1)[1].strip()
    if "\n## " in remainder:
        remainder = remainder.split("\n## ", 1)[0].strip()
    return " ".join(remainder.split())


def record_key(record: dict[str, str]) -> str:
    return f"{record['round']}/{record['node_id']}"


def resolve_feeders(
    target: dict[str, str],
    records: list[dict[str, str]],
    round_titles: dict[str, str],
) -> tuple[list[dict[str, str]], list[str]]:
    target_key = record_key(target)
    record_keys = {record_key(record): record for record in records}
    feeders = parse_feeders(target["feeders"])
    if feeders == ["unknown"]:
        return [], ["feeder relationship is still unknown"]

    resolved: list[dict[str, str]] = []
    seen: set[str] = set()
    warnings: list[str] = []

    for feeder in feeders:
        pool_round = feeder_pool_round(feeder, target["round"])
        if pool_round is not None:
            if pool_round not in round_titles:
                warnings.append(
                    f"feeder pool {feeder!r} refers to an unknown Round"
                )
                continue
            keys = sorted(
                key
                for key, record in record_keys.items()
                if record["round"] == pool_round
                and record["round_feeder"] == "yes"
                and key != target_key
            )
            if not keys:
                warnings.append(
                    f"feeder pool {feeder!r} resolves to no Nodes"
                )
                continue
        else:
            keys = [
                feeder
                if "/" in feeder
                else f"{target['round']}/{feeder}"
            ]

        for key in keys:
            if key == target_key:
                warnings.append("Node may not feed itself")
            elif key in seen:
                warnings.append(f"duplicate resolved feeder {key!r}")
            elif key not in record_keys:
                warnings.append(f"feeder {feeder!r} has not been created")
            else:
                resolved.append(record_keys[key])
            seen.add(key)

    return resolved, warnings


def table_cell(value: str) -> str:
    compact = " ".join((value or "").split())
    return compact.replace("|", "&#124;") or "—"


def print_inventory(
    heading: str,
    directory: Path,
    warnings: list[str],
    all_files: bool,
) -> None:
    print(f"\n## {heading}")
    if not directory.exists():
        print(f"\nMissing: `{directory}`")
        warnings.append(f"{heading.lower()} directory is missing")
        return

    files = files_under(directory)
    if not files:
        print("\n(empty)")
        warnings.append(f"{heading.lower()} contains no files")
        return

    print()
    extension_counts = Counter(
        path.suffix.lower() or "[no extension]" for path in files
    )
    count_text = ", ".join(
        f"{extension}: {count}"
        for extension, count in sorted(extension_counts.items())
    )
    print(f"{len(files)} file(s) — {count_text}\n")

    displayed = files if all_files else files[:MAX_LISTED_FILES]
    for path in displayed:
        relative = path.relative_to(directory).as_posix()
        print(f"- `{relative}` — {describe_file(path)}")
    if len(displayed) < len(files):
        print(
            f"- … {len(files) - len(displayed)} more; "
            "rerun with `--all-files` to list them"
        )

    for html_file in (
        path for path in files if path.suffix.lower() in {".html", ".htm"}
    ):
        warnings.extend(missing_html_assets(html_file, directory))


def main() -> int:
    args = parse_args()
    requested_round, requested_node = args.node
    records, round_titles, errors, validation_warnings = collect_records()

    target = next(
        (
            record
            for record in records
            if record["round"] == requested_round
            and record["directory"] == requested_node
        ),
        None,
    )
    if target is None:
        print(
            f"Node not found: {requested_round}/{requested_node}",
            file=sys.stderr,
        )
        for message in errors:
            if message.startswith(f"{requested_round}/{requested_node}:"):
                print(f"- {message}", file=sys.stderr)
        return 2

    target_key = record_key(target)
    node_dir = ROUNDS / target["round"] / "nodes" / target["directory"]
    solution = node_dir / "solution.md"
    body = ""
    if solution.exists():
        try:
            _, body = read_frontmatter(solution)
        except (OSError, UnicodeError, ValueError):
            pass

    resolved, warnings = resolve_feeders(target, records, round_titles)
    relevant_keys = {target_key, *(record_key(record) for record in resolved)}
    relevant_errors = [
        message
        for message in errors
        if any(message.startswith(f"{key}:") for key in relevant_keys)
    ]
    warnings.extend(
        message
        for message in validation_warnings
        if any(message.startswith(f"{key}:") for key in relevant_keys)
    )

    if not (ROOT / "HUNT.md").exists():
        warnings.append("root HUNT.md is missing")

    print(f"# Node brief: `{target_key}`")
    print()
    print(f"- Title: {target['title'] or '—'}")
    print(f"- Kind: {target['kind'] or '—'}")
    print(f"- Status: {target['status'] or '—'}")
    print(f"- Answer: {target['answer'] or '—'}")
    print(f"- Confidence: {target['confidence'] or '—'}")
    print(f"- Round feeder: {target['round_feeder'] or '—'}")
    print(f"- Feeders: {target['feeders'] or '—'}")
    next_action = (
        section_text(body, "## Next action")
        if target["status"] != "pending"
        else ""
    )
    print(f"- Next action: {next_action or '—'}")

    print_inventory(
        "Own input",
        node_dir / "input",
        warnings,
        args.all_files,
    )

    if target["source"]:
        source_dir = (
            ROUNDS
            / target["round"]
            / "shared"
            / Path(target["source"].replace("/", os.sep))
        )
        print_inventory(
            "Declared shared source",
            source_dir,
            warnings,
            args.all_files,
        )

    print("\n## Resolved feeders")
    if not resolved:
        print("\n(none)")
    else:
        print()
        print(
            "| Node | Kind | Status | Answer | Confidence | Summary | Material |"
        )
        print("|---|---|---|---|---|---|---|")
        for feeder in resolved:
            feeder_dir = (
                ROUNDS
                / feeder["round"]
                / "nodes"
                / feeder["directory"]
            )
            input_count = len(files_under(feeder_dir / "input"))
            material = f"{input_count} input file(s)"
            if feeder["source"]:
                material += f"; shared/{feeder['source']}"
            values = (
                record_key(feeder),
                feeder["kind"],
                feeder["status"],
                feeder["answer"],
                feeder["confidence"],
                feeder["summary"],
                material,
            )
            print("| " + " | ".join(table_cell(value)
                  for value in values) + " |")

    all_messages: list[str] = []
    for message in [*relevant_errors, *warnings]:
        if message not in all_messages:
            all_messages.append(message)

    print("\n## Checks")
    if not all_messages:
        print("\nNo warnings.")
    else:
        print()
        for message in all_messages:
            print(f"- {message}")

    return 2 if relevant_errors else 0


if __name__ == "__main__":
    sys.exit(main())
