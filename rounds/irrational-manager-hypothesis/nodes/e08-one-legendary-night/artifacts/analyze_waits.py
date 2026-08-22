"""Enumerate Washizu-mahjong concealed tiles and score every legal ron wait.

The opponent's gray tiles are transparent; blue backs are the one opaque copy
of their respective tile types.  Consequently, all blue-backed concealed tiles
must have distinct tile types, and a face-up opaque copy elsewhere rules that
type out.  This script generates complete hand shapes consistent with the
visible tiles, groups them by the actual pre-win hidden set, applies furiten,
and delegates riichi scoring to MahjongRepository/mahjong.

Run from the repository root:

    python rounds/.../artifacts/analyze_waits.py --opaque-mode faceup
    python rounds/.../artifacts/analyze_waits.py --opaque-mode ignore
"""

from __future__ import annotations

import argparse
import csv
import itertools
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path


WORK_DIR = Path(__file__).resolve().parent
VENDOR_DIR = WORK_DIR / "vendor"
if not VENDOR_DIR.exists():
    VENDOR_DIR = WORK_DIR.parent / "work" / "vendor"
sys.path.insert(0, str(VENDOR_DIR))

from mahjong.constants import EAST  # noqa: E402
from mahjong.hand_calculating.hand import HandCalculator  # noqa: E402
from mahjong.hand_calculating.hand_config import (  # noqa: E402
    HandConfig,
    OptionalRules,
)
from mahjong.meld import Meld  # noqa: E402


TILE_NAMES = (
    *(f"{n}m" for n in range(1, 10)),
    *(f"{n}p" for n in range(1, 10)),
    *(f"{n}s" for n in range(1, 10)),
    "E",
    "S",
    "W",
    "N",
    "P",
    "F",
    "C",
)
TILE_INDEX = {name: i for i, name in enumerate(TILE_NAMES)}


def tid(name: str) -> int:
    return TILE_INDEX[name]


def counts(names: list[str] | tuple[str, ...]) -> tuple[int, ...]:
    result = [0] * 34
    for name in names:
        result[tid(name)] += 1
    return tuple(result)


@dataclass(frozen=True)
class MeldSpec:
    kind: str
    tiles: tuple[str, ...]
    opened: bool = True


@dataclass(frozen=True)
class Position:
    panel: int
    known_closed: tuple[str, ...]
    unknown_count: int
    fixed_melds: tuple[MeldSpec, ...]
    dora_indicators: tuple[str, ...]
    riichi: bool
    dealer_river: frozenset[str]
    blocked_opaque: frozenset[str]
    scores: tuple[int, int, int, int]  # dealer, bottom, left, right
    riichi_pot: int


POSITIONS = (
    Position(
        panel=1,
        known_closed=("C", "C", "N", "N", "6s", "5s", "4s", "2p", "1p"),
        unknown_count=4,
        fixed_melds=(),
        dora_indicators=("2p",),
        riichi=True,
        dealer_river=frozenset(("9s", "2s", "W", "S", "P")),
        blocked_opaque=frozenset(("2p", "9s", "W", "S", "P", "E", "5s", "8s", "3m")),
        scores=(9000, 33000, 28500, 28500),
        riichi_pot=1000,
    ),
    Position(
        panel=2,
        known_closed=("7m", "9m", "9m"),
        unknown_count=10,
        fixed_melds=(),
        dora_indicators=("P",),
        riichi=True,
        dealer_river=frozenset(("9p", "4s", "1m", "9s", "F")),
        blocked_opaque=frozenset(("4s", "F", "E", "8m", "P")),
        scores=(2000, 38000, 29500, 29500),
        riichi_pot=1000,
    ),
    Position(
        panel=3,
        known_closed=("9s", "7s", "5p", "5p"),
        unknown_count=3,
        fixed_melds=(
            MeldSpec(Meld.CHI, ("2m", "3m", "4m"), True),
            MeldSpec(Meld.PON, ("P", "P", "P"), True),
        ),
        dora_indicators=("4p",),
        riichi=False,
        dealer_river=frozenset(("9p", "3s", "1s", "F")),
        blocked_opaque=frozenset(("P", "3s", "C", "F", "E", "3m")),
        scores=(9200, 33000, 28900, 28900),
        riichi_pot=0,
    ),
    Position(
        panel=4,
        known_closed=("E", "E", "7p", "7p", "6p", "2s", "2s", "7m", "9m"),
        unknown_count=4,
        fixed_melds=(),
        dora_indicators=("6m",),
        riichi=False,
        dealer_river=frozenset(("4m", "F", "6m", "1s", "P", "1p")),
        blocked_opaque=frozenset(("4m", "1s", "7p", "4s", "8p")),
        scores=(9200, 33000, 28900, 28900),
        riichi_pot=0,
    ),
    Position(
        panel=5,
        known_closed=("F", "F", "1p", "5m"),
        unknown_count=3,
        fixed_melds=(
            MeldSpec(Meld.CHI, ("3s", "4s", "5s"), True),
            MeldSpec(Meld.KAN, ("C", "C", "C", "C"), False),
        ),
        dora_indicators=("6m", "3p"),
        riichi=False,
        dealer_river=frozenset(("P", "9m", "S", "6s")),
        blocked_opaque=frozenset(("6m", "3s", "P", "1m", "7s", "C")),
        scores=(9200, 33000, 28900, 28900),
        riichi_pot=0,
    ),
)


