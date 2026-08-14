#!/usr/bin/env python3
"""Recover the 12x12 text grid and locate the ten orthogonal fire sources."""

from __future__ import annotations

import argparse
from functools import reduce
import math
from pathlib import Path
import sys
import time

from z3 import Bool, If, Int, Not, Optimize, Or, Solver, Sum, Xor, sat


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


RESTORED_TEXT = (
    "一场大火把这道题烧成了残骸。"
    "这些字本应该被排成一个方阵，但题中所有字都发生了位移。"
    "想要解开这道谜题，你可能需要暴力穷举来复原这道题的题面。"
    "每团火都烧毁了自身和周围四个格子。"
    "为了得到答案，你应该先定位每团火所在的位置，然后，"
    "让盘面继续燃烧直到只剩两个字，它们会指向一个与本题有关的十字母词。"
)

SURVIVING_TEXT = (
    "一场这道了残骸。这字本应该排一个方阵但题中所有生了想要"
    "解开这谜题，你能需要暴力穷举复原道题的题面。每都自身和"
    "周围四个子。了得答案，你应该先定位每在置，然后，让盘继"
    "到只剩两字，它们向一个与关的十字母词。"
)


def neighbors(index: int, side: int, wrap: bool, shape: str) -> list[int]:
    row, col = divmod(index, side)
    if shape == "plus":
        offsets = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
    else:
        offsets = ((0, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))

    if wrap:
        return sorted(
            {
                ((row + row_delta) % side) * side + (col + col_delta) % side
                for row_delta, col_delta in offsets
            }
        )

    return [
        (row + row_delta) * side + col + col_delta
        for row_delta, col_delta in offsets
        if 0 <= row + row_delta < side and 0 <= col + col_delta < side
    ]


def layout_order(side: int, layout: str) -> list[int]:
    if layout == "row":
        return list(range(side * side))
    if layout == "snake":
        return [
            row * side + (col if row % 2 == 0 else side - 1 - col)
            for row in range(side)
            for col in range(side)
        ]

    order = []
    top, bottom, left, right = 0, side - 1, 0, side - 1
    while top <= bottom and left <= right:
        order.extend(top * side + col for col in range(left, right + 1))
        top += 1
        order.extend(row * side + right for row in range(top, bottom + 1))
        right -= 1
        if top <= bottom:
            order.extend(bottom * side + col for col in range(right, left - 1, -1))
            bottom -= 1
        if left <= right:
            order.extend(row * side + left for row in range(bottom, top - 1, -1))
            left += 1
    return order


def distance_to_sources(
    index: int, source_indices: list[int], side: int, wrap: bool
) -> int:
    row, col = divmod(index, side)
    distances = []
    for source in source_indices:
        source_row, source_col = divmod(source, side)
        row_distance = abs(row - source_row)
        col_distance = abs(col - source_col)
        if wrap:
            row_distance = min(row_distance, side - row_distance)
            col_distance = min(col_distance, side - col_distance)
        distances.append(row_distance + col_distance)
    return min(distances)


def board_text(text: str, side: int) -> str:
    return "\n".join(text[row * side : (row + 1) * side] for row in range(side))


def candidate_gap_sizes() -> dict[int, int]:
    """Return observed-character offsets and gap sizes in the prose restoration."""
    gaps = {}
    restored_offset = 0
    previous_position = -1
    for surviving_offset, char in enumerate(SURVIVING_TEXT):
        restored_offset = RESTORED_TEXT.index(char, restored_offset)
        if restored_offset > previous_position + 1:
            gaps[surviving_offset] = restored_offset - previous_position - 1
        previous_position = restored_offset
        restored_offset += 1
    return gaps


def candidate_gap_offsets() -> set[int]:
    return set(candidate_gap_sizes())


def advance_gap_automaton(
    state: tuple[int, int],
    burn_mask: int,
    side: int,
    gap_bounds: dict[int, tuple[int, int]],
) -> tuple[int, int] | None:
    observed, current_gap = state
    for col in range(side):
        burned = (burn_mask >> col) & 1
        if burned:
            bounds = gap_bounds.get(observed)
            if bounds is None or current_gap >= bounds[1]:
                return None
            current_gap += 1
        else:
            if observed >= len(SURVIVING_TEXT):
                return None
            bounds = gap_bounds.get(observed)
            if bounds is not None and current_gap < bounds[0]:
                return None
            observed += 1
            current_gap = 0
    return observed, current_gap


def advance_gap_automaton_cost(
    state: tuple[int, int],
    burn_mask: int,
    side: int,
    gap_bounds: dict[int, tuple[int, int]],
    candidate_gaps: dict[int, int],
) -> tuple[tuple[int, int], int] | None:
    observed, current_gap = state
    cost = 0
    for col in range(side):
        burned = (burn_mask >> col) & 1
        if burned:
            bounds = gap_bounds.get(observed)
            if bounds is None or current_gap >= bounds[1]:
                return None
            current_gap += 1
        else:
            if observed >= len(SURVIVING_TEXT):
                return None
            bounds = gap_bounds.get(observed)
            if bounds is not None and current_gap < bounds[0]:
                return None
            if observed in candidate_gaps:
                cost += abs(current_gap - candidate_gaps[observed])
            observed += 1
            current_gap = 0
    return (observed, current_gap), cost


