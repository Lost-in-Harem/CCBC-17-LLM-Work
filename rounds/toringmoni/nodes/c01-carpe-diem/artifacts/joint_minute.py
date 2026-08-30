#!/usr/bin/env python3
"""Verify the Hint 3-7 extraction without querying the live puzzle.

The dynamic model uses the page's minute clock.  E=0 is the retained sample at
2026-08-19 14:51.  The official-hint route first checks the diagnostic photo-4
phase (3.14), then evaluates the bird orbit at the historical minute supplied
by the two famous lines from 《阿飞正传》.  The terminal comparison deliberately
keeps the raw cell/coordinate separate from rejected or unsupported encodings.
The one-based row-major cell is checked against the maze post's fixed like
count, but both the number and its English cardinal have been rejected.  The
cell's A1Z26 reading has now failed both as BLUE+S = BLUES and BIRD+S = BIRDS,
so the whole alphabet-suffix family is retained only as a negative control.
The second famous line supplies the literal object word BIRD.  Its rejected
direct compound with target photo 1's BLUE is retained as a negative control.
The rejected animal-grid branch asked whether all five animal cells form HOUSE
and hence BIRDHOUSE.  Four cells are reproduced algebraically; the horse=H
premise is explicitly conditional because the retained horse anchors do not
force it.  The user's rejection stops that entire branch.  Number, wall-state,
musical 4/4, Polybius and S_n readings are likewise retained only as negative
controls.  The current branch instead uses the exact match between one-based
bird cell 19 and the maze post's 19 likes.  The post template visibly labels
the like action with a white heart, giving LOVE; LOVE + BIRD gives LOVEBIRD.
"""

from __future__ import annotations

