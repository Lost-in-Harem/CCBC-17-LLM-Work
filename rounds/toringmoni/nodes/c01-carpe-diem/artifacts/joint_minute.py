#!/usr/bin/env python3
"""Verify the Hint 3-7 extraction without querying the live puzzle.

The dynamic model uses the page's minute clock.  E=0 is the retained sample at
2026-08-19 14:51.  The official-hint route first checks the diagnostic photo-4
phase (3.14), then evaluates the bird orbit at the historical minute supplied
by the two famous lines from 《阿飞正传》.  Earlier numeric, alphabetic, wall,
compound-word and cross-photo readings remain in the report only as rejected
controls.

The two famous lines are used only as parameters: the first supplies the target
minute and the second selects the BIRD.  A separate ten-sample wall fit covers
all target residues of the known periods 2,3,4,5,7,10.  It reconstructs 37
target walls with no ambiguous edge: the bird's (4,4) cell opens only east into
(4,5), while all six outer edges of that two-cell component are walls.  In a
maze the enclosed unit is a cell; reading it specifically as a jail cell gives
the current English candidate JAILBIRD.  CAGED BIRD and AS THE CROW FLIES remain
explicitly rejected controls.

The target photo-2 S/FLY synchronization and the TIME FLIES phrase are retained
only as a rejected control.  The famous-line words TIME and BIRD locate the
observation; they are not answer fragments.

The previous S_19 = 尤 -> YOU route is retained only as a rejected control.
The BLUE BIRD flying OVER R(AINBOW) route is also retained only as a rejected
control despite its 1/175 joint phase count.

One tempting motion reading is kept only as a failed distinctiveness control.
The bird arrives via cell 17 -> 19 and its segment intersects the Hint-5 path at
cell 18, but the same fixed path intersects every one of the bird orbit's 25
minute-to-minute segments.  CROSSING PATHS therefore does not explain the
historical minute and is not promoted.
"""

from __future__ import annotations

import argparse
from datetime import datetime
from fractions import Fraction


ANCHOR = datetime(2026, 8, 19, 14, 51)
DEFAULT_TARGET = datetime(1960, 4, 16, 14, 59)
PHOTO4_PHASE = 5474

ZODIAC = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
RADICALS_2 = "二亠人儿入八冂冖冫几凵刀力勹匕匚匸十卜卩厂厶又"
EMOTIONS = "喜怒哀乐"
POEM_TITLE = "念奴娇鸟儿问答"
MANTRA = "嗡嘛呢呗咪吽"
NECESSITIES = "柴米油盐酱醋茶"
KNOWN_1 = "精忠报国"
KNOWN_2 = "印度尼西亚"
WUYIXIANG = "旧时王谢堂前燕飞入寻常百姓家"
BAIJIA_PREFIX = (
    "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张"
    "孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛"
)
A_TO_Y = "ABCDEFGHIJKLMNOPQRSTUVWXY"
POLYBIUS_IJ = ("ABCDE", "FGHIK", "LMNOP", "QRSTU", "VWXYZ")
MAZE_SOLVABLE_PHASES = (9, 65)
MAZE_PATH = (
    (1, 1), (1, 2), (1, 3), (2, 3), (3, 3),
    (4, 3), (5, 3), (5, 4), (5, 5),
)
HORSE_ANCHOR = (3, 2)
PHOTO_LIKES = (24, 31, 19, 42)
PHOTO1_COLOURS = "赤橙黄绿青蓝紫"
CONDITIONAL_HORSE = (2, 3)
LIKE_ICON = "WHITE HEART ICON"
FLAVOR = "我这一生只会为你停留一次，只有这一分钟。"
START_CELL = (1, 1)
END_CELL = (5, 5)
MAIN_DIAGONAL = tuple((index, index) for index in range(1, 6))
CURRENT_CANDIDATE = "JAILBIRD"
TARGET_WALL_SAMPLE_COUNT = 10
TARGET_WALL_COUNT = 37
TARGET_WALL_AMBIGUITIES = 0
TARGET_BIRD_WALLS = {"north": 1, "east": 0, "south": 1, "west": 1}
TARGET_BIRD_COMPONENT = ((4, 4), (4, 5))


