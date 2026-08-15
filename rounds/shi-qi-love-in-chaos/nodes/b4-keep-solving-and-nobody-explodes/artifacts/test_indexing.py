"""Reproduce the current one-based indexing hypothesis.

Only ASCII letters count.  The first three extracted letters are treated as a
mechanism checksum: they must spell ``ANS``.  The four letters after the colon
form the answer candidate.
"""

from __future__ import annotations

import re


INDICES = (3, 9, 6, 5, 4, 6, 4)

ROWS = (
    ("red", "CHARLES", "candidate king name"),
    ("orange", "SKY GARDEN", "candidate rooftop attraction"),
    ("yellow", "SANTOS", "candidate port name"),
    ("green", "SERUM RAKER", "candidate blue flying Magic card; printed P/T 3/2"),
    ("cyan", "FAKER", "player lifting the trophy at the O2"),
    (
        "blue",
        "MORDEN'S BATTLESHIP",
        "Metal Slug 3D Mission 6 boss; both numbers independently give r6c3",
    ),
    ("purple", "MEDUSA", "candidate green woman in an old Dota guide/interface"),
)


def normalize(value: str) -> str:
    return re.sub(r"[^A-Z]", "", value.upper())


def main() -> None:
    letters: list[str] = []
    print("color\tlabel\tnormalized\tindex\tletter")
    for (color, label, _note), index in zip(ROWS, INDICES, strict=True):
        normalized = normalize(label)
        letter = normalized[index - 1]
        letters.append(letter)
        print(f"{color}\t{label}\t{normalized}\t{index}\t{letter}")

    joined = "".join(letters)
    prefix, answer = joined[:3], joined[3:]
    print(f"display\t{prefix}:{answer}")
    print(f"prefix-check\t{prefix == 'ANS'}")
    print(f"answer\t{answer}")


if __name__ == "__main__":
    main()
