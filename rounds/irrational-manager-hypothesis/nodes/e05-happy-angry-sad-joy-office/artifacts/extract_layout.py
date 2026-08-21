from __future__ import annotations

import argparse
import csv
import html
import json
from pathlib import Path

from bs4 import BeautifulSoup


CELL_W = 48
CELL_H = 40
COLOR_NAMES = {
    "c17-emoji-blue": "blue",
    "c17-emoji-pink": "pink",
}
BORDER_NAMES = {
    "c17-emoji-bt": "T",
    "c17-emoji-br": "R",
    "c17-emoji-bb": "B",
    "c17-emoji-bl": "L",
}


def parse_tables(input_path: Path) -> list[dict]:
    soup = BeautifulSoup(input_path.read_text(encoding="utf-8"), "html.parser")
    tables: list[dict] = []
    for table_index, table in enumerate(soup.select("table.c17-emoji-table"), start=1):
        rows = []
        for row_index, tr in enumerate(table.select("tr"), start=1):
            cells = []
            for column_index, td in enumerate(tr.find_all("td", recursive=False), start=1):
                classes = td.get("class") or []
                color = next((name for cls, name in COLOR_NAMES.items() if cls in classes), "")
                borders = "".join(mark for cls, mark in BORDER_NAMES.items() if cls in classes)
                cells.append(
                    {
                        "row": row_index,
                        "column": column_index,
                        "text": td.get_text("", strip=True),
                        "color": color,
                        "borders": borders,
                        "classes": classes,
                    }
                )
            rows.append(cells)
        tables.append(
            {
                "id": f"table-{table_index}",
                "label": table.get("aria-label", ""),
                "classes": table.get("class") or [],
                "rows": rows,
            }
        )
    return tables


def token(cell: dict) -> str:
    if cell["text"]:
        return cell["text"]
    if cell["color"] == "blue":
        return "B"
    if cell["color"] == "pink":
        return "P"
    if cell["borders"]:
        return "#"
    return "."


def write_tsv(tables: list[dict], output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["table", "label", "row", "column", "text", "color", "borders", "classes"])
        for table in tables:
            for row in table["rows"]:
                for cell in row:
                    writer.writerow(
                        [
                            table["id"],
                            table["label"],
                            cell["row"],
                            cell["column"],
                            cell["text"],
                            cell["color"],
                            cell["borders"],
                            " ".join(cell["classes"]),
                        ]
                    )


def write_text(tables: list[dict], output_path: Path) -> None:
    lines = [
        "Legend: B=blue cell, P=pink cell, #=unfilled cell carrying at least one border, .=plain empty cell.",
        "Rows and columns are 1-based. Emoji strings are preserved exactly from the HTML.",
        "",
    ]
    for table in tables:
        width = max((len(row) for row in table["rows"]), default=0)
        lines.append(f"{table['id']} | {table['label']} | {len(table['rows'])} rows x {width} columns")
        lines.append("    " + " ".join(f"c{column:02d}" for column in range(1, width + 1)))
        for row_index, row in enumerate(table["rows"], start=1):
            lines.append(f"r{row_index:02d} " + " | ".join(token(cell) for cell in row))
        lines.append("")
        lines.append("Occupied/text cells:")
        for row in table["rows"]:
            occupied = [cell for cell in row if cell["text"]]
            if occupied:
                details = ", ".join(f"c{cell['column']:02d}={cell['text']}" for cell in occupied)
                lines.append(f"r{row[0]['row']:02d}: {details}")
        lines.append("")
        lines.append("Colored cells:")
        for row in table["rows"]:
            colored = [cell for cell in row if cell["color"]]
            if colored:
                details = ", ".join(f"c{cell['column']:02d}={cell['color']}" for cell in colored)
                lines.append(f"r{row[0]['row']:02d}: {details}")
        lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_svg(table: dict, output_path: Path) -> None:
    rows = table["rows"]
    height = len(rows) * CELL_H
    width = max((len(row) for row in rows), default=0) * CELL_W
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
    ]
    for row in rows:
        for cell in row:
            x = (cell["column"] - 1) * CELL_W
            y = (cell["row"] - 1) * CELL_H
            fill = "#C7ECFF" if cell["color"] == "blue" else "#FFC9C7" if cell["color"] == "pink" else "white"
            if cell["color"]:
                parts.append(f'<rect x="{x}" y="{y}" width="{CELL_W}" height="{CELL_H}" fill="{fill}"/>')
            if "T" in cell["borders"]:
                parts.append(f'<line x1="{x}" y1="{y}" x2="{x + CELL_W}" y2="{y}" stroke="black"/>')
            if "R" in cell["borders"]:
                parts.append(f'<line x1="{x + CELL_W}" y1="{y}" x2="{x + CELL_W}" y2="{y + CELL_H}" stroke="black"/>')
            if "B" in cell["borders"]:
                parts.append(f'<line x1="{x}" y1="{y + CELL_H}" x2="{x + CELL_W}" y2="{y + CELL_H}" stroke="black"/>')
            if "L" in cell["borders"]:
                parts.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + CELL_H}" stroke="black"/>')
            if cell["text"]:
                label = html.escape(cell["text"])
                parts.append(
                    f'<text x="{x + CELL_W / 2}" y="{y + CELL_H / 2}" '
                    'font-family="Noto Color Emoji, Segoe UI Emoji, sans-serif" font-size="24" '
                    f'text-anchor="middle" dominant-baseline="central">{label}</text>'
                )
    parts.append("</svg>")
    output_path.write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract coordinate-stable emoji puzzle tables from the saved HTML archive.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    tables = parse_tables(args.input)
    (args.output / "layout.json").write_text(json.dumps(tables, ensure_ascii=False, indent=2), encoding="utf-8")
    write_tsv(tables, args.output / "layout.tsv")
    write_text(tables, args.output / "layout.txt")
    for table in tables:
        write_svg(table, args.output / f"{table['id']}.svg")
    print(f"Extracted {len(tables)} tables to {args.output}")


if __name__ == "__main__":
    main()
