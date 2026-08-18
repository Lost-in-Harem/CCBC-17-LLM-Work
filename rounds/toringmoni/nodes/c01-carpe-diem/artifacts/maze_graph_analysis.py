#!/usr/bin/env python3
"""Enumerate cell/axis-node routes for Photo 3's fixed 5x5 maze.

This is a reproducible exploratory model: walls block ordinary cell-boundary
crossings, while every drawn internal circle is treated as a four-way portal.
It reports shortest routes and the animal cells they visit; it does not claim
that this is the puzzle's final extraction.
"""
from __future__ import annotations

import argparse
from collections import defaultdict, deque
from pathlib import Path

from bs4 import BeautifulSoup


def parse(path: Path):
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    walls: set[tuple[int, int, int, int]] = set()
    for line in soup.select("line.maze-wall"):
        p = tuple(int(float(line[k])) for k in ("x1", "y1", "x2", "y2"))
        walls.add(p)
        walls.add((p[2], p[3], p[0], p[1]))
    animals = {}
    mapping = {"🐴": "马", "🐦": "鸟", "🐟️": "鱼", "🐯": "虎", "🐐": "羊"}
    for node in soup.select("text.maze-icon"):
        x, y = int(float(node["x"])), int(float(node["y"]))
        animals[(y, x)] = mapping.get(node.get_text(strip=True), node.get_text(strip=True))
    return walls, animals


def routes(path: Path, avoid_animals: bool = False, portal_mode: str = "all"):
    walls, animals = parse(path)
    graph: dict[tuple[str, int, int], set[tuple[str, int, int]]] = defaultdict(set)

    # Open crossings between adjacent cells where no wall segment is drawn.
    blocked_cells = set(animals) if avoid_animals else set()
    blocked_cells -= {(0, 0), (4, 4)}
    for r in range(5):
        for c in range(5):
            cell = ("C", r, c)
            if (r, c) in blocked_cells:
                continue
            candidates = [
                ((r - 1, c), (c, r, c + 1, r)),
                ((r + 1, c), (c, r + 1, c + 1, r + 1)),
                ((r, c - 1), (c, r, c, r + 1)),
                ((r, c + 1), (c + 1, r, c + 1, r + 1)),
            ]
            for (rr, cc), edge in candidates:
                if 0 <= rr < 5 and 0 <= cc < 5 and (rr, cc) not in blocked_cells and edge not in walls:
                    graph[cell].add(("C", rr, cc))

    # Model each internal circle according to the selected finite hypothesis.
    # ``all`` means a four-way crossing; ``diagonal`` means only opposite
    # quadrants connect; ``none`` leaves circles as ordinary wall vertices.
    for r in range(1, 5):
        for c in range(1, 5):
            portal = ("P", r, c)
            cells = (("C", r - 1, c - 1), ("C", r - 1, c), ("C", r, c - 1), ("C", r, c))
            if portal_mode == "diagonal":
                cells = (cells[0], cells[3])
            elif portal_mode == "none":
                cells = ()
            for cell in cells:
                if (cell[1], cell[2]) not in blocked_cells:
                    graph[cell].add(portal)
                    graph[portal].add(cell)

    start, goal = ("C", 0, 0), ("C", 4, 4)
    dist = {start: 0}
    parents: dict[tuple[str, int, int], list[tuple[str, int, int]]] = defaultdict(list)
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for other in sorted(graph[node]):
            nd = dist[node] + 1
            if other not in dist:
                dist[other] = nd
                parents[other].append(node)
                queue.append(other)
            elif dist[other] == nd:
                parents[other].append(node)

    paths: list[list[tuple[str, int, int]]] = []
    def backtrack(node, suffix):
        if node == start:
            paths.append([start, *suffix])
            return
        for parent in parents[node]:
            backtrack(parent, [node, *suffix])

    if goal in dist:
        backtrack(goal, [])

    def fmt(node):
        kind, r, c = node
        return f"{kind}{r+1},{c+1}"

    result = {
        "source": str(path),
        "distance": dist.get(goal),
        "shortest_path_count": len(paths),
        "avoid_animals": avoid_animals,
        "portal_mode": portal_mode,
        "animals": {f"r{r+1}c{c+1}": animal for (r, c), animal in sorted(animals.items())},
        "shortest_paths": [
            {
                "nodes": [fmt(node) for node in route],
                "cells": [fmt(node) for node in route if node[0] == "C"],
                "animals_on_cells": [animals[(node[1], node[2])] for node in route if node[0] == "C" and (node[1], node[2]) in animals],
            }
            for route in paths
        ],
    }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--avoid-animals", action="store_true")
    parser.add_argument("--portal-mode", choices=("all", "diagonal", "none"), default="all")
    args = parser.parse_args()
    import json
    args.output.write_text(json.dumps(routes(args.source, args.avoid_animals, args.portal_mode), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
