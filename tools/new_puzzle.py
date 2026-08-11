from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
ROUNDS = ROOT / "rounds"
TEMPLATE = ROUNDS / "_template" / "solution.md"


def safe_directory_name(value: str) -> str:
    candidate = value.strip()
    invalid_characters = '<>:"/\\|?*'
    if (
        not candidate
        or candidate in {".", ".."}
        or candidate.startswith("_")
        or candidate.endswith((".", " "))
        or Path(candidate).name != candidate
        or any(character in candidate for character in invalid_characters)
    ):
        raise argparse.ArgumentTypeError(
            "ID must be one safe directory name, may not start with _, "
            "and may not contain Windows-reserved characters"
        )
    return candidate


def safe_shared_source(value: str) -> str:
    candidate = value.strip().replace("\\", "/")
    if not candidate:
        return ""
    path = PurePosixPath(candidate)
    if path.is_absolute() or ".." in path.parts:
        raise argparse.ArgumentTypeError(
            "source must be a safe relative path under Round shared/"
        )
    return candidate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create one Round-scoped Puzzle Hunt Node."
    )
    parser.add_argument("node_id", type=safe_directory_name)
    parser.add_argument(
        "--round",
        "-r",
        dest="round_id",
        type=safe_directory_name,
        default="unassigned",
    )
    parser.add_argument("--title", "-t", default="")
    parser.add_argument("--round-title", default="")
    parser.add_argument(
        "--kind",
        "-k",
        choices=("puzzle", "subpuzzle", "meta"),
        default="puzzle",
    )
    parser.add_argument("--parent", default="")
    parser.add_argument("--source", type=safe_shared_source, default="")
    parser.add_argument(
        "--round-feeder",
        choices=("yes", "no"),
        default=None,
        help="Whether this Node belongs to the Round's default feeder pool.",
    )
    parser.add_argument(
        "--feeders",
        "-f",
        nargs="*",
        default=None,
        help=(
            "Feeder Node IDs or [round/]all-round-feeders; "
            "use round/id for cross-Round references."
        ),
    )
    return parser.parse_args()


def create_round(round_id: str, round_title: str) -> Path:
    round_dir = ROUNDS / round_id
    (round_dir / "nodes").mkdir(parents=True, exist_ok=True)
    (round_dir / "shared").mkdir(parents=True, exist_ok=True)

    round_file = round_dir / "ROUND.md"
    if not round_file.exists():
        title = round_title.strip() or round_id
        text = (
            "---\n"
            f"round_id: {round_id}\n"
            f"title: {title}\n"
            "---\n\n"
            f"# {title}\n\n"
            "记录这个 Round 的主题、解锁条件或简短说明。\n"
        )
        try:
            with round_file.open("x", encoding="utf-8", newline="\n") as stream:
                stream.write(text)
        except FileExistsError:
            pass
    return round_dir


def main() -> int:
    args = parse_args()
    if not TEMPLATE.exists():
        print(f"Missing template: {TEMPLATE}", file=sys.stderr)
        return 2
    if args.kind == "subpuzzle" and not args.parent.strip():
        print("Subpuzzles require --parent.", file=sys.stderr)
        return 2

    round_dir = create_round(args.round_id, args.round_title)
    target = round_dir / "nodes" / args.node_id
    if target.exists():
        print(
            f"Refusing to overwrite existing directory: {target}",
            file=sys.stderr,
        )
        return 2

    feeders = args.feeders
    if args.kind == "meta" and not feeders:
        feeders = ["unknown"]
    feeder_text = ", ".join(feeders or [])
    round_feeder = args.round_feeder
    if round_feeder is None:
        round_feeder = "no" if args.kind == "meta" else "yes"

    title = args.title.strip() or args.node_id
    text = TEMPLATE.read_text(encoding="utf-8")
    replacements = {
        "<NODE_ID>": args.node_id,
        "<NODE_TITLE>": title,
        "<KIND>": args.kind,
        "<ROUND_ID>": args.round_id,
        "<PARENT>": args.parent.strip(),
        "<SOURCE>": args.source,
        "<ROUND_FEEDER>": round_feeder,
        "<FEEDERS>": feeder_text,
    }
    for placeholder, value in replacements.items():
        text = text.replace(placeholder, value)

    temporary = target.parent / f".{args.node_id}.creating.{os.getpid()}"
    try:
        for name in ("input", "work", "artifacts"):
            directory = temporary / name
            directory.mkdir(parents=True, exist_ok=False)
            (directory / ".gitkeep").touch()
        (temporary / "solution.md").write_text(
            text,
            encoding="utf-8",
            newline="\n",
        )
        os.replace(temporary, target)
    except Exception:
        if temporary.exists():
            shutil.rmtree(temporary)
        raise

    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "build_summary.py")],
        cwd=ROOT,
        check=False,
    )
    if result.returncode:
        return result.returncode

    print(f"Created {target}")
    print(f"Put Node-specific puzzle files in {target / 'input'}")
    if args.source:
        print(
            f"Put shared source files in {round_dir / 'shared' / args.source}")
    print(
        "Inspect with: "
        f"python tools/inspect_node.py {args.round_id}/{args.node_id}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
