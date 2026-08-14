"""Crop timestamped subtitle bands from uniformly sampled video frames."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def parse_box(value: str) -> tuple[int, int, int, int]:
    parts = tuple(int(part) for part in value.split(","))
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be left,top,right,bottom")
    return parts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--box", type=parse_box, default=(0, 1700, 1280, 2200))
    parser.add_argument("--interval", type=float, default=1.0)
    parser.add_argument("--step", type=int, default=1)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    frames = sorted(args.input_dir.glob("frame-*.png"))
    font = ImageFont.load_default(size=28)

    written = 0
    for frame_number, frame_path in enumerate(frames, start=1):
        if (frame_number - 1) % args.step:
            continue
        with Image.open(frame_path) as image:
            crop = image.crop(args.box).convert("RGB")
        label_height = 44
        labeled = Image.new("RGB", (crop.width, crop.height + label_height), "#111111")
        labeled.paste(crop, (0, label_height))
        timestamp = (frame_number - 1) * args.interval
        ImageDraw.Draw(labeled).text(
            (12, 7), f"{timestamp:06.1f}s  {frame_path.name}", fill="white", font=font
        )
        labeled.save(args.output_dir / frame_path.name)
        written += 1

    print(f"Wrote {written} subtitle crops to {args.output_dir}")


if __name__ == "__main__":
    main()
