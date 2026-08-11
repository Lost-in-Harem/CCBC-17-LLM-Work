#!/usr/bin/env python3
"""Bounded, reproducible visual inspection helpers for Puzzle Hunt inputs."""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import io
import json
import math
import mimetypes
import re
import shutil
import subprocess
import sys
import zipfile
from collections.abc import Iterable
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import unquote_to_bytes, urlsplit

sys.dont_write_bytecode = True

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError:  # The command reports a useful error in main().
    Image = None  # type: ignore[assignment]
    ImageDraw = None  # type: ignore[assignment]
    ImageFont = None  # type: ignore[assignment]
    ImageOps = None  # type: ignore[assignment]


RASTER_SUFFIXES = {
    ".bmp",
    ".gif",
    ".jpeg",
    ".jpg",
    ".pbm",
    ".pgm",
    ".png",
    ".ppm",
    ".tif",
    ".tiff",
    ".webp",
}
HTML_SUFFIXES = {".htm", ".html", ".xhtml"}
VIDEO_SUFFIXES = {".avi", ".gif", ".mkv", ".mov", ".mp4", ".webm"}
AUDIO_SUFFIXES = {".aac", ".flac", ".m4a", ".mp3", ".ogg", ".opus", ".wav"}
FORMAT_SUFFIX = {
    "BMP": ".bmp",
    "GIF": ".gif",
    "JPEG": ".jpg",
    "PNG": ".png",
    "PPM": ".ppm",
    "TIFF": ".tiff",
    "WEBP": ".webp",
}
PALETTE = [
    "#e6194b",
    "#3cb44b",
    "#4363d8",
    "#f58231",
    "#911eb4",
    "#008080",
    "#9a6324",
    "#000000",
]
DATA_IMAGE_PATTERN = re.compile(
    r"""data:image/[a-zA-Z0-9.+-]+
        (?:;[a-zA-Z0-9=.+-]+)*
        (?:;base64)?,
        [^"'()<>\s]+
    """,
    re.IGNORECASE | re.VERBOSE,
)
CSS_URL_PATTERN = re.compile(
    r"""url\(\s*(?P<quote>["']?)(?P<url>[^"')]+)(?P=quote)\s*\)""",
    re.IGNORECASE,
)


class WorkbenchError(RuntimeError):
    """A user-facing validation or dependency error."""


@dataclass
class RawImage:
    source: str
    payload: bytes
    suffix_hint: str


