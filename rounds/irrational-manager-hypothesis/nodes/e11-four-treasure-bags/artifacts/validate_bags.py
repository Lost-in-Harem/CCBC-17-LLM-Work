"""Reproduce the boundary-hidden chickens and middle-letter extraction.

Run from the Node directory or repository root:
    python artifacts/validate_bags.py
"""

from __future__ import annotations

import re


ROWS = [
    ("During Mardi Gras, spies might commit sabotage here.", 5, "GRASS", "SNAKE"),
    ("Which signing will fulfill the championship wishes of these clubs: the bot TL entered into talks with earlier this year, or the top DSG discovered in the LCP?", 6, "BOTTLE", "GENIE"),
    ("The fans are facing utter despair after seeing their favorite team lose to the weakest opponent.", 6, "GUTTER", "LOSER"),
    ("The Cantonese rapper carries lethal weapon during his shows as part of his supreme blueprint—a dangerous stunt with no silver lining.", 4, "POND", "AROWANA"),
    ("I need to wrap the gift with a fancy ribbon. Networking is so important to me that I can't help bringing it up every minute.", 6, "BONNET", "BEE"),
    ("What a wonder! Landslide victories have been secured by Tim Burton across multiple Oscar categories.", 10, "WONDERLAND", "ALICE"),
    ("The critic made a rude, vile, and disrespectful comment on a song by a former S.H.E member.", 5, "DEVIL", "ANGEL"),
    ("Which male animal can lay eggs? Maybe male kangaroos. Terrific achievement if you actually discovered one.", 7, "ROOSTER", "SHE"),
    ("I feel like I am destined to watch the best Arsenal performance today.", 5, "STARS", "DESTINY"),
]


def crosses_word_boundary(clue: str, target: str) -> bool:
    tokens = re.findall(r"[A-Za-z]+", clue)
    joined = "".join(tokens).upper()
    boundaries = set()
    cursor = 0
    for token in tokens[:-1]:
        cursor += len(token)
        boundaries.add(cursor)
    start = joined.index(target)
    end = start + len(target)
    return any(start < boundary < end for boundary in boundaries)


def main() -> int:
    centers = []
    for index, (clue, bracket, chicken, pigeon) in enumerate(ROWS, start=1):
        assert len(chicken) == bracket, (index, chicken, bracket)
        assert crosses_word_boundary(clue, chicken), (index, chicken)
        assert len(pigeon) % 2 == 1, (index, pigeon)
        center = pigeon[len(pigeon) // 2]
        centers.append(center)
        print(f"{index}: {chicken} <- boundary; {pigeon} -> {center}")

    extraction = "".join(centers)
    assert extraction == "ANSWEIGHT", extraction
    assert extraction[:3] == "ANS"
    answer = extraction[3:]
    assert answer == "WEIGHT"
    print(f"extraction={extraction} -> ANS {answer}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
