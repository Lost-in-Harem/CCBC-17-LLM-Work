import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


HERE = Path(__file__).resolve().parent
EXTRACTIONS = (
    (HERE / "semaphore-extraction.tsv", HERE / "semaphore-extraction.png", "INONEFAMILY"),
    (HERE / "family-extraction.tsv", HERE / "family-extraction.png", "ANSLITHARGE"),
)

# Physical directions as seen on the 5x5 board.  Each signal is unordered:
# which matching card is clicked first has no significance.
SEMAPHORE = {
    frozenset(("SW", "S")): "A",
    frozenset(("W", "S")): "B",
    frozenset(("NW", "S")): "C",
    frozenset(("N", "S")): "D",
    frozenset(("S", "NE")): "E",
    frozenset(("S", "E")): "F",
    frozenset(("S", "SE")): "G",
    frozenset(("W", "SW")): "H",
    frozenset(("NW", "SW")): "I",
    frozenset(("N", "E")): "J",
    frozenset(("SW", "N")): "K",
    frozenset(("SW", "NE")): "L",
    frozenset(("SW", "E")): "M",
    frozenset(("SW", "SE")): "N",
    frozenset(("W", "NW")): "O",
    frozenset(("W", "N")): "P",
    frozenset(("W", "NE")): "Q",
    frozenset(("W", "E")): "R",
    frozenset(("W", "SE")): "S",
    frozenset(("NW", "N")): "T",
    frozenset(("NW", "NE")): "U",
    frozenset(("N", "SE")): "V",
    frozenset(("NE", "E")): "W",
    frozenset(("SE", "NE")): "X",
    frozenset(("NW", "E")): "Y",
    frozenset(("SE", "E")): "Z",
}

CELL = 34
PANEL = 206
GRID_ORIGIN = (34, 34)


def grid_xy(position: int) -> tuple[int, int]:
    row, col = divmod(position - 1, 5)
    return col, row


def direction(position: int) -> str:
    x, y = grid_xy(position)
    dx, dy = x - 2, y - 2
    if dx == 0 and dy < 0:
        return "N"
    if dx == 0 and dy > 0:
        return "S"
    if dy == 0 and dx > 0:
        return "E"
    if dy == 0 and dx < 0:
        return "W"
    if abs(dx) == abs(dy):
        return ("N" if dy < 0 else "S") + ("W" if dx < 0 else "E")
    raise ValueError(f"position {position} is not on an eight-direction ray from the flag")


def pixel(position: int, panel_x: int, panel_y: int) -> tuple[int, int]:
    col, row = grid_xy(position)
    ox, oy = GRID_ORIGIN
    return panel_x + ox + col * CELL, panel_y + oy + row * CELL


def decode_table(table: Path, image: Path, expected: str) -> str:
    with table.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    canvas = Image.new("RGB", (PANEL * 4, PANEL * 3), "white")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    letters = []

    for row in rows:
        level = int(row["level"])
        a, b = int(row["pos_a"]), int(row["pos_b"])
        dir_a, dir_b = direction(a), direction(b)
        decoded = SEMAPHORE[frozenset((dir_a, dir_b))]
        assert (dir_a, dir_b) == (row["dir_a"], row["dir_b"]), (table.name, row["level"], dir_a, dir_b)
        assert decoded == row["letter"], (table.name, row["level"], decoded, row["letter"])
        letters.append(decoded)

        index = level - 1
        panel_x, panel_y = index % 4 * PANEL, index // 4 * PANEL
        center = pixel(13, panel_x, panel_y)
        endpoint_a = pixel(a, panel_x, panel_y)
        endpoint_b = pixel(b, panel_x, panel_y)
        draw.text((panel_x + 10, panel_y + 8), f"L{level}  {decoded}  {dir_a}+{dir_b}", fill="black", font=font)
        draw.line((center, endpoint_a), fill=(25, 75, 155), width=5)
        draw.line((center, endpoint_b), fill=(25, 75, 155), width=5)
        for endpoint, position in ((endpoint_a, a), (endpoint_b, b)):
            x, y = endpoint
            draw.ellipse((x - 8, y - 8, x + 8, y + 8), fill=(235, 235, 245), outline=(25, 75, 155), width=2)
            draw.text((x - 6, y - 5), str(position), fill="black", font=font)
        cx, cy = center
        draw.ellipse((cx - 10, cy - 10, cx + 10, cy + 10), fill=(220, 45, 55), outline="black")
        draw.text((cx - 4, cy - 5), "F", fill="white", font=font)

    message = "".join(letters)
    assert message == expected
    canvas.save(image)

    print(table.name)
    print("level\tpositions\tdirections\tletter")
    for row in rows:
        print(f'{row["level"]}\t{row["pos_a"]},{row["pos_b"]}\t{row["dir_a"]}+{row["dir_b"]}\t{row["letter"]}')
    print(f"message\t{message}")
    print(image)
    return message


def main() -> None:
    messages = [decode_table(*extraction) for extraction in EXTRACTIONS]
    assert messages == ["INONEFAMILY", "ANSLITHARGE"]


if __name__ == "__main__":
    main()