GROUPS: list[tuple[int, ...]] = []
for suit_offset in (0, 9, 18):
    for start in range(7):
        group = [0] * 34
        for tile in (suit_offset + start, suit_offset + start + 1, suit_offset + start + 2):
            group[tile] += 1
        GROUPS.append(tuple(group))
for tile in range(34):
    group = [0] * 34
    group[tile] = 3
    GROUPS.append(tuple(group))


@dataclass
class HiddenHand:
    waits: set[int] = field(default_factory=set)


def add_vectors(*vectors: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(items) for items in zip(*vectors, strict=True))


def fixed_actual_counts(position: Position) -> tuple[int, ...]:
    result = [0] * 34
    for meld in position.fixed_melds:
        for name in meld.tiles:
            result[tid(name)] += 1
    return tuple(result)


def compatible_hidden_sets(
    closed_complete: tuple[int, ...],
    known: tuple[int, ...],
    unknown_count: int,
    blocked: set[int],
) -> list[tuple[tuple[int, ...], int]]:
    residual = [closed_complete[i] - known[i] for i in range(34)]
    if any(value < 0 for value in residual) or sum(residual) != unknown_count + 1:
        return []

    output: list[tuple[tuple[int, ...], int]] = []
    for win_tile, value in enumerate(residual):
        if value == 0:
            continue
        residual[win_tile] -= 1
        if all(value in (0, 1) for value in residual):
            hidden = tuple(i for i, value in enumerate(residual) if value)
            if len(hidden) == unknown_count and not any(tile in blocked for tile in hidden):
                output.append((hidden, win_tile))
        residual[win_tile] += 1
    return output


def enumerate_standard(position: Position, blocked: set[int], hands: dict[tuple[int, ...], HiddenHand]) -> None:
    known = counts(position.known_closed)
    fixed = fixed_actual_counts(position)
    needed_melds = 4 - len(position.fixed_melds)

    for group_indices in itertools.combinations_with_replacement(range(len(GROUPS)), needed_melds):
        grouped = [0] * 34
        valid = True
        for group_index in group_indices:
            group = GROUPS[group_index]
            for tile, value in enumerate(group):
                grouped[tile] += value
                if grouped[tile] + fixed[tile] > 4:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            continue

        for pair in range(34):
            if grouped[pair] + 2 + fixed[pair] > 4:
                continue
            complete = list(grouped)
            complete[pair] += 2
            complete_tuple = tuple(complete)
            for hidden, win_tile in compatible_hidden_sets(
                complete_tuple, known, position.unknown_count, blocked
            ):
                hands[hidden].waits.add(win_tile)


