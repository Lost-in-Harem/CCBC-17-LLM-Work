"""Verify the eight covers, endpoint chain, and Board 4 paste extraction.

The script also retains the mechanically reproducible cores of FLING,
FLYING, GAATTC, and 42 only as negative evidence after explicit rejection.
"""

from __future__ import annotations

import itertools
from functools import lru_cache


GRIDS = {
    1: "SGNIZI UVGRRE RENEAS LIISIN GLTDSG NIENEA PPHIHR AREGNC".split(),
    2: "NRUCEL GILTEK BNOHOS IATLHN BBIGSO GOSENW UEILOB LGNDRA".split(),
    3: "URGEOE SCONSU ORTRRN DADGIS CPIOOT HDILIN YINECA SCIATI".split(),
    4: "IAUTTI RCNMAO AETIFN VLCUHT FUYASN ITLTIO DUFVNG IWAERI".split(),
    5: "RUOVTI INGEAN ICDREG NOPORM GPRACB NECNON INILGC NGNIAE".split(),
    6: "EULVTY GABIIG EMTOLA NDOAPT SESRMH OWPIEY ROAHCL RYLONA".split(),
    7: "PASSRY AIRUAG GNFUNM AARHIS OBINGU NOCARO STNUMB EAILXE".split(),
    8: "TSEREL HNKAWO GITLGR SAOITR PTRFSE EAREUS GSOFPS SURTRE".split(),
}

PACKS = {
    1: ("APPREHENDING", "ARRESTING", "SEIZING", "SEARCHING", "SURVEILLING"),
    2: ("SNOWBOARDING", "BOBSLEIGH", "BIATHLON", "CURLING", "SKELETON", "LUGE"),
    3: ("CARDIOLOGIST", "PHYSICIAN", "DIETICIAN", "SURGEON", "DOCTOR", "NURSE"),
    4: ("WAVERING", "SHIFT", "VARIANCE", "MUTATION", "FLUCTUATION", "FLUIDITY"),
    5: ("INCORPORATING", "EMBRACING", "CONCEALING", "DEVOURING", "PENNING"),
    6: ("DESPAIR", "SORROW", "NEGATIVITY", "MELANCHOLY", "GLOOM", "APATHY", "BLUE"),
    7: ("RUSSIA", "HUNGARY", "LUXEMBOURG", "ESTONIA", "GABON", "PANAFRICANISM"),
    8: ("STRATOLIFTER", "GROWLER", "SEAKNIGHT", "PEGASUS", "SUPERFORTRESS"),
}

SPANGRAMS = {
    1: "APPREHENDING",
    2: "BIATHLON",
    3: "CARDIOLOGIST",
    4: "FLUCTUATION",
    5: "INCORPORATING",
    6: "NEGATIVITY",
    7: "PANAFRICANISM",
    8: "STRATOLIFTER",
}

PASTED_BOARD4_PACK = (
    "WAVER",
    "SHIFT",
    "VARIANCE",
    "MUTATION",
    "FLUCTUATING",
    "FLUIDITY",
)


def diagonals(path):
    result = set()
    for (row, col), (rr, cc) in zip(path, path[1:]):
        if abs(rr - row) == abs(cc - col) == 1:
            result.add((min(row, rr), min(col, cc), (rr - row) * (cc - col)))
    return frozenset(result)


def cross(first, second):
    return any((row, col, -slope) in second for row, col, slope in first)


def paths(grid, word):
    found = []

    def visit(offset, row, col, used, path, path_diagonals):
        if offset == len(word):
            found.append(tuple(path))
            return
        for dr, dc in itertools.product((-1, 0, 1), repeat=2):
            if not (dr or dc):
                continue
            rr, cc = row + dr, col + dc
            if not (0 <= rr < 8 and 0 <= cc < 6):
                continue
            if (rr, cc) in used or grid[rr][cc] != word[offset]:
                continue
            new_diagonals = path_diagonals
            if abs(dr) == abs(dc) == 1:
                diagonal = (min(row, rr), min(col, cc), dr * dc)
                if (diagonal[0], diagonal[1], -diagonal[2]) in path_diagonals:
                    continue
                new_diagonals = path_diagonals | {diagonal}
            visit(
                offset + 1,
                rr,
                cc,
                used | {(rr, cc)},
                path + [(rr, cc)],
                new_diagonals,
            )

    for row, col in itertools.product(range(8), range(6)):
        if grid[row][col] == word[0]:
            visit(1, row, col, {(row, col)}, [(row, col)], frozenset())
    return found


