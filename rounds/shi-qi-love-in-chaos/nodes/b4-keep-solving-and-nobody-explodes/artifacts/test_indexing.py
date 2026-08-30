"""Bounded audit of the hint-directed Seven Wonders extraction.

The unlocked hints require:

* the full English names of the seven Ancient Wonders;
* one-based indices from the rainbow Sudoku cells;
* addition for the two blue values, 9 and 6;
* the fixed first field ``ANS``;
* enumeration of the five missing color values only over 1..9.

The script tests all 9 x 9 green/cyan pairs after the ``ANS`` prefix fixes
red, orange, and yellow. It writes every English-frequency closure that meets
the chosen threshold. It does not submit an answer.
"""

from __future__ import annotations

import argparse
import itertools
import re
from pathlib import Path

from wordfreq import zipf_frequency


NAMES = (
    "MAUSOLEUM AT HALICARNASSUS",
    "HANGING GARDENS OF BABYLON",
    "LIGHTHOUSE OF ALEXANDRIA",
    "GREAT PYRAMID OF GIZA",
    "STATUE OF ZEUS AT OLYMPIA",
    "COLOSSUS OF RHODES",
    "TEMPLE OF ARTEMIS AT EPHESUS",
)
COLORS = ("red", "orange", "yellow", "green", "cyan", "blue", "purple")
EXPECTED_PREFIX = "ANS"
BLUE_VALUES = (9, 6)
PURPLE_INDEX = 4


def normalize(value: str) -> str:
    """Keep only A-Z, matching the extraction convention."""

    return re.sub(r"[^A-Z]", "", value.upper())


def positions(label: str, wanted: str, limit: int = 9) -> list[int]:
    """Return legal Sudoku indices that extract ``wanted`` from ``label``."""

    return [
        index
        for index, char in enumerate(normalize(label), start=1)
        if index <= limit and char == wanted
    ]


def candidate_rows(min_zipf: float) -> list[dict[str, object]]:
    """Enumerate all bounded candidates compatible with the unlocked hints."""

    prefix_positions = [
        positions(label, wanted)
        for label, wanted in zip(NAMES[:3], EXPECTED_PREFIX, strict=True)
    ]
    if any(not choices for choices in prefix_positions):
        raise ValueError("The formal names cannot produce the required ANS prefix")

    blue_index = sum(BLUE_VALUES)
    blue_name = normalize(NAMES[5])
    purple_name = normalize(NAMES[6])
    if blue_index > len(blue_name) or PURPLE_INDEX > len(purple_name):
        raise ValueError("A fixed extraction index is outside its formal name")

    blue_letter = blue_name[blue_index - 1]
    purple_letter = purple_name[PURPLE_INDEX - 1]
    prefix_zipf = zipf_frequency(EXPECTED_PREFIX.lower(), "en")
    rows: list[dict[str, object]] = []

    for green_index, cyan_index in itertools.product(range(1, 10), repeat=2):
        green_letter = normalize(NAMES[3])[green_index - 1]
        cyan_letter = normalize(NAMES[4])[cyan_index - 1]
        suffix = f"{green_letter}{cyan_letter}{blue_letter}{purple_letter}"
        suffix_zipf = zipf_frequency(suffix.lower(), "en")
        if prefix_zipf < min_zipf or suffix_zipf < min_zipf:
            continue
        rows.append(
            {
                "phrase": f"{EXPECTED_PREFIX}:{suffix}",
                "operation": "sum",
                "blue_index": blue_index,
                "prefix_zipf": prefix_zipf,
                "suffix_zipf": suffix_zipf,
                "score": prefix_zipf + suffix_zipf,
                "indices": ";".join(
                    (
                        f"red={','.join(map(str, prefix_positions[0]))}",
                        f"orange={','.join(map(str, prefix_positions[1]))}",
                        f"yellow={','.join(map(str, prefix_positions[2]))}",
                        f"green={green_index}",
                        f"cyan={cyan_index}",
                        f"blue={BLUE_VALUES[0]}+{BLUE_VALUES[1]}={blue_index}",
                        f"purple={PURPLE_INDEX}",
                    )
                ),
            }
        )

    rows.sort(key=lambda row: (-float(row["score"]), str(row["phrase"])))
    return rows


def render_tsv(rows: list[dict[str, object]]) -> str:
    lines = [
        "rank\toperation\tblue_index\tphrase\tprefix_zipf\t"
        "suffix_zipf\tscore\tindices"
    ]
    for rank, row in enumerate(rows, start=1):
        lines.append(
            f"{rank}\t{row['operation']}\t{row['blue_index']}\t{row['phrase']}\t"
            f"{row['prefix_zipf']:.2f}\t{row['suffix_zipf']:.2f}\t"
            f"{row['score']:.2f}\t{row['indices']}"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank-output", type=Path)
    parser.add_argument("--min-zipf", type=float, default=2.0)
    args = parser.parse_args()

    rows = candidate_rows(args.min_zipf)
    output = render_tsv(rows)
    if args.rank_output is not None:
        args.rank_output.write_text(output, encoding="utf-8")
    print(f"tested-green-cyan-pairs={9 * 9}")
    print(f"ranked-candidates={len(rows)}")
    for rank, row in enumerate(rows, start=1):
        print(
            f"rank={rank} phrase={row['phrase']} operation={row['operation']} "
            f"indices={row['indices']}"
        )


if __name__ == "__main__":
    main()