def advance_any_gap_cost(
    state: tuple[int, int],
    burn_mask: int,
    side: int,
    expected_gaps: dict[int, int],
    max_gap: int,
    unexpected_penalty: int,
    unexpected_open_penalty: int,
) -> tuple[tuple[int, int], int] | None:
    observed, current_gap = state
    cost = 0
    for col in range(side):
        burned = (burn_mask >> col) & 1
        if burned:
            if observed == 0 or observed >= len(SURVIVING_TEXT) or current_gap >= max_gap:
                return None
            current_gap += 1
        else:
            if observed >= len(SURVIVING_TEXT):
                return None
            if observed in expected_gaps:
                cost += abs(current_gap - expected_gaps[observed])
            elif current_gap:
                cost += (
                    current_gap * unexpected_penalty + unexpected_open_penalty
                )
            observed += 1
            current_gap = 0
    return (observed, current_gap), cost


def horizontal_burn(source_mask: int, side: int, wrap: bool) -> int:
    full_mask = (1 << side) - 1
    result = source_mask | ((source_mask << 1) & full_mask) | (source_mask >> 1)
    if wrap:
        if source_mask & 1:
            result |= 1 << (side - 1)
        if source_mask & (1 << (side - 1)):
            result |= 1
    return result


def submasks(mask: int):
    value = mask
    while True:
        yield value
        if value == 0:
            return
        value = (value - 1) & mask


def summarize_prefix_states(
    states: dict[tuple[int, int, int, int, int], tuple[int, ...]],
    processed_rows: int,
    side: int,
    limit: int,
    max_sources: int,
) -> None:
    candidate_gaps = candidate_gap_sizes()
    signatures = {}
    for path in states.values():
        if sum(source_mask.bit_count() for source_mask in path) > max_sources:
            continue
        burn_bits = []
        for row in range(processed_rows):
            above = path[row - 1] if row else 0
            here = path[row]
            below = path[row + 1]
            burn_mask = horizontal_burn(here, side, False) | above | below
            burn_bits.extend((burn_mask >> col) & 1 for col in range(side))

        observed = 0
        current_gap = 0
        gaps = {}
        for burned in burn_bits:
            if burned:
                current_gap += 1
            else:
                if current_gap:
                    gaps[observed] = current_gap
                observed += 1
                current_gap = 0

        completed_offsets = [offset for offset in candidate_gaps if offset < observed]
        score = sum(
            abs(gaps.get(offset, 0) - candidate_gaps[offset])
            for offset in completed_offsets
        )
        signature = (observed, tuple(sorted(gaps.items())), current_gap)
        previous = signatures.get(signature)
        if previous is None or score < previous[0]:
            signatures[signature] = (score, path)

    ranked = sorted(
        (score, signature, path) for signature, (score, path) in signatures.items()
    )
    print(
        f"prefix summary: {len(signatures)} unique burn/gap signatures; "
        f"showing {min(limit, len(ranked))}"
    )
    for rank, (score, signature, path) in enumerate(ranked[:limit], 1):
        observed, gaps, trailing = signature
        gap_text = ",".join(f"{offset}:{size}" for offset, size in gaps)
        source_text = ";".join(
            f"R{row + 1}C{col + 1}"
            for row, source_mask in enumerate(path)
            for col in range(side)
            if (source_mask >> col) & 1
        )
        print(
            f"{rank:02d} score={score} observed={observed} "
            f"gaps=[{gap_text}] trailing={trailing} sources={source_text}"
        )


