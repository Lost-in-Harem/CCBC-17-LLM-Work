"""Verify the eight covers, the protein/DNA extraction, and final symbol.

Hint 11 identifies the last glyph as protein-beta-sheet-like, licensing DNA
translation rather than endpoint equality. Hint 12 fixes the word order at
2-6-7-8-4-5-3-1. Translation gives MINIFYHAVE. Independently, reverse whole
four-base columns as needed so every adjacent pair has exactly two same-row
Watson-Crick matches. Hint-12 order, first-strand-forward anchoring, and the
ordinary convention "reversed = 1" give 00111101, ASCII ``=``. Its standard
Unicode name is ``EQUALS SIGN``. The pictured ``x2`` is the two-match
constraint; the rejected ``==``/``FALSE`` interpretation is retained only as
negative evidence, along with older semantic, mass, and letter-edit routes.
"""

from __future__ import annotations

import itertools
from functools import lru_cache
import unicodedata


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

HINT12_ORDER = (2, 6, 7, 8, 4, 5, 3, 1)

CODON_TO_AMINO = {
    "ATG": "M",
    "ATT": "I",
    "AAC": "N",
    "ATA": "I",
    "TTC": "F",
    "TAT": "Y",
    "CAT": "H",
    "GCA": "A",
    "GTA": "V",
    "GAG": "E",
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


def minified_dna(word):
    """Keep only unambiguous DNA bases, preserving their word order."""
    return "".join(char for char in word if char in "ACGT")


def translate_dna(sequence):
    assert len(sequence) % 3 == 0
    return "".join(
        CODON_TO_AMINO[sequence[index:index + 3]]
        for index in range(0, len(sequence), 3)
    )


def interleaved_endpoint_code(word):
    """Interweave the forward and reverse ends as a,d,b,c."""
    return word[0] + word[-1] + word[1] + word[-2]


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

    # Current evidence: Hint 12 supplies an official order that is different
    # from the historical exact-two chain below.  Circle order cannot change
    # these set-intersection counts.
    hint12_shared = [
        "".join(sorted(set(codes[left]) & set(codes[right])))
        for left, right in zip(HINT12_ORDER, HINT12_ORDER[1:])
    ]
    hint12_counts = [len(value) for value in hint12_shared]
    assert hint12_shared == ["N", "", "S", "", "N", "", "A"]
    assert hint12_counts == [1, 0, 1, 0, 1, 0, 1]

    # Hint 11's beta-sheet-like backbone and dotted hydrogen bonds identify a
    # protein context.  Minify each ordered spangram to the unambiguous DNA
    # alphabet.  Six words already give four bases; the two two-base results
    # are repeated once to fill the four-circle template.  The printed x2 is
    # separately verified below as the two-complementary-match constraint.
    dna_fragments = {
        board: minified_dna(word)
        for board, word in SPANGRAMS.items()
    }
    assert dna_fragments == {
        1: "AG",
        2: "AT",
        3: "CAGT",
        4: "CTAT",
        5: "CATG",
        6: "GATT",
        7: "AACA",
        8: "TATT",
    }
    four_base_fragments = {
        board: fragment * 2 if len(fragment) == 2 else fragment
        for board, fragment in dna_fragments.items()
    }
    assert all(len(fragment) == 4 for fragment in four_base_fragments.values())
    ordered_fragments = tuple(
        four_base_fragments[board] for board in HINT12_ORDER
    )
    assert ordered_fragments == (
        "ATAT", "GATT", "AACA", "TATT",
        "CTAT", "CATG", "CAGT", "AGAG",
    )

    complement = str.maketrans("ACGT", "TGCA")
    orientation_solutions = []
    for reversals in itertools.product((False, True), repeat=8):
        oriented = tuple(
            fragment[::-1] if reverse else fragment
            for fragment, reverse in zip(ordered_fragments, reversals)
        )
        match_positions = tuple(
            tuple(
                position
                for position, (left, right) in enumerate(zip(first, second), 1)
                if left.translate(complement) == right
            )
            for first, second in zip(oriented, oriented[1:])
        )
        if all(len(matches) == 2 for matches in match_positions):
            orientation_solutions.append((reversals, oriented, match_positions))
    assert len(orientation_solutions) == 2
    assert {
        "".join("R" if reverse else "F" for reverse in reversals)
        for reversals, _, _ in orientation_solutions
    } == {"FFRRRRFR", "RRFFFFRF"}
    anchored_solutions = [
        solution for solution in orientation_solutions if not solution[0][0]
    ]
    assert len(anchored_solutions) == 1
    reversals, oriented_fragments, complementary_matches = anchored_solutions[0]
    orientation_text = "".join("R" if reverse else "F" for reverse in reversals)
    orientation_bits = "".join("1" if reverse else "0" for reverse in reversals)
    assert orientation_text == "FFRRRRFR"
    assert orientation_bits == "00111101"
    comparison_character = chr(int(orientation_bits, 2))
    assert comparison_character == "="
    candidate = unicodedata.name(comparison_character)
    assert candidate == "EQUALS SIGN"
    dna_sequence = "".join(ordered_fragments)
    assert dna_sequence == "ATATGATTAACATATTCTATCATGCAGTAGAG"

    # The first biological start codon is ATG at zero-based offset 2.  The
    # remaining 30 bases are ten complete codons whose one-letter amino-acid
    # codes give an explicit instruction plus operand.
    start = dna_sequence.index("ATG")
    assert start == 2
    coding_sequence = dna_sequence[start:]
    codons = tuple(
        coding_sequence[index:index + 3]
        for index in range(0, len(coding_sequence), 3)
    )
    assert codons == (
        "ATG", "ATT", "AAC", "ATA", "TTC",
        "TAT", "CAT", "GCA", "GTA", "GAG",
    )
    peptide_message = translate_dna(coding_sequence)
    assert peptide_message == "MINIFYHAVE"

    # The flavour says to interweave forward and reverse and use an overlap.
    # Alternating HAVE's left and right ends gives HEAV; it shares the terminal
    # Y of MINIFY to form HEAVY without adding or dropping a decoded letter.
    clue_pair = peptide_message[:6], peptide_message[6:]
    assert clue_pair == ("MINIFY", "HAVE")

    # Rejected interpretation retained for audit only.  The x2 label specifies
    # exactly two complementary rows at every adjacent gap; it does not repeat
    # the already extracted character.  Treating it as ``==`` and evaluating
    # the two English words produced FALSE, which the user explicitly rejected.
    rejected_comparison_operator = comparison_character * 2
    assert rejected_comparison_operator == "=="
    rejected_comparison_expression = (
        f"{clue_pair[0]} {rejected_comparison_operator} {clue_pair[1]}"
    )
    assert rejected_comparison_expression == "MINIFY == HAVE"
    rejected_false = str(clue_pair[0] == clue_pair[1]).upper()
    assert rejected_false == "FALSE"

    # Rejected ordinary wordplay retained for audit only.
    small_code = "S"
    rejected_shave = small_code + clue_pair[1]
    assert rejected_shave[1:] == clue_pair[1]
    assert rejected_shave == "SHAVE"

    # Rejected tail route retained for audit only. It uniquely makes an
    # ordinary word under this bounded weave, but the user rejected HEAVY and
    # the puzzle does not license taking only MINIFY's terminal Y.
    def outside_in(word):
        result = []
        left, right = 0, len(word) - 1
        while left <= right:
            result.append(word[left])
            left += 1
            if left <= right:
                result.append(word[right])
                right -= 1
        return "".join(result)

    interwoven_operand = outside_in(clue_pair[1])
    shared_code = clue_pair[0][-1]
    heavy = interwoven_operand + shared_code
    assert interwoven_operand == "HEAV"
    assert shared_code == "Y"
    assert heavy == "HEAVY"
    assert sorted(peptide_message) == sorted(clue_pair[0] + heavy[:-1])
    rejected_heavy = heavy
    assert rejected_heavy == "HEAVY"
    rejected_lighten = "LIGHTEN"

    # Rejected one-edit family retained for audit only.
    one_edit_reductions = {
        "HALVE": {"edit": "insert L at 3", "factor": 2},
        "SHAVE": {"edit": "insert S at 1", "factor": None},
        "SAVE": {"edit": "replace H with S", "factor": None},
    }
    factor_two_matches = tuple(
        word
        for word, evidence in one_edit_reductions.items()
        if evidence["factor"] == 2
    )
    assert factor_two_matches == ("HALVE",)
    rejected_halve = factor_two_matches[0]
    assert rejected_halve[:2] + rejected_halve[3:] == clue_pair[1]
    assert rejected_halve == "HALVE"
    added_codes = tuple(
        char
        for char in rejected_halve
        if rejected_halve.count(char) > clue_pair[1].count(char)
    )
    assert added_codes == ("L",)
    protein_code_names = {"L": "LEUCINE"}
    rejected_leucine = protein_code_names[added_codes[0]]
    assert rejected_leucine == "LEUCINE"

    # Rejected post-hoc route retained for audit: treating both English words
    # as peptide sequences and minimizing molar mass gives I/A, then CURRENT.
    amino_acid_names = {
        "M": "METHIONINE",
        "I": "ISOLEUCINE",
        "N": "ASPARAGINE",
        "F": "PHENYLALANINE",
        "Y": "TYROSINE",
        "H": "HISTIDINE",
        "A": "ALANINE",
        "V": "VALINE",
        "E": "GLUTAMICACID",
    }
    amino_acid_masses = {
        "M": 149.21,
        "I": 131.17,
        "N": 132.12,
        "F": 165.19,
        "Y": 181.19,
        "H": 155.16,
        "A": 89.09,
        "V": 117.15,
        "E": 147.13,
    }

    # Pair the two decoded protein strands. HAVE must fully overlap a
    # four-residue window of MINIFY. Enumerating both strand directions and
    # all three offsets gives twelve outputs; the node-local WordNet audit in
    # work/amino_minification.py finds only NAVE to be an ordinary word.
    pairwise_outputs = {}
    for first_direction, first in (
        ("forward", clue_pair[0]),
        ("reverse", clue_pair[0][::-1]),
    ):
        for second_direction, second in (
            ("forward", clue_pair[1]),
            ("reverse", clue_pair[1][::-1]),
        ):
            for offset in range(len(first) - len(second) + 1):
                window = first[offset:offset + len(second)]
                result = "".join(
                    left
                    if amino_acid_masses[left] < amino_acid_masses[right]
                    else right
                    for left, right in zip(window, second)
                )
                pairwise_outputs[first_direction, second_direction, offset] = result
    assert pairwise_outputs == {
        ("forward", "forward", 0): "MAVI",
        ("forward", "forward", 1): "IAVE",
        ("forward", "forward", 2): "NAVE",
        ("forward", "reverse", 0): "EVAI",
        ("forward", "reverse", 1): "IVAH",
        ("forward", "reverse", 2): "NVAH",
        ("reverse", "forward", 0): "HAVN",
        ("reverse", "forward", 1): "HAVI",
        ("reverse", "forward", 2): "IAVE",
        ("reverse", "reverse", 0): "EVAN",
        ("reverse", "reverse", 1): "EVAI",
        ("reverse", "reverse", 2): "IVAM",
    }
    rejected_nave = pairwise_outputs["forward", "forward", 2]
    assert rejected_nave == "NAVE"

    def unique_minimum_code(word, values):
        codes = tuple(dict.fromkeys(word))
        minimum = min(values[code] for code in codes)
        minima = tuple(code for code in codes if values[code] == minimum)
        assert len(minima) == 1
        return minima[0]

    mass_minima = tuple(
        unique_minimum_code(word, amino_acid_masses) for word in clue_pair
    )
    assert mass_minima == ("I", "A")
    quantity_and_unit = {("I", "A"): "CURRENT"}
    rejected_current = quantity_and_unit[mass_minima]
    assert rejected_current == "CURRENT"

    # The rejected name-length metric gives Y/V and then VALINE instead.
    amino_acid_name_lengths = {
        code: len(name) for code, name in amino_acid_names.items()
    }
    name_length_minima = tuple(
        unique_minimum_code(word, amino_acid_name_lengths)
        for word in clue_pair
    )
    assert name_length_minima == ("Y", "V")

    # Retain explicitly rejected interpretations as negative evidence.
    rejected_bare_candidate = minified_dna(clue_pair[1])
    assert rejected_bare_candidate == "A"
    rejected_alanine = "ALANINE"
    rejected_adenine = "ADENINE"
    rejected_valine = "VALINE"

    orders = [
        order
        for order in itertools.permutations(range(1, 9))
        if all(len(set(codes[a]) & set(codes[b])) == 2 for a, b in zip(order, order[1:]))
    ]
    assert orders == [(4, 2, 5, 1, 7, 3, 8, 6), (6, 8, 3, 7, 1, 5, 2, 4)]
    order = orders[0]
    assert HINT12_ORDER not in orders
    print("official Hint 12 order:", "-".join(map(str, HINT12_ORDER)))
    print("official adjacent endpoint-common counts:", hint12_counts)
    print("rejected historical exact-two chain:", "-".join(map(str, order)))
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

    # Rejected FLEETING route retained for audit.  Under the natural a,d,b,c
    # order, impose "cross the far-right equality and take one terminal step."
    # This really includes E-E-T, but the image does not authorize that start,
    # direction, or extra step, and the user rejected the resulting answer.
    interleaved_codes = {
        board: interleaved_endpoint_code(word)
        for board, word in SPANGRAMS.items()
    }
    assert [interleaved_codes[board] for board in order] == [
        "FNLO", "BNIO", "IGNN", "AGPN", "PMAS", "CTAS", "SRTE", "NYET"
    ]
    terminal_left = interleaved_codes[8]
    terminal_right = interleaved_codes[6]
    assert terminal_left == "SRTE"
    assert terminal_right == "NYET"

    terminal_chunks = set()
    terminal_paths = set()
    for char in sorted(set(terminal_left) & set(terminal_right)):
        for left_row, left_char in enumerate(terminal_left):
            if left_char != char:
                continue
            for right_row, right_char in enumerate(terminal_right):
                if right_char != char:
                    continue
                for step in (-1, 1):
                    following = right_row + step
                    if 0 <= following < 4:
                        text = char + char + terminal_right[following]
                        terminal_chunks.add(text)
                        terminal_paths.add((text, (8, left_row), (6, right_row), (6, following)))
                for step in (-1, 1):
                    following = left_row + step
                    if 0 <= following < 4:
                        text = char + char + terminal_left[following]
                        terminal_chunks.add(text)
                        terminal_paths.add((text, (6, right_row), (8, left_row), (8, following)))
    assert terminal_chunks == {"EEY", "EET", "TTE", "TTR"}
    assert (
        "EET", (8, 3), (6, 2), (6, 3)
    ) in terminal_paths

    rejected_fleeting_target = left_residue + "EET"
    rejected_fleeting = rejected_fleeting_target + "ING"
    assert rejected_fleeting_target == "FLEET"
    assert rejected_fleeting == "FLEETING"

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

    # Rejected Board 4 rewrite retained for audit.  Replacing FLUCTUATION's
    # ION suffix with ING really does permit the unusual 45-cell cover below,
    # but the user rejected FLUCTUATING.  The later claim that EET completes
    # the edge-only FL target was also rejected through FLEETING.
    target = SPANGRAMS[4]
    rejected_fluctuating = target[:-3] + "ING"
    assert target.startswith(left_residue)
    assert target.endswith("ION")
    assert rejected_fluctuating == "FLUCTUATING"
    assert rejected_fluctuating in PASTED_BOARD4_PACK

    full_board4_covers = exact_covers(4)
    assert len(full_board4_covers) == 1
    full_board4 = dict(full_board4_covers[0])
    pasted_covers = covers_for_pack(4, PASTED_BOARD4_PACK, 45)
    assert len(pasted_covers) == 1
    pasted_board4 = dict(pasted_covers[0])

    assert pasted_board4["WAVER"] == full_board4["WAVERING"][:5]
    assert pasted_board4[rejected_fluctuating][:9] == full_board4["FLUCTUATION"][:9]
    assert pasted_board4[rejected_fluctuating][9:] == full_board4["WAVERING"][-2:]

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
    print("rejected historical instruction: PASTE ING ON FL")
    print("interleaved codes:", " ".join(interleaved_codes[board] for board in order))
    print("far-end bounded chunks:", "/".join(sorted(terminal_chunks)))
    print("rejected terminal target: FL + EET ->", rejected_fleeting_target)
    print("rejected terminal completion:", rejected_fleeting_target, "+ ING ->", rejected_fleeting)
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
    print("rejected operation on Board 4:")
    print("  WAVERING -> WAVER + ING")
    print("  FLUCTUATION - ION + ING ->", rejected_fluctuating)
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
        "BINGO / FLOUNDERING / MEANING / FLUCTUATING / FLEETING / A / HAVE / "
        "CONTRACT / ALANINE / ADENINE / VALINE / CURRENT / HALVE / LEUCINE / "
        "LIGHTEN / HEAVY / SHAVE / NAVE / FALSE"
    )
    print("Hint 11 protein/DNA extraction:")
    print("  minified fragments:", " / ".join(ordered_fragments))
    print("  DNA:", dna_sequence)
    print("  start at base 3:", " / ".join(codons))
    print("  peptide message:", peptide_message)
    print("  decoded instruction:", " / ".join(clue_pair))
    print("  unique four-circle orientation:", orientation_text)
    print(
        "  orientation bits:", orientation_bits, "->", comparison_character,
        "->", candidate,
    )
    print("  pictured x2: exactly two complementary rows at each gap")
    print(
        "  rejected comparison:", rejected_comparison_expression,
        "->", rejected_false,
    )
    print("  rejected word operation: S(small) + HAVE ->", rejected_shave)
    print("  rejected bare endpoint:", rejected_bare_candidate)
    print("  rejected physical-size selection:", rejected_alanine)
    print("  rejected DNA-base expansion:", rejected_adenine)
    print("  rejected name-length minima:", name_length_minima, "->", rejected_valine)
    print("  rejected amino-acid mass minima:", mass_minima, "->", rejected_current)
    print("  pairwise lower-mass outputs:")
    for key, result in pairwise_outputs.items():
        print("   ", key, "->", result)
    print("  rejected mass-selected word:", rejected_nave)
    print("  bounded one-edit reductions:", ", ".join(one_edit_reductions))
    print("  rejected-as-final factor-two word: HAVE + L ->", rejected_halve)
    print("  rejected inserted-code expansion:", added_codes[0], "->", rejected_leucine)
    print("  rejected outside-in HAVE:", interwoven_operand)
    print("  rejected shared terminal code:", shared_code)
    print("  rejected overlap result:", rejected_heavy)
    print("  rejected semantic continuation:", rejected_lighten)
    print("current candidate:", candidate)


if __name__ == "__main__":
    main()