import argparse
from datetime import datetime


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
HORSE_ANCHOR = (3, 2)
PHOTO_LIKES = (24, 31, 19, 42)
PHOTO1_COLOURS = "赤橙黄绿青蓝紫"
CONDITIONAL_HORSE = (2, 3)
LIKE_ICON = "🤍"
CURRENT_CANDIDATE = "LOVEBIRD"


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
    animals = known_nonhorse_animals(e)
    animal_letters = {animal: row_major_letter(position) for animal, position in animals.items()}
    conditional_animals = {"horse": CONDITIONAL_HORSE, **animals}
    conditional_letters = {
        animal: row_major_letter(position)
        for animal, position in conditional_animals.items()
    }
    framed, question, question_char = photo2_target_state(e)
    a_to_y, polybius, raw_cell, raw_coordinate = direct_encodings(cell, row, column)
    target_colour = PHOTO1_COLOURS[(e + 3) % len(PHOTO1_COLOURS)]

    if target == DEFAULT_TARGET:
        assert e == -34_892_632
        assert e % 25 == 18
        assert (cell, row, column) == (19, 4, 4)
        assert (framed, question, question_char) == ("百家姓", 8, "飞")
        assert (a_to_y, polybius, raw_cell, raw_coordinate) == ("S", "T", 19, 44)
        assert target_colour == "蓝"
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

    print("stage\tinput\tcalculation\toutput")
    print(f"photo4\tE={PHOTO4_PHASE}; " + "/".join("".join(r) for r in rows) + f"\tone-based differences\t{values[0]}.{values[1]}{values[2]}=π")
    print(f"intermediate\t阿/飞/正/传\tconcatenate\t阿飞正传")
    print(f"target\t阿飞正传 famous lines\tminute + object\t{target:%Y-%m-%d %H:%M}; 鸟")
    print(f"offset\tanchor={ANCHOR:%Y-%m-%d %H:%M}\ttarget-anchor\tE={e}; E mod25={e % 25}")
    print(f"photo2_target\tE mod14={e % 14}\tcaption frames + question\t{framed}=S; cell={question}→{question_char}")
    print(f"bird\t(2E+7) mod25\tzero-based={(2 * e + 7) % 25}\tcell={cell}; coordinate=({row},{column})")
    print(f"target_maze_control\tE mod140={e % 140}\tcompare solvable phases {MAZE_SOLVABLE_PHASES}\tno traversable route at target minute")
    print(f"raw_position\tvisible row={row}; column={column}\tconcatenate the two displayed coordinates\t{raw_coordinate} (rejected)")
    print(f"row_major_value\tbird zero-based cell={(2 * e + 7) % 25}\tconvert page orbit to one-based cell\t{raw_cell}")
    print(f"photo3_like_check\tmaze post fixed likes={PHOTO_LIKES[2]}\tcompare with one-based bird cell\t{raw_cell}={PHOTO_LIKES[2]}")
    print(f"rejected_alphabet_suffix\trow-major cell={cell}\t19th alphabet letter\t{a_to_y} (S, BLUES and BIRDS all rejected; family stopped)")
    print(f"rejected_polybius\tcoordinate=({row},{column})\tstandard I/J-combined 5×5 Polybius square\t{polybius} (rejected)")
    print("animal_alphabet_control\tfully recovered non-horse tracks\tA-Y row-major\t" + "; ".join(f"{animal}={animals[animal]}→{animal_letters[animal]}" for animal in ("goat", "fish", "tiger", "bird")) + " (EOUS only; horse cell and ordering are not recovered)")
    print(f"horse_overlap_control\thorse anchor={HORSE_ANCHOR}; target is {e % 25} knight moves later\tchessboard parity\tno overlap with bird ({row},{column})")
    print(f"rejected_lookup\trow-major cell={cell}; coordinate={raw_coordinate}\tS{cell}; S{raw_coordinate}\t{BAIJIA_PREFIX[cell - 1]}; {BAIJIA_PREFIX[raw_coordinate - 1]} (both rejected)")
    print(f"rejected_number\tcell={raw_cell}; maze-post likes={PHOTO_LIKES[2]}\twrite 19 as digits or an English cardinal\t19 / NINETEEN (both rejected)")
    print(f"thematic_control\tfootless-bird line; title Carpe Diem\tdeath / Memento Mori association\t死/死亡/MEMENTO MORI (thematic only)")
    print("rejected_wall_state\ttwo non-target captures enclose (4,4)-(4,5)\textrapolate the walls and lexicalize the enclosure\tCAGED BIRD (rejected; target wall phase was never reproduced)")
    print("object_word\tsecond famous line specifies 鸟\ttranslate the selected object\tBIRD")
    print(f"target_colour\ttarget photo1 colour={target_colour}; visible bird emoji is also blue\ttranslate 蓝\tBLUE")
    print(f"rejected_suffix_compositions\tcell {cell}={a_to_y}\tBLUE + {a_to_y}; BIRD + {a_to_y}\tBLUES / BIRDS (both rejected)")
    print("rejected_direct_compound\ttarget colour BLUE + selected object BIRD\tBLUE + BIRD\tBLUEBIRD (rejected)")
    print("rejected_music\tcoordinate=(4,4)\tread as a 4/4 time signature\tCOMMON TIME (rejected)")
    print("rejected_conditional_horse\tretained knight-walk anchors allow 12 target cells\tadd one-animal-per-row constraint\t(2,3)→H (not forced by the horse data)")
    print("rejected_conditional_house\tconditional horse=H plus E/O/U/S from the recovered tracks\tA-Y cells, then reorder\tHOUSE (unsupported intermediate; do not submit)")
    print("rejected_animal_compound\tfamous-line object BIRD + conditional grid word HOUSE\tBIRD + HOUSE\tBIRDHOUSE (rejected; whole animal-grid compound family stopped)")
    print(f"like_icon\tmaze post action is {LIKE_ICON}; fixed likes={PHOTO_LIKES[2]}\tmatch bird cell {cell} to likes, then read the visible heart concept\t{raw_cell}={PHOTO_LIKES[2]}→LOVE")
    print(f"current_candidate\tLOVE from the matched like/heart field + selected object BIRD\tform the common singular compound\t{CURRENT_CANDIDATE}")


if __name__ == "__main__":
    main()