def row_dp_solve(args: argparse.Namespace) -> int:
    if args.layout != "row" or args.shape != "plus":
        raise ValueError("row-dp currently supports only row layout and plus-shaped fires")
    if args.wrap:
        return row_dp_wrap_solve(args)

    side = args.grid
    full_mask = (1 << side) - 1
    candidate_gaps = candidate_gap_sizes()
    gap_bounds = {
        offset: (
            max(0, gap_size - args.gap_slack),
            min(args.max_gap, gap_size + args.gap_slack),
        )
        for offset, gap_size in candidate_gaps.items()
    }
    transition_cache: dict[tuple[int, int], list[tuple[int, tuple[int, int]]]] = {}

    def transitions(state: tuple[int, int]):
        if state not in transition_cache:
            options = []
            for burn_mask in range(full_mask + 1):
                next_state = advance_gap_automaton(
                    state, burn_mask, side, gap_bounds
                )
                if next_state is not None:
                    options.append((burn_mask, next_state))
            transition_cache[state] = options
        return transition_cache[state]

    started = time.monotonic()
    source_masks = sorted(range(full_mask + 1), key=int.bit_count)
    states: dict[tuple[int, int, int, int, int], tuple[int, ...]] = {}
    for first_mask in source_masks:
        source_count = first_mask.bit_count()
        if source_count <= args.sources:
            states[(0, first_mask, 0, 0, source_count)] = (first_mask,)

    explored = 0
    solution_rows: tuple[int, ...] | None = None
    solution_burn_rows: tuple[int, ...] | None = None

    for row in range(side):
        next_states: dict[tuple[int, int, int, int, int], tuple[int, ...]] = {}
        for (previous, current, observed, current_gap, source_count), path in states.items():
            base_burn = horizontal_burn(current, side, False) | previous
            for burn_mask, next_automaton in transitions((observed, current_gap)):
                explored += 1
                if explored > args.max_transitions or (
                    time.monotonic() - started > args.timeout_ms / 1000
                ):
                    print(
                        f"row-dp stopped after {explored} transitions and "
                        f"{time.monotonic() - started:.2f}s"
                    )
                    return 2
                if base_burn & ~burn_mask:
                    continue

                required_next = burn_mask & ~base_burn
                optional_next = burn_mask & base_burn
                next_candidates = (0,) if row == side - 1 else submasks(optional_next)
                for optional in next_candidates:
                    next_source = required_next | optional
                    if row == side - 1 and next_source:
                        continue
                    next_count = source_count + next_source.bit_count()
                    if next_count > args.sources:
                        continue
                    if row < side - 1 and args.prefix_source_slack >= 0:
                        chosen_source_rows = row + 2
                        prefix_cap = (
                            math.ceil(args.sources * chosen_source_rows / side)
                            + args.prefix_source_slack
                        )
                        if next_count > prefix_cap:
                            continue

                    if row == side - 1:
                        if (
                            next_count == args.sources
                            and next_automaton == (len(SURVIVING_TEXT), 0)
                        ):
                            solution_rows = path
                            burn_rows = []
                            for burn_row_index in range(side):
                                above = solution_rows[burn_row_index - 1] if burn_row_index else 0
                                here = solution_rows[burn_row_index]
                                below = (
                                    solution_rows[burn_row_index + 1]
                                    if burn_row_index + 1 < side
                                    else 0
                                )
                                burn_rows.append(
                                    horizontal_burn(here, side, False) | above | below
                                )
                            solution_burn_rows = tuple(burn_rows)
                            break
                    else:
                        key = (
                            current,
                            next_source,
                            next_automaton[0],
                            next_automaton[1],
                            next_count,
                        )
                        next_states.setdefault(key, path + (next_source,))
                if solution_rows is not None:
                    break
            if solution_rows is not None:
                break
        if solution_rows is not None:
            break
        states = next_states
        print(f"row {row + 1}: {len(states)} states; {explored} transitions")
        if args.prefix_rows == row + 1:
            summarize_prefix_states(
                states,
                row + 1,
                side,
                args.prefix_limit,
                args.prefix_max_sources,
            )
            return 0
        if len(states) > args.max_states:
            print(f"row-dp state cap exceeded: {len(states)} > {args.max_states}")
            return 2
        if not states:
            break

    if solution_rows is None or solution_burn_rows is None:
        print(
            f"row-dp found no model after {explored} transitions and "
            f"{time.monotonic() - started:.2f}s"
        )
        return 1

    source_indices = [
        row * side + col
        for row, source_mask in enumerate(solution_rows)
        for col in range(side)
        if (source_mask >> col) & 1
    ]
    burned_indices = [
        row * side + col
        for row, burn_mask in enumerate(solution_burn_rows)
        for col in range(side)
        if (burn_mask >> col) & 1
    ]
    kept_indices = sorted(set(range(side * side)) - set(burned_indices))
    source_labels = [f"R{index // side + 1}C{index % side + 1}" for index in source_indices]

    print("ROW-DP MODEL")
    print("Sources:", ", ".join(source_labels))
    print("Burned cells:", len(burned_indices))
    surviving_offset = 0
    for row in range(side):
        rendered = []
        for col in range(side):
            index = row * side + col
            if index in source_indices:
                rendered.append("火")
            elif index in burned_indices:
                rendered.append("·")
            else:
                rendered.append(SURVIVING_TEXT[surviving_offset])
                surviving_offset += 1
        print("".join(rendered))

    print("Nonzero gaps (left|right: length):")
    previous_kept = -1
    for surviving_offset, index in enumerate(kept_indices):
        gap_size = index - previous_kept - 1
        if gap_size and surviving_offset:
            print(
                f"{surviving_offset:03d} "
                f"{SURVIVING_TEXT[surviving_offset - 1]}|"
                f"{SURVIVING_TEXT[surviving_offset]}: {gap_size}"
            )
        previous_kept = index

    result_path = Path(args.result)
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(
        "model\tsources_1_based\tburned\n"
        f"1\t{';'.join(source_labels)}\t{len(burned_indices)}\n",
        encoding="utf-8",
    )
    print(f"Wrote {result_path}")
    return 0


