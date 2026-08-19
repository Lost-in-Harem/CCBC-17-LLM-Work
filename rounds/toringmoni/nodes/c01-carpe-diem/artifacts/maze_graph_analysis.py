#!/usr/bin/env python3
"""Parse Photo 3's maze straight out of the saved SingleFile capture and report
connectivity under the ordinary "a drawn segment is a wall" model.

Usage:
    python3 artifacts/maze_graph_analysis.py input/3.html

The capture is a SingleFileZ archive: index.html inside a zip appended to an
HTML shell. The maze is an inline SVG on a 5x5 unit grid, so wall segments and
animal positions can be read exactly instead of by OCR.

Result for the 2026-08-17 23:48 capture: 36 wall segments (18 border, 18
internal), 22 open internal edges, and the 25 cells split into FOUR connected
components. The entrance component is only {(1,1),(1,2)}, so the drawn board
has no ordinary path from the entrance to the exit. Any solution therefore
needs a movement rule beyond "cross an edge that has no drawn segment".
"""
from __future__ import annotations

import re
import sys
import zipfile
from collections import deque
from pathlib import Path

N = 5
ICON = {"\U0001F434": "马", "\U0001F426": "鸟", "\U0001F41F️": "鱼",
        "\U0001F42F": "虎", "\U0001F410": "羊"}


def read_capture(path: Path) -> str:
    try:
        with zipfile.ZipFile(path) as zf:
            return zf.read("index.html").decode("utf-8", errors="replace")
    except zipfile.BadZipFile:
        return path.read_text(encoding="utf-8", errors="replace")


def parse(src: str):
    walls = {tuple(float(v) for v in m.groups()) for m in re.finditer(
        r"<line class=maze-wall x1=([\d.-]+) y1=([\d.-]+) x2=([\d.-]+) y2=([\d.-]+)>", src)}
    animals = {}
    for m in re.finditer(r"<text class=maze-icon x=([\d.]+) y=([\d.]+)[^>]*>(.*?)</text>", src):
        r, c = int(float(m.group(2)) - 0.5), int(float(m.group(1)) - 0.5)
        animals[(r, c)] = ICON.get(m.group(3), m.group(3))
    axes = {(int(m.group(1)), int(m.group(2))) for m in re.finditer(
        r"<circle class=maze-axis cx=(\d+) cy=(\d+)", src)}
    return walls, animals, axes


def main() -> None:
    src = read_capture(Path(sys.argv[1] if len(sys.argv) > 1 else "input/3.html"))
    walls, animals, axes = parse(src)
    hw = lambda r, c: (float(c), float(r), float(c + 1), float(r)) in walls
    vw = lambda r, c: (float(c), float(r), float(c), float(r + 1)) in walls

    print(f"walls={len(walls)} axis-circles={len(axes)} animals={ {f'({r+1},{c+1})': a for (r, c), a in sorted(animals.items())} }")
    for r in range(N + 1):
        print("".join("+" + ("---" if hw(r, c) else "   ") for c in range(N)) + "+")
        if r < N:
            row = ""
            for c in range(N + 1):
                row += "|" if vw(r, c) else " "
                if c < N:
                    row += f" {animals.get((r, c), ' ')} "
            print(row)

    seen, comps = set(), []
    for start in ((r, c) for r in range(N) for c in range(N)):
        if start in seen:
            continue
        comp, q = {start}, deque([start])
        seen.add(start)
        while q:
            r, c = q.popleft()
            for nr, nc, blocked in ((r - 1, c, hw(r, c)), (r + 1, c, hw(r + 1, c)),
                                    (r, c - 1, vw(r, c)), (r, c + 1, vw(r, c + 1))):
                if 0 <= nr < N and 0 <= nc < N and not blocked and (nr, nc) not in seen:
                    seen.add((nr, nc)); comp.add((nr, nc)); q.append((nr, nc))
        comps.append(sorted(comp))
    print(f"connected components: {len(comps)}")
    for comp in comps:
        print("   size", len(comp), [(r + 1, c + 1) for r, c in comp])
    entrance = next(comp for comp in comps if (0, 0) in comp)
    print("entrance component reaches exit:", (N - 1, N - 1) in entrance)


if __name__ == "__main__":
    main()
