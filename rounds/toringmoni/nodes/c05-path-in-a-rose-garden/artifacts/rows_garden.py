#!/usr/bin/env python3
"""Build and validate the filled Rows Garden as a triangular-cell graph.

The source matrix is a standard 21-by-12 Rows Garden.  Every six-petal bloom
uses three consecutive letters from the row above and three from the row
below; the lower trigram is encountered in reverse when circling a bloom.
This script keeps one canonical coordinate system for later path tracing.
"""

from __future__ import annotations

import argparse
import csv
import functools
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROWS = {
    "A": "HTAWREATH",
    "B": "LYCEERIDESKCHASMLEONE",
    "C": "PMORBSHPLGERENOLEDLAM",
    "D": "UPLOADTORNADOTROOPLUA",
    "E": "OCEXSANEIMOTOBETENANT",
    "F": "PATHOSIRISROHITOPTICS",
    "G": "MOCAUSUSSGIEPOPULARET",
    "H": "ANINAESUCHTHOMSMARTER",
    "I": "POLISHTEHITOOLBELEMUS",
    # The row clue suggests CANNER, but RELISH crossing forces chunk LER.
    # Preserve the fully crossed grid as CANLER and record the anomaly.
    "J": "CANLEROKIHIMMAIHANDEL",
    "K": "ADAMECLINENCODNOVOCAL",
    "L": "ENAHWEIDS",
}


BLOOMS = [
    ("A-B", "pink", ["THEERA", "WRECKS", "THELMA"]),
    ("B-C", "white", ["COMPLY", "DELPHI", "ONEHAS", "MALONE"]),
    ("C-D", "gray", ["BROADS", "DANGER", "POOLED"]),
    ("D-E", "pink", ["COUPLE", "ORIENT", "REBOOT", "LANTAU"]),
    ("E-F", "white", ["XHOSAS", "MOTORS", "POTENT"]),
    ("F-G", "gray", ["COMPAT", "SIRIUS", "POPHIT", "STERIC"]),
    ("G-H", "pink", ["NAUSEA", "HEIGHT", "ALUMAR"]),
    ("H-I", "white", ["POLINA", "SUCHET", "BLOOMS", "SUMTER"]),
    ("I-J", "gray", ["RELISH", "HITOMI", "HELENA"]),
    ("J-K", "pink", ["CANADA", "NIKOLI", "DOMAIN", "CALLED"]),
    ("K-L", "white", ["MENACE", "WHENCE", "OVOIDS"]),
]


TERMINALS = {
    "start-top-left": "A01",
    "start-top-right": "A07",
    "start-bottom-middle": "L04",
    "end-top-middle": "B07",
    "end-bottom-left": "L01",
    "end-bottom-right": "K13",
}


@dataclass
class Cell:
    cell_id: str
    row: str
    index: int
    letter: str
    x: float
    y: float
    bloom: str
    petal: str
    polygon: tuple[tuple[float, float], ...]


def rotations(word: str) -> set[str]:
    reverse = word[::-1]
    return {
        word[i:] + word[:i] for i in range(len(word))
    } | {
        reverse[i:] + reverse[:i] for i in range(len(reverse))
    }


def cyclic_equivalent(left: str, right: str) -> bool:
    return right in rotations(left)


def chunks(row: str) -> list[str]:
    return [row[i : i + 3] for i in range(0, len(row), 3)]


def chunk_indices(pair_index: int, side: str) -> list[int]:
    count = 3 if pair_index % 2 == 0 else 4
    if side == "upper" and pair_index == 0:
        return [0, 1, 2]
    if side == "lower" and pair_index == 10:
        return [0, 1, 2]
    return [1, 3, 5] if count == 3 else [0, 2, 4, 6]