def enumerate_chiitoitsu(position: Position, blocked: set[int], hands: dict[tuple[int, ...], HiddenHand]) -> None:
    if position.fixed_melds:
        return
    known = counts(position.known_closed)
    if any(value > 2 for value in known):
        return
    forced = {tile for tile, value in enumerate(known) if value}
    if len(forced) > 7:
        return
    candidates = [tile for tile in range(34) if tile not in forced]
    for extra in itertools.combinations(candidates, 7 - len(forced)):
        pair_types = forced | set(extra)
        complete = tuple(2 if tile in pair_types else 0 for tile in range(34))
        for hidden, win_tile in compatible_hidden_sets(complete, known, position.unknown_count, blocked):
            hands[hidden].waits.add(win_tile)


def enumerate_kokushi(position: Position, blocked: set[int], hands: dict[tuple[int, ...], HiddenHand]) -> None:
    if position.fixed_melds:
        return
    terminals_honors = {0, 8, 9, 17, 18, 26, *range(27, 34)}
    known = counts(position.known_closed)
    if any(value and tile not in terminals_honors for tile, value in enumerate(known)):
        return
    for duplicate in terminals_honors:
        complete = tuple(
            (2 if tile == duplicate else 1) if tile in terminals_honors else 0
            for tile in range(34)
        )
        for hidden, win_tile in compatible_hidden_sets(complete, known, position.unknown_count, blocked):
            hands[hidden].waits.add(win_tile)


def allocate_tiles(position: Position, hidden: tuple[int, ...], win_tile: int) -> tuple[list[int], int, list[Meld]]:
    closed_counts = list(counts(position.known_closed))
    for tile in hidden:
        closed_counts[tile] += 1
    closed_counts[win_tile] += 1

    fixed = fixed_actual_counts(position)
    total = [closed_counts[i] + fixed[i] for i in range(34)]
    assert all(0 <= value <= 4 for value in total)

    pools = {tile: [tile * 4 + copy for copy in range(total[tile])] for tile in range(34)}
    used = defaultdict(int)
    melds: list[Meld] = []
    for spec in position.fixed_melds:
        meld_tiles: list[int] = []
        for name in spec.tiles:
            tile = tid(name)
            meld_tiles.append(pools[tile][used[tile]])
            used[tile] += 1
        melds.append(Meld(meld_type=spec.kind, tiles=meld_tiles, opened=spec.opened))

    concealed_ids: dict[int, list[int]] = {}
    for tile in range(34):
        concealed_ids[tile] = pools[tile][used[tile] :]
    win_id = concealed_ids[win_tile][-1]
    all_tiles = [tile_id for tile in range(34) for tile_id in pools[tile]]
    return all_tiles, win_id, melds


def score_hand(position: Position, hidden: tuple[int, ...], win_tile: int, open_tanyao: bool):
    all_tiles, win_id, melds = allocate_tiles(position, hidden, win_tile)
    config = HandConfig(
        is_riichi=position.riichi,
        player_wind=EAST,
        round_wind=EAST,
        options=OptionalRules(
            has_open_tanyao=open_tanyao,
            has_aka_dora=False,
            kiriage=False,
        ),
    )
    dora = [tid(name) * 4 for name in position.dora_indicators]
    return HandCalculator.estimate_hand_value(
        all_tiles,
        win_id,
        melds=melds,
        dora_indicators=dora,
        ura_dora_indicators=[],
        config=config,
    )


def escapes_fourth(position: Position, ron_points: int) -> bool:
    dealer, bottom, left, right = position.scores
    dealer_after = dealer + position.riichi_pot + ron_points
    # The speaker is the bottom player opposite the dealer.  A ron transfers
    # the full hand value from that player to the dealer; the two side scores
    # remain unchanged.
    others_after = (bottom - ron_points, left, right)
    return dealer_after > min(others_after)


def notation(hidden: tuple[int, ...]) -> str:
    return " ".join(TILE_NAMES[tile] for tile in hidden)


