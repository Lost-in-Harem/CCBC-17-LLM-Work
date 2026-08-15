"""Reproduce confirmed milestones and opt-in failed-route audits."""

from __future__ import annotations

import argparse
import csv
import itertools
import math
import sys
from collections import defaultdict
from pathlib import Path


MILESTONE_TABLE = Path(__file__).with_name("extraction.tsv")
DA_COLLOCATIONS_TABLE = Path(__file__).with_name("da-collocations.tsv")
DA_GLOSSES_TABLE = Path(__file__).with_name("da-dictionary-glosses.tsv")
DA_SENSE_EXTRACTION_TABLE = Path(__file__).with_name("da-sense-extraction.tsv")
SECOND_TABLE = Path(__file__).with_name("second-extraction.tsv")
RED_GLYPH_TABLE = Path(__file__).with_name("red-glyphs.tsv")
EXPECTED_MILESTONE = "DICTDEFSFORREDAREAHANZI"
EXPECTED_FINAL_CLUE = "ATENNISBALL"
EXPECTED_ANSWER = "RACKET"
REJECTED_PINYIN = "FOUREN"

ICONS = [
    ("metaphor", 950.0, 372.0),
    ("podium", 800.0, 431.0),
    ("box", 950.0, 491.0),
    ("broom", 800.0, 558.0),
    ("morse", 950.0, 700.0),
    ("nunchaku", 800.0, 754.0),
]

parser = argparse.ArgumentParser()
parser.add_argument(
    "--audit-rejected-strike",
    action="store_true",
    help="also reproduce the rejected direct-gloss -> STRIKE route",
)
parser.add_argument(
    "--audit-rejected-twelve",
    action="store_true",
    help="also reproduce the rejected 11+1 -> TWELVE route",
)
parser.add_argument(
    "--audit-rejected-nearest",
    action="store_true",
    help="also reproduce the rejected FOUREN nearest-icon route",
)
parser.add_argument(
    "--jitter",
    type=int,
    default=0,
    help="exhaustively perturb every icon center by integer offsets in ±N pixels",
)
args = parser.parse_args()

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


with MILESTONE_TABLE.open(encoding="utf-8", newline="") as handle:
    rows = sorted(
        csv.DictReader(handle, delimiter="\t"),
        key=lambda row: int(row["reading_order"]),
    )

glyphs = [row["glyph"] for row in rows]
assert len(glyphs) == len(set(glyphs)), "a glyph hit by two lines must only be read once"
message = "".join(row["letter"] for row in rows)
assert message == EXPECTED_MILESTONE, message

print("DICT DEFS FOR RED AREA HANZI")
print("confirmed red-area Hanzi (visual/site milestone): 打")

with DA_COLLOCATIONS_TABLE.open(encoding="utf-8", newline="") as handle:
    da_rows = list(csv.DictReader(handle, delimiter="\t"))

assert len(da_rows) == 11
assert [int(row["order"]) for row in da_rows] == list(range(1, 12))
assert all(row["打搭配"].startswith("打") for row in da_rows)

with DA_SENSE_EXTRACTION_TABLE.open(encoding="utf-8", newline="") as handle:
    sense_rows = list(csv.DictReader(handle, delimiter="\t"))

assert len(sense_rows) == 11
assert [int(row["central_order"]) for row in sense_rows] == list(range(1, 12))
for row in sense_rows:
    sense_number = int(row["汉典基本释义编号"])
    assert 1 <= sense_number <= 26
    assert row["A1Z26"] == chr(64 + sense_number)

final_clue = "".join(row["A1Z26"] for row in sense_rows)
assert final_clue == EXPECTED_FINAL_CLUE, final_clue
print("numbered 打 senses in central-icon order: A TENNIS BALL")
assert len(EXPECTED_ANSWER) == 6
print("accepted tool for the extracted object, matching (6): RACKET")

if args.audit_rejected_strike:
    with DA_GLOSSES_TABLE.open(encoding="utf-8", newline="") as handle:
        gloss_rows = list(csv.DictReader(handle, delimiter="\t"))

    direct_glosses = [row for row in gloss_rows if row["role"] == "direct_gloss"]
    assert all(int(row["length"]) == len(row["gloss"]) for row in direct_glosses)
    length_matches = [
        row["gloss"] for row in direct_glosses if int(row["length"]) == 6
    ]
    assert length_matches == ["STRIKE"], length_matches
    print(
        "REJECTED AUDIT ONLY: unique 6-letter direct CC-CEDICT gloss "
        "for 打 = STRIKE"
    )

