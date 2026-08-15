from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw


OUTPUT_DIR = Path(__file__).resolve().parent

COLOR_HEX = {
    "R": "#ff0000",
    "Y": "#f1c232",
    "G": "#34a853",
    "B": "#00b0f0",
}

DIRECTION_STEP = {
    "right": (0, 1),
    "down": (1, 0),
    "diagonal": (1, 1),
}


@dataclass(frozen=True)
class WordLine:
    color: str
    original: str
    corrected: str
    direction: str
    start_row: int
    start_col: int

    def cells(self) -> list[tuple[int, int]]:
        row_step, col_step = DIRECTION_STEP[self.direction]
        return [
            (self.start_row + row_step * i, self.start_col + col_step * i)
            for i in range(len(self.original))
        ]


@dataclass(frozen=True)
class ExtractionSlot:
    color: str
    slot: int
    number: int
    corrected: str
    removed_char: str
    pinyin: str
    note: str = ""

    @property
    def letter(self) -> str:
        return self.pinyin[self.number - 1].upper()


LINES = [
    WordLine("R", "西方柿", "西红柿", "right", 2, 3),
    WordLine("R", "满江英", "满江红", "down", 1, 8),
    WordLine("R", "大寒袍", "大红袍", "diagonal", 3, 6),
    WordLine("R", "藏同花", "藏红花", "down", 4, 4),
    WordLine("R", "冰袍茶", "冰红茶", "down", 4, 8),
    WordLine("Y", "明日用花", "明日黄花", "right", 6, 1),
    WordLine("Y", "人约门昏后", "人约黄昏后", "diagonal", 4, 5),
    WordLine("Y", "信口雌水", "信口雌黄", "down", 6, 5),
    WordLine("Y", "雄音酒", "雄黄酒", "diagonal", 8, 6),
    WordLine("Y", "丽金屋", "黄金屋", "right", 11, 3),
    WordLine("Y", "大楼蜂", "大黄蜂", "down", 10, 7),
    WordLine("G", "静林好汉", "绿林好汉", "diagonal", 3, 15),
    WordLine("G", "青山盼水", "青山绿水", "down", 2, 11),
    WordLine("G", "鸭在江", "鸭绿江", "right", 6, 13),
    WordLine("G", "叶谁体", "叶绿体", "diagonal", 6, 9),
    WordLine("B", "板实根", "板蓝根", "down", 7, 12),
    WordLine("B", "碧把幻想", "碧蓝幻想", "right", 8, 17),
    WordLine("B", "天国色", "天蓝色", "right", 9, 14),
    WordLine("B", "忧郁也调", "忧郁蓝调", "right", 12, 13),
]

# Read the four colored columns from left to right (R, Y, G, B), and each
# column from top to bottom. The number printed in a colored cell indexes the
# pinyin of the character removed from the passage.
SLOTS = [
    ExtractionSlot("R", 1, 1, "冰红茶", "袍", "pao"),
    ExtractionSlot("R", 2, 2, "西红柿", "方", "fang", "R2/R4 may swap with 大红袍; letters stay A/N"),
    ExtractionSlot("R", 3, 2, "满江红", "英", "ying"),
    ExtractionSlot("R", 4, 3, "大红袍", "寒", "han", "R2/R4 may swap with 西红柿; letters stay A/N"),
    ExtractionSlot("R", 5, 1, "藏红花", "同", "tong"),
    ExtractionSlot("Y", 1, 1, "大黄蜂", "楼", "lou"),
    ExtractionSlot("Y", 2, 2, "黄金屋", "丽", "li"),
    ExtractionSlot("Y", 3, 3, "明日黄花", "用", "yong"),
    ExtractionSlot("Y", 4, 2, "人约黄昏后", "门", "men"),
    ExtractionSlot("Y", 5, 1, "信口雌黄", "水", "shui"),
    ExtractionSlot("Y", 6, 2, "雄黄酒", "音", "yin"),
    ExtractionSlot("G", 1, 3, "绿林好汉", "静", "jing"),
    ExtractionSlot("G", 2, 1, "青山绿水", "盼", "pan"),
    ExtractionSlot("G", 3, 2, "鸭绿江", "在", "zai"),
    ExtractionSlot("G", 4, 1, "叶绿体", "谁", "shei"),
    ExtractionSlot("B", 1, 1, "板蓝根", "实", "shi"),
    ExtractionSlot("B", 2, 2, "碧蓝幻想", "把", "ba"),
    ExtractionSlot("B", 3, 1, "天蓝色", "国", "guo"),
    ExtractionSlot("B", 4, 2, "忧郁蓝调", "也", "ye"),
]


def write_extraction_table() -> str:
    message = "".join(slot.letter for slot in SLOTS)
    expected = "PAINTLINESINPASSAGE"
    if message != expected:
        raise ValueError(f"Unexpected extraction: {message}")

    rows = ["color\tslot\tnumber\tword\tremoved_char\tpinyin\tletter\tnote"]
    rows.extend(
        "\t".join(
            [
                slot.color,
                str(slot.slot),
                str(slot.number),
                slot.corrected,
                slot.removed_char,
                slot.pinyin,
                slot.letter,
                slot.note,
            ]
        ).rstrip()
        for slot in SLOTS
    )
    (OUTPUT_DIR / "replacement_extraction.tsv").write_text(
        "\n".join(rows) + "\n", encoding="utf-8"
    )
    return message