def covers_for_pack(board, pack, target_size):
    grid = GRIDS[board]
    candidates = [(word, paths(grid, word)) for word in pack]
    assert all(options for _, options in candidates)
    covers = []

    def search(index, used, used_diagonals, chosen):
        if index == len(candidates):
            if len(used) == target_size:
                covers.append(tuple(chosen))
            return
        word, options = candidates[index]
        for path in options:
            cells = frozenset(path)
            ds = diagonals(path)
            if cells & used or cross(ds, used_diagonals):
                continue
            search(index + 1, used | cells, used_diagonals | ds, chosen + [(word, path)])

    search(0, frozenset(), frozenset(), [])
    return covers


def exact_covers(board):
    return covers_for_pack(board, PACKS[board], 48)


def endpoint_code(word):
    return word[:2] + word[-1:-3:-1]


def endpoint_path_code(word):
    """Four endpoint letters in the spangram's left-to-right path order."""
    return word[:2] + word[-2:]


def edge_trails(edges):
    degrees = {}
    for edge in edges:
        for char in edge:
            degrees[char] = degrees.get(char, 0) + 1
    starts = [char for char, degree in degrees.items() if degree % 2]
    if len(starts) not in (0, 2):
        return set()
    if not starts:
        starts = [min(degrees)]
    found = set()

    def walk(char, unused, text):
        if not unused:
            found.add(text)
            return
        for index, edge in enumerate(unused):
            if char not in edge:
                continue
            other = edge[1] if edge[0] == char else edge[0]
            walk(other, unused[:index] + unused[index + 1 :], text + other)

    for start in starts:
        walk(start, tuple(edges), start)
    return found


def shortest_common_supersequences(strings):
    """Return the exact minimum length and all minimum interleavings."""

    @lru_cache(maxsize=None)
    def visit(state):
        if all(position == len(value) for position, value in zip(state, strings)):
            return 0, frozenset({""})
        choices = sorted({
            value[position]
            for position, value in zip(state, strings)
            if position < len(value)
        })
        best_length = 10**9
        best = set()
        for char in choices:
            following = tuple(
                position + 1
                if position < len(value) and value[position] == char
                else position
                for position, value in zip(state, strings)
            )
            suffix_length, suffixes = visit(following)
            length = 1 + suffix_length
            candidates = {char + suffix for suffix in suffixes}
            if length < best_length:
                best_length = length
                best = candidates
            elif length == best_length:
                best.update(candidates)
        return best_length, frozenset(best)

    return visit(tuple(0 for _ in strings))


