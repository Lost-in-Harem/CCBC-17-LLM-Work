from __future__ import annotations

import argparse
import hashlib
import html
import re
from pathlib import Path

from bs4 import BeautifulSoup


MAIN_RE = re.compile(rb"<main\s+hidden[^>]*>(.*?)</main>", re.DOTALL | re.IGNORECASE)


def iter_html(paths: list[Path]) -> list[Path]:
    found: set[Path] = set()
    for path in paths:
        if path.is_dir():
            found.update(p.resolve() for p in path.rglob("*.html"))
        elif path.suffix.lower() == ".html":
            found.add(path.resolve())
    return sorted(found, key=lambda p: p.name.casefold())


def extract(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    match = MAIN_RE.search(raw)
    if not match:
        return digest, "[No <main hidden> search-text block found.]"

    block = match.group(1).decode("utf-8", errors="replace")
    text = BeautifulSoup(block, "html.parser").get_text("\n")
    text = html.unescape(text)
    lines = [line.strip() for line in text.splitlines()]
    compact: list[str] = []
    for line in lines:
        if line or (compact and compact[-1]):
            compact.append(line)
    return digest, "\n".join(compact).strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract the visible search-text block from SingleFile ZIP HTML captures."
    )
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    sections: list[str] = []
    for path in iter_html(args.inputs):
        digest, text = extract(path)
        sections.append(
            f"## {path.name}\n\n"
            f"- SHA-256: `{digest}`\n"
            f"- Source: `{path.as_posix()}`\n\n"
            f"```text\n{text}\n```"
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "# WIG page text report\n\n" + "\n\n".join(sections) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
