#!/usr/bin/env python3
"""Transcribe the four 秒克 album riddles out of SingleFile(Z) captures.

The album regenerates every minute, so every capture is a fresh instance. This
script turns any capture into an exact, comparable record instead of an OCR
guess: it auto-detects which of the four riddle types the page contains.

Usage:
    python3 artifacts/extract_riddles.py input/1.html input/2.html ...
    python3 artifacts/extract_riddles.py input/*.html

Output per file: the page's in-app clock (the album bio prints the live
"现在是YYYY年M月D日HH:MM"), the riddle type, and its exact content.

- photo 1 (riddle1)    : the three rows' square pattern class + result image class
                         (`sq--solid`, `sq--lr-left`, ...; `riddle1-image--huangshan` = 黄鳝)
- photo 2 (box-puzzle) : the 7x2 grid cell by cell, border colours, and the footer
- photo 3 (maze-photo) : wall segments, animal cells, and cell connectivity
- photo 4 (rebus-grid) : the three 「A op B ↔ C」 rows
"""
from __future__ import annotations

import re
import sys
import zipfile
from collections import deque
from pathlib import Path

# Hint 3 says to compare the square's split with the structure of the character
# after 黄.  Only left/right and top/bottom patterns match this image set.  The
# coloured region selects the corresponding component.
IMAGE_STRUCTURE = {
    "huangjiu": ("酒", "lr", {"sq--lr-left": "氵", "sq--lr-right": "酉"}),
    "huanghe": ("河", "lr", {"sq--lr-left": "氵", "sq--lr-right": "可"}),
    "huangli": ("鹂", "lr", {"sq--lr-left": "丽", "sq--lr-right": "鸟"}),
    "huangpi": ("陂", "lr", {"sq--lr-left": "阝", "sq--lr-right": "皮"}),
    "huangshan": ("鳝", "lr", {"sq--lr-left": "鱼", "sq--lr-right": "善"}),
    "huangque": ("雀", "tb", {"sq--tb-top": "小", "sq--tb-bottom": "隹"}),
}

# 刘禹锡《乌衣巷》末联, laid out as the 7x2 grid of photo 2.
WUYIXIANG = ["旧时王谢堂前燕", "飞入寻常百姓家"]
SURNAME_INDEX = {"時": 83, "时": 83, "王": 8, "謝": 34, "谢": 34,
                 "燕": 315, "常": 80}

ICON = {"\U0001F434": "马", "\U0001F426": "鸟", "\U0001F41F️": "鱼",
        "\U0001F42F": "虎", "\U0001F410": "羊", "\U0001F40E": "马"}


def read_capture(path: Path) -> str:
    try:
        with zipfile.ZipFile(path) as zf:
            return zf.read("index.html").decode("utf-8", errors="replace")
    except zipfile.BadZipFile:
        return path.read_text(encoding="utf-8", errors="replace")


def clock(src: str) -> str:
    m = re.search(r"现在是(\d+年\d+月\d+日\d+:\d+)", src)
    return m.group(1) if m else "?"


def photo1(src: str) -> list[str]:
    rows = []
    examples = []
    unknown_patterns = []
    for m in re.finditer(r'<div class=riddle1-row>(.*?)</div>\s*(?=<div class=riddle1-row>|</div>)', src, re.S):
        block = m.group(1)
        sq = re.search(r'class="riddle1-square (sq--[\w-]+)"', block)
        col = re.search(r'--c:(#\w+)', block)
        img = re.search(r'riddle1-image riddle1-image--(\w+)', block)
        unk = "riddle1-unknown" in block
        pat = sq.group(1) if sq else "?"
        image_id = img.group(1) if img else None
        rows.append(f"{pat} [{col.group(1) if col else '?'}] = "
                    f"{'?' if unk else (image_id or '?')}")
        if image_id:
            examples.append((pat, image_id))
        if unk:
            unknown_patterns.append(pat)
    selected = []
    coherent = len(examples) >= 2
    for pat, image_id in examples:
        item = IMAGE_STRUCTURE.get(image_id)
        component = item[2].get(pat) if item else None
        coherent = coherent and component is not None
        selected.append(component)
    if coherent:
        rows.append(f"    -> 两条示例的分割都匹配字形；着色部分依次选出：{'、'.join(selected)}")
        if selected == ["可", "阝"]:
            rows.append("    -> 按部件原左右位置合并：⿰阝可 = 阿")
    elif unknown_patterns:
        rows.append("    -> 当前分钟并非两条分割同时匹配字形的有效相位")
    return rows