def validate_blooms() -> list[dict[str, str]]:
    table: list[dict[str, str]] = []
    row_names = list(ROWS)
    for pair_index, (pair, color, answers) in enumerate(BLOOMS):
        upper_name, lower_name = row_names[pair_index : pair_index + 2]
        upper_chunks = chunks(ROWS[upper_name])
        lower_chunks = chunks(ROWS[lower_name])
        upper_indices = chunk_indices(pair_index, "upper")
        lower_indices = chunk_indices(pair_index, "lower")
        assert len(answers) == len(upper_indices) == len(lower_indices)
        for position, (u_index, l_index, answer) in enumerate(
            zip(upper_indices, lower_indices, answers, strict=True)
        ):
            upper = upper_chunks[u_index]
            lower = lower_chunks[l_index]
            signature = upper + lower[::-1]
            if not cyclic_equivalent(answer, signature):
                raise ValueError(
                    f"Bloom mismatch {pair} #{position}: "
                    f"{upper}+reverse({lower})={signature}, expected {answer}"
                )
            table.append(
                {
                    "pair": pair,
                    "color": color,
                    "position": str(position),
                    "upper": upper,
                    "lower": lower,
                    "signature": signature,
                    "answer": answer,
                }
            )
    return table


def make_cells() -> dict[str, Cell]:
    cells: dict[str, Cell] = {}
    row_names = list(ROWS)
    half_width = 40.0
    half_height = 70.5
    first_y = 147.0

    for pair_index, (pair, _color, answers) in enumerate(BLOOMS):
        count = len(answers)
        centers_x = [296.0 + 240.0 * j for j in range(3)] if count == 3 else [176.0 + 240.0 * j for j in range(4)]
        center_y = first_y + half_height * pair_index
        upper_name, lower_name = row_names[pair_index : pair_index + 2]
        upper_indices = chunk_indices(pair_index, "upper")
        lower_indices = chunk_indices(pair_index, "lower")

        for flower_index, center_x in enumerate(centers_x):
            center = (center_x, center_y)
            vertices = {
                "ul": (center_x - half_width, center_y - half_height),
                "ur": (center_x + half_width, center_y - half_height),
                "r": (center_x + 2 * half_width, center_y),
                "lr": (center_x + half_width, center_y + half_height),
                "ll": (center_x - half_width, center_y + half_height),
                "l": (center_x - 2 * half_width, center_y),
            }
            polygons = {
                "NW": (center, vertices["l"], vertices["ul"]),
                "N": (center, vertices["ul"], vertices["ur"]),
                "NE": (center, vertices["ur"], vertices["r"]),
                "SE": (center, vertices["r"], vertices["lr"]),
                "S": (center, vertices["lr"], vertices["ll"]),
                "SW": (center, vertices["ll"], vertices["l"]),
            }
            assignments = [
                (upper_name, upper_indices[flower_index] * 3 + 0, "NW"),
                (upper_name, upper_indices[flower_index] * 3 + 1, "N"),
                (upper_name, upper_indices[flower_index] * 3 + 2, "NE"),
                (lower_name, lower_indices[flower_index] * 3 + 0, "SW"),
                (lower_name, lower_indices[flower_index] * 3 + 1, "S"),
                (lower_name, lower_indices[flower_index] * 3 + 2, "SE"),
            ]
            bloom_id = f"{pair}-{flower_index + 1}"
            for row_name, index, petal in assignments:
                cell_id = f"{row_name}{index:02d}"
                polygon = polygons[petal]
                x = sum(point[0] for point in polygon) / 3
                y = sum(point[1] for point in polygon) / 3
                if cell_id in cells:
                    raise ValueError(f"Duplicate cell assignment: {cell_id}")
                cells[cell_id] = Cell(
                    cell_id=cell_id,
                    row=row_name,
                    index=index,
                    letter=ROWS[row_name][index],
                    x=x,
                    y=y,
                    bloom=bloom_id,
                    petal=petal,
                    polygon=polygon,
                )
    if len(cells) != 228:
        raise ValueError(f"Expected 228 cells, generated {len(cells)}")
    return cells


