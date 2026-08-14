"""Solve and extract from the 9x9 Miracle Sudoku heard in the puzzle audio.

Rules: ordinary Sudoku, anti-king, anti-knight, and no orthogonally
adjacent consecutive digits. Coordinates use one-based rNcM notation.
"""

from __future__ import annotations

import argparse
import re

from z3 import Abs, And, Distinct, Int, Or, Solver, sat


COORD_RE = re.compile(r"r([1-9])c([1-9])", re.IGNORECASE)


def parse_coord(value: str) -> tuple[int, int]:
    match = COORD_RE.fullmatch(value)
    if not match:
        raise argparse.ArgumentTypeError("coordinate must look like r5c3")
    return int(match.group(1)) - 1, int(match.group(2)) - 1


def make_solver() -> tuple[Solver, list[list]]:
    cells = [[Int(f"r{r + 1}c{c + 1}") for c in range(9)] for r in range(9)]
    solver = Solver()

    for row in cells:
        solver.add(Distinct(row))
        solver.add(*(And(cell >= 1, cell <= 9) for cell in row))
    for c in range(9):
        solver.add(Distinct([cells[r][c] for r in range(9)]))
    for box_r in range(0, 9, 3):
        for box_c in range(0, 9, 3):
            solver.add(
                Distinct(
                    [
                        cells[r][c]
                        for r in range(box_r, box_r + 3)
                        for c in range(box_c, box_c + 3)
                    ]
                )
            )

    # Anti-king (the orthogonal moves are already covered by row/column rules).
    for r in range(8):
        for c in range(8):
            solver.add(cells[r][c] != cells[r + 1][c + 1])
            solver.add(cells[r + 1][c] != cells[r][c + 1])

    # Anti-knight: constrain each unordered pair only once.
    knight_steps = ((1, 2), (2, 1), (1, -2), (2, -1))
    for r in range(9):
        for c in range(9):
            for dr, dc in knight_steps:
                rr, cc = r + dr, c + dc
                if 0 <= rr < 9 and 0 <= cc < 9:
                    solver.add(cells[r][c] != cells[rr][cc])

    # Orthogonally adjacent cells cannot be consecutive.
    for r in range(9):
        for c in range(9):
            if r < 8:
                solver.add(Abs(cells[r][c] - cells[r + 1][c]) != 1)
            if c < 8:
                solver.add(Abs(cells[r][c] - cells[r][c + 1]) != 1)

    return solver, cells


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--given",
        action="append",
        default=["r5c3=9", "r6c7=8"],
        help="given in rNcM=d form; may be repeated",
    )
    parser.add_argument(
        "--extract",
        nargs="*",
        type=parse_coord,
        default=[],
        metavar="rNcM",
    )
    args = parser.parse_args()

    solver, cells = make_solver()
    for given in args.given:
        coord_text, digit_text = given.split("=", 1)
        r, c = parse_coord(coord_text)
        digit = int(digit_text)
        if not 1 <= digit <= 9:
            raise ValueError("given digit must be 1 through 9")
        solver.add(cells[r][c] == digit)

    if solver.check() != sat:
        raise SystemExit("no solution")
    model = solver.model()
    solution = [[model.evaluate(cells[r][c]).as_long() for c in range(9)] for r in range(9)]
    for row in solution:
        print(" ".join(map(str, row)))

    solver.add(
        Or(
            *[
                cells[r][c] != solution[r][c]
                for r in range(9)
                for c in range(9)
            ]
        )
    )
    print(f"unique: {solver.check() != sat}")

    if args.extract:
        digits = "".join(str(solution[r][c]) for r, c in args.extract)
        labels = " ".join(f"r{r + 1}c{c + 1}={solution[r][c]}" for r, c in args.extract)
        print(f"extract: {digits} ({labels})")


if __name__ == "__main__":
    main()
