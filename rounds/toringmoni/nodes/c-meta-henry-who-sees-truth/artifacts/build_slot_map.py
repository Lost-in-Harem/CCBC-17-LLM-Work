#!/usr/bin/env python3
"""Join the two halves of the Meta's data into one 30-slot table.

  half A: `<use>` slots of the dashed divider on each feeder's puzzle page
          (3 folders per page, extracted by dashline_folders.py)
  half B: the `L.i1.i2.i3` code printed beside the anomalous <em> slogan on
          each feeder's WIG source page

The k-th folder slot of a feeder receives the letter at position i_k of that
feeder's L-letter slogan answer.

Includes the ten resolved strings recorded in solution.md and the accepted
feeders (c03 synchronized from its 2026-08-31 verdict). Verifies the accepted
answer and writes artifacts/meta-slot-map.tsv. Run from anywhere:
    python3 rounds/toringmoni/nodes/c-meta-henry-who-sees-truth/artifacts/build_slot_map.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent

# node -> (folder slots 1..30, WIG code as printed)
DATA = {
    "c01": ([2, 8, 18],  [4, 3, 1, 3]),
    "c02": ([1, 3, 20],  [14, 4, 1, 12]),
    "c03": ([6, 21, 27], [18, 17, 7, 14]),
    "c04": ([7, 19, 25], [7, 3, 4, 5]),
    "c05": ([5, 9, 17],  [16, 14, 4, 6]),
    "c06": ([11, 16, 24], [4, 4, 1, 3]),
    "c07": ([10, 14, 29], [16, 1, 9, 4]),
    "c08": ([4, 15, 30], [11, 10, 5, 4]),
    "c09": ([13, 22, 28], [6, 2, 6, 1]),
    "c10": ([12, 23, 26], [17, 12, 7, 3]),
}

# Final feeder answer -> transformed string; the transformation axes are
# documented in solution.md. Keep spaces in source answers for readability.
ANSWERS = {
    "c01": ("PITA", "NAAN"),
    "c02": ("LITHARGE", "CARBONMONOXIDE"),
    "c03": ("JOHN TYLER", "CARLOAZEGLIOCIAMPI"),
    "c04": ("UMBREON", "FLAREON"),
    "c05": ("BOUGAINVILLEA", "VANDAMISSJOAQUIM"),
    "c06": ("JAMES SHOAL", "MOHE"),
    "c07": ("EMERGENCY SKIN", "TWOTRUTHSANDALIE"),
    "c08": ("KAGAMINE RIN", "HATSUNEMIKU"),
    "c09": ("PAINTBRUSH", "STROKE"),
    "c10": ("CLOTHOID", "LOGARITHMICSPIRAL"),
}

rows = []
for node, (folders, code) in DATA.items():
    assert len(folders) == 3
    L, *idx = code
    assert L == max(code), f"{node}: first number is not the maximum"
    assert len(idx) == 3
    feeder_answer, transformed = ANSWERS[node]
    assert len(transformed) == L, (node, transformed, L)
    for k, (slot, i) in enumerate(zip(folders, idx), 1):
        assert 1 <= i <= L, (node, i)
        rows.append((slot, node, k, L, i, transformed[i - 1],
                     feeder_answer, transformed))

rows.sort()
assert [r[0] for r in rows] == list(range(1, 31)), "slots do not tile 1..30"
answer = "".join(r[5] for r in rows)
assert answer == "BACKUPANDTESTSUMMARIZETHEGISTS", answer

out = HERE / "meta-slot-map.tsv"
with out.open("w", encoding="utf-8") as fh:
    fh.write("slot\tnode\tnth_folder\tstring_len_L\tletter_index\tletter"
             "\tfeeder_answer\ttransformed_string\n")
    for r in rows:
        fh.write("\t".join(str(x) for x in r) + "\n")

for r in rows:
    print("\t".join(str(x) for x in r))
print(f"\nwrote {out}")
print(f"answer\t{answer}")
