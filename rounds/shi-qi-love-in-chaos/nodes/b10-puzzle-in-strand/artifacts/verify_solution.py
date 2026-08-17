"""Verify the eight covers, endpoint chain, and FLUCTUATING extraction.

The script retains PASTE ING ON FL as a licensed intermediate instruction.
It also retains the reproducible cores of MEANING, FLOUNDERING, BINGO, ECORI,
ION, FLING, FLYING, NASTY, and 42 as negative evidence after rejection.
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
    # instruction PASTE ING ON FL.
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
    instruction = ("PASTE", "ING", "ON", left_residue)
    assert instruction == ("PASTE", "ING", "ON", "FL")
    fling_intermediate = left_residue + "ING"
    assert fling_intermediate == "FLING"

    # Rejected endpoint-matrix continuation. FLING and MEANING are real paths,
    # but restoring the original board order and extending through ING is not
    # instructed by the final diagram.
    matrix = tuple(
        "".join(codes[board][row] for board in range(1, 9))
        for row in range(4)
    )
    assert matrix == ("ABCFINPS", "PIALNEAT", "GNTNGYMR", "NOSONTSE")

    def matrix_read(path):
        assert len(path) == len(set(path))
        assert all(
            max(abs(ar - br), abs(ac - bc)) == 1
            for (ar, ac), (br, bc) in zip(path, path[1:])
        )
        return "".join(matrix[row][column] for row, column in path)

    ing_path = ((0, 4), (1, 4), (2, 4))
    fling_path = ((0, 3), (1, 3)) + ing_path
    meaning_path = ((2, 6), (1, 5), (1, 6), (0, 5)) + ing_path
    assert matrix_read(fling_path) == "FLING"
    rejected_meaning = matrix_read(meaning_path)
    assert rejected_meaning == "MEANING"
    assert set(fling_path) & set(meaning_path) == set(ing_path)

    # ON and ING meet at the same letter-value vertex N in the edge-trail
    # graph. Moving the complete ING trail therefore moves that N instead of
    # copying it. ON leaves O behind next to FL, making FLO. Pasting ING above
    # it is the standard rebus FLO UNDER ING.
    on_trail = "ON"
    ing_trail = "ING"
    shared_hinge = set(on_trail) & set(ing_trail)
    assert shared_hinge == {"N"}
    on_residue = "".join(char for char in on_trail if char not in shared_hinge)
    lower = left_residue + on_residue
    upper = ing_trail
    assert on_residue == "O"
    assert lower == "FLO"
    rejected_floundering = lower + "UNDER" + upper
    assert rejected_floundering == "FLOUNDERING"

    # Rejected BINGO experiment: overwrite Board 4's first three circles with
    # Board 5's ING, then retain an obsolete N/N junction and choose a new read
    # start on BINO. The mechanics are reproducible, but the user rejected the
    # result and the diagram does not license either extra assumption.
    target_before = codes[4]
    neighbor = codes[2]
    donor = codes[5]
    assert target_before == "FLNO"
    assert neighbor == "BINO"
    assert donor == "INGN"
    paste_segment = donor[:3]
    assert paste_segment == "ING"
    paste_start = target_before.index("FL")
    target_after_chars = list(target_before)
    for offset, char in enumerate(paste_segment):
        target_after_chars[paste_start + offset] = char
    target_after = "".join(target_after_chars)
    assert target_after == "INGO"
    changed_pair_position = 2
    assert target_before[changed_pair_position] == neighbor[changed_pair_position] == "N"
    assert target_after[changed_pair_position] == "G"
    rejected_bingo = (
        neighbor[: changed_pair_position + 1]
        + target_after[changed_pair_position:]
    )
    assert rejected_bingo == "BINGO"

    # Execute the instruction on the complete spangram identified by its FL
    # endpoint. Replacing FLUCTUATION's ION suffix with ING gives the exact
    # candidate FLUCTUATING. The Board 4 layout independently supports the
    # rewrite: shortening WAVERING to WAVER leaves exactly one noncrossing
    # 45-cell pack containing the candidate.
    target = SPANGRAMS[4]
    candidate = target[:-3] + "ING"
    assert target.startswith(left_residue)
    assert target.endswith("ION")
    assert candidate == "FLUCTUATING"
    assert candidate in PASTED_BOARD4_PACK

    full_board4_covers = exact_covers(4)
    assert len(full_board4_covers) == 1
    full_board4 = dict(full_board4_covers[0])
    pasted_covers = covers_for_pack(4, PASTED_BOARD4_PACK, 45)
    assert len(pasted_covers) == 1
    pasted_board4 = dict(pasted_covers[0])

    assert pasted_board4["WAVER"] == full_board4["WAVERING"][:5]
    assert pasted_board4[candidate][:9] == full_board4["FLUCTUATION"][:9]
    assert pasted_board4[candidate][9:] == full_board4["WAVERING"][-2:]

    all_cells = frozenset(itertools.product(range(8), range(6)))
    pasted_used = frozenset().union(
        *(frozenset(path) for path in pasted_board4.values())
    )
    leftover = all_cells - pasted_used
    assert leftover == frozenset({(4, 5), (5, 5), (7, 5)})
    assert {col for _, col in leftover} == {5}
    rejected_ion = "".join(
        GRIDS[4][row][5] for row, _ in sorted(leftover, reverse=True)
    )
    assert rejected_ion == "ION"

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

    # The flavour's life/strand/pairing language licenses the literal DNA-base
    # letters at the seven overlaps.  The forward chain spells GAATT.
    dna = "".join(
        char
        for pair in shared_pairs
        for char in pair
        if char in "ACGT"
    )
    assert dna == "GAATT"

    # FLING clues the only ordinary English path-order endpoint code, CAST.
    # Its A/S/T are shared with its two neighbors, leaving C.  This is also the
    # sole DNA-base letter not shared with either neighboring strand.
    unshared_dna = []
    for index, board in enumerate(order):
        neighbor_shared = set()
        if index:
            neighbor_shared |= set(codes[board]) & set(codes[order[index - 1]])
        if index + 1 < len(order):
            neighbor_shared |= set(codes[board]) & set(codes[order[index + 1]])
        for position, char in enumerate(path_codes[board]):
            if char in "ACGT" and char not in neighbor_shared:
                unshared_dna.append((board, position, char))
    assert unshared_dna == [(3, 0, "C")]

    fling_targets = [
        board for board, code in path_codes.items() if code == "CAST"
    ]
    assert fling_targets == [3]
    cast_index = order.index(fling_targets[0])
    cast_used = path_pairs[cast_index - 1] | path_pairs[cast_index]
    cast_residue = "".join(
        char for char in path_codes[3] if char not in cast_used
    )
    assert cast_residue == "C"

    recognition_site = dna + cast_residue
    complementary_site = recognition_site.translate(
        str.maketrans("ACGT", "TGCA")
    )[::-1]
    assert recognition_site == "GAATTC"
    assert complementary_site == "GAATTC"
    reverse_strand = recognition_site.translate(str.maketrans("ACGT", "TGCA"))
    assert reverse_strand == "CTTAAG"
    rejected_ecori = "ECORI"

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
    print("instruction: PASTE ING ON FL")
    print("endpoint matrix in board order:", "/".join(matrix))
    print("  execute instruction path:", matrix_read(fling_path))
    print("  shared cells:", matrix_read(ing_path))
    print("rejected endpoint-matrix continuation:", rejected_meaning)
    print("  ON and ING share:", "".join(sorted(shared_hinge)))
    print("  move ING; ON leaves:", on_residue)
    print("  rebus rows:", upper, "/", lower)
    print("rejected rebus: FLO UNDER ING ->", rejected_floundering)
    print("rejected overlay result:", rejected_bingo)
    print("  circle fill:", target_before, "beside", neighbor)
    print("  donor Board 5:", donor, "(paste", paste_segment + ")")
    print("  align ING on FL ->", target_after)
    print("  B-I-N, cross the changed N/G pair, then G-O ->", rejected_bingo)
    print("rejected semantic continuation:")
    print("  FL + ING ->", fling_intermediate)
    print("  FLING -> CAST; CAST residue ->", cast_residue)
    print("  overlap DNA + C ->", recognition_site, "->", rejected_ecori)
    print("candidate operation on Board 4:")
    print("  WAVERING -> WAVER + ING")
    print("  FLUCTUATION - ION + ING ->", candidate)
    print("  unique leftover column, bottom-to-top ->", rejected_ion, "(rejected residue)")
    print("rejected bare concatenation: FL + ING ->", fling_intermediate)
    print("rejected extra-end/SCS route: FL / YN / ING -> FLYING")
    print("rejected final answer but retained recognition site:", recognition_site)
    print(
        "rejected top-circle binary core:",
        top_overlap_bits,
        "->",
        rejected_binary_answer,
    )
    print(
        "rejected final candidates: COPY AND PASTE / PASTE / CUT AND PASTE / "
        "42 / PASTEUR / GAATTC / ECORI / FLYING / FLING / NASTY / ION / "
        "BINGO / FLOUNDERING / MEANING"
    )
    print("candidate:", candidate)


if __name__ == "__main__":
    main()