def minute_offset(moment: datetime) -> int:
    return int((moment - ANCHOR).total_seconds() // 60)


def one_based(sequence: str, char: str) -> int:
    return sequence.index(char) + 1


def apply(left: int, operator: str, right: int) -> int:
    return left + right if operator == "+" else left - right


def photo4_state(e: int) -> tuple[tuple[str, str, str, str], ...]:
    a1 = ZODIAC[(e + 1) % len(ZODIAC)]
    b1 = RADICALS_2[e % len(RADICALS_2)]
    c1 = KNOWN_1[e % len(KNOWN_1)]
    op1 = "++----++"[e % 8]

    a2 = EMOTIONS[(e + 3) % len(EMOTIONS)]
    b2 = POEM_TITLE[e % len(POEM_TITLE)]
    c2 = KNOWN_2[(e + 1) % len(KNOWN_2)]
    op2 = "+" if a2 in "喜乐" else "-"

    a3 = MANTRA[(e + 2) % len(MANTRA)]
    b3 = NECESSITIES[e % len(NECESSITIES)]
    op3 = "-" if a3 in "嗡呢咪" else "+"
    return (a1, op1, b1, c1), (a2, op2, b2, c2), (a3, op3, b3, "?")


def photo4_values(e: int) -> tuple[int, int, int]:
    rows = photo4_state(e)
    sequences = ((ZODIAC, RADICALS_2), (EMOTIONS, POEM_TITLE), (MANTRA, NECESSITIES))
    return tuple(
        apply(one_based(a_seq, a), op, one_based(b_seq, b))
        for (a, op, b, _), (a_seq, b_seq) in zip(rows, sequences)
    )


def bird_cell(e: int) -> tuple[int, int, int]:
    """Return one-based row-major cell, row and column on the 5x5 maze."""
    zero_based = (2 * e + 7) % 25
    return zero_based + 1, zero_based // 5 + 1, zero_based % 5 + 1


def skipped_bird_cell(e: int) -> int:
    """Return the one-based cell crossed while the bird advances E-1 -> E."""
    current_zero_based = (2 * e + 7) % 25
    return (current_zero_based - 1) % 25 + 1


def cell_number(position: tuple[int, int]) -> int:
    """Return the one-based row-major cell for a (row, column) position."""
    row, column = position
    return (row - 1) * 5 + column


def segment_intersections(
    first: tuple[int, int], second: tuple[int, int]
) -> tuple[tuple[Fraction, Fraction], ...]:
    """Intersect a bird segment with the fixed maze route.

    Input positions use (row, column); returned points use the same order.  All
    arithmetic is exact.  The target segments are not collinear with any route
    edge, so a zero denominator can simply be skipped.
    """

    def xy(position: tuple[int, int]) -> tuple[Fraction, Fraction]:
        row, column = position
        return Fraction(column), Fraction(row)

    def cross(
        left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
    ) -> Fraction:
        return left[0] * right[1] - left[1] * right[0]

    p = xy(first)
    p2 = xy(second)
    r = (p2[0] - p[0], p2[1] - p[1])
    intersections: list[tuple[Fraction, Fraction]] = []
    for route_start, route_end in zip(MAZE_PATH, MAZE_PATH[1:]):
        q = xy(route_start)
        q2 = xy(route_end)
        s = (q2[0] - q[0], q2[1] - q[1])
        denominator = cross(r, s)
        if denominator == 0:
            continue
        q_minus_p = (q[0] - p[0], q[1] - p[1])
        t = cross(q_minus_p, s) / denominator
        u = cross(q_minus_p, r) / denominator
        if 0 <= t <= 1 and 0 <= u <= 1:
            point_xy = (p[0] + t * r[0], p[1] + t * r[1])
            point_row_column = (point_xy[1], point_xy[0])
            if point_row_column not in intersections:
                intersections.append(point_row_column)
    return tuple(intersections)


def format_fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def format_point(point: tuple[Fraction, Fraction]) -> str:
    row, column = point
    return f"({format_fraction(row)},{format_fraction(column)})"


def known_nonhorse_animals(e: int) -> dict[str, tuple[int, int]]:
    """Return the four animal tracks whose formulas are fully recovered."""
    return {
        "goat": ((1, 1), (1, 5), (5, 3))[(-e) % 3],
        "fish": ((3, 1), (3, 3), (3, 5))[(1 - e) % 3],
        "tiger": (5, ((e + 2) % 5) + 1),
        "bird": bird_cell(e)[1:],
    }


def row_major_letter(position: tuple[int, int]) -> str:
    row, column = position
    return A_TO_Y[(row - 1) * 5 + column - 1]


def photo2_target_state(e: int) -> tuple[str, int, str]:
    """Return caption-order framed text, question cell and its poem character."""
    red = (e + 9) % 14 + 1
    yellow = red % 14 + 1
    blue = (red + 1) % 14 + 1
    framed = "".join(WUYIXIANG[position - 1] for position in (red, blue, yellow))
    question = 8 + (e + 5) % 7
    return framed, question, WUYIXIANG[question - 1]


def direct_encodings(cell: int, row: int, column: int) -> tuple[str, str, int, int]:
    """Return non-S_n readings of the visible bird position."""
    a_to_y = A_TO_Y[cell - 1]
    polybius = POLYBIUS_IJ[row - 1][column - 1]
    return a_to_y, polybius, cell, int(f"{row}{column}")


def third_person_singular(verb: str) -> str:
    """Apply the regular consonant+y English third-person singular rule."""
    if len(verb) >= 2 and verb.endswith("Y") and verb[-2] not in "AEIOU":
        return verb[:-1] + "IES"
    return verb + "S"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default=DEFAULT_TARGET.isoformat(timespec="minutes"))
    args = parser.parse_args()
    target = datetime.fromisoformat(args.target)

    rows = photo4_state(PHOTO4_PHASE)
    values = photo4_values(PHOTO4_PHASE)
    assert rows == (("兔", "-", "二", "报"), ("怒", "-", "念", "印"), ("咪", "-", "柴", "?"))
    assert values == (3, 1, 4)

    e = minute_offset(target)
    cell, row, column = bird_cell(e)
    previous_cell, previous_row, previous_column = bird_cell(e - 1)
    next_cell, next_row, next_column = bird_cell(e + 1)
    skipped_cell = skipped_bird_cell(e)
    skipped_letter = A_TO_Y[skipped_cell - 1]
    previous_position = (previous_row, previous_column)
    current_position = (row, column)
    next_position = (next_row, next_column)
    arrival_intersections = segment_intersections(previous_position, current_position)
    departure_intersections = segment_intersections(current_position, next_position)
    crossing_phases = tuple(
        phase
        for phase in range(25)
        if segment_intersections(bird_cell(phase - 1)[1:], bird_cell(phase)[1:])
    )
    blue_over_r_phases = tuple(
        phase
        for phase in range(175)
        if skipped_bird_cell(phase) == 18
        and PHOTO1_COLOURS[(phase + 3) % len(PHOTO1_COLOURS)] == "蓝"
    )
    time_flies_phases = tuple(
        phase
        for phase in range(350)
        if bird_cell(phase)[0] == 19
        and photo2_target_state(phase) == ("百家姓", 8, "飞")
    )
    bird_diagonal_phases = tuple(
        phase for phase in range(25) if bird_cell(phase)[1:] in MAIN_DIAGONAL
    )
    only_bird_direct_phases = tuple(
        phase
        for phase in range(75)
        if {
            animal
            for animal, position in known_nonhorse_animals(phase).items()
            if position in MAIN_DIAGONAL
        } == {"bird"}
        and (sum(HORSE_ANCHOR) + phase % 25) % 2 == 1
    )
    animals = known_nonhorse_animals(e)
    animals_on_diagonal = {
        animal: position
        for animal, position in animals.items()
        if position in MAIN_DIAGONAL
    }
    animal_letters = {animal: row_major_letter(position) for animal, position in animals.items()}
    conditional_animals = {"horse": CONDITIONAL_HORSE, **animals}
    conditional_letters = {
        animal: row_major_letter(position)
        for animal, position in conditional_animals.items()
    }
    framed, question, question_char = photo2_target_state(e)
    a_to_y, polybius, raw_cell, raw_coordinate = direct_encodings(cell, row, column)
    target_colour = PHOTO1_COLOURS[(e + 3) % len(PHOTO1_COLOURS)]
    target_photo4_rows = photo4_state(e)
    target_photo4_values = photo4_values(e)
    centre = (3, 3)
    centre_delta = (row - centre[0], column - centre[1])

    if target == DEFAULT_TARGET:
        assert e == -34_892_632
        assert e % 25 == 18
        assert (cell, row, column) == (19, 4, 4)
        assert (framed, question, question_char) == ("百家姓", 8, "飞")
        assert (a_to_y, polybius, raw_cell, raw_coordinate) == ("S", "T", 19, 44)
        assert target_colour == "蓝"
        assert target_photo4_rows == (("鸡", "+", "亠", "精"), ("乐", "+", "娇", "亚"), ("咪", "-", "油", "?"))
        assert target_photo4_values == (12, 7, 2)
        assert centre_delta == (1, 1)
        assert (previous_cell, previous_position) == (17, (4, 2))
        assert (skipped_cell, skipped_letter) == (18, "R")
        assert (next_cell, next_position) == (21, (5, 1))
        assert arrival_intersections == ((Fraction(4), Fraction(3)),)
        assert departure_intersections == ((Fraction(13, 3), Fraction(3)),)
        assert crossing_phases == tuple(range(25))
        assert e % 175 == 93
        assert blue_over_r_phases == (93,)
        assert e % 350 == 268
        assert time_flies_phases == (268,)
        assert third_person_singular("FLY") == "FLIES"
        assert current_position == MAIN_DIAGONAL[-2]
        assert (row + 1, column + 1) == END_CELL
        assert animals_on_diagonal == {"bird": (4, 4)}
        assert len(bird_diagonal_phases) == 5
        assert e % 75 == 68
        assert only_bird_direct_phases == (43, 68)
        assert (4, 3) in MAZE_PATH
        assert MAZE_PATH.index((4, 3)) + 1 == 6
        assert cell_number((4, 3)) == 18
        assert previous_position not in MAZE_PATH and current_position not in MAZE_PATH
        assert animal_letters == {"goat": "E", "fish": "O", "tiger": "U", "bird": "S"}
        assert conditional_letters == {
            "horse": "H", "goat": "E", "fish": "O", "tiger": "U", "bird": "S"
        }
        assert sorted(conditional_letters.values()) == sorted("HOUSE")
        assert {position[0] for position in conditional_animals.values()} == {1, 2, 3, 4, 5}
        assert BAIJIA_PREFIX[cell - 1] == "尤"  # rejected row-major interpretation
        assert BAIJIA_PREFIX[raw_coordinate - 1] == "葛"  # rejected coordinate interpretation
        assert cell == PHOTO_LIKES[2]  # photo 3 / maze post's fixed like count
        # A knight flips chessboard colour every move.  E mod 25 = 18 is an
        # even number of moves from the retained horse anchor, so the horse
        # cannot occupy the even-colour bird cell (4,4).
        assert (sum(HORSE_ANCHOR) + e % 25) % 2 != (row + column) % 2
        # Every main-diagonal cell has even row+column parity; the target horse
        # has the opposite colour, so it cannot share the direct route either.
        assert (sum(HORSE_ANCHOR) + e % 25) % 2 == 1
        assert all(sum(position) % 2 == 0 for position in MAIN_DIAGONAL)

    print("stage\tinput\tcalculation\toutput")
    print(f"photo4\tE={PHOTO4_PHASE}; " + "/".join("".join(r) for r in rows) + f"\tone-based differences\t{values[0]}.{values[1]}{values[2]}=π")
    print(f"intermediate\t阿/飞/正/传\tconcatenate\t阿飞正传")
    print(f"target\t阿飞正传 famous lines\tminute + object\t{target:%Y-%m-%d %H:%M}; 鸟")
    print(f"offset\tanchor={ANCHOR:%Y-%m-%d %H:%M}\ttarget-anchor\tE={e}; E mod25={e % 25}")
    print(f"photo2_target\tE mod14={e % 14}\tcaption frames + question\t{framed}=S; cell={question}→{question_char}=FLY")
    print(f"bird\t(2E+7) mod25\tzero-based={(2 * e + 7) % 25}\tcell={cell}; coordinate=({row},{column})")
    print(f"bird_motion\trow-major orbit advances two cells per minute\tE-1 / E / E+1\tcell {previous_cell}{previous_position} -> {cell}{current_position} -> {next_cell}{next_position}")
    print(f"rejected_skipped_square\tarrival cell {previous_cell} -> {cell}\tlabel the crossed one-based cell {skipped_cell} by A-Y\t{skipped_letter} (OVER THE RAINBOW rejected)")
    print("hint5_path\tunique route shared by every solvable maze phase\t" + " -> ".join(map(str, MAZE_PATH)) + "\tPATH")
    print(f"arrival_crossing\tcell {previous_cell}{previous_position} -> cell {cell}{current_position}\tintersect fixed route\t{', '.join(map(format_point, arrival_intersections))} = cell 18 = route step 6")
    print(f"departure_control\tcell {cell}{current_position} -> cell {next_cell}{next_position}\tintersect fixed route\t{', '.join(map(format_point, departure_intersections))} (same crossing relation under the other minute-edge convention)")
    print(f"failed_crossing_paths\ttest all 25 bird phases against the fixed route\tcount intersecting arrival segments\t{len(crossing_phases)}/25; CROSSING PATHS is non-discriminating")
    print(f"rejected_rainbow_rebus\ttest the full lcm(25,7)=175 bird/colour period\tskipped square R and target colour BLUE\t{len(blue_over_r_phases)}/175; phase={blue_over_r_phases[0]}; OVER THE RAINBOW rejected")
    print(f"target_maze_control\tE mod140={e % 140}\tcompare solvable phases {MAZE_SOLVABLE_PHASES}\tno traversable route at target minute")
    print(f"rejected_direct_line\tentry cell={START_CELL}; exit cell={END_CELL}\tcentre-to-centre straight route\t" + " -> ".join(map(str, MAIN_DIAGONAL)) + "; AS THE CROW FLIES rejected")
    print(f"rejected_crow_geometry\ttarget BIRD={current_position}\tlocate it on the direct entry-to-exit line\tAS THE CROW FLIES rejected; no CROW variants restored")
    print("other_animals_geometry_control\ttarget non-horse animals plus horse parity\tcheck the entry-exit diagonal\t" + "; ".join(f"{animal}={position}" for animal, position in animals.items()) + "; only BIRD is on the line; HORSE is parity-forbidden")
    print(f"diagonal_phase_control\ttest all 25 bird phases\tcount bird positions on the five-cell entry-exit diagonal\t{len(bird_diagonal_phases)}/25; phases={bird_diagonal_phases}")
    print(f"joint_animal_geometry_control\ttest the lcm(3,5,25)=75 recovered-animal period plus horse parity\tonly BIRD can lie on the direct line\t{len(only_bird_direct_phases)}/75; phases={only_bird_direct_phases}; target phase={e % 75}")
    print(f"rejected_time_flies_sync\ttest lcm(14,25)=350 phases\tphoto2 gives 百家姓=S and 飞=FLY while BIRD is in cell 19=S\t{len(time_flies_phases)}/350; phase={time_flies_phases[0]}; TIME FLIES rejected")
    print(f"raw_position\tvisible row={row}; column={column}\tconcatenate the two displayed coordinates\t{raw_coordinate} (rejected)")
    print(f"row_major_value\tbird zero-based cell={(2 * e + 7) % 25}\tconvert page orbit to one-based cell\t{raw_cell}")
    print(f"photo3_like_check\tmaze post fixed likes={PHOTO_LIKES[2]}\tcompare with one-based bird cell\t{raw_cell}={PHOTO_LIKES[2]}")
    print(f"square_letter\tone-based row-major square={cell}\tA1Z26 used as an intermediate only\t{a_to_y}")
    print(f"rejected_polybius\tcoordinate=({row},{column})\tstandard I/J-combined 5×5 Polybius square\t{polybius} (rejected)")
    print("animal_alphabet_control\tfully recovered non-horse tracks\tA-Y row-major\t" + "; ".join(f"{animal}={animals[animal]}→{animal_letters[animal]}" for animal in ("goat", "fish", "tiger", "bird")) + " (EOUS only; horse cell and ordering are not recovered)")
    print(f"horse_overlap_control\thorse anchor={HORSE_ANCHOR}; target E parity={e % 2}\tknight moves flip chessboard colour\tno overlap with bird ({row},{column}); adjacent (4,5) is not excluded")
    print(f"target_sequence_lookup\ttarget photo2 frames {framed}=S; bird one-based cell={cell}\tS{cell} in 百家姓\t{BAIJIA_PREFIX[cell - 1]}")
    print(f"rejected_english_romanisation\tS{cell}={BAIJIA_PREFIX[cell - 1]}; final must be English; Hint 6 uses pinyin\tromanise surname {BAIJIA_PREFIX[cell - 1]}\tYOU (rejected)")
    print(f"rejected_flavor_check\t{FLAVOR}\tread 为你 in the final answer language\tfor YOU (rejected with candidate)")
    print(f"rejected_coordinate_lookup\tcoordinate={raw_coordinate}\tS{raw_coordinate}\t{BAIJIA_PREFIX[raw_coordinate - 1]} (rejected; coordinate-subscript branch stopped)")
    print(f"rejected_number\tcell={raw_cell}; maze-post likes={PHOTO_LIKES[2]}\twrite 19 as digits or an English cardinal\t19 / NINETEEN (both rejected)")
    print(f"thematic_control\tfootless-bird line; title Carpe Diem\tdeath / Memento Mori association\t死/死亡/MEMENTO MORI (thematic only)")
    print("rejected_wall_state\ttwo old non-target captures enclose (4,4)-(4,5)\textrapolate and lexicalize generically\tCAGED BIRD rejected")
    print(f"target_wall_fit\t{TARGET_WALL_SAMPLE_COUNT} read-only samples cover the target residues of periods 2/3/4/5/7/10\tfit all 60 unit edges independently\t{TARGET_WALL_COUNT} target walls; ambiguous_edges={TARGET_WALL_AMBIGUITIES}")
    print("target_bird_walls\ttarget BIRD=(4,4)\tread exact N/E/S/W wall bits\t" + ",".join(f"{key}={value}" for key, value in TARGET_BIRD_WALLS.items()))
    print("target_bird_component\tstart at (4,4) and follow every open edge\tconnected component\t" + " -> ".join(map(str, TARGET_BIRD_COMPONENT)) + "; six outer boundary walls present")
    print("object_word\tsecond famous line specifies 鸟\ttranslate the selected object\tBIRD")
    print(f"target_colour\ttarget photo1 colour={target_colour}; visible bird emoji is also blue\ttranslate 蓝\tBLUE")
    print(f"rainbow_carrier\tphoto1 cycles through {PHOTO1_COLOURS}\tidentify the standard seven-colour set\tRAINBOW")
    print("rejected_rainbow_answer\tBLUE BIRD flies over R; expand R by the colour carrier\tvisual rebus\tOVER THE RAINBOW (rejected)")
    print(f"target_photo4\t" + "/".join("".join(r) for r in target_photo4_rows) + f"\tone-based arithmetic control\tvalues={target_photo4_values}; row2 right={target_photo4_rows[1][3]}")
    print(f"rejected_geography\t5×5 centre={centre}; bird=({row},{column}); photo4 row2 right={target_photo4_rows[1][3]}\tSOUTHEAST + ASIA\tSOUTHEAST ASIA (rejected)")
    print(f"rejected_suffix_compositions\tcell {cell}={a_to_y}\tBLUE + {a_to_y}; BIRD + {a_to_y}\tBLUES / BIRDS (both rejected)")
    print("rejected_direct_compound\ttarget colour BLUE + selected object BIRD\tBLUE + BIRD\tBLUEBIRD (rejected)")
    print("rejected_music\tcoordinate=(4,4)\tread as a 4/4 time signature\tCOMMON TIME (rejected)")
    print("rejected_conditional_horse\tretained knight-walk anchors allow 12 target cells\tadd one-animal-per-row constraint\t(2,3)→H (not forced by the horse data)")
    print("rejected_conditional_house\tconditional horse=H plus E/O/U/S from the recovered tracks\tA-Y cells, then reorder\tHOUSE (unsupported intermediate; do not submit)")
    print("rejected_animal_compound\tfamous-line object BIRD + conditional grid word HOUSE\tBIRD + HOUSE\tBIRDHOUSE (rejected; whole animal-grid compound family stopped)")
    print(f"rejected_like_compound\tmaze post action is {LIKE_ICON}; fixed likes={PHOTO_LIKES[2]}\tread the heart as LOVE and append BIRD\tLOVEBIRD (rejected; 19 likes is numbering check only)")
    print(f"rejected_time_square\tbird coordinate=({row},{column}); target month/day={target.month}/{target.day}\tTIME + {a_to_y} + SQUARE; {row}×{column}={row * column}\tTIMES SQUARE (rejected; A1Z26 and numeric pun stopped)")
    print("rejected_dead_end\ttwo retained wall captures at E=-2988 and E=-2343\t(4,4) opens east only; graph degree=1 in both\tDEAD END rejected; later exact fit confirms the degree but does not restore the death reading")
    print(f"current_candidate\tBIRD lies inside a closed maze cell\tmaze cell -> jail cell; bird in jail\t{CURRENT_CANDIDATE}")


if __name__ == "__main__":
    main()