def main():
    for board in range(1, 9):
        covers = exact_covers(board)
        assert covers
        for cover in covers:
            span_path = dict(cover)[SPANGRAMS[board]]
            assert {col for _, col in span_path} >= {0, 5}
        print(f"board {board}: {len(covers)} exact cover(s), spangram={SPANGRAMS[board]}")

    codes = {board: endpoint_code(word) for board, word in SPANGRAMS.items()}
    orders = [
        order
        for order in itertools.permutations(range(1, 9))
        if all(len(set(codes[a]) & set(codes[b])) == 2 for a, b in zip(order, order[1:]))
    ]
    assert orders == [(4, 2, 5, 1, 7, 3, 8, 6), (6, 8, 3, 7, 1, 5, 2, 4)]
    order = orders[0]
    print("chain:", "-".join(map(str, order)))
    print("codes:", " ".join(codes[board] for board in order))

    shared_pairs = []
    for left_board, right_board in zip(order, order[1:]):
        left, right = codes[left_board], codes[right_board]
        shared = sorted(set(left) & set(right))
        shared_pairs.append("".join(shared))
    assert shared_pairs == ["NO", "IN", "GN", "AP", "AS", "ST", "ET"]

    # The seven undirected edges split into ON / ING / PASTE.  Together with
    # the unused FL at the left terminal, reverse block order gives the exact
    # instruction PASTE ING ON FL.  Treating bare FL+ING as the answer led to
    # the explicitly rejected FLING; FL instead selects the Board 4 spangram.
    assert edge_trails(shared_pairs[:1]) == {"NO", "ON"}
    assert edge_trails(shared_pairs[1:3]) == {"ING", "GNI"}
    assert edge_trails(shared_pairs[3:]) == {"PASTE", "ETSAP"}

    # The three edge blocks occupy the diagram left-to-right as ON / ING /
    # PASTE.  Reading the grammatical instruction right-to-left therefore
    # ends with ON followed by the left-end residue FL.
    left_residue = "".join(
        char for char in codes[order[0]] if char not in set(shared_pairs[0])
    )
    right_residue = "".join(
        char for char in codes[order[-1]] if char not in set(shared_pairs[-1])
    )
    assert left_residue == "FL"
    assert right_residue == "NY"
    rejected_instruction = ("PASTE", "ING", "ON", left_residue)
    assert rejected_instruction == ("PASTE", "ING", "ON", "FL")
    rejected_fling = left_residue + "ING"
    assert rejected_fling == "FLING"

    # Execute the instruction on Board 4.  The full cover supplies the donor
    # WAVERING and target FLUCTUATION.  Removing ING from the donor leaves the
    # valid path WAVER; pasting it onto the word beginning FL changes that path
    # to FLUCTUATING.  Across every possible path spelling there is exactly one
    # noncrossing 45-cell pack.
    full_board4_covers = exact_covers(4)
    assert len(full_board4_covers) == 1
    full_board4 = dict(full_board4_covers[0])
    pasted_covers = covers_for_pack(4, PASTED_BOARD4_PACK, 45)
    assert len(pasted_covers) == 1
    pasted_board4 = dict(pasted_covers[0])

    assert pasted_board4["WAVER"] == full_board4["WAVERING"][:5]
    assert (
        pasted_board4["FLUCTUATING"][:9]
        == full_board4["FLUCTUATION"][:9]
    )
    assert (
        pasted_board4["FLUCTUATING"][9:]
        == full_board4["WAVERING"][-2:]
    )

    all_cells = frozenset(itertools.product(range(8), range(6)))
    pasted_used = frozenset().union(
        *(frozenset(path) for path in pasted_board4.values())
    )
    leftover = all_cells - pasted_used
    assert leftover == frozenset({(4, 5), (5, 5), (7, 5)})
    assert {col for _, col in leftover} == {5}
    answer = "".join(GRIDS[4][row][5] for row, _ in sorted(leftover, reverse=True))
    assert answer == "ION"

    # Put the four endpoint letters on each strand in their actual
    # left-to-right spangram order.  An internal circle is an extraction
    # junction only if the same physical occurrence is forced to serve the
    # x2 match on both its left and right.  Board 5 has two N circles, so its
    # two N matches can use different occurrences and do not make a junction.
    path_codes = {
        board: endpoint_path_code(word)
        for board, word in SPANGRAMS.items()
    }
    path_pairs = [
        set(path_codes[left]) & set(path_codes[right])
        for left, right in zip(order, order[1:])
    ]
    assert ["".join(sorted(pair)) for pair in path_pairs] == shared_pairs
    forced_double = []
    for index, board in enumerate(order[1:-1], 1):
        reused = path_pairs[index - 1] & path_pairs[index]
        forced_double.append("".join(
            char
            for char in path_codes[board]
            if char in reused and path_codes[board].count(char) == 1
        ))
    assert forced_double == ["N", "", "", "A", "S", "T"]
    junction_read = "".join(forced_double)
    assert junction_read == "NAST"

    # The last junction T is matched into terminal NETY.  Continue along that
    # left-to-right spangram from T to its right endpoint, contributing Y.
    terminal = path_codes[order[-1]]
    tail = terminal[terminal.index(junction_read[-1]) + 1 :]
    assert terminal == "NETY"
    assert tail == "Y"
    rejected_nasty = junction_read + tail
    assert rejected_nasty == "NASTY"

    reverse = order[::-1]
    reverse_pairs = [
        set(path_codes[left]) & set(path_codes[right])
        for left, right in zip(reverse, reverse[1:])
    ]
    reverse_forced = []
    for index, board in enumerate(reverse[1:-1], 1):
        reused = reverse_pairs[index - 1] & reverse_pairs[index]
        reverse_forced.append("".join(
            char
            for char in path_codes[board]
            if char in reused and path_codes[board].count(char) == 1
        ))
    reverse_junction_read = "".join(reverse_forced)
    reverse_terminal = path_codes[reverse[-1]]
    reverse_tail = reverse_terminal[
        reverse_terminal.index(reverse_junction_read[-1]) + 1 :
    ]
    assert reverse_junction_read == "TSAN"
    assert reverse_tail == ""

    # Rejected negative evidence: adding the opposite end's Y and treating
    # FL / YN / ING as a shortest-common-supersequence problem produced
    # FLYING, but neither extra step is present in the diagram's instruction.
    right_inward = right_residue[::-1]
    audited = {}
    for left in (left_residue, left_residue[::-1]):
        for right in (right_residue, right_inward):
            length, candidates = shortest_common_supersequences((left, right, "ING"))
            assert length == 6
            assert len(candidates) == 30
            audited[left, right] = candidates
    assert "FLYING" in audited["FL", "YN"]
    assert all(
        "FLYING" not in candidates
        for orientation, candidates in audited.items()
        if orientation != ("FL", "YN")
    )

    # Rejected negative evidence: literal DNA bases spell GAATT, but filtering
    # bases and closing it to GAATTC were not licensed and GAATTC was rejected.
    dna = "".join(
        char
        for pair in shared_pairs
        for char in pair
        if char in "ACGT"
    )
    assert dna == "GAATT"

    # The sole DNA-base letter not shared with either neighboring strand is C.
    unshared_dna = []
    for index, board in enumerate(order):
        neighbor_shared = set()
        if index:
            neighbor_shared |= set(codes[board]) & set(codes[order[index - 1]])
        if index + 1 < len(order):
            neighbor_shared |= set(codes[board]) & set(codes[order[index + 1]])
        for position, char in enumerate(codes[board]):
            if char in "ACGT" and char not in neighbor_shared:
                unshared_dna.append((board, position, char))
    assert unshared_dna == [(3, 0, "C")]

    # Rejected negative evidence: the arbitrary top-circle convention makes 42.
    top_overlap_bits = "".join(
        "1" if codes[right][0] in set(codes[left]) & set(codes[right]) else "0"
        for left, right in zip(order, order[1:])
    )
    assert top_overlap_bits == "0101010"
    rejected_binary_answer = int(top_overlap_bits, 2)
    assert rejected_binary_answer == 42
    print("take the first two and last two letters of each left-to-right spangram")
    print("shared pairs:", "/".join(shared_pairs))
    print("path-order codes:", " ".join(path_codes[board] for board in order))
    print("forced double-paired circles:", "/".join(value or "-" for value in forced_double))
    print("rejected junction + terminal-tail route:", junction_read, "+", tail, "->", rejected_nasty)
    print("reverse audit:", reverse_junction_read, "+", reverse_tail or "(empty)")
    print("candidate:", answer)
    print("instruction: PASTE ING ON FL")
    print("  WAVERING -> WAVER + ING")
    print("  FLUCTUATION + ING -> FLUCTUATING")
    print("  unique leftover column, bottom-to-top ->", answer)
    print("rejected bare concatenation: FL + ING ->", rejected_fling)
    print("rejected extra-end/SCS route: FL / YN / ING -> FLYING")
    print("rejected DNA-filter core:", dna, "+ C -> GAATTC")
    print(
        "rejected top-circle binary core:",
        top_overlap_bits,
        "->",
        rejected_binary_answer,
    )
    print(
        "rejected final candidates: COPY AND PASTE / PASTE / CUT AND PASTE / "
        "42 / PASTEUR / GAATTC / FLYING / FLING / NASTY"
    )


if __name__ == "__main__":
    main()