def row_dp_wrap_solve(args: argparse.Namespace) -> int:
    side = args.grid
    full_mask = (1 << side) - 1
    candidate_gaps = candidate_gap_sizes()
    gap_bounds = {
        offset: (
            max(0, gap_size - args.gap_slack),
            min(args.max_gap, gap_size + args.gap_slack),
        )
        for offset, gap_size in candidate_gaps.items()
    }
    transition_cache: dict[
        tuple[int, int], list[tuple[int, tuple[int, int], int]]
    ] = {}

    def transitions(state: tuple[int, int]):
        if state not in transition_cache:
            options = []
            for burn_mask in range(full_mask + 1):
                advanced = advance_gap_automaton_cost(
                    state, burn_mask, side, gap_bounds, candidate_gaps
                )
                if advanced is not None:
                    next_state, cost = advanced
                    options.append((burn_mask, next_state, cost))
            transition_cache[state] = options
        return transition_cache[state]

    started = time.monotonic()
    row_masks = [
        mask
        for mask in range(full_mask + 1)
        if mask.bit_count() <= args.max_row_sources
    ]
    states: dict[
        tuple[int, int, int, int, int, int, int], tuple[int, tuple[int, ...]]
    ] = {}
    explored = 0

    for seam in row_masks:
        for first in row_masks:
            base_burn = horizontal_burn(first, side, True) | seam
            for burn_mask, next_automaton, transition_cost in transitions((0, 0)):
                explored += 1
                if base_burn & ~burn_mask:
                    continue
                required_next = burn_mask & ~base_burn
                optional_next = burn_mask & base_burn
                for optional in submasks(optional_next):
                    next_source = required_next | optional
                    if next_source.bit_count() > args.max_row_sources:
                        continue
                    source_count = (
                        seam.bit_count()
                        + first.bit_count()
                        + next_source.bit_count()
                    )
                    if source_count > args.sources:
                        continue
                    key = (
                        seam,
                        first,
                        first,
                        next_source,
                        next_automaton[0],
                        next_automaton[1],
                        source_count,
                    )
                    candidate = (transition_cost, (first, next_source))
                    previous_candidate = states.get(key)
                    if previous_candidate is None or candidate[0] < previous_candidate[0]:
                        states[key] = candidate

    print(f"wrapped row 1: {len(states)} states; {explored} transitions")
    if len(states) > args.max_states:
        print(f"wrapped row-dp state cap exceeded: {len(states)}")
        return 2

    for row in range(1, side - 2):
        next_states = {}
        for (
            seam,
            first,
            previous,
            current,
            observed,
            current_gap,
            source_count,
        ), (accumulated_cost, path) in states.items():
            base_burn = horizontal_burn(current, side, True) | previous
            for burn_mask, next_automaton, transition_cost in transitions(
                (observed, current_gap)
            ):
                explored += 1
                if explored > args.max_transitions or (
                    time.monotonic() - started > args.timeout_ms / 1000
                ):
                    print(
                        f"wrapped row-dp stopped after {explored} transitions and "
                        f"{time.monotonic() - started:.2f}s"
                    )
                    return 2
                if base_burn & ~burn_mask:
                    continue
                required_next = burn_mask & ~base_burn
                optional_next = burn_mask & base_burn
                for optional in submasks(optional_next):
                    next_source = required_next | optional
                    if next_source.bit_count() > args.max_row_sources:
                        continue
                    next_count = source_count + next_source.bit_count()
                    if next_count > args.sources:
                        continue
                    key = (
                        seam,
                        first,
                        current,
                        next_source,
                        next_automaton[0],
                        next_automaton[1],
                        next_count,
                    )
                    candidate = (
                        accumulated_cost + transition_cost,
                        path + (next_source,),
                    )
                    previous_candidate = next_states.get(key)
                    if previous_candidate is None or candidate[0] < previous_candidate[0]:
                        next_states[key] = candidate
        states = next_states
        print(f"wrapped row {row + 1}: {len(states)} states; {explored} transitions")
        if len(states) > args.max_states:
            print(f"wrapped row-dp state cap exceeded: {len(states)}")
            return 2
        if not states:
            break

    solution_rows = None
    solution_cost = None
    for (
        seam,
        first,
        previous,
        current,
        observed,
        current_gap,
        source_count,
    ), (accumulated_cost, path) in states.items():
        burn_row_10 = horizontal_burn(current, side, True) | previous | seam
        advanced_10 = advance_gap_automaton_cost(
            (observed, current_gap),
            burn_row_10,
            side,
            gap_bounds,
            candidate_gaps,
        )
        if advanced_10 is None:
            continue
        next_automaton, cost_10 = advanced_10
        burn_row_11 = horizontal_burn(seam, side, True) | current | first
        advanced_11 = advance_gap_automaton_cost(
            next_automaton, burn_row_11, side, gap_bounds, candidate_gaps
        )
        if advanced_11 is None:
            continue
        final_automaton, cost_11 = advanced_11
        if (
            source_count == args.sources
            and final_automaton == (len(SURVIVING_TEXT), 0)
        ):
            total_cost = accumulated_cost + cost_10 + cost_11
            if solution_cost is None or total_cost < solution_cost:
                solution_cost = total_cost
                solution_rows = path + (seam,)

    if solution_rows is None:
        print(
            f"wrapped row-dp found no model after {explored} transitions and "
            f"{time.monotonic() - started:.2f}s"
        )
        return 1

    burn_rows = []
    for row in range(side):
        above = solution_rows[(row - 1) % side]
        here = solution_rows[row]
        below = solution_rows[(row + 1) % side]
        burn_rows.append(horizontal_burn(here, side, True) | above | below)

    source_indices = [
        row * side + col
        for row, source_mask in enumerate(solution_rows)
        for col in range(side)
        if (source_mask >> col) & 1
    ]
    burned_indices = [
        row * side + col
        for row, burn_mask in enumerate(burn_rows)
        for col in range(side)
        if (burn_mask >> col) & 1
    ]
    kept_indices = sorted(set(range(side * side)) - set(burned_indices))
    source_labels = [f"R{index // side + 1}C{index % side + 1}" for index in source_indices]
    print("WRAPPED ROW-DP MODEL")
    print("Gap-distance cost:", solution_cost)
    print("Sources:", ", ".join(source_labels))
    print("Burned cells:", len(burned_indices))
    surviving_offset = 0
    for row in range(side):
        rendered = []
        for col in range(side):
            index = row * side + col
            if index in source_indices:
                rendered.append("火")
            elif index in burned_indices:
                rendered.append("·")
            else:
                rendered.append(SURVIVING_TEXT[surviving_offset])
                surviving_offset += 1
        print("".join(rendered))
    print("Nonzero gaps (left|right: length):")
    previous_kept = -1
    for surviving_offset, index in enumerate(kept_indices):
        gap_size = index - previous_kept - 1
        if gap_size and surviving_offset:
            print(
                f"{surviving_offset:03d} "
                f"{SURVIVING_TEXT[surviving_offset - 1]}|"
                f"{SURVIVING_TEXT[surviving_offset]}: {gap_size}"
            )
        previous_kept = index

    result_path = Path(args.result)
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(
        "model\tsources_1_based\tburned\n"
        f"1\t{';'.join(source_labels)}\t{len(burned_indices)}\n",
        encoding="utf-8",
    )
    print(f"Wrote {result_path}")
    return 0


