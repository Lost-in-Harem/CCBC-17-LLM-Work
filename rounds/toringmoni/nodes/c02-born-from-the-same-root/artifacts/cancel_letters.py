"""Reproduce the final pair-cancellation step from the credits clue."""

from argparse import ArgumentParser
from collections import Counter


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        "sources",
        nargs="*",
        default=["PENCILLEAD", "NDAL"],
        help="Strings whose letters are cancelled in identical pairs.",
    )
    parser.add_argument("--target", default="CLIP")
    args = parser.parse_args()

    letters = "".join(args.sources).replace(" ", "").upper()
    counts = Counter(letters)
    residue = Counter({letter: count % 2 for letter, count in counts.items() if count % 2})

    print("sources:", " + ".join(args.sources))
    print("counts:", " ".join(f"{letter}:{counts[letter]}" for letter in sorted(counts)))
    print("uncancelled multiset:", "".join(sorted(residue.elements())))
    print("target anagram:", args.target.upper())

    if residue != Counter(args.target.upper()):
        raise SystemExit("target does not match the uncancelled letter multiset")


if __name__ == "__main__":
    main()