if args.audit_rejected_twelve:
    # This count is arithmetically reproducible but was explicitly rejected by
    # the Hunt site, so it is never promoted by the default run.
    total = len(da_rows) + 1
    assert total == 12
    print("REJECTED AUDIT ONLY: 11 illustrated uses + 1 drawn 打 = 12 -> TWELVE")

if not args.audit_rejected_nearest:
    raise SystemExit(0)

with RED_GLYPH_TABLE.open(encoding="utf-8", newline="") as handle:
    red_glyphs = list(csv.DictReader(handle, delimiter="\t"))

assert len(red_glyphs) == 42
assert len({row["glyph"] for row in red_glyphs}) == len(red_glyphs)

cells: dict[str, list[tuple[float, dict[str, str]]]] = defaultdict(list)
for glyph in red_glyphs:
    gx, gy = float(glyph["x"]), float(glyph["y"])
    nearest_icon, distance = min(
        (
            (icon, math.hypot(gx - icon_x, gy - icon_y))
            for icon, icon_x, icon_y in ICONS
        ),
        key=lambda item: item[1],
    )
    cells[nearest_icon].append((distance, glyph))

with SECOND_TABLE.open(encoding="utf-8", newline="") as handle:
    expected_rows = {
        row["icon"]: row for row in csv.DictReader(handle, delimiter="\t")
    }

selected: list[str] = []
for icon, _, _ in ICONS:
    ranked = sorted(cells[icon], key=lambda item: item[0])
    best_distance, best = ranked[0]
    runner_distance, runner = ranked[1]
    expected = expected_rows[icon]
    assert best["letter"] == expected["letter"]
    assert runner["letter"] == expected["runner_letter"]
    assert math.isclose(best_distance, float(expected["distance"]), abs_tol=0.11)
    assert math.isclose(
        runner_distance, float(expected["runner_distance"]), abs_tol=0.11
    )
    selected.append(best["letter"])
    print(
        f"{icon:10s}: {best['letter']} {best_distance:5.1f}px; "
        f"runner-up {runner['letter']} {runner_distance:5.1f}px"
    )

pinyin = "".join(selected)
assert pinyin == REJECTED_PINYIN, pinyin

print("REJECTED AUDIT ONLY: FOUREN -> fǒu rèn -> 否认 -> DENIAL")

if args.jitter:
    import numpy as np

    radius = args.jitter
    offsets = list(itertools.product(range(-radius, radius + 1), repeat=2))
    layouts = itertools.product(offsets, repeat=len(ICONS))
    base_centers = np.array([(x, y) for _, x, y in ICONS], dtype=float)
    glyph_points = np.array(
        [(float(row["x"]), float(row["y"])) for row in red_glyphs], dtype=float
    )
    glyph_letters = np.array([row["letter"] for row in red_glyphs])
    variants: set[str] = set()
    layout_count = 0
    batch_size = 4096

    while batch := list(itertools.islice(layouts, batch_size)):
        moved_centers = base_centers[None, :, :] + np.asarray(batch, dtype=float)
        delta = glyph_points[None, :, None, :] - moved_centers[:, None, :, :]
        squared_distances = np.sum(delta * delta, axis=3)
        owners = np.argmin(squared_distances, axis=2)
        batch_letters: list[np.ndarray] = []
        for icon_index in range(len(ICONS)):
            owned_distances = np.where(
                owners == icon_index,
                squared_distances[:, :, icon_index],
                np.inf,
            )
            winners = np.argmin(owned_distances, axis=1)
            batch_letters.append(glyph_letters[winners])
        variants.update(
            "".join(letters)
            for letters in zip(*(column.tolist() for column in batch_letters))
        )
        layout_count += len(batch)

    assert variants == {REJECTED_PINYIN}, sorted(variants)
    print(f"rejected ±{radius}px center-jitter audit: {layout_count:,} layouts -> FOUREN")