def beam_dp_solve(args: argparse.Namespace) -> int:
    if args.layout != "row" or args.shape != "plus" or args.combine != "union":
        raise ValueError("beam-dp supports row layout, plus fires, and union")
    if args.wrap:
        raise ValueError("beam-dp currently supports bounded, non-wrapping edges")

    side = args.grid
    full_mask = (1 << side) - 1
    expected_gaps = candidate_gap_sizes()
    row_masks = [
        mask
        for mask in range(full_mask + 1)
        if mask.bit_count() <= args.max_row_sources
    ]
    started = time.monotonic()
    explored = 0
    transition_cache = {}

    def advance(state: tuple[int, int], burn_mask: int):
        key = (state, burn_mask)
        if key not in transition_cache:
            transition_cache[key] = advance_any_gap_cost(
                state,
                burn_mask,
                side,
                expected_gaps,
                args.max_gap,
                args.unexpected_gap_penalty,
                args.unexpected_gap_open_penalty,
            )
        return transition_cache[key]

    states: dict[
        tuple[int, int, int, int, int], tuple[int, tuple[int, ...]]
    ] = {}
    for first in row_masks:
        for second in row_masks:
            source_count = first.bit_count() + second.bit_count()
            if source_count > args.sources:
                continue
            burn_mask = horizontal_burn(first, side, False) | second
            advanced = advance((0, 0), burn_mask)
            explored += 1
            if advanced is None:
                continue
            next_automaton, transition_cost = advanced
            key = (
                first,
                second,
                next_automaton[0],
                next_automaton[1],
                source_count,
            )
            candidate = (transition_cost, (first, second))
            previous_candidate = states.get(key)
            if previous_candidate is None or candidate[0] < previous_candidate[0]:
                states[key] = candidate

    print(f"beam row 1: {len(states)} states; {explored} transitions")

    for row in range(1, side - 1):
        next_states = {}
        for (
            previous,
            current,
            observed,
            current_gap,
            source_count,
        ), (accumulated_cost, path) in states.items():
            for next_source in row_masks:
                explored += 1
                if explored > args.max_transitions or (
                    time.monotonic() - started > args.timeout_ms / 1000
                ):
                    print(
                        f"beam-dp stopped after {explored} transitions and "
                        f"{time.monotonic() - started:.2f}s"
                    )
                    return 2
                next_count = source_count + next_source.bit_count()
                remaining_source_rows = side - (len(path) + 1)
                if next_count > args.sources:
                    continue
                if next_count + remaining_source_rows * args.max_row_sources < args.sources:
                    continue
                burn_mask = (
                    horizontal_burn(current, side, False) | previous | next_source
                )
                advanced = advance((observed, current_gap), burn_mask)
                if advanced is None:
                    continue
                next_automaton, transition_cost = advanced
                key = (
                    current,
                    next_source,
                    next_automaton[0],
                    next_automaton[1],
                    next_count,
                )
                candidate = (
                    accumulated_cost + transition_cost,
                    path + (next_source,),
                )
                previous_candidate = next_states.get(key)
                if previous_candidate is None or candidate[0] < previous_candidate[0]:
                    next_states[key] = candidate

        if len(next_states) > args.beam_size:
            ranked = sorted(next_states.items(), key=lambda item: item[1][0])
            next_states = dict(ranked[: args.beam_size])
        states = next_states
        best_cost = min((value[0] for value in states.values()), default=None)
        print(
            f"beam row {row + 1}: {len(states)} states; best_cost={best_cost}; "
            f"{explored} transitions"
        )
        if not states:
            break

    solution_rows = None
    solution_cost = None
    for (
        previous,
        current,
        observed,
        current_gap,
        source_count,
    ), (accumulated_cost, path) in states.items():
        if source_count != args.sources:
            continue
        burn_mask = horizontal_burn(current, side, False) | previous
        advanced = advance((observed, current_gap), burn_mask)
        if advanced is None:
            continue
        final_automaton, transition_cost = advanced
        if final_automaton != (len(SURVIVING_TEXT), 0):
            continue
        total_cost = accumulated_cost + transition_cost
        if solution_cost is None or total_cost < solution_cost:
            solution_cost = total_cost
            solution_rows = path

    if solution_rows is None:
        print(
            f"beam-dp found no model after {explored} transitions and "
            f"{time.monotonic() - started:.2f}s"
        )
        return 1

    burn_rows = []
    for row in range(side):
        above = solution_rows[row - 1] if row else 0
        here = solution_rows[row]
        below = solution_rows[row + 1] if row + 1 < side else 0
        burn_rows.append(horizontal_burn(here, side, False) | above | below)
    source_indices = [
        row * side + col
        for row, source_mask in enumerate(solution_rows)
        for col in range(side)
        if (source_mask >> col) & 1
    ]
    burned_indices = [
        row * side + col
        for row, burn_mask in enumerate(burn_rows)
        for col in range(side)
        if (burn_mask >> col) & 1
    ]
    kept_indices = sorted(set(range(side * side)) - set(burned_indices))
    source_labels = [f"R{index // side + 1}C{index % side + 1}" for index in source_indices]
    print("BEAM-DP MODEL")
    print("Gap cost:", solution_cost)
    print("Sources:", ", ".join(source_labels))
    print("Burned cells:", len(burned_indices))
    surviving_offset = 0
    for row in range(side):
        rendered = []
        for col in range(side):
            index = row * side + col
            if index in source_indices:
                rendered.append("火")
            elif index in burned_indices:
                rendered.append("·")
            else:
                rendered.append(SURVIVING_TEXT[surviving_offset])
                surviving_offset += 1
        print("".join(rendered))
    print("Nonzero gaps (left|right: length):")
    previous_kept = -1
    for surviving_offset, index in enumerate(kept_indices):
        gap_size = index - previous_kept - 1
        if gap_size and surviving_offset:
            print(
                f"{surviving_offset:03d} "
                f"{SURVIVING_TEXT[surviving_offset - 1]}|"
                f"{SURVIVING_TEXT[surviving_offset]}: {gap_size}"
            )
        previous_kept = index
    result_path = Path(args.result)
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(
        "model\tgap_cost\tsources_1_based\tburned\n"
        f"1\t{solution_cost}\t{';'.join(source_labels)}\t{len(burned_indices)}\n",
        encoding="utf-8",
    )
    print(f"Wrote {result_path}")
    return 0


