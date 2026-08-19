#!/usr/bin/env python3
"""Extract the dashed-divider SVG (30 slots, 3 folders) from every toringmoni
feeder puzzle page and check that the 10x3 folder slots tile 1..30 exactly.

Run from the repository root:
    python3 rounds/toringmoni/nodes/c-meta-henry-who-sees-truth/artifacts/dashline_folders.py
"""
import io
import re
import struct
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]          # repo root
NODES = ROOT / "rounds" / "toringmoni" / "nodes"

PAGES = [
    ("c01", "c01-carpe-diem/input/把握今朝.html"),
    ("c02", "c02-born-from-the-same-root/input/本是同根生.html"),
    ("c03", "c03-make-your-own-history/input/创造你的历史.html"),
    ("c04", "c04-radio-calisthenics-26/input/广播体操二十六式.html"),
    ("c05", "c05-path-in-a-rose-garden/input/玫瑰花园的小径.html"),
    ("c06", "c06-love-in-florence/input/情迷翡冷翠.html"),
    ("c07", "c07-carbon-based-lifeform-calculator/input/碳基生物计算器.html"),
    ("c08", "c08-novel-therapies/input/新式疗法.html"),
    ("c09", "c09-asia-trio/input/亚细亚三重奏.html"),
    ("c10", "c10-traveling-around/input/周游列国.html"),
    ("meta", "c-meta-henry-who-sees-truth/input/去伪存真的李昌钰.html"),
]


def index_html(path: Path) -> str:
    """SingleFile-Z pages embed the real page as a zip inside an HTML comment."""
    data = path.read_bytes()
    start = data.find(b"PK\x03\x04")
    eocd = data.rfind(b"PK\x05\x06")
    clen = struct.unpack("<H", data[eocd + 20:eocd + 22])[0]
    zf = zipfile.ZipFile(io.BytesIO(data[start:eocd + 22 + clen]))
    return zf.read("index.html").decode("utf-8", "replace")


def slots(html: str):
    body = re.search(r"class=puzzle-body>([\s\S]*?)</section>", html)
    if not body:
        return []
    return re.findall(r"<use href=#(dash|folder)", body.group(1))


def main() -> int:
    owner = {}
    rows = []
    for pid, rel in PAGES:
        seq = slots(index_html(NODES / rel))
        if not seq:
            rows.append((pid, 0, [], []))
            continue
        folders = [i + 1 for i, u in enumerate(seq) if u == "folder"]
        segs, run = [], 0
        for u in seq:
            if u == "folder":
                segs.append(run)
                run = 0
            else:
                run += 1
        segs.append(run)
        rows.append((pid, len(seq), folders, segs))
        for p in folders:
            if p in owner:
                print(f"COLLISION at slot {p}: {owner[p]} and {pid}")
            owner[p] = pid

    print(f"{'node':5s} {'slots':>5s}  {'folder slots':<14s} {'dash segments'}")
    for pid, n, folders, segs in rows:
        print(f"{pid:5s} {n:5d}  {str(folders):<14s} {segs}")

    covered = sorted(owner)
    print(f"\ncovered slots: {len(covered)}  distinct: {len(set(covered))}")
    print("perfect tiling of 1..30:", covered == list(range(1, 31)))
    print("\nslot -> owning node")
    print(" ".join(f"{p}:{owner[p][1:]}" for p in covered))
    return 0 if covered == list(range(1, 31)) else 1


if __name__ == "__main__":
    sys.exit(main())