def edge_key(a: tuple[float, float], b: tuple[float, float]) -> tuple[tuple[float, float], tuple[float, float]]:
    rounded = [tuple(round(value, 3) for value in point) for point in (a, b)]
    return tuple(sorted(rounded))  # type: ignore[return-value]


def make_adjacency(cells: dict[str, Cell], mode: str = "edge") -> dict[str, set[str]]:
    edge_to_cells: dict[tuple[tuple[float, float], tuple[float, float]], list[str]] = defaultdict(list)
    for cell in cells.values():
        polygon = cell.polygon
        for i in range(3):
            edge_to_cells[edge_key(polygon[i], polygon[(i + 1) % 3])].append(cell.cell_id)

    adjacency = {cell_id: set() for cell_id in cells}
    if mode == "edge":
        for occupants in edge_to_cells.values():
            if len(occupants) == 2:
                a, b = occupants
                adjacency[a].add(b)
                adjacency[b].add(a)
            elif len(occupants) > 2:
                raise ValueError(f"Non-manifold edge shared by {occupants}")
    elif mode == "vertex":
        vertex_to_cells: dict[tuple[float, float], list[str]] = defaultdict(list)
        for cell in cells.values():
            for point in cell.polygon:
                key = tuple(round(value, 3) for value in point)
                vertex_to_cells[key].append(cell.cell_id)
        for occupants in vertex_to_cells.values():
            for index, a in enumerate(occupants):
                for b in occupants[index + 1 :]:
                    adjacency[a].add(b)
                    adjacency[b].add(a)
    else:
        raise ValueError(f"Unknown adjacency mode: {mode}")
    return adjacency


def normalize_path_text(text: str) -> str:
    return re.sub(r"[^A-Z]", "", text.upper())


def find_letter_paths(
    text: str,
    cells: dict[str, Cell],
    adjacency: dict[str, set[str]],
    start: str | None,
    end: str | None,
    limit: int = 20,
) -> list[list[str]]:
    target = normalize_path_text(text)
    if not target:
        return []
    starts = [start] if start else [cell_id for cell_id, cell in cells.items() if cell.letter == target[0]]
    results: list[list[str]] = []

    def visit(path: list[str], used: set[str]) -> None:
        if len(results) >= limit:
            return
        if len(path) == len(target):
            if end is None or path[-1] == end:
                results.append(path.copy())
            return
        next_letter = target[len(path)]
        for neighbor in sorted(adjacency[path[-1]]):
            if neighbor not in used and cells[neighbor].letter == next_letter:
                used.add(neighbor)
                path.append(neighbor)
                visit(path, used)
                path.pop()
                used.remove(neighbor)

    for first in starts:
        if first not in cells or cells[first].letter != target[0]:
            continue
        visit([first], {first})
    return results


def path_turns(path: list[str], cells: dict[str, Cell]) -> str:
    """Return visual L/R turns for triples of cell centers (screen y grows down)."""
    turns = []
    for previous, current, following in zip(path, path[1:], path[2:], strict=False):
        ax = cells[current].x - cells[previous].x
        ay = cells[current].y - cells[previous].y
        bx = cells[following].x - cells[current].x
        by = cells[following].y - cells[current].y
        cross = ax * by - ay * bx
        if abs(cross) < 1e-6:
            turns.append("S")
        else:
            # In image coordinates a positive cross product is clockwise/right.
            turns.append("R" if cross > 0 else "L")
    return "".join(turns)


@functools.lru_cache(maxsize=None)
def best_english_segmentation(text: str) -> tuple[float, str]:
    """Score a complete A-Z string as English words using unigram frequency."""
    from wordfreq import zipf_frequency

    if not text:
        return 0.0, ""
    best_score = float("-inf")
    best_words = ""
    for length in range(1, min(20, len(text)) + 1):
        word = text[:length]
        if length == 1 and word not in {"A", "I"}:
            continue
        frequency = zipf_frequency(word.lower(), "en")
        if frequency < 2.5:
            continue
        tail_score, tail_words = best_english_segmentation(text[length:])
        if tail_score == float("-inf"):
            continue
        score = (frequency - 9.0) + tail_score
        if score > best_score:
            best_score = score
            best_words = word if not tail_words else f"{word} {tail_words}"
    return best_score, best_words