def cells_within_radius(index: int, radius: int, side: int, wrap: bool) -> list[int]:
    row, col = divmod(index, side)
    result = []
    for source_row in range(side):
        for source_col in range(side):
            row_distance = abs(row - source_row)
            col_distance = abs(col - source_col)
            if wrap:
                row_distance = min(row_distance, side - row_distance)
                col_distance = min(col_distance, side - col_distance)
            if row_distance + col_distance <= radius:
                result.append(source_row * side + source_col)
    return result


def geometry_final_solve(args: argparse.Namespace) -> int:
    if args.layout != "row" or args.shape != "plus" or args.combine != "union":
        raise ValueError(
            "geometry-final currently supports row layout, plus fires, and union"
        )

    side = args.grid
    cell_count = side * side
    all_rows = []
    total_models = 0

    for radius in range(args.min_radius, args.max_radius + 1):
        solver = Solver()
        solver.set(timeout=args.timeout_ms)
        sources = [Bool(f"r{radius}_source_{index:03d}") for index in range(cell_count)]
        initial_burn = [
            Or(
                [
                    sources[source]
                    for source in cells_within_radius(index, 1, side, args.wrap)
                ]
            )
            for index in range(cell_count)
        ]
        final_burn = [
            Or(
                [
                    sources[source]
                    for source in cells_within_radius(index, radius, side, args.wrap)
                ]
            )
            for index in range(cell_count)
        ]
        solver.add(Sum([If(source, 1, 0) for source in sources]) == args.sources)
        solver.add(Sum([If(burned, 1, 0) for burned in initial_burn]) == 44)
        solver.add(Sum([If(burned, 0, 1) for burned in final_burn]) == 2)

        radius_models = 0
        while radius_models < args.max_models:
            check = solver.check()
            if check != sat:
                print(f"radius {radius}: {check} after {radius_models} model(s)")
                break
            model = solver.model()
            source_indices = [
                index for index, source in enumerate(sources) if model.evaluate(source)
            ]
            burned_indices = [
                index
                for index, burned in enumerate(initial_burn)
                if model.evaluate(burned)
            ]
            kept_indices = sorted(set(range(cell_count)) - set(burned_indices))
            final_indices = [
                index
                for index, burned in enumerate(final_burn)
                if not model.evaluate(burned)
            ]
            assigned = {
                index: SURVIVING_TEXT[offset]
                for offset, index in enumerate(kept_indices)
            }
            score = sum(
                assigned[index] == RESTORED_TEXT[index] for index in kept_indices
            )
            source_labels = [
                f"R{index // side + 1}C{index % side + 1}"
                for index in source_indices
            ]
            last_labels = [
                f"R{index // side + 1}C{index % side + 1}:{assigned[index]}"
                for index in final_indices
            ]
            radius_models += 1
            total_models += 1
            all_rows.append(
                {
                    "radius": radius,
                    "model": radius_models,
                    "score": score,
                    "sources": source_labels,
                    "last": last_labels,
                    "burned": burned_indices,
                    "assigned": assigned,
                }
            )
            solver.add(Or([source != model.evaluate(source) for source in sources]))
        else:
            print(f"radius {radius}: stopped at {args.max_models} model(s)")

    all_rows.sort(key=lambda row: (-row["score"], row["radius"], row["model"]))
    result_path = Path(args.result)
    result_path.parent.mkdir(parents=True, exist_ok=True)
    table = ["radius\tmodel\ttext_matches\tsources_1_based\tlast_two"]
    for row in all_rows:
        table.append(
            "\t".join(
                [
                    str(row["radius"]),
                    str(row["model"]),
                    str(row["score"]),
                    ";".join(row["sources"]),
                    ";".join(row["last"]),
                ]
            )
        )
    result_path.write_text("\n".join(table) + "\n", encoding="utf-8")

    print(f"geometry-final enumerated {total_models} model(s)")
    for rank, row in enumerate(all_rows[: min(10, len(all_rows))], 1):
        print(
            f"rank {rank}: radius={row['radius']} score={row['score']}/100 "
            f"last={','.join(row['last'])} sources={','.join(row['sources'])}"
        )
    print(f"Wrote {result_path}")
    return 0 if all_rows else 1


