"""Reproduce the failed HART/CRANE/LINER and withdrawn ORIZABA route."""

from __future__ import annotations

import argparse
from collections import Counter


ELEMENTS = [
    "", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og",
]

# Page order. Teams are the terminal letters of astronomY, racE, mineralS.
BASE_ROWS = [
    ("Y", 45), ("E", 33), ("E", 22), ("E", 34),
    ("Y", 59), ("Y", 55), ("Y", 58), ("E", 21),
    ("Y", 72), ("Y", 54), ("E", 11), ("E", 16),
    ("Y", 85), ("Y", 56), ("E", 34), ("E", 23),
    ("S", 52), ("S", 95), ("S", 39), ("S", 99),
    ("S", 27), ("S", 28), ("S", 22), ("S", 74),
    ("S", 94), ("S", 88), ("Y", 54), ("E", 11),
]

TEAM_WORDS = ("ALIEN", "RACER", "STONE")
TARGETS = ("HART", "CRANE", "LINER")


def base5(number: int) -> tuple[int, int, int]:
    return number // 25, number // 5 % 5, number % 5


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--row2", type=int, choices=(31, 33), default=33)
    parser.add_argument("--row26", type=int, choices=(88, 89), default=88)
    args = parser.parse_args()

    rows = list(BASE_ROWS)
    rows[1] = ("E", args.row2)
    rows[25] = ("S", args.row26)

    instruction = "".join(ELEMENTS[rows[index - 1][1]] for index in range(10, 21))
    bottom = "".join(ELEMENTS[rows[index - 1][1]] for index in (27, 28))
    assert instruction.upper() == "XENASATBASEVTEAMYES"
    assert bottom.upper() == "XENA"

    data = [
        row for index, row in enumerate(rows, start=1)
        if not 10 <= index <= 20 and index not in (27, 28)
    ]
    grouped = {team: [number for row_team, number in data if row_team == team]
               for team in "YES"}
    assert [len(grouped[team]) for team in "YES"] == [5, 4, 6]

    recombined: list[int] = []
    triples: list[str] = []
    for column in range(4):
        digits = tuple(base5(grouped[team][column])[position]
                       for position, team in enumerate("YES"))
        triples.append("".join(map(str, digits)))
        recombined.append(25 * digits[0] + 5 * digits[1] + digits[2])
    law = "".join(ELEMENTS[number] for number in recombined).upper()
    assert law == "GETALAW"

    leftovers = (grouped["Y"][4], grouped["S"][4], grouped["S"][5])
    differences = tuple(left - right for left, right in zip(leftovers, (71, 6, 39)))
    fragments = tuple(ELEMENTS[number] for number in differences)

    extracted: list[str] = []
    failed_words: list[str] = []
    for number, fragment, target in zip(differences, fragments, TARGETS):
        letters = "".join(word[digit] for word, digit in zip(TEAM_WORDS, base5(number)))
        extracted.append(letters)
        if Counter(fragment.upper() + letters) == Counter(target):
            failed_words.append(target)
        else:
            failed_words.append("NO UNIQUE TARGET")

    print(f"instruction: {instruction} -> XENA'S AT BASE / V / TEAM YES")
    print(f"set aside bottom: {bottom}")
    print(f"team sizes Y/E/S: {[len(grouped[team]) for team in 'YES']}")
    print(f"recombined: {' '.join(triples)} -> {law}")
    print(f"LAWLESS - LAW: LESS; Hf/Pu/{ELEMENTS[args.row26]} - Lu/C/Y")
    print(f"differences: {differences} -> {'/'.join(fragments)}")
    print(f"team indices: {'/'.join(extracted)}")
    print(f"failed unvalidated words: {'/'.join(failed_words)}")
    if tuple(failed_words) == TARGETS:
        print("failed association: HART CRANE + LINER points to ORIZABA")


if __name__ == "__main__":
    main()