class ImageSourceParser(HTMLParser):
    """Collect image-like source attributes without executing page content."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.sources: list[str] = []

    def handle_starttag(
        self, tag: str, attrs_list: list[tuple[str, str | None]]
    ) -> None:
        attrs = dict(attrs_list)
        if tag.lower() in {"img", "source"}:
            source = attrs.get("src")
            if source:
                self.sources.append(source)
            srcset = attrs.get("srcset")
            if srcset:
                for item in srcset.split(","):
                    candidate = item.strip().split(maxsplit=1)[0]
                    if candidate:
                        self.sources.append(candidate)


def require_pillow() -> None:
    if Image is None:
        raise WorkbenchError(
            "Pillow is required. Run `python tools/doctor.py` to inspect "
            "capabilities, then install Pillow in this project environment."
        )


def resolve_executable(name: str) -> str | None:
    """Prefer a native executable when a Windows PATH shim is a batch file."""
    location = shutil.which(name)
    if location is None:
        return None
    path = Path(location)
    if sys.platform == "win32" and path.suffix.lower() in {".bat", ".cmd"}:
        executable_name = (
            name if name.lower().endswith(".exe") else f"{name}.exe"
        )
        for ancestor in list(path.parents)[:4]:
            native = ancestor / "native"
            if not native.is_dir():
                continue
            matches = sorted(
                native.rglob(executable_name),
                key=lambda candidate: (len(candidate.parts), str(candidate)),
            )
            if matches:
                return str(matches[0])
    return location


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def safe_label(value: str, limit: int = 52) -> str:
    compact = " ".join(value.split())
    if len(compact) > limit:
        compact = compact[: limit - 1] + "…"
    # Pillow's bundled fallback font may not contain CJK glyphs.
    return compact.encode("ascii", errors="replace").decode("ascii")


def safe_source_label(value: str, limit: int = 49) -> str:
    compact = " ".join(value.replace("\\", "/").split())
    if len(compact) > limit:
        compact = "…" + compact[-(limit - 1):]
    return compact.encode("ascii", errors="replace").decode("ascii")


def draw_text_safe(draw: Any, xy: tuple[int, int], text: str, **kwargs: Any) -> None:
    try:
        draw.text(xy, text, **kwargs)
    except (UnicodeEncodeError, OSError):
        draw.text(xy, safe_label(text, 200), **kwargs)


def normalized_source(path: Path) -> str:
    return str(path.resolve()).replace("\\", "/")


def data_image(source: str) -> tuple[bytes, str] | None:
    if not source.lower().startswith("data:image/"):
        return None
    try:
        header, encoded = source.split(",", 1)
    except ValueError:
        return None
    media = header[5:].split(";", 1)[0].lower()
    suffix = mimetypes.guess_extension(media) or "." + media.split("/")[-1]
    try:
        if ";base64" in header.lower():
            payload = base64.b64decode(encoded, validate=False)
        else:
            payload = unquote_to_bytes(encoded)
    except (ValueError, base64.binascii.Error):
        return None
    return payload, suffix


def local_image_reference(
    html_path: Path, source: str, allowed_root: Path
) -> Path | None:
    split = urlsplit(source)
    if split.scheme or split.netloc or source.startswith(("#", "//", "blob:")):
        return None
    candidate = (html_path.parent / unquote_to_bytes(split.path).decode(
        "utf-8", errors="replace"
    )).resolve()
    try:
        candidate.relative_to(allowed_root.resolve())
    except ValueError:
        return None
    if candidate.is_file() and candidate.suffix.lower() in RASTER_SUFFIXES:
        return candidate
    return None


def add_raw(
    images: list[RawImage],
    notes: list[str],
    source: str,
    payload: bytes,
    suffix_hint: str,
    max_images: int,
    max_item_bytes: int,
    total_state: list[int],
    max_total_bytes: int,
) -> None:
    if len(images) >= max_images:
        if not any(note.startswith("Stopped at max-images") for note in notes):
            notes.append(f"Stopped at max-images={max_images}.")
        return
    if len(payload) > max_item_bytes:
        notes.append(
            f"Skipped oversized image ({len(payload)} bytes): {source}"
        )
        return
    if total_state[0] + len(payload) > max_total_bytes:
        if not any(note.startswith("Stopped at max-total") for note in notes):
            notes.append(
                f"Stopped at max-total-bytes={max_total_bytes}."
            )
        return
    total_state[0] += len(payload)
    images.append(RawImage(source, payload, suffix_hint.lower()))


def images_from_html(
    path: Path,
    allowed_root: Path,
    images: list[RawImage],
    notes: list[str],
    limits: dict[str, int],
    total_state: list[int],
) -> None:
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError as error:
        notes.append(f"Could not read HTML {path}: {error}")
        return
    parser = ImageSourceParser()
    try:
        parser.feed(content)
    except Exception as error:
        notes.append(f"Could not parse HTML {path}: {error}")
        return
    regex_sources = [
        match.group(0) for match in DATA_IMAGE_PATTERN.finditer(content)
    ]
    regex_sources.extend(
        match.group("url") for match in CSS_URL_PATTERN.finditer(content)
    )
    seen_refs: set[str] = set()
    for index, source in enumerate([*parser.sources, *regex_sources], start=1):
        if source in seen_refs:
            continue
        seen_refs.add(source)
        inline = data_image(source)
        if inline is not None:
            payload, suffix = inline
            add_raw(
                images,
                notes,
                f"{normalized_source(path)}#data-image-{index}",
                payload,
                suffix,
                limits["max_images"],
                limits["max_item_bytes"],
                total_state,
                limits["max_total_bytes"],
            )
            continue
        local = local_image_reference(path, source, allowed_root)
        if local is None:
            continue
        try:
            payload = local.read_bytes()
        except OSError as error:
            notes.append(f"Could not read HTML asset {local}: {error}")
            continue
        add_raw(
            images,
            notes,
            f"{normalized_source(path)} -> {normalized_source(local)}",
            payload,
            local.suffix,
            limits["max_images"],
            limits["max_item_bytes"],
            total_state,
            limits["max_total_bytes"],
        )


def images_from_archive(
    path: Path,
    images: list[RawImage],
    notes: list[str],
    limits: dict[str, int],
    total_state: list[int],
) -> None:
    try:
        with zipfile.ZipFile(path) as archive:
            members = sorted(
                (
                    info
                    for info in archive.infolist()
                    if not info.is_dir()
                    and Path(info.filename).suffix.lower() in RASTER_SUFFIXES
                ),
                key=lambda info: info.filename.lower(),
            )
            for info in members:
                if len(images) >= limits["max_images"]:
                    notes.append(
                        f"Stopped archive at max-images={limits['max_images']}."
                    )
                    break
                if info.file_size > limits["max_item_bytes"]:
                    notes.append(
                        f"Skipped oversized archive member: {info.filename}"
                    )
                    continue
                try:
                    payload = archive.read(info)
                except (OSError, RuntimeError, zipfile.BadZipFile) as error:
                    notes.append(
                        f"Could not read archive member {info.filename}: {error}"
                    )
                    continue
                add_raw(
                    images,
                    notes,
                    f"{normalized_source(path)}!/{info.filename}",
                    payload,
                    Path(info.filename).suffix,
                    limits["max_images"],
                    limits["max_item_bytes"],
                    total_state,
                    limits["max_total_bytes"],
                )
    except (OSError, zipfile.BadZipFile) as error:
        notes.append(f"Could not inspect archive {path}: {error}")


def discover_images(
    input_path: Path,
    *,
    max_files: int,
    max_images: int,
    max_item_bytes: int,
    max_total_bytes: int,
    excluded_root: Path | None = None,
) -> tuple[list[RawImage], list[str], int]:
    images: list[RawImage] = []
    notes: list[str] = []
    total_state = [0]

    if not input_path.exists():
        raise WorkbenchError(f"Input does not exist: {input_path}")

    allowed_root = input_path.resolve(
    ) if input_path.is_dir() else input_path.resolve().parent
    if input_path.is_dir():
        files: Iterable[Path] = (
            path for path in sorted(input_path.rglob("*")) if path.is_file()
        )
    else:
        files = [input_path]

    visited = 0
    for path in files:
        if excluded_root is not None:
            try:
                path.resolve().relative_to(excluded_root.resolve())
                continue
            except ValueError:
                pass
        visited += 1
        if visited > max_files:
            notes.append(f"Stopped at max-files={max_files}.")
            break
        if len(images) >= max_images:
            notes.append(f"Stopped at max-images={max_images}.")
            break

        try:
            is_archive = zipfile.is_zipfile(path)
        except OSError:
            is_archive = False
        if is_archive:
            images_from_archive(
                path, images, notes, {
                    "max_images": max_images,
                    "max_item_bytes": max_item_bytes,
                    "max_total_bytes": max_total_bytes,
                }, total_state
            )
            continue

        suffix = path.suffix.lower()
        if suffix in RASTER_SUFFIXES:
            try:
                if path.stat().st_size > max_item_bytes:
                    notes.append(f"Skipped oversized image: {path}")
                    continue
                payload = path.read_bytes()
            except OSError as error:
                notes.append(f"Could not read image {path}: {error}")
                continue
            add_raw(
                images,
                notes,
                normalized_source(path),
                payload,
                suffix,
                max_images,
                max_item_bytes,
                total_state,
                max_total_bytes,
            )
        elif suffix in HTML_SUFFIXES:
            images_from_html(
                path, allowed_root, images, notes, {
                    "max_images": max_images,
                    "max_item_bytes": max_item_bytes,
                    "max_total_bytes": max_total_bytes,
                }, total_state
            )

    images.sort(key=lambda item: item.source.casefold())
    return images, notes, visited


def inspect_payload(payload: bytes) -> tuple[str, int, int]:
    require_pillow()
    try:
        with Image.open(io.BytesIO(payload)) as image:
            image_format = (image.format or "").upper()
            transformed = ImageOps.exif_transpose(image)
            return image_format, transformed.width, transformed.height
    except Exception as error:
        raise WorkbenchError(f"Unreadable raster image: {error}") from error


def extension_for(image_format: str, suffix_hint: str) -> str:
    return FORMAT_SUFFIX.get(image_format, suffix_hint or ".bin")


def clear_generated_inventory(output: Path) -> None:
    assets = output / "assets"
    if assets.is_dir():
        for path in assets.glob("image-*.*"):
            if path.is_file():
                path.unlink()
    if output.is_dir():
        for path in output.glob("contact-*.png"):
            if path.is_file():
                path.unlink()


def make_contact_sheets(
    records: list[dict[str, Any]],
    output: Path,
    *,
    columns: int,
    rows: int,
    thumb_width: int,
    thumb_height: int,
) -> list[str]:
    require_pillow()
    if not records:
        return []
    font = ImageFont.load_default()
    label_height = 58
    cell_width = thumb_width
    cell_height = thumb_height + label_height
    per_sheet = columns * rows
    sheets: list[str] = []

    for sheet_index, start in enumerate(
        range(0, len(records), per_sheet), start=1
    ):
        sheet_records = records[start: start + per_sheet]
        sheet = Image.new(
            "RGB",
            (columns * cell_width, rows * cell_height),
            "#d8d8d8",
        )
        draw = ImageDraw.Draw(sheet)
        for offset, record in enumerate(sheet_records):
            row, column = divmod(offset, columns)
            x = column * cell_width
            y = row * cell_height
            draw.rectangle(
                (x, y, x + cell_width - 1, y + cell_height - 1),
                fill="white",
                outline="#777777",
            )
            asset = output / record["asset"]
            with Image.open(asset) as raw:
                image = ImageOps.exif_transpose(raw).convert("RGBA")
                available_width = thumb_width - 8
                available_height = thumb_height - 8
                if image.width < available_width and image.height < available_height:
                    factor = max(
                        1,
                        min(
                            16,
                            available_width // max(1, image.width),
                            available_height // max(1, image.height),
                        ),
                    )
                    image = image.resize(
                        (image.width * factor, image.height * factor),
                        Image.Resampling.NEAREST,
                    )
                else:
                    image.thumbnail(
                        (available_width, available_height),
                        Image.Resampling.LANCZOS,
                    )
                thumb = Image.new("RGBA", image.size, "white")
                thumb.alpha_composite(image)
                paste_x = x + (thumb_width - image.width) // 2
                paste_y = y + label_height + (thumb_height - image.height) // 2
                sheet.paste(thumb.convert("RGB"), (paste_x, paste_y))
            line_one = (
                f"{record['id']}  {record['width']}x{record['height']}  "
                f"{record['bytes']} bytes"
            )
            line_two = safe_source_label(record["sources"][0], 49)
            draw_text_safe(draw, (x + 6, y + 5), line_one,
                           fill="black", font=font)
            draw_text_safe(
                draw, (x + 6, y + 30), line_two, fill="#333333", font=font
            )
        filename = f"contact-{sheet_index:02d}.png"
        sheet.save(output / filename)
        sheets.append(filename)
    return sheets


def build_inventory(
    input_path: Path,
    output: Path,
    *,
    max_files: int = 2000,
    max_images: int = 240,
    max_item_bytes: int = 64 * 1024 * 1024,
    max_total_bytes: int = 512 * 1024 * 1024,
    columns: int = 3,
    rows: int = 4,
    thumb_width: int = 360,
    thumb_height: int = 250,
) -> dict[str, Any]:
    require_pillow()
    output.mkdir(parents=True, exist_ok=True)
    (output / "assets").mkdir(parents=True, exist_ok=True)
    clear_generated_inventory(output)

    images, notes, visited = discover_images(
        input_path,
        max_files=max_files,
        max_images=max_images,
        max_item_bytes=max_item_bytes,
        max_total_bytes=max_total_bytes,
        excluded_root=output,
    )
    records: list[dict[str, Any]] = []
    digest_to_record: dict[str, dict[str, Any]] = {}

    for raw in images:
        digest = sha256_bytes(raw.payload)
        if digest in digest_to_record:
            digest_to_record[digest]["sources"].append(raw.source)
            continue
        try:
            image_format, width, height = inspect_payload(raw.payload)
        except WorkbenchError as error:
            notes.append(f"Skipped {raw.source}: {error}")
            continue
        image_id = f"image-{len(records) + 1:03d}"
        suffix = extension_for(image_format, raw.suffix_hint)
        asset_relative = Path("assets") / f"{image_id}{suffix}"
        (output / asset_relative).write_bytes(raw.payload)
        record = {
            "id": image_id,
            "asset": asset_relative.as_posix(),
            "format": image_format or suffix.lstrip(".").upper(),
            "width": width,
            "height": height,
            "bytes": len(raw.payload),
            "sha256": digest,
            "sources": [raw.source],
        }
        records.append(record)
        digest_to_record[digest] = record

    sheets = make_contact_sheets(
        records,
        output,
        columns=columns,
        rows=rows,
        thumb_width=thumb_width,
        thumb_height=thumb_height,
    )
    index_lines = [
        "id\tasset\tformat\twidth\theight\tbytes\tsha256\tsource_count\tsources"
    ]
    for record in records:
        sources = " | ".join(
            source.replace("\t", " ").replace("\n", " ")
            for source in record["sources"]
        )
        index_lines.append(
            "\t".join(
                [
                    record["id"],
                    record["asset"],
                    record["format"],
                    str(record["width"]),
                    str(record["height"]),
                    str(record["bytes"]),
                    record["sha256"],
                    str(len(record["sources"])),
                    sources,
                ]
            )
        )
    (output / "index.tsv").write_text(
        "\n".join(index_lines) + "\n", encoding="utf-8"
    )
    manifest = {
        "command": "inventory",
        "input": normalized_source(input_path),
        "limits": {
            "max_files": max_files,
            "max_images": max_images,
            "max_item_bytes": max_item_bytes,
            "max_total_bytes": max_total_bytes,
        },
        "files_visited": visited,
        "raw_images_seen": len(images),
        "unique_images": len(records),
        "contact_sheets": sheets,
        "notes": notes,
        "images": records,
    }
    write_json(output / "manifest.json", manifest)
    return manifest


def open_display_image(path: Path) -> Any:
    require_pillow()
    if not path.is_file():
        raise WorkbenchError(f"Image does not exist: {path}")
    try:
        with Image.open(path) as raw:
            return ImageOps.exif_transpose(raw).convert("RGBA")
    except Exception as error:
        raise WorkbenchError(
            f"Could not open image {path}: {error}") from error


def parse_box(value: str) -> tuple[int, int, int, int]:
    try:
        parts = tuple(int(part.strip()) for part in value.split(","))
    except ValueError as error:
        raise argparse.ArgumentTypeError(
            "Box must contain four integers: LEFT,TOP,RIGHT,BOTTOM"
        ) from error
    if len(parts) != 4:
        raise argparse.ArgumentTypeError(
            "Box must contain four integers: LEFT,TOP,RIGHT,BOTTOM"
        )
    return parts


def ensure_box(
    box: tuple[int, int, int, int], width: int, height: int
) -> None:
    left, top, right, bottom = box
    if not (0 <= left < right <= width and 0 <= top < bottom <= height):
        raise WorkbenchError(
            f"Box {box} is outside the displayed image bounds {width}x{height}."
        )


def command_crop(args: argparse.Namespace) -> None:
    image = open_display_image(args.image)
    ensure_box(args.box, image.width, image.height)
    left, top, right, bottom = args.box
    crop = image.crop(args.box)
    if args.scale < 1 or args.scale > 16:
        raise WorkbenchError("--scale must be between 1 and 16.")
    resampling = {
        "nearest": Image.Resampling.NEAREST,
        "lanczos": Image.Resampling.LANCZOS,
    }[args.resample]
    if args.scale != 1:
        crop = crop.resize(
            (crop.width * args.scale, crop.height * args.scale), resampling
        )
    if args.grid:
        if args.grid < 1:
            raise WorkbenchError("--grid must be positive.")
        draw = ImageDraw.Draw(crop)
        font = ImageFont.load_default()
        line_width = max(1, args.scale // 2)
        first_x = math.ceil(left / args.grid) * args.grid
        for source_x in range(first_x, right, args.grid):
            x = (source_x - left) * args.scale
            draw.line((x, 0, x, crop.height),
                      fill=args.grid_color, width=line_width)
            draw_text_safe(
                draw, (x + 2, 2), str(source_x), fill=args.grid_color, font=font
            )
        first_y = math.ceil(top / args.grid) * args.grid
        for source_y in range(first_y, bottom, args.grid):
            y = (source_y - top) * args.scale
            draw.line((0, y, crop.width, y),
                      fill=args.grid_color, width=line_width)
            draw_text_safe(
                draw, (2, y + 2), str(source_y), fill=args.grid_color, font=font
            )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    crop.save(args.output)
    write_json(
        args.output.with_suffix(args.output.suffix + ".json"),
        {
            "command": "crop",
            "source": normalized_source(args.image),
            "source_sha256": sha256_file(args.image),
            "coordinate_space": "EXIF-transposed source pixels",
            "source_dimensions": [image.width, image.height],
            "box": list(args.box),
            "scale": args.scale,
            "resample": args.resample,
            "grid": args.grid,
            "output": normalized_source(args.output),
        },
    )
    print(f"Wrote crop: {args.output}")


def save_l_channel(channel: Any, path: Path) -> None:
    channel.convert("L").save(path)


def command_channels(args: argparse.Namespace) -> None:
    image = open_display_image(args.image)
    args.output.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []

    canonical = args.output / "source.png"
    image.save(canonical)
    outputs.append(canonical.name)
    rgb = image.convert("RGB")
    gray = ImageOps.grayscale(rgb)
    gray_path = args.output / "gray.png"
    gray.save(gray_path)
    outputs.append(gray_path.name)

    for name, channel in zip(("red", "green", "blue"), rgb.split()):
        path = args.output / f"{name}.png"
        save_l_channel(channel, path)
        outputs.append(path.name)

    cmyk = rgb.convert("CMYK")
    for name, channel in zip(("cyan", "magenta", "yellow", "black"), cmyk.split()):
        path = args.output / f"{name}.png"
        save_l_channel(channel, path)
        outputs.append(path.name)

    alpha = image.getchannel("A")
    if alpha.getextrema() != (255, 255):
        alpha_path = args.output / "alpha.png"
        alpha.save(alpha_path)
        outputs.append(alpha_path.name)

    for threshold in args.threshold:
        if not 0 <= threshold <= 255:
            raise WorkbenchError(
                "Every --threshold must be between 0 and 255.")
        path = args.output / f"threshold-{threshold:03d}.png"
        gray.point(lambda value, t=threshold: 255 if value >=
                   t else 0).save(path)
        outputs.append(path.name)

    write_json(
        args.output / "manifest.json",
        {
            "command": "channels",
            "source": normalized_source(args.image),
            "source_sha256": sha256_file(args.image),
            "coordinate_space": "EXIF-transposed source pixels",
            "dimensions": [image.width, image.height],
            "thresholds": args.threshold,
            "outputs": outputs,
        },
    )
    print(f"Wrote {len(outputs)} channel views to {args.output}")


def number(value: Any, context: str) -> float:
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        raise WorkbenchError(f"{context} must contain finite numbers.")
    return float(value)


def points(value: Any, context: str) -> list[tuple[float, float]]:
    if not isinstance(value, list):
        raise WorkbenchError(f"{context} must be a list of [x, y] points.")
    result: list[tuple[float, float]] = []
    for index, item in enumerate(value):
        if not isinstance(item, list) or len(item) != 2:
            raise WorkbenchError(f"{context}[{index}] must be [x, y].")
        result.append(
            (number(item[0], context), number(item[1], context))
        )
    return result


def scaled_xy(values: Iterable[float], scale: int) -> tuple[int, ...]:
    return tuple(round(value * scale) for value in values)


def command_annotate(args: argparse.Namespace) -> None:
    image = open_display_image(args.image)
    try:
        spec_value = json.loads(args.spec.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise WorkbenchError(
            f"Could not read annotation spec: {error}") from error
    annotations = (
        spec_value.get("annotations") if isinstance(
            spec_value, dict) else spec_value
    )
    if not isinstance(annotations, list):
        raise WorkbenchError(
            "Annotation spec must be a list or an object with `annotations`."
        )
    if not 1 <= args.scale <= 16:
        raise WorkbenchError("--scale must be between 1 and 16.")
    if args.scale != 1:
        image = image.resize(
            (image.width * args.scale, image.height * args.scale),
            Image.Resampling.NEAREST,
        )
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    for index, annotation in enumerate(annotations):
        if not isinstance(annotation, dict):
            raise WorkbenchError(f"Annotation {index} must be an object.")
        kind = str(annotation.get("type", "")).lower()
        color = str(annotation.get("color") or PALETTE[index % len(PALETTE)])
        width = max(1, round(int(annotation.get("width", 3)) * args.scale))
        label = str(annotation.get("label", ""))

        if kind == "box":
            xy = annotation.get("xy")
            if not isinstance(xy, list) or len(xy) != 4:
                raise WorkbenchError(
                    f"Annotation {index} box needs xy=[l,t,r,b].")
            coords = scaled_xy(
                [number(value, f"annotation {index} xy") for value in xy],
                args.scale,
            )
            draw.rectangle(coords, outline=color, width=width)
            label_xy = (coords[0] + 3, coords[1] + 3)
        elif kind == "line":
            xy = annotation.get("xy")
            if not isinstance(xy, list) or len(xy) != 4:
                raise WorkbenchError(
                    f"Annotation {index} line needs xy=[x1,y1,x2,y2].")
            coords = scaled_xy(
                [number(value, f"annotation {index} xy") for value in xy],
                args.scale,
            )
            draw.line(coords, fill=color, width=width)
            label_xy = (coords[0] + 3, coords[1] + 3)
        elif kind == "point":
            xy = points([annotation.get("xy")], f"annotation {index} xy")[0]
            x, y = scaled_xy(xy, args.scale)
            radius = max(
                2, round(int(annotation.get("radius", 5)) * args.scale))
            draw.ellipse(
                (x - radius, y - radius, x + radius, y + radius),
                outline=color,
                width=width,
            )
            label_xy = (x + radius + 2, y - radius)
        elif kind == "polyline":
            path_points = points(
                annotation.get("points"), f"annotation {index} points"
            )
            if len(path_points) < 2:
                raise WorkbenchError(
                    f"Annotation {index} polyline needs at least two points."
                )
            coords = [scaled_xy(point, args.scale) for point in path_points]
            draw.line(coords, fill=color, width=width, joint="curve")
            label_xy = (coords[0][0] + 3, coords[0][1] + 3)
        elif kind == "text":
            xy = points([annotation.get("xy")], f"annotation {index} xy")[0]
            label_xy = scaled_xy(xy, args.scale)
            if not label:
                raise WorkbenchError(f"Annotation {index} text needs a label.")
        else:
            raise WorkbenchError(
                f"Annotation {index} has unsupported type {kind!r}."
            )

        if label:
            draw_text_safe(draw, label_xy, label, fill=color, font=font)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.output)
    write_json(
        args.output.with_suffix(args.output.suffix + ".json"),
        {
            "command": "annotate",
            "source": normalized_source(args.image),
            "source_sha256": sha256_file(args.image),
            "spec": normalized_source(args.spec),
            "spec_sha256": sha256_file(args.spec),
            "coordinate_space": "EXIF-transposed source pixels",
            "scale": args.scale,
            "annotation_count": len(annotations),
            "output": normalized_source(args.output),
        },
    )
    print(f"Wrote annotation: {args.output}")


def run_checked(command: list[str]) -> subprocess.CompletedProcess[bytes]:
    try:
        result = subprocess.run(
            command,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except OSError as error:
        raise WorkbenchError(f"Could not run {command[0]}: {error}") from error
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        if len(detail) > 1200:
            detail = detail[-1200:]
        raise WorkbenchError(
            f"{command[0]} exited with {result.returncode}: {detail}"
        )
    return result


def command_ocr(args: argparse.Namespace) -> None:
    require_pillow()
    executable = resolve_executable("tesseract")
    if executable is None:
        raise WorkbenchError(
            "Tesseract is not available. Run `python tools/doctor.py`."
        )
    args.output.mkdir(parents=True, exist_ok=True)
    command = [
        executable,
        str(args.image),
        "stdout",
        "-l",
        args.lang,
        "--psm",
        str(args.psm),
        "tsv",
    ]
    result = run_checked(command)
    tsv = result.stdout.decode("utf-8", errors="replace")
    (args.output / "ocr.tsv").write_text(tsv, encoding="utf-8")
    reader = csv.DictReader(io.StringIO(tsv), delimiter="\t")
    words: list[dict[str, Any]] = []
    lines: dict[tuple[str, str, str, str], list[str]] = {}
    for row in reader:
        text = (row.get("text") or "").strip()
        if not text or row.get("level") != "5":
            continue
        try:
            left = int(row.get("left") or "0")
            top = int(row.get("top") or "0")
            width = int(row.get("width") or "0")
            height = int(row.get("height") or "0")
            confidence = float(row.get("conf") or "-1")
        except ValueError:
            continue
        word = {
            "text": text,
            "confidence": confidence,
            "box": [left, top, left + width, top + height],
            "block": row.get("block_num"),
            "paragraph": row.get("par_num"),
            "line": row.get("line_num"),
            "word": row.get("word_num"),
        }
        words.append(word)
        key = (
            row.get("page_num") or "",
            row.get("block_num") or "",
            row.get("par_num") or "",
            row.get("line_num") or "",
        )
        lines.setdefault(key, []).append(text)
    reconstructed = "\n".join(" ".join(line) for line in lines.values())
    (args.output / "ocr.txt").write_text(
        reconstructed + ("\n" if reconstructed else ""), encoding="utf-8"
    )

    image = open_display_image(args.image)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    for word in words:
        confidence = word["confidence"]
        color = "#20a020" if confidence >= 80 else (
            "#e0a000" if confidence >= 50 else "#d02020"
        )
        box = tuple(word["box"])
        draw.rectangle(box, outline=color, width=2)
        draw_text_safe(
            draw,
            (box[0] + 2, max(0, box[1] - 12)),
            f"{word['text']} {confidence:.0f}",
            fill=color,
            font=font,
        )
    overlay = args.output / "ocr-overlay.png"
    image.save(overlay)
    write_json(
        args.output / "manifest.json",
        {
            "command": "ocr",
            "source": normalized_source(args.image),
            "source_sha256": sha256_file(args.image),
            "coordinate_space": "Tesseract source pixels",
            "tesseract_command": command,
            "language": args.lang,
            "page_segmentation_mode": args.psm,
            "word_count": len(words),
            "words": words,
            "outputs": ["ocr.tsv", "ocr.txt", "ocr-overlay.png"],
        },
    )
    print(f"Wrote OCR for {len(words)} words to {args.output}")


def clear_files(directory: Path, patterns: Iterable[str]) -> None:
    if not directory.is_dir():
        return
    for pattern in patterns:
        for path in directory.glob(pattern):
            if path.is_file():
                path.unlink()


def maybe_probe_media(input_path: Path, output: Path) -> list[str] | None:
    executable = resolve_executable("ffprobe")
    if executable is None:
        return None
    command = [
        executable,
        "-v",
        "error",
        "-of",
        "json",
        "-show_format",
        "-show_streams",
        "-show_chapters",
        str(input_path),
    ]
    result = run_checked(command)
    (output / "probe.json").write_bytes(result.stdout)
    return command


def command_render(args: argparse.Namespace) -> None:
    if not args.media.is_file():
        raise WorkbenchError(f"Media input does not exist: {args.media}")
    args.output.mkdir(parents=True, exist_ok=True)
    suffix = args.media.suffix.lower()
    commands: list[list[str]] = []
    generated: list[str] = []

    if suffix == ".pdf":
        executable = resolve_executable("pdftoppm")
        if executable is None:
            raise WorkbenchError(
                "pdftoppm is not available. Run `python tools/doctor.py`."
            )
        if not (1 <= args.first_page <= args.last_page):
            raise WorkbenchError(
                "PDF page range must satisfy 1 <= first <= last.")
        if args.last_page - args.first_page + 1 > args.max_pages:
            raise WorkbenchError(
                f"PDF range exceeds --max-pages={args.max_pages}."
            )
        rendered = args.output / "pages"
        rendered.mkdir(parents=True, exist_ok=True)
        clear_files(rendered, ["page-*.png"])
        command = [
            executable,
            "-png",
            "-r",
            str(args.dpi),
            "-f",
            str(args.first_page),
            "-l",
            str(args.last_page),
            str(args.media),
            str(rendered / "page"),
        ]
        run_checked(command)
        commands.append(command)
        generated.extend(
            path.relative_to(args.output).as_posix()
            for path in sorted(rendered.glob("page-*.png"))
        )
        build_inventory(
            rendered,
            args.output / "catalog",
            max_images=args.max_pages,
            max_total_bytes=512 * 1024 * 1024,
        )
    elif suffix in VIDEO_SUFFIXES:
        executable = resolve_executable("ffmpeg")
        if executable is None:
            raise WorkbenchError(
                "FFmpeg is not available. Run `python tools/doctor.py`."
            )
        if args.interval <= 0 or not 1 <= args.max_frames <= 240:
            raise WorkbenchError(
                "--interval must be positive and --max-frames must be 1..240."
            )
        frames = args.output / "frames"
        frames.mkdir(parents=True, exist_ok=True)
        clear_files(frames, ["frame-*.png"])
        command = [
            executable,
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(args.media),
            "-vf",
            (
                f"fps=1/{args.interval:g},"
                f"scale={args.max_width}:-2:force_original_aspect_ratio=decrease"
            ),
            "-frames:v",
            str(args.max_frames),
            str(frames / "frame-%03d.png"),
        ]
        run_checked(command)
        commands.append(command)
        generated.extend(
            path.relative_to(args.output).as_posix()
            for path in sorted(frames.glob("frame-*.png"))
        )
        build_inventory(
            frames,
            args.output / "catalog",
            max_images=args.max_frames,
            max_total_bytes=512 * 1024 * 1024,
        )
        probe = maybe_probe_media(args.media, args.output)
        if probe is not None:
            commands.append(probe)
            generated.append("probe.json")
    elif suffix in AUDIO_SUFFIXES:
        executable = resolve_executable("ffmpeg")
        if executable is None:
            raise WorkbenchError(
                "FFmpeg is not available. Run `python tools/doctor.py`."
            )
        views = [
            (
                "waveform.png",
                "aformat=channel_layouts=mono,"
                "showwavespic=s=1600x400:colors=royalblue",
            ),
            (
                "spectrum.png",
                "showspectrumpic=s=1600x900:legend=1",
            ),
        ]
        for filename, filter_value in views:
            command = [
                executable,
                "-y",
                "-hide_banner",
                "-loglevel",
                "error",
                "-i",
                str(args.media),
                "-filter_complex",
                filter_value,
                "-frames:v",
                "1",
                str(args.output / filename),
            ]
            run_checked(command)
            commands.append(command)
            generated.append(filename)
        probe = maybe_probe_media(args.media, args.output)
        if probe is not None:
            commands.append(probe)
            generated.append("probe.json")
    else:
        raise WorkbenchError(
            f"Unsupported render type {suffix!r}; use inventory for raster/HTML."
        )

    write_json(
        args.output / "render-manifest.json",
        {
            "command": "render",
            "source": normalized_source(args.media),
            "source_sha256": sha256_file(args.media),
            "commands": commands,
            "generated": generated,
            "bounds": {
                "first_page": args.first_page,
                "last_page": args.last_page,
                "max_pages": args.max_pages,
                "dpi": args.dpi,
                "interval_seconds": args.interval,
                "max_frames": args.max_frames,
                "max_width": args.max_width,
            },
        },
    )
    print(f"Wrote {len(generated)} rendered media files to {args.output}")


def command_inventory(args: argparse.Namespace) -> None:
    manifest = build_inventory(
        args.input,
        args.output,
        max_files=args.max_files,
        max_images=args.max_images,
        max_item_bytes=args.max_item_mib * 1024 * 1024,
        max_total_bytes=args.max_total_mib * 1024 * 1024,
        columns=args.columns,
        rows=args.rows,
        thumb_width=args.thumb_width,
        thumb_height=args.thumb_height,
    )
    print(
        f"Wrote {manifest['unique_images']} unique images and "
        f"{len(manifest['contact_sheets'])} contact sheets to {args.output}"
    )
    for note in manifest["notes"]:
        print(f"NOTE: {note}", file=sys.stderr)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        description=(
            "Create bounded, reproducible visual representations without "
            "modifying puzzle inputs."
        )
    )
    subparsers = root.add_subparsers(dest="command", required=True)

    inventory = subparsers.add_parser(
        "inventory",
        help="Extract, deduplicate, number, and contact-sheet raster images.",
    )
    inventory.add_argument("input", type=Path)
    inventory.add_argument("--output", required=True, type=Path)
    inventory.add_argument("--max-files", type=int, default=2000)
    inventory.add_argument("--max-images", type=int, default=240)
    inventory.add_argument("--max-item-mib", type=int, default=64)
    inventory.add_argument("--max-total-mib", type=int, default=512)
    inventory.add_argument("--columns", type=int, default=3)
    inventory.add_argument("--rows", type=int, default=4)
    inventory.add_argument("--thumb-width", type=int, default=360)
    inventory.add_argument("--thumb-height", type=int, default=250)
    inventory.set_defaults(handler=command_inventory)

    crop = subparsers.add_parser(
        "crop", help="Crop using displayed source coordinates and optionally grid it."
    )
    crop.add_argument("image", type=Path)
    crop.add_argument("output", type=Path)
    crop.add_argument("--box", required=True, type=parse_box)
    crop.add_argument("--scale", type=int, default=1)
    crop.add_argument("--resample", choices=("nearest",
                      "lanczos"), default="nearest")
    crop.add_argument("--grid", type=int)
    crop.add_argument("--grid-color", default="#e00000")
    crop.set_defaults(handler=command_crop)

    channels = subparsers.add_parser(
        "channels", help="Write canonical, channel, alpha, and threshold views."
    )
    channels.add_argument("image", type=Path)
    channels.add_argument("output", type=Path)
    channels.add_argument("--threshold", type=int, action="append", default=[])
    channels.set_defaults(handler=command_channels)

    annotate = subparsers.add_parser(
        "annotate", help="Draw stable JSON boxes, lines, points, paths, and labels."
    )
    annotate.add_argument("image", type=Path)
    annotate.add_argument("spec", type=Path)
    annotate.add_argument("output", type=Path)
    annotate.add_argument("--scale", type=int, default=1)
    annotate.set_defaults(handler=command_annotate)

    ocr = subparsers.add_parser(
        "ocr", help="Run Tesseract and preserve text, boxes, confidence, and overlay."
    )
    ocr.add_argument("image", type=Path)
    ocr.add_argument("output", type=Path)
    ocr.add_argument("--lang", default="eng")
    ocr.add_argument("--psm", type=int, default=11)
    ocr.set_defaults(handler=command_ocr)

    render = subparsers.add_parser(
        "render", help="Boundedly render PDF pages, video frames, or audio views."
    )
    render.add_argument("media", type=Path)
    render.add_argument("output", type=Path)
    render.add_argument("--first-page", type=int, default=1)
    render.add_argument("--last-page", type=int, default=20)
    render.add_argument("--max-pages", type=int, default=20)
    render.add_argument("--dpi", type=int, default=200)
    render.add_argument("--interval", type=float, default=10.0)
    render.add_argument("--max-frames", type=int, default=36)
    render.add_argument("--max-width", type=int, default=1200)
    render.set_defaults(handler=command_render)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        args.handler(args)
    except WorkbenchError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("ERROR: interrupted", file=sys.stderr)
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