def solve_position(
    position: Position, opaque_mode: str, open_tanyao: bool
) -> tuple[list[dict[str, object]], dict[str, int], list[str]]:
    blocked = {tid(name) for name in position.blocked_opaque} if opaque_mode == "faceup" else set()
    hands: dict[tuple[int, ...], HiddenHand] = defaultdict(HiddenHand)
    enumerate_standard(position, blocked, hands)
    enumerate_chiitoitsu(position, blocked, hands)
    enumerate_kokushi(position, blocked, hands)

    river = {tid(name) for name in position.dealer_river}
    wait_rows: dict[int, dict[str, object]] = {}
    legal_hidden = 0
    furiten_hidden = 0
    hand_details: list[str] = []
    for hidden, record in hands.items():
        if record.waits & river:
            furiten_hidden += 1
            continue
        legal_hidden += 1
        qualifying_for_hand: list[str] = []
        for win_tile in record.waits:
            result = score_hand(position, hidden, win_tile, open_tanyao)
            row = wait_rows.setdefault(
                win_tile,
                {
                    "panel": position.panel,
                    "wait": TILE_NAMES[win_tile],
                    "hidden_assignments": 0,
                    "scoring_assignments": 0,
                    "qualifying_assignments": 0,
                    "min_ron": None,
                    "max_ron": 0,
                    "best_han": None,
                    "best_fu": None,
                    "best_yaku": "",
                    "example_hidden": "",
                },
            )
            row["hidden_assignments"] += 1
            if result.error:
                continue
            ron = int(result.cost["main"])
            row["scoring_assignments"] += 1
            row["min_ron"] = ron if row["min_ron"] is None else min(int(row["min_ron"]), ron)
            if escapes_fourth(position, ron):
                row["qualifying_assignments"] += 1
                qualifying_for_hand.append(f"{TILE_NAMES[win_tile]}={ron}")
            if ron > int(row["max_ron"]):
                row["max_ron"] = ron
                row["best_han"] = result.han
                row["best_fu"] = result.fu
                row["best_yaku"] = ", ".join(str(yaku) for yaku in (result.yaku or []))
                row["example_hidden"] = notation(hidden)
        if qualifying_for_hand:
            all_waits = " ".join(TILE_NAMES[tile] for tile in sorted(record.waits))
            hand_details.append(
                f"hidden=[{notation(hidden)}] waits=[{all_waits}] "
                f"qualifying=[{' '.join(qualifying_for_hand)}]"
            )

    rows = sorted(wait_rows.values(), key=lambda row: tid(str(row["wait"])))
    stats = {
        "all_hidden": len(hands),
        "legal_hidden": legal_hidden,
        "furiten_hidden": furiten_hidden,
    }
    return rows, stats, hand_details


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--opaque-mode", choices=("faceup", "ignore"), default="faceup")
    parser.add_argument("--closed-tanyao", action="store_true", help="Disable open tanyao")
    parser.add_argument(
        "--panels",
        default="1,2,3,4,5",
        help="Comma-separated panel numbers to analyze",
    )
    parser.add_argument("--show-hands", action="store_true")
    parser.add_argument("--output", type=Path, default=WORK_DIR / "mahjong_results.tsv")
    args = parser.parse_args()
    selected_panels = {int(value) for value in args.panels.split(",") if value.strip()}

    fieldnames = (
        "opaque_mode",
        "panel",
        "wait",
        "hidden_assignments",
        "scoring_assignments",
        "qualifying_assignments",
        "min_ron",
        "max_ron",
        "best_han",
        "best_fu",
        "best_yaku",
        "example_hidden",
    )
    all_rows: list[dict[str, object]] = []
    for position in POSITIONS:
        if position.panel not in selected_panels:
            continue
        rows, stats, hand_details = solve_position(position, args.opaque_mode, not args.closed_tanyao)
        print(
            f"panel {position.panel}: hidden={stats['all_hidden']} "
            f"legal={stats['legal_hidden']} furiten={stats['furiten_hidden']} waits={len(rows)}"
        )
        for row in rows:
            row["opaque_mode"] = args.opaque_mode
            qualifies = int(row["qualifying_assignments"]) > 0
            marker = "QUALIFIES" if qualifies else ""
            print(
                f"  {row['wait']:>2} assignments={row['hidden_assignments']:>4} "
                f"ron={row['min_ron']!s:>5}..{row['max_ron']!s:<5} "
                f"qualifying={row['qualifying_assignments']:>4} {marker}"
            )
            all_rows.append(row)
        if args.show_hands:
            for detail in hand_details:
                print(f"    {detail}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