def photo2(src: str) -> list[str]:
    grid = re.search(r'<div class="box-grid box-grid--large">(.*?)</div></div><div class="box-footer', src, re.S)
    out = []
    if grid:
        cells = re.findall(r'<div class=box-cell(.*?)</div>(?=<div class=box-cell|$)', grid.group(1) + "", re.S)
        cells = re.split(r'<div class=box-cell', grid.group(1))[1:]
        for i, cell in enumerate(cells, 1):
            border = re.search(r'border-color:(rgb\([^)]*\))', cell)
            sub = re.findall(r'<sub class=box-sn-sub>(\d+)</sub>', cell)
            img = "燕子" in cell
            unk = "box-unknown" in cell
            what = "?" if unk else ("燕子图+S" + sub[0] if img and sub else ("S" + sub[0] if sub else "_"))
            r, c = (i - 1) // 7 + 1, (i - 1) % 7 + 1
            out.append(f"r{r}c{c}={what}" + (f"[{border.group(1)}]" if border else ""))
            if unk and r <= 2 and c <= 7:
                underlying = WUYIXIANG[r-1][c-1]
                out.append(f"    -> 《乌衣巷》末联底字 = {underlying}（底字会随分钟移动，不等于固定答案）")
                if underlying in SURNAME_INDEX:
                    out.append(f"    -> 该底字是《百家姓》成员：S{SURNAME_INDEX[underlying]}")
    foot = re.search(r'<span class=box-footer-text>(.*?)</span>.*?<sub class=box-sn-sub>(\d+)</sub>', src, re.S)
    if foot:
        out.append(f"{foot.group(1)}∈S{foot.group(2)}")
    return out


def photo3(src: str) -> list[str]:
    walls = {tuple(float(v) for v in m.groups()) for m in re.finditer(
        r"<line class=maze-wall x1=([\d.-]+) y1=([\d.-]+) x2=([\d.-]+) y2=([\d.-]+)>", src)}
    animals = {}
    for m in re.finditer(r"<text class=maze-icon x=([\d.]+) y=([\d.]+)[^>]*>(.*?)</text>", src):
        animals[(int(float(m.group(2)) - 0.5), int(float(m.group(1)) - 0.5))] = ICON.get(m.group(3), m.group(3))
    n = 5
    hw = lambda r, c: (float(c), float(r), float(c + 1), float(r)) in walls
    vw = lambda r, c: (float(c), float(r), float(c), float(r + 1)) in walls
    out = [f"walls={len(walls)} animals=" + str({f"({r+1},{c+1})": a for (r, c), a in sorted(animals.items())})]
    for r in range(n + 1):
        out.append("".join("+" + ("---" if hw(r, c) else "   ") for c in range(n)) + "+")
        if r < n:
            row = ""
            for c in range(n + 1):
                row += "|" if vw(r, c) else " "
                if c < n:
                    row += f" {animals.get((r, c), ' ')} "
            out.append(row)
    seen, comps = set(), []
    for start in ((r, c) for r in range(n) for c in range(n)):
        if start in seen:
            continue
        comp, q = {start}, deque([start])
        seen.add(start)
        while q:
            r, c = q.popleft()
            for nr, nc, blocked in ((r - 1, c, hw(r, c)), (r + 1, c, hw(r + 1, c)),
                                    (r, c - 1, vw(r, c)), (r, c + 1, vw(r, c + 1))):
                if 0 <= nr < n and 0 <= nc < n and not blocked and (nr, nc) not in seen:
                    seen.add((nr, nc)); comp.add((nr, nc)); q.append((nr, nc))
        comps.append(sorted(comp))
    entrance = next(c for c in comps if (0, 0) in c)
    out.append(f"components={len(comps)}  entrance-reaches-exit={(n-1, n-1) in entrance}")
    cols = [0] * (n + 1); rows = [0] * (n + 1)
    for (r, c) in animals:
        cols[c + 1] += 1; rows[r + 1] += 1
    out.append(f"animals per column(1..5)={cols[1:]}  per row(1..5)={rows[1:]}"
               "   # exact distribution for this minute; all five animals move with E")
    return out


def photo4(src: str) -> list[str]:
    cells = re.findall(r'<span class="rebus-cell (hanzi|symbol|unknown)"[^>]*>(.*?)</span>', src)
    vals = [c[1] for c in cells]
    out = []
    for i in range(0, len(vals), 5):
        row = vals[i:i + 5]
        out.append(" ".join(row))
        if len(row) == 5 and row[4] in "？?":
            out.append("    -> 逐字拆字/方位读法已被提交否定；请与其他分钟比较后再解释")
    return out


def main() -> None:
    for arg in sys.argv[1:]:
        src = read_capture(Path(arg))
        print(f"=== {arg}   in-app clock: {clock(src)}")
        for name, marker, fn in (("photo1 riddle1", "riddle1-row", photo1),
                                 ("photo2 box-puzzle", "box-grid", photo2),
                                 ("photo3 maze", "maze-wall", photo3),
                                 ("photo4 rebus", "rebus-cell", photo4)):
            if marker in src:
                print(f"  [{name}]")
                for line in fn(src):
                    print("   ", line)
        print()


if __name__ == "__main__":
    main()
