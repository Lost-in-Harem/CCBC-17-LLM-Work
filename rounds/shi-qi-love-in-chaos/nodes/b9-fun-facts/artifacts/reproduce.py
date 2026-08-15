"""Reproduce the confirmed first-layer milestone."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


MILESTONE_TABLE = Path(__file__).with_name("extraction.tsv")
EXPECTED_MILESTONE = "DICTDEFSFORREDAREAHANZI"

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
