#!/usr/bin/env python3
"""Report Puzzle Hunt template structure and optional solving capabilities."""

from __future__ import annotations

import argparse
import importlib.metadata
import importlib.util
import json
import os
import shutil
import sys
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Check:
    group: str
    name: str
    available: bool
    required: bool
    detail: str


def package_check(
    import_name: str, distribution_name: str, purpose: str
) -> Check:
    available = importlib.util.find_spec(import_name) is not None
    version = ""
    if available:
        try:
            version = importlib.metadata.version(distribution_name)
        except importlib.metadata.PackageNotFoundError:
            version = "installed"
    detail = f"{version}; {purpose}" if version else purpose
    return Check("python", distribution_name, available, False, detail)


def command_check(name: str, purpose: str) -> Check:
    location = resolve_executable(name)
    return Check(
        "command",
        name,
        location is not None,
        False,
        f"{location}; {purpose}" if location else purpose,
    )


def resolve_executable(name: str) -> str | None:
    """Prefer a native executable when a Windows PATH shim is a batch file."""
    location = shutil.which(name)
    if location is None:
        return None
    path = Path(location)
    if sys.platform == "win32" and path.suffix.lower() in {".bat", ".cmd"}:
        executable_name = (
            name if name.lower().endswith(".exe") else f"{name}.exe"
        )
        for ancestor in list(path.parents)[:4]:
            native = ancestor / "native"
            if not native.is_dir():
                continue
            matches = sorted(
                native.rglob(executable_name),
                key=lambda candidate: (len(candidate.parts), str(candidate)),
            )
            if matches:
                return str(matches[0])
    return location


def file_check(relative: str) -> Check:
    path = ROOT / relative
    return Check(
        "repository",
        relative,
        path.is_file(),
        True,
        str(path),
    )


def directory_check(relative: str) -> Check:
    path = ROOT / relative
    return Check(
        "repository",
        relative,
        path.is_dir(),
        True,
        str(path),
    )


def collect_checks() -> list[Check]:
    checks = [
        Check(
            "runtime",
            "Python >= 3.10",
            sys.version_info >= (3, 10),
            True,
            sys.version.split()[0],
        ),
        Check(
            "runtime",
            "project writable",
            os.access(ROOT, os.W_OK),
            True,
            str(ROOT),
        ),
        file_check("AGENTS.md"),
        file_check("HUNT.md"),
        file_check("PUZZLE_TASK_PROMPT.md"),
        file_check("META_TASK_PROMPT.md"),
        file_check("VERIFY_TASK_PROMPT.md"),
        file_check("tools/new_puzzle.py"),
        file_check("tools/move_node.py"),
        file_check("tools/next_nodes.py"),
        file_check("tools/inspect_node.py"),
        file_check("tools/build_summary.py"),
        directory_check(".agents/skills/work-on-node"),
        directory_check(".agents/skills/inspect-puzzle-visuals"),
        file_check(
            ".agents/skills/inspect-puzzle-visuals/scripts/visual_workbench.py"
        ),
        package_check("PIL", "Pillow", "raster inventory and annotation"),
        package_check("z3", "z3-solver", "optional constraint models"),
        package_check("bs4", "beautifulsoup4",
                      "optional complex HTML analysis"),
        command_check("rg", "fast local text and file search"),
        command_check("tesseract", "OCR with boxes and confidence"),
        command_check("pdftoppm", "bounded PDF page rendering"),
        command_check("ffmpeg", "video frames, waveform, and spectrum"),
        command_check("ffprobe", "machine-readable media metadata"),
        command_check(
            "exiftool", "broad file and embedded metadata inspection"),
        command_check("magick", "optional image conversion and montage"),
    ]
    return checks


def available(checks: Iterable[Check], name: str) -> bool:
    return any(check.name == name and check.available for check in checks)


def capabilities(checks: list[Check]) -> dict[str, dict[str, object]]:
    pillow = available(checks, "Pillow")
    values = {
        "core_hunt_workflow": {
            "available": not any(
                check.required and not check.available for check in checks
            ),
            "requires": ["repository structure", "Python >= 3.10"],
        },
        "raster_inventory_crop_channels_annotation": {
            "available": pillow,
            "requires": ["Pillow"],
        },
        "ocr_with_coordinates": {
            "available": pillow and available(checks, "tesseract"),
            "requires": ["Pillow", "tesseract"],
        },
        "pdf_rendering": {
            "available": pillow and available(checks, "pdftoppm"),
            "requires": ["Pillow", "pdftoppm"],
        },
        "video_audio_rendering": {
            "available": (
                pillow
                and available(checks, "ffmpeg")
                and available(checks, "ffprobe")
            ),
            "requires": ["Pillow", "ffmpeg", "ffprobe"],
        },
        "optional_constraint_modeling": {
            "available": available(checks, "z3-solver"),
            "requires": ["z3-solver"],
        },
    }
    return values


def print_checks(checks: list[Check]) -> None:
    headers = ("state", "need", "group", "name", "detail")
    rows: list[tuple[str, str, str, str, str]] = []
    for check in checks:
        state = "OK" if check.available else (
            "FAIL" if check.required else "missing"
        )
        need = "required" if check.required else "optional"
        rows.append((state, need, check.group, check.name, check.detail))
    widths = [
        max(len(headers[index]), *(len(row[index]) for row in rows))
        for index in range(len(headers))
    ]
    print(
        "  ".join(
            header.ljust(widths[index])
            for index, header in enumerate(headers)
        )
    )
    print(
        "  ".join("-" * width for width in widths)
    )
    for row in rows:
        print(
            "  ".join(
                value.ljust(widths[index])
                for index, value in enumerate(row)
            )
        )


def print_capabilities(values: dict[str, dict[str, object]]) -> None:
    print("\nCapabilities")
    for name, value in values.items():
        state = "available" if value["available"] else "unavailable"
        requirements = ", ".join(value["requires"])  # type: ignore[arg-type]
        print(f"- {name}: {state} ({requirements})")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description=(
            "Inspect the template and optional local tools. This command "
            "does not install or modify anything."
        )
    )
    result.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON instead of a table.",
    )
    result.add_argument(
        "--strict",
        action="store_true",
        help="Return nonzero when any optional check is missing.",
    )
    return result


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = parser().parse_args()
    checks = collect_checks()
    capability_values = capabilities(checks)
    if args.json:
        print(
            json.dumps(
                {
                    "root": str(ROOT),
                    "checks": [asdict(check) for check in checks],
                    "capabilities": capability_values,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print_checks(checks)
        print_capabilities(capability_values)
        print("\nMissing optional tools do not break the core Hunt workflow.")
    if any(check.required and not check.available for check in checks):
        return 1
    if args.strict and any(not check.available for check in checks):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
