#!/usr/bin/env python3
"""Analyze extraction candidates induced by the three garden-sentence paths."""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict, deque
from pathlib import Path

from rows_garden import BLOOMS, find_letter_paths, make_adjacency, make_cells


PATH_QUERIES = [
    ("left", "A01", "L01", "THE COMPLEX HOUSES THREE MEN"),
    ("right", "A07", "K13", "THE OLD PLANT PLUMS BEHIND"),
    ("middle", "L04", "B07", "WHEN I HIT THE PHOTO ANGLED"),
]

TARGET = "DECELERATIONS"

OPPOSITE = {"NW": "SE", "N": "S", "NE": "SW", "SE": "NW", "S": "N", "SW": "NE"}


def point_segment_distance(
    point: tuple[float, float],
    start: tuple[float, float],
    end: tuple[float, float],
) -> tuple[float, tuple[float, float]]:
    px, py = point
    ax, ay = start
    bx, by = end
    dx, dy = bx - ax, by - ay
    denominator = dx * dx + dy * dy
    if denominator == 0:
        projection = start
    else:
        fraction = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / denominator))
        projection = (ax + fraction * dx, ay + fraction * dy)
    return math.hypot(px - projection[0], py - projection[1]), projection


def write_tsv(path: Path, rows: list[dict[str, object]], headers: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--middle-match", type=int, choices=[1, 2], default=1)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "grid" / "extraction-candidates.tsv",
    )
    parser.add_argument(
        "--final-output",
        type=Path,
        default=Path(__file__).resolve().parent / "grid" / "final-extraction.tsv",
    )
    args = parser.parse_args()

    cells = make_cells()
    adjacency = make_adjacency(cells, "edge")
    paths: dict[str, list[str]] = {}
    for label, start, end, text in PATH_QUERIES:
        matches = find_letter_paths(text, cells, adjacency, start, end)
        match_index = args.middle_match - 1 if label == "middle" else 0
        if match_index >= len(matches):
            raise ValueError(f"Missing requested {label} path match")
        paths[label] = matches[match_index]

    selected_cells = {cell_id for path in paths.values() for cell_id in path}
    selected_blooms = {cells[cell_id].bloom for cell_id in selected_cells}
    graph_distance = {cell_id: 0 for cell_id in selected_cells}
    frontier = deque(selected_cells)
    while frontier:
        current = frontier.popleft()
        for neighbor in adjacency[current]:
            if neighbor not in graph_distance:
                graph_distance[neighbor] = graph_distance[current] + 1
                frontier.append(neighbor)

    answer_by_bloom: dict[str, str] = {}
    color_by_bloom: dict[str, str] = {}
    bloom_order: list[str] = []
    for pair, color, answers in BLOOMS:
        for position, answer in enumerate(answers, start=1):
            bloom_id = f"{pair}-{position}"
            bloom_order.append(bloom_id)
            answer_by_bloom[bloom_id] = answer
            color_by_bloom[bloom_id] = color

    bloom_cells: dict[str, list] = defaultdict(list)
    for cell in cells.values():
        bloom_cells[cell.bloom].append(cell)

    segments: list[tuple[str, tuple[float, float], tuple[float, float]]] = []
    for label, path in paths.items():
        for a, b in zip(path, path[1:], strict=False):
            segments.append((label, (cells[a].x, cells[a].y), (cells[b].x, cells[b].y)))

    rows: list[dict[str, object]] = []
    for bloom_id in bloom_order:
        if bloom_id in selected_blooms:
            continue
        petals = bloom_cells[bloom_id]
        center = (
            sum(cell.x for cell in petals) / len(petals),
            sum(cell.y for cell in petals) / len(petals),
        )
        nearest_distance = float("inf")
        nearest_point = center
        nearest_label = ""
        for label, start, end in segments:
            distance, projection = point_segment_distance(center, start, end)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_point = projection
                nearest_label = label

        vx, vy = nearest_point[0] - center[0], nearest_point[1] - center[1]
        facing = max(petals, key=lambda cell: (cell.x - center[0]) * vx + (cell.y - center[1]) * vy)
        behind = next(cell for cell in petals if cell.petal == OPPOSITE[facing.petal])
        nearest_petal = min(
            petals,
            key=lambda cell: min(
                point_segment_distance((cell.x, cell.y), start, end)[0]
                for _label, start, end in segments
            ),
        )
        graph_nearest = min(petals, key=lambda cell: (graph_distance[cell.cell_id], cell.petal))
        graph_farthest = max(petals, key=lambda cell: (graph_distance[cell.cell_id], cell.petal))
        rows.append(
            {
                "bloom": bloom_id,
                "color": color_by_bloom[bloom_id],
                "answer": answer_by_bloom[bloom_id],
                "nearest_path": nearest_label,
                "distance": f"{nearest_distance:.2f}",
                "facing_petal": facing.petal,
                "facing_cell": facing.cell_id,
                "facing_letter": facing.letter,
                "behind_petal": behind.petal,
                "behind_cell": behind.cell_id,
                "behind_letter": behind.letter,
                "nearest_petal": nearest_petal.petal,
                "nearest_cell": nearest_petal.cell_id,
                "nearest_letter": nearest_petal.letter,
                "graph_nearest_petal": graph_nearest.petal,
                "graph_nearest_letter": graph_nearest.letter,
                "graph_farthest_petal": graph_farthest.petal,
                "graph_farthest_letter": graph_farthest.letter,
            }
        )

    headers = [
        "bloom",
        "color",
        "answer",
        "nearest_path",
        "distance",
        "facing_petal",
        "facing_cell",
        "facing_letter",
        "behind_petal",
        "behind_cell",
        "behind_letter",
        "nearest_petal",
        "nearest_cell",
        "nearest_letter",
        "graph_nearest_petal",
        "graph_nearest_letter",
        "graph_farthest_petal",
        "graph_farthest_letter",
    ]
    write_tsv(args.output, rows, headers)
    reverse_rows = list(reversed(rows))
    if len(reverse_rows) != len(TARGET):
        raise ValueError(f"Expected {len(TARGET)} untouched blooms, found {len(reverse_rows)}")
    final_rows: list[dict[str, object]] = []
    for order, (row, letter) in enumerate(zip(reverse_rows, TARGET, strict=True), start=1):
        answer = str(row["answer"])
        if letter not in answer:
            raise ValueError(f"{row['bloom']}={answer} cannot supply target letter {letter}")
        matching_cells = [cell for cell in bloom_cells[str(row["bloom"])] if cell.letter == letter]
        final_rows.append(
            {
                "order": order,
                "bloom": row["bloom"],
                "color": row["color"],
                "answer": answer,
                "selected_letter": letter,
                "answer_positions": "/".join(
                    str(index) for index, character in enumerate(answer, start=1) if character == letter
                ),
                "grid_cells": "/".join(cell.cell_id for cell in matching_cells),
                "petals": "/".join(cell.petal for cell in matching_cells),
            }
        )
    write_tsv(
        args.final_output,
        final_rows,
        [
            "order",
            "bloom",
            "color",
            "answer",
            "selected_letter",
            "answer_positions",
            "grid_cells",
            "petals",
        ],
    )

    # The answer enumeration supplies the word length.  Check how strongly the
    # remaining blooms constrain ordinary English words in both grid orders;
    # the flavor text resolves the small reverse-order candidate set.
    from wordfreq import top_n_list, zipf_frequency

    common_words = [word for word in top_n_list("en", 500_000) if len(word) == len(rows) and word.isalpha()]
    forward_answers = [str(row["answer"]) for row in rows]
    reverse_answers = list(reversed(forward_answers))
    forward_candidates = [
        word for word in common_words if all(letter.upper() in answer for letter, answer in zip(word, forward_answers, strict=True))
    ]
    reverse_candidates = [
        word for word in common_words if all(letter.upper() in answer for letter, answer in zip(word, reverse_answers, strict=True))
    ]
    print(f"visited blooms: {len(selected_blooms)}; untouched blooms: {len(rows)}")
    for key in (
        "facing_letter",
        "behind_letter",
        "nearest_letter",
        "graph_nearest_letter",
        "graph_farthest_letter",
    ):
        print(f"{key}: {''.join(str(row[key]) for row in rows)}")
    print(f"forward common-word candidates: {forward_candidates[:10]}")
    print(
        "reverse common-word candidates: "
        f"{[(word, zipf_frequency(word, 'en')) for word in reverse_candidates[:10]]}"
    )
    print(f"final extraction: {''.join(str(row['selected_letter']) for row in final_rows)}")
    print(f"wrote {args.output}")
    print(f"wrote {args.final_output}")


if __name__ == "__main__":
    main()