def solve(args: argparse.Namespace) -> int:
    if args.mode == "row-dp":
        return row_dp_solve(args)
    if args.mode == "beam-dp":
        return beam_dp_solve(args)
    if args.mode == "geometry-final":
        return geometry_final_solve(args)

    side = args.grid
    cell_count = side * side
    if len(RESTORED_TEXT) != cell_count:
        raise ValueError(
            f"restored text has {len(RESTORED_TEXT)} characters, not {cell_count}"
        )

    solver = Optimize() if args.mode == "best-fit" else Solver()
    solver.set(timeout=args.timeout_ms)

    positions = [Int(f"position_{offset:03d}") for offset in range(len(SURVIVING_TEXT))]
    sources = [Bool(f"source_{index:03d}") for index in range(cell_count)]
    text_to_grid = layout_order(side, args.layout)

    for offset, char in enumerate(SURVIVING_TEXT):
        if args.mode == "exact":
            candidates = [
                index
                for index, restored_char in enumerate(RESTORED_TEXT)
                if restored_char == char
            ]
            solver.add(Or([positions[offset] == index for index in candidates]))
        else:
            solver.add(positions[offset] >= 0, positions[offset] < cell_count)
        if offset:
            solver.add(positions[offset - 1] < positions[offset])

    if args.mode == "gap-fit":
        gap_offsets = candidate_gap_offsets()
        solver.add(positions[0] == 0, positions[-1] == cell_count - 1)
        for offset in range(1, len(positions)):
            gap_size = positions[offset] - positions[offset - 1] - 1
            if offset in gap_offsets:
                solver.add(gap_size >= 0, gap_size <= args.max_gap)
            else:
                solver.add(gap_size == 0)

    solver.add(Sum([If(source, 1, 0) for source in sources]) == args.sources)

    for index in range(cell_count):
        if args.mode == "exact":
            possible_positions = [
                positions[offset]
                for offset, char in enumerate(SURVIVING_TEXT)
                if char == RESTORED_TEXT[index]
            ]
        else:
            possible_positions = positions
        kept = Or([position == index for position in possible_positions])
        grid_index = text_to_grid[index]
        affecting_sources = [
            sources[source]
            for source in neighbors(grid_index, side, args.wrap, args.shape)
        ]
        burned = (
            reduce(Xor, affecting_sources)
            if args.combine == "xor"
            else Or(affecting_sources)
        )
        solver.add(kept == Not(burned))

    match_terms = []
    for offset, char in enumerate(SURVIVING_TEXT):
        matching_indices = [
            index for index, restored_char in enumerate(RESTORED_TEXT) if restored_char == char
        ]
        match_terms.append(
            If(Or([positions[offset] == index for index in matching_indices]), 1, 0)
        )
    match_score = Sum(match_terms)
    if args.mode == "best-fit":
        solver.maximize(match_score)

    result_path = Path(args.result)
    result_path.parent.mkdir(parents=True, exist_ok=True)
    rows = ["model\tmatches\tsources_1_based\tburned\tstop_radius\tlast_two"]
    model_count = 0

    print(
        f"RESTORED {side}x{side} GRID "
        f"(layout={args.layout}, shape={args.shape}, wrap={args.wrap})"
    )
    print(board_text(RESTORED_TEXT, side))
    print()

    model_limit = 1 if args.mode != "exact" else args.max_models
    while model_count < model_limit and solver.check() == sat:
        model = solver.model()
        source_indices = [
            index for index, source in enumerate(sources) if model.evaluate(source)
        ]
        kept_indices = [model.evaluate(position).as_long() for position in positions]
        burned_indices = sorted(set(range(cell_count)) - set(kept_indices))

        distances = [
            distance_to_sources(index, source_indices, side, args.wrap)
            for index in range(cell_count)
        ]
        stop_radius = None
        last_two: list[int] = []
        for radius in range(1, max(distances) + 1):
            survivors = [index for index, distance in enumerate(distances) if distance > radius]
            if len(survivors) == 2:
                stop_radius = radius
                last_two = survivors
                break

        model_count += 1
        matches = model.evaluate(match_score).as_long()
        source_labels = [f"R{index // side + 1}C{index % side + 1}" for index in source_indices]
        last_labels = [
            f"R{index // side + 1}C{index % side + 1}:{RESTORED_TEXT[index]}"
            for index in last_two
        ]
        rows.append(
            "\t".join(
                [
                    str(model_count),
                    str(matches),
                    ";".join(source_labels),
                    str(len(burned_indices)),
                    "" if stop_radius is None else str(stop_radius),
                    ";".join(last_labels),
                ]
            )
        )

        print(f"MODEL {model_count}")
        print(f"Candidate-text matches: {matches}/{len(SURVIVING_TEXT)}")
        print("Sources:", ", ".join(source_labels))
        print("Burned cells:", len(burned_indices))
        for row in range(side):
            rendered = []
            for col in range(side):
                index = row * side + col
                if index in source_indices:
                    rendered.append("火")
                elif index in burned_indices:
                    rendered.append("·")
                else:
                    rendered.append(RESTORED_TEXT[index])
            print("".join(rendered))
        print("Propagation counts (radius: survivors):")
        print(
            ", ".join(
                f"{radius}:{sum(distance > radius for distance in distances)}"
                for radius in range(1, max(distances) + 1)
            )
        )
        print("Stop radius:", stop_radius)
        print("Last two:", ", ".join(last_labels) if last_labels else "(none)")
        if args.mode == "gap-fit":
            print("Nonzero gaps (left|right: length):")
            resolved_positions = [model.evaluate(position).as_long() for position in positions]
            for offset in range(1, len(resolved_positions)):
                gap_size = resolved_positions[offset] - resolved_positions[offset - 1] - 1
                if gap_size:
                    print(
                        f"{offset:03d} "
                        f"{SURVIVING_TEXT[offset - 1]}|{SURVIVING_TEXT[offset]}: {gap_size}"
                    )
        print()

        if args.mode == "exact":
            solver.add(Or([source != model.evaluate(source) for source in sources]))

    result_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"Enumerated {model_count} model(s); wrote {result_path}")
    if args.mode == "exact" and model_count == args.max_models:
        print("Enumeration stopped at the configured model bound.")
    return 0 if model_count else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", type=int, default=12)
    parser.add_argument("--sources", type=int, default=10)
    parser.add_argument("--timeout-ms", type=int, default=60_000)
    parser.add_argument("--max-models", type=int, default=100)
    parser.add_argument("--wrap", action="store_true")
    parser.add_argument("--shape", choices=("plus", "x"), default="plus")
    parser.add_argument("--combine", choices=("union", "xor"), default="union")
    parser.add_argument("--layout", choices=("row", "snake", "spiral"), default="row")
    parser.add_argument(
        "--mode",
        choices=(
            "exact",
            "best-fit",
            "gap-fit",
            "row-dp",
            "beam-dp",
            "geometry-final",
        ),
        default="exact",
    )
    parser.add_argument("--max-gap", type=int, default=9)
    parser.add_argument("--gap-slack", type=int, default=1)
    parser.add_argument("--max-states", type=int, default=500_000)
    parser.add_argument("--max-transitions", type=int, default=10_000_000)
    parser.add_argument("--prefix-rows", type=int, default=0)
    parser.add_argument("--prefix-limit", type=int, default=30)
    parser.add_argument("--prefix-max-sources", type=int, default=10)
    parser.add_argument("--prefix-source-slack", type=int, default=-1)
    parser.add_argument("--max-row-sources", type=int, default=2)
    parser.add_argument("--beam-size", type=int, default=100_000)
    parser.add_argument("--unexpected-gap-penalty", type=int, default=3)
    parser.add_argument("--unexpected-gap-open-penalty", type=int, default=2)
    parser.add_argument("--min-radius", type=int, default=2)
    parser.add_argument("--max-radius", type=int, default=11)
    parser.add_argument(
        "--result",
        default=(
            "rounds/shi-qi-love-in-chaos/nodes/b2-embers/"
            "work/fire_results.tsv"
        ),
    )
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(solve(parse_args()))