def enumerate_continuations(
    prefix_path: list[str],
    depth: int,
    cells: dict[str, Cell],
    adjacency: dict[str, set[str]],
    cap: int = 200_000,
) -> list[tuple[str, list[str]]]:
    results: list[tuple[str, list[str]]] = []
    used = set(prefix_path)

    def visit(path: list[str], letters: list[str]) -> None:
        if len(results) >= cap:
            return
        if len(letters) == depth:
            results.append(("".join(letters), path.copy()))
            return
        for neighbor in sorted(adjacency[path[-1]]):
            if neighbor not in used:
                used.add(neighbor)
                path.append(neighbor)
                letters.append(cells[neighbor].letter)
                visit(path, letters)
                letters.pop()
                path.pop()
                used.remove(neighbor)

    visit(prefix_path.copy(), [])
    return results


def enumerate_endpoint_continuations(
    prefix_path: list[str],
    end: str,
    length: int,
    cells: dict[str, Cell],
    adjacency: dict[str, set[str]],
    cap: int = 200_000,
) -> list[tuple[str, list[str]]]:
    """Enumerate exact-length unused continuations that land on ``end``."""
    results: list[tuple[str, list[str]]] = []
    used = set(prefix_path)

    # Unconstrained graph distance is an admissible pruning bound.
    distances = {end: 0}
    frontier = [end]
    while frontier:
        current = frontier.pop(0)
        for neighbor in adjacency[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                frontier.append(neighbor)

    def visit(path: list[str], letters: list[str]) -> None:
        if len(results) >= cap:
            return
        remaining = length - len(letters)
        current = path[-1]
        if distances.get(current, length + 1) > remaining:
            return
        if not remaining:
            if current == end:
                results.append(("".join(letters), path.copy()))
            return
        for neighbor in sorted(adjacency[current]):
            if neighbor not in used:
                used.add(neighbor)
                path.append(neighbor)
                letters.append(cells[neighbor].letter)
                visit(path, letters)
                letters.pop()
                path.pop()
                used.remove(neighbor)

    visit(prefix_path.copy(), [])
    return results


def write_tsv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "grid",
    )
    parser.add_argument(
        "--path-query",
        action="append",
        default=[],
        metavar="LABEL|START|END|TEXT",
        help="Search a no-revisit cell path; START or END may be '-'",
    )
    parser.add_argument(
        "--adjacency-mode",
        choices=["edge", "vertex"],
        default="edge",
        help="Whether path cells must share an edge or may merely share a vertex",
    )
    parser.add_argument(
        "--continuation-query",
        action="append",
        default=[],
        metavar="LABEL|START|PREFIX|DEPTH",
        help="Enumerate and unigram-rank fixed-depth continuations of a known prefix",
    )
    parser.add_argument(
        "--endpoint-query",
        action="append",
        default=[],
        metavar="LABEL|START|PREFIX|END|LENGTH",
        help="Enumerate exact-length continuations of PREFIX that land on END",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    expected_lengths = {"A": 9, "L": 9} | {row: 21 for row in "BCDEFGHIJK"}
    for row_name, answer in ROWS.items():
        if len(answer) != expected_lengths[row_name]:
            raise ValueError(f"Row {row_name} has length {len(answer)}: {answer}")

    bloom_table = validate_blooms()
    cells = make_cells()
    adjacency = make_adjacency(cells, args.adjacency_mode)

    write_tsv(
        args.output_dir / "blooms.tsv",
        bloom_table,
        ["pair", "color", "position", "upper", "lower", "signature", "answer"],
    )
    cell_rows = []
    for cell_id in sorted(cells, key=lambda item: (item[0], int(item[1:]))):
        cell = cells[cell_id]
        cell_rows.append(
            {
                "id": cell.cell_id,
                "row": cell.row,
                "index": cell.index,
                "letter": cell.letter,
                "x": f"{cell.x:.2f}",
                "y": f"{cell.y:.2f}",
                "bloom": cell.bloom,
                "petal": cell.petal,
                "neighbors": ",".join(sorted(adjacency[cell_id])),
            }
        )
    write_tsv(
        args.output_dir / "cells.tsv",
        cell_rows,
        ["id", "row", "index", "letter", "x", "y", "bloom", "petal", "neighbors"],
    )

    edges = []
    for a in sorted(adjacency):
        for b in sorted(adjacency[a]):
            if a < b:
                edges.append({"a": a, "b": b})
    write_tsv(args.output_dir / "edges.tsv", edges, ["a", "b"])

    annotations = []
    terminal_by_cell = {cell_id: label for label, cell_id in TERMINALS.items()}
    for cell in cells.values():
        annotations.append(
            {
                "type": "text",
                "xy": [round(cell.x - 5, 2), round(cell.y - 7, 2)],
                "label": cell.letter,
            }
        )
        if cell.cell_id in terminal_by_cell:
            annotations.append(
                {
                    "type": "point",
                    "xy": [round(cell.x, 2), round(cell.y, 2)],
                    "label": terminal_by_cell[cell.cell_id],
                }
            )
    (args.output_dir / "letters-spec.json").write_text(
        json.dumps({"annotations": annotations}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    path_rows: list[dict[str, object]] = []
    for raw_query in args.path_query:
        try:
            label, start, end, query_text = raw_query.split("|", 3)
        except ValueError as error:
            raise ValueError(f"Invalid --path-query {raw_query!r}") from error
        start_id = None if start == "-" else start
        end_id = None if end == "-" else end
        matches = find_letter_paths(query_text, cells, adjacency, start_id, end_id)
        if matches:
            for result_index, path in enumerate(matches, start=1):
                path_rows.append(
                    {
                        "label": label,
                        "adjacency": args.adjacency_mode,
                        "text": normalize_path_text(query_text),
                        "start": start_id or "",
                        "end": end_id or "",
                        "match": result_index,
                        "cell_path": ",".join(path),
                        "turns": path_turns(path, cells),
                    }
                )
        else:
            path_rows.append(
                {
                    "label": label,
                    "adjacency": args.adjacency_mode,
                    "text": normalize_path_text(query_text),
                    "start": start_id or "",
                    "end": end_id or "",
                    "match": 0,
                    "cell_path": "",
                    "turns": "",
                }
            )
        print(f"path-query {label}: {len(matches)} match(es)")
    if args.path_query:
        write_tsv(
            args.output_dir / "path-tests.tsv",
            path_rows,
            ["label", "adjacency", "text", "start", "end", "match", "cell_path", "turns"],
        )
        path_spec_dir = args.output_dir / "path-specs"
        path_spec_dir.mkdir(parents=True, exist_ok=True)
        palette = ["#0066ff", "#e6004c", "#00a36c", "#9b4dca", "#ff8c00"]
        primary_annotations = []
        for row_index, row in enumerate(path_rows):
            if not row["cell_path"]:
                continue
            path = str(row["cell_path"]).split(",")
            annotation = {
                "type": "polyline",
                # filled-grid.png was rendered at scale 2 from the source.
                "points": [[round(2 * cells[cell_id].x, 2), round(2 * cells[cell_id].y, 2)] for cell_id in path],
                "label": f"{row['label']} #{row['match']}",
                "color": palette[row_index % len(palette)],
                "width": 3,
            }
            spec = {"annotations": [annotation]}
            spec_path = path_spec_dir / f"{row['label']}-{row['match']}.json"
            spec_path.write_text(json.dumps(spec, indent=2), encoding="utf-8")
            if row["match"] == 1:
                primary_annotations.append(annotation)
        (path_spec_dir / "all-primary.json").write_text(
            json.dumps({"annotations": primary_annotations}, indent=2),
            encoding="utf-8",
        )

    continuation_rows: list[dict[str, object]] = []
    for raw_query in args.continuation_query:
        try:
            label, start, prefix_text, raw_depth = raw_query.split("|", 3)
            depth = int(raw_depth)
        except ValueError as error:
            raise ValueError(f"Invalid --continuation-query {raw_query!r}") from error
        prefix_matches = find_letter_paths(prefix_text, cells, adjacency, start, None)
        ranked: list[tuple[float, str, str, list[str]]] = []
        for prefix_path in prefix_matches:
            for continuation, path in enumerate_continuations(prefix_path, depth, cells, adjacency):
                score, segmented = best_english_segmentation(continuation)
                ranked.append((score, continuation, segmented, path))
        ranked.sort(key=lambda item: (-item[0], item[1], item[3]))
        print(
            f"continuation-query {label}: {len(prefix_matches)} prefix match(es), "
            f"{len(ranked)} continuation(s)"
        )
        for rank, (score, continuation, segmented, path) in enumerate(ranked[:100], start=1):
            continuation_rows.append(
                {
                    "label": label,
                    "adjacency": args.adjacency_mode,
                    "prefix": normalize_path_text(prefix_text),
                    "depth": depth,
                    "rank": rank,
                    "score": f"{score:.3f}",
                    "continuation": continuation,
                    "segmentation": segmented,
                    "cell_path": ",".join(path),
                }
            )
    if args.continuation_query:
        write_tsv(
            args.output_dir / "continuations.tsv",
            continuation_rows,
            [
                "label",
                "adjacency",
                "prefix",
                "depth",
                "rank",
                "score",
                "continuation",
                "segmentation",
                "cell_path",
            ],
        )

    endpoint_rows: list[dict[str, object]] = []
    for raw_query in args.endpoint_query:
        try:
            label, start, prefix_text, end, raw_length = raw_query.split("|", 4)
            length = int(raw_length)
        except ValueError as error:
            raise ValueError(f"Invalid --endpoint-query {raw_query!r}") from error
        prefix_matches = find_letter_paths(prefix_text, cells, adjacency, start, None)
        ranked: list[tuple[float, str, str, list[str]]] = []
        for prefix_path in prefix_matches:
            for continuation, path in enumerate_endpoint_continuations(
                prefix_path, end, length, cells, adjacency
            ):
                score, segmented = best_english_segmentation(continuation)
                ranked.append((score, continuation, segmented, path))
        ranked.sort(key=lambda item: (-item[0], item[1], item[3]))
        print(
            f"endpoint-query {label}: {len(prefix_matches)} prefix match(es), "
            f"{len(ranked)} endpoint continuation(s)"
        )
        for rank, (score, continuation, segmented, path) in enumerate(ranked, start=1):
            endpoint_rows.append(
                {
                    "label": label,
                    "adjacency": args.adjacency_mode,
                    "prefix": normalize_path_text(prefix_text),
                    "end": end,
                    "length": length,
                    "rank": rank,
                    "score": f"{score:.3f}",
                    "continuation": continuation,
                    "segmentation": segmented,
                    "cell_path": ",".join(path),
                    "turns": path_turns(path, cells),
                }
            )
    if args.endpoint_query:
        write_tsv(
            args.output_dir / "endpoint-continuations.tsv",
            endpoint_rows,
            [
                "label",
                "adjacency",
                "prefix",
                "end",
                "length",
                "rank",
                "score",
                "continuation",
                "segmentation",
                "cell_path",
                "turns",
            ],
        )

    print(
        f"Validated {len(ROWS)} rows, {len(bloom_table)} blooms, {len(cells)} cells, "
        f"and {len(edges)} {args.adjacency_mode}-adjacency edges."
    )
    for label, cell_id in TERMINALS.items():
        cell = cells[cell_id]
        print(f"{label}: {cell_id}={cell.letter} at ({cell.x:.1f}, {cell.y:.1f}), degree {len(adjacency[cell_id])}")


if __name__ == "__main__":
    main()
