import sys
from pathlib import Path
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding='utf-8')

OUTPUT_DIR = Path(__file__).resolve().parent

# 19 slots and their coordinates in the passage (1-based row, col)
# Formatted into the exact segments specified by the bottom pattern table:
# - Red (1 segment, 5 dots): (5, 8) -> (2, 4) -> (3, 8) -> (4, 7) -> (5, 4) => R
# - Yellow (2 segments):
#     Seg 1 (4 dots): (11, 7) -> (11, 3) -> (6, 3) -> (6, 7) (Outer frame)
#     Seg 2 (2 dots): (9, 5) -> (9, 7) (Middle bar)
#     => E
# - Green (1 segment, 4 dots): (3, 15) -> (4, 11) -> (6, 14) -> (7, 10) => S
# - Blue (2 segments):
#     Seg 1 (2 dots): (8, 12) -> (8, 18) (Top bar)
#     Seg 2 (2 dots): (9, 15) -> (12, 15) (Stem)
#     => T

SEGMENTS = [
    ('R', [(5, 8), (2, 4), (3, 8), (4, 7), (5, 4)], 'Red -> R'),
    ('Y', [(11, 7), (11, 3), (6, 3), (6, 7)], 'Yellow Seg 1 (Frame)'),
    ('Y', [(9, 5), (9, 7)], 'Yellow Seg 2 (Middle Bar)'),
    ('G', [(3, 15), (4, 11), (6, 14), (7, 10)], 'Green -> S'),
    ('B', [(8, 12), (8, 18)], 'Blue Seg 1 (Top Bar)'),
    ('B', [(9, 15), (12, 15)], 'Blue Seg 2 (Stem)'),
]

COLOR_HEX = {
    'R': '#ff4d4d',
    'Y': '#f1c232',
    'G': '#34a853',
    'B': '#00b0f0',
}

def draw_polylines():
    cell_size = 50
    margin = 40
    width = 21 * cell_size + 2 * margin
    height = 12 * cell_size + 2 * margin
    img = Image.new('RGB', (width, height), '#141414')
    draw = ImageDraw.Draw(img)

    for r in range(13):
        y = margin + r * cell_size
        draw.line([(margin, y), (margin + 21 * cell_size, y)], fill='#242424', width=1)
    for c in range(22):
        x = margin + c * cell_size
        draw.line([(x, margin), (x, margin + 12 * cell_size)], fill='#242424', width=1)

    for col, pts, name in SEGMENTS:
        points = [(margin + (c - 0.5) * cell_size, margin + (r - 0.5) * cell_size) for r, c in pts]
        draw.line(points, fill=COLOR_HEX[col], width=14, joint='curve')
        for p in points:
            draw.ellipse([p[0]-9, p[1]-9, p[0]+9, p[1]+9], fill=COLOR_HEX[col])

    img.save(OUTPUT_DIR / 'segmented_polylines_rest.png')
    print('Generated segmented_polylines_rest.png')

if __name__ == '__main__':
    draw_polylines()