def build_coverage() -> dict[tuple[int, int], set[str]]:
    coverage: dict[tuple[int, int], set[str]] = {}
    for line in LINES:
        for cell in line.cells():
            coverage.setdefault(cell, set()).add(line.color)
    return coverage


def write_mask_text(coverage: dict[tuple[int, int], set[str]]) -> None:
    rows = []
    for row in range(1, 13):
        rendered = []
        for col in range(1, 22):
            colors = coverage.get((row, col), set())
            rendered.append("*" if len(colors) > 1 else next(iter(colors), "."))
        rows.append("".join(rendered))
    (OUTPUT_DIR / "painted_mask.txt").write_text(
        "\n".join(rows) + "\n", encoding="utf-8"
    )


def write_mask_image(coverage: dict[tuple[int, int], set[str]]) -> None:
    cell_size = 44
    margin = 20
    width = 21 * cell_size + 2 * margin
    height = 12 * cell_size + 2 * margin
    image = Image.new("RGB", (width, height), "#101010")
    draw = ImageDraw.Draw(image)

    for row in range(1, 13):
        for col in range(1, 22):
            x0 = margin + (col - 1) * cell_size
            y0 = margin + (row - 1) * cell_size
            x1 = x0 + cell_size - 1
            y1 = y0 + cell_size - 1
            colors = coverage.get((row, col), set())
            if not colors:
                fill = "#000000"
            elif len(colors) == 1:
                fill = COLOR_HEX[next(iter(colors))]
            else:
                fill = "#f28c28"
            draw.rectangle((x0, y0, x1, y1), fill=fill, outline="#202020")

    image.save(OUTPUT_DIR / "painted_mask.png")


def write_stroke_image() -> None:
    cell_size = 50
    margin = 30
    width = 21 * cell_size + 2 * margin
    height = 12 * cell_size + 2 * margin
    image = Image.new("RGB", (width, height), "#000000")
    draw = ImageDraw.Draw(image)

    for line in LINES:
        cells = line.cells()
        points = [
            (
                margin + (col - 0.5) * cell_size,
                margin + (row - 0.5) * cell_size,
            )
            for row, col in cells
        ]
        draw.line(points, fill=COLOR_HEX[line.color], width=20, joint="curve")
        radius = 10
        for x, y in (points[0], points[-1]):
            draw.ellipse(
                (x - radius, y - radius, x + radius, y + radius),
                fill=COLOR_HEX[line.color],
            )

    image.save(OUTPUT_DIR / "painted_strokes.png")


def write_rotation_contact_sheet() -> None:
    source = Image.open(OUTPUT_DIR / "painted_mask.png")
    rotations = [
        ("0", source),
        ("90", source.rotate(90, expand=True)),
        ("180", source.rotate(180, expand=True)),
        ("270", source.rotate(270, expand=True)),
    ]
    panel_width = max(image.width for _, image in rotations)
    panel_height = max(image.height for _, image in rotations)
    sheet = Image.new("RGB", (panel_width * 2, panel_height * 2), "#303030")
    for index, (_, image) in enumerate(rotations):
        x = (index % 2) * panel_width + (panel_width - image.width) // 2
        y = (index // 2) * panel_height + (panel_height - image.height) // 2
        sheet.paste(image, (x, y))
    sheet.save(OUTPUT_DIR / "painted_rotations.png")


def write_color_contact_sheet() -> None:
    cell_size = 48
    panel_size = 480
    sheet = Image.new("RGB", (panel_size * 2, panel_size * 2), "#202020")
    for index, color in enumerate("RGYB"):
        color_lines = [line for line in LINES if line.color == color]
        cells = [cell for line in color_lines for cell in line.cells()]
        min_row = min(row for row, _ in cells)
        max_row = max(row for row, _ in cells)
        min_col = min(col for _, col in cells)
        max_col = max(col for _, col in cells)
        width = (max_col - min_col + 1) * cell_size
        height = (max_row - min_row + 1) * cell_size
        panel = Image.new("RGB", (width, height), "#000000")
        draw = ImageDraw.Draw(panel)
        for line in color_lines:
            points = [
                (
                    (col - min_col + 0.5) * cell_size,
                    (row - min_row + 0.5) * cell_size,
                )
                for row, col in line.cells()
            ]
            draw.line(points, fill=COLOR_HEX[color], width=18)
        panel.thumbnail((panel_size - 40, panel_size - 40))
        x = (index % 2) * panel_size + (panel_size - panel.width) // 2
        y = (index // 2) * panel_size + (panel_size - panel.height) // 2
        sheet.paste(panel, (x, y))
    sheet.save(OUTPUT_DIR / "painted_colors.png")


def main() -> None:
    message = write_extraction_table()
    coverage = build_coverage()
    if len(coverage) != 63:
        raise ValueError(f"Expected 63 unique painted cells, found {len(coverage)}")
    write_mask_text(coverage)
    write_mask_image(coverage)
    write_stroke_image()
    write_rotation_contact_sheet()
    write_color_contact_sheet()
    print(f"MESSAGE={message}")
    print(f"UNIQUE_PAINTED_CELLS={len(coverage)}")
    print(f"SHARED_CELLS={sorted(cell for cell, colors in coverage.items() if len(colors) > 1)}")


if __name__ == "__main__":
    main()
