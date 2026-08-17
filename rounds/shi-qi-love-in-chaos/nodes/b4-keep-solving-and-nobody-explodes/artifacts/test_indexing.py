"""Audit name and commutative-operation hypotheses without choosing an answer.

The recording fixes the blue digits as an unordered pair (9, 6) and the
purple index as 4.  The other five indices are intentionally left unknown in
this audit.  Run from the repository root, or pass a word-list path with
``--words``.  The output is evidence about ambiguity, not a submission.
"""

from __future__ import annotations

import argparse
import itertools
import math
import re
from pathlib import Path


BLUE_DIGITS = (9, 6)
PURPLE_INDEX = 4


def normalize(value: str) -> str:
    return re.sub(r"[^A-Z]", "", value.upper())


def operations() -> dict[str, int]:
    left, right = BLUE_DIGITS
    return {
        "sum": left + right,
        "absdiff": abs(left - right),
        "gcd": math.gcd(left, right),
        "min": min(left, right),
        "max": max(left, right),
    }


# These are deliberately explicit competing interpretations.  They are not
# silently selected by the target output.
FAMILIES: dict[str, tuple[tuple[tuple[str, str], ...], ...]] = {
    "short-anchor": (
        (("MAUSOLUS", "ruler linked to the Mausoleum"),),
        (("BABYLON", "city linked to the Hanging Gardens"),),
        (
            ("PHAROS", "lighthouse/harbor anchor"),
            ("ALEXANDRIA", "harbor/city anchor"),
            ("LIGHTHOUSE", "lighthouse anchor"),
        ),
        (("SPHINX", "blue flying Magic creature type"),),
        (("ZEUS", "O2 trophy winner"),),
        (
            ("COLOSSUS", "large tracked game vehicle"),
            ("MORDEN'S BATTLESHIP", "Metal Slug land battleship"),
            ("COCOON", "Peace Walker AI weapon"),
        ),
        (
            ("ARTEMIS", "hunt-goddess anchor"),
            ("TEMPLAR ASSASSIN", "old Dota hero candidate"),
            ("MEDUSA", "old Dota hero candidate"),
        ),
    ),
    "formal-wonder": (
        (("MAUSOLEUM AT HALICARNASSUS", "formal wonder name"),),
        (("HANGING GARDENS OF BABYLON", "formal wonder name"),),
        (("LIGHTHOUSE OF ALEXANDRIA", "formal wonder name"),),
        (("GREAT PYRAMID OF GIZA", "formal wonder name"),),
        (("STATUE OF ZEUS AT OLYMPIA", "formal wonder name"),),
        (("COLOSSUS OF RHODES", "formal wonder name"),),
        (("TEMPLE OF ARTEMIS AT EPHESUS", "formal wonder name"),),
    ),
}


def positions_for(label: str, wanted: str) -> list[int]:
    text = normalize(label)
    return [index for index, char in enumerate(text, 1) if char == wanted]


def load_words(path: Path | None) -> set[str]:
    if path is None or not path.exists():
        return set()
    return {
        line.strip().upper()
        for line in path.read_text(encoding="utf-8").splitlines()
        if re.fullmatch(r"[A-Za-z]{4}", line.strip())
    }


def suffix_words(
    rows: tuple[tuple[tuple[str, str], ...], ...],
    blue_index: int,
    words: set[str],
) -> tuple[list[str], list[str]]:
    if not words:
        return [], []
    green, cyan, _blue, purple = rows[3:7]
    blue_letters = {
        normalize(label)[blue_index - 1]
        for label, _ in _blue
        if len(normalize(label)) >= blue_index
    }
    purple_letters = {
        normalize(label)[PURPLE_INDEX - 1]
        for label, _ in purple
        if len(normalize(label)) >= PURPLE_INDEX
    }
    if not blue_letters or not purple_letters:
        return [], []
    allowed = [
        {
            normalize(label)[index - 1]
            for label, _ in green
            for index in range(1, min(9, len(normalize(label))) + 1)
        },
        {
            normalize(label)[index - 1]
            for label, _ in cyan
            for index in range(1, min(9, len(normalize(label))) + 1)
        },
        blue_letters,
        purple_letters,
    ]
    matches = sorted(
        word
        for word in words
        if all(char in choices for char, choices in zip(word, allowed, strict=True))
    )
    witnesses: list[str] = []
    for word in matches[:12]:
        witnesses.append(word)
    return matches, witnesses


def prefix_ans(rows: tuple[tuple[tuple[str, str], ...], ...]) -> list[str]:
    wanted = "ANS"
    choices: list[list[tuple[str, int]]] = []
    for row, char in zip(rows[:3], wanted, strict=True):
        row_choices = []
        for label, _ in row:
            for index in positions_for(label, char):
                row_choices.append((label, index))
        choices.append(row_choices)
    return [
        ";".join(f"{label}[{index}]" for label, index in combo)
        for combo in itertools.product(*choices)
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--words", type=Path, help="optional four-letter word list")
    args = parser.parse_args()
    words = load_words(args.words)

    print("family\toperation\tblue-index\tblue-letters\tANS-prefix-witnesses\tsuffix-word-count\tsuffix-word-samples")
    for family, rows in FAMILIES.items():
        ans_witnesses = prefix_ans(rows)
        prefix_text = ",".join(ans_witnesses[:8]) or "none"
        for operation, blue_index in operations().items():
            blue_letters = sorted(
                {
                    normalize(label)[blue_index - 1]
                    for label, _ in rows[5]
                    if len(normalize(label)) >= blue_index
                }
            )
            matches, samples = suffix_words(rows, blue_index, words)
            print(
                f"{family}\t{operation}\t{blue_index}\t{''.join(blue_letters) or '-'}\t"
                f"{prefix_text}\t{len(matches)}\t{','.join(samples) or '-'}"
            )


if __name__ == "__main__":
    main()
