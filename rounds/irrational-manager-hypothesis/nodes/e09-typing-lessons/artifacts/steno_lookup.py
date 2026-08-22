"""Look up Plover outlines and render them as QWERTY keyboard chords.

Usage:
    python steno_lookup.py DICTIONARY WORD [WORD ...]
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path


QWERTY_KEY = {
    "S-": "a",
    "T-": "w",
    "K-": "s",
    "P-": "e",
    "W-": "d",
    "H-": "r",
    "R-": "f",
    "A": "c",
    "O": "v",
    "*": "g",
    "E": "n",
    "U": "m",
    "-F": "u",
    "-R": "j",
    "-P": "i",
    "-B": "k",
    "-L": "o",
    "-G": "l",
    "-T": "p",
    "-S": ";",
    "-D": "[",
    "-Z": "'",
}

LEFT_ORDER = "STKPWHR"
MID_ORDER = "AO*EU"
RIGHT_ORDER = "FRPBLGTSDZ"


def parse_stroke(stroke: str) -> list[str] | None:
    """Return canonical steno key names, or None for unsupported strokes."""
    if not stroke or any(ch not in "STKPWHRAO*EUFRPBLGTSDZ-" for ch in stroke):
        return None

    if "-" in stroke:
        if stroke.count("-") != 1:
            return None
        left_mid, right = stroke.split("-", 1)
        split_at = next((i for i, ch in enumerate(left_mid) if ch in MID_ORDER), len(left_mid))
        left = left_mid[:split_at]
        mid = left_mid[split_at:]
    else:
        split_at = next((i for i, ch in enumerate(stroke) if ch in MID_ORDER), None)
        if split_at is None:
            left, mid, right = stroke, "", ""
        else:
            left = stroke[:split_at]
            rest = stroke[split_at:]
            right_at = next((i for i, ch in enumerate(rest) if ch in RIGHT_ORDER), len(rest))
            mid, right = rest[:right_at], rest[right_at:]

    if (
        "".join(sorted(left, key=LEFT_ORDER.index)) != left
        or "".join(sorted(mid, key=MID_ORDER.index)) != mid
        or "".join(sorted(right, key=RIGHT_ORDER.index)) != right
    ):
        return None

    keys = [*(f"{ch}-" for ch in left), *mid, *(f"-{ch}" for ch in right)]
    if len(keys) != len(set(keys)) or any(key not in QWERTY_KEY for key in keys):
        return None
    return keys


def outline_to_chords(outline: str) -> list[str] | None:
    chords: list[str] = []
    for stroke in outline.split("/"):
        keys = parse_stroke(stroke)
        if keys is None:
            return None
        chords.append("".join(QWERTY_KEY[key] for key in keys))
    return chords


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__.strip(), file=sys.stderr)
        return 2

    dictionary_path = Path(sys.argv[1])
    targets = sys.argv[2:]
    dictionary = json.loads(dictionary_path.read_text(encoding="utf-8"))
    reverse: dict[str, list[tuple[str, list[str]]]] = defaultdict(list)
    for outline, translation in dictionary.items():
        if not isinstance(translation, str):
            continue
        chords = outline_to_chords(outline)
        if chords is not None:
            reverse[translation].append((outline, chords))

    for target in targets:
        entries = sorted(
            reverse.get(target, []),
            key=lambda item: (len(item[1]), sum(map(len, item[1])), item[0]),
        )
        print(f"{target}:")
        for outline, chords in entries[:12]:
            print(f"  {outline:<24} {' / '.join(chords)}")
        if not entries:
            print("  (no exact entry)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
