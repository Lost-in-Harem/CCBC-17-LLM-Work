from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import json
import re
import time
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


PIECE_RE = re.compile(
    r'"\.\./assets/jigsaw-pieces/([^"/]+\.png)":"data:image/png;base64,([^"\\]+)"'
)
LAYOUT_RE = re.compile(r'R\(k\.value,U,"([^"]+)",J\)')

CORE_LO = 64
CORE_HI = 191
PROFILE_START = 76
PROFILE_STOP = 180
SIDES = ("top", "right", "bottom", "left")
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"


def extract(source: Path, output_dir: Path) -> None:
    text = source.read_text(encoding="utf-8")
    matches = PIECE_RE.findall(text)
    if len(matches) != 64:
        raise SystemExit(f"expected 64 embedded PNGs, found {len(matches)}")

    pieces_dir = output_dir / "pieces"
    pieces_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str | int]] = []
    for index, (filename, payload) in enumerate(matches, start=1):
        data = base64.b64decode(payload)
        path = pieces_dir / filename
        path.write_bytes(data)
        with Image.open(path) as image:
            rows.append(
                {
                    "stable_id": f"piece-{index:02d}",
                    "filename": filename,
                    "width": image.width,
                    "height": image.height,
                    "bytes": len(data),
                    "sha256": hashlib.sha256(data).hexdigest(),
                }
            )

    with (output_dir / "piece_index.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    print(f"extracted {len(rows)} pieces to {pieces_dir}")


def edge_profile(alpha: np.ndarray, side: str) -> np.ndarray:
    mask = alpha > 127
    values: list[int] = []
    for tangent in range(PROFILE_START, PROFILE_STOP):
        if side in ("top", "bottom"):
            opaque = np.flatnonzero(mask[:, tangent])
        else:
            opaque = np.flatnonzero(mask[tangent, :])
        if not len(opaque):
            raise ValueError(f"empty alpha line on {side} at {tangent}")
        if side == "top":
            values.append(CORE_LO - int(opaque[0]))
        elif side == "right":
            values.append(int(opaque[-1]) - CORE_HI)
        elif side == "bottom":
            values.append(int(opaque[-1]) - CORE_HI)
        else:
            values.append(CORE_LO - int(opaque[0]))
    return np.asarray(values, dtype=np.int16)


def edge_kind(profile: np.ndarray) -> str:
    if int(np.max(np.abs(profile))) <= 1:
        return "flat"
    signed_area = int(profile.sum())
    return "tab" if signed_area > 0 else "hole"


def analyze(output_dir: Path) -> None:
    pieces_dir = output_dir / "pieces"
    piece_paths = sorted(pieces_dir.glob("*.png"))
    if len(piece_paths) != 64:
        raise SystemExit(f"expected 64 extracted pieces, found {len(piece_paths)}")

    profiles: dict[tuple[str, str], np.ndarray] = {}
    summaries: list[dict[str, str | int | float]] = []
    for path in piece_paths:
        rgba = np.asarray(Image.open(path).convert("RGBA"))
        for side in SIDES:
            profile = edge_profile(rgba[:, :, 3], side)
            profiles[(path.stem, side)] = profile
            summaries.append(
                {
                    "piece": path.stem,
                    "side": side,
                    "kind": edge_kind(profile),
                    "signed_area": int(profile.sum()),
                    "min": int(profile.min()),
                    "max": int(profile.max()),
                }
            )
    with (output_dir / "edge_summary.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=summaries[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(summaries)

    scores: list[dict[str, str | float]] = []
    for axis, side_a, side_b in (
        ("horizontal", "right", "left"),
        ("vertical", "bottom", "top"),
    ):
        for path_a in piece_paths:
            profile_a = profiles[(path_a.stem, side_a)]
            kind_a = edge_kind(profile_a)
            if kind_a == "flat":
                continue
            for path_b in piece_paths:
                if path_a == path_b:
                    continue
                profile_b = profiles[(path_b.stem, side_b)]
                kind_b = edge_kind(profile_b)
                if {kind_a, kind_b} != {"tab", "hole"}:
                    continue
                residual = profile_a.astype(np.int32) + profile_b.astype(np.int32)
                scores.append(
                    {
                        "axis": axis,
                        "piece_a": path_a.stem,
                        "side_a": side_a,
                        "piece_b": path_b.stem,
                        "side_b": side_b,
                        "shape_mae": float(np.mean(np.abs(residual))),
                        "shape_max": float(np.max(np.abs(residual))),
                    }
                )

    scores.sort(key=lambda row: (str(row["axis"]), float(row["shape_mae"])))
    with (output_dir / "edge_scores.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=scores[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(scores)

    flat_counts = {
        side: sum(row["side"] == side and row["kind"] == "flat" for row in summaries)
        for side in SIDES
    }
    best_exact = sum(float(row["shape_mae"]) <= 0.25 for row in scores)
    print(f"flat edge counts: {flat_counts}")
    print(f"candidate matches with shape MAE <= 0.25: {best_exact}")
    for axis in ("horizontal", "vertical"):
        best = [row for row in scores if row["axis"] == axis][:12]
        print(axis)
        for row in best:
            print(
                f"  {row['piece_a']} -> {row['piece_b']}: "
                f"mae={float(row['shape_mae']):.3f}, max={float(row['shape_max']):.0f}"
            )


def inspect_runtime(source: Path, output_dir: Path) -> None:
    text = source.read_text(encoding="utf-8")
    layout_match = LAYOUT_RE.search(text)
    if not layout_match:
        raise SystemExit("layout code not found")
    layout_code = layout_match.group(1)
    (output_dir / "layout_code.txt").write_text(layout_code + "\n", encoding="utf-8")

    script_start = text.index("var __vue_puzzle_component__")
    asset_start = text.index("const k=Object.assign", script_start)
    runtime = text[script_start:asset_start]
    (output_dir / "runtime_min.js").write_text(runtime + "\n", encoding="utf-8")
    print(f"layout code length: {len(layout_code)}")
    print(f"layout alphabet: {''.join(sorted(set(layout_code)))}")
    print(f"runtime without image payloads: {len(runtime)} characters")


def decode_edges(source: Path, output_dir: Path) -> None:
    text = source.read_text(encoding="utf-8")
    layout_match = LAYOUT_RE.search(text)
    if not layout_match:
        raise SystemExit("layout code not found")
    layout_code = layout_match.group(1)
    radius = ALPHABET.index(layout_code[0])
    payload = layout_code[1:]
    if radius < 1 or len(payload) != 256:
        raise SystemExit("invalid edge-code payload")

    filenames = sorted(filename for filename, _ in PIECE_RE.findall(text))
    rows: list[dict[str, str | int]] = []
    for index, filename in enumerate(filenames):
        codes = [ALPHABET.index(char) - radius for char in payload[4 * index : 4 * index + 4]]
        rows.append(
            {
                "stable_id": f"piece-{index + 1:02d}",
                "filename": filename,
                "top": codes[0],
                "right": codes[1],
                "bottom": codes[2],
                "left": codes[3],
            }
        )

    with (output_dir / "edge_codes.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    print(f"edge-code radius: {radius}")
    for side in SIDES:
        zero_count = sum(int(row[side]) == 0 for row in rows)
        candidate_counts = []
        opposite = {"top": "bottom", "right": "left", "bottom": "top", "left": "right"}[side]
        for row in rows:
            code = int(row[side])
            if code:
                candidate_counts.append(sum(int(other[opposite]) == -code for other in rows))
        print(
            f"{side}: {zero_count} flat; complementary candidates per nonflat edge "
            f"min={min(candidate_counts)}, max={max(candidate_counts)}, "
            f"mean={np.mean(candidate_counts):.2f}"
        )


def decoded_rows(source: Path) -> list[dict[str, str | int]]:
    text = source.read_text(encoding="utf-8")
    layout_match = LAYOUT_RE.search(text)
    if not layout_match:
        raise SystemExit("layout code not found")
    layout_code = layout_match.group(1)
    radius = ALPHABET.index(layout_code[0])
    payload = layout_code[1:]
    filenames = sorted(filename for filename, _ in PIECE_RE.findall(text))
    if radius < 1 or len(payload) != 4 * len(filenames):
        raise SystemExit("invalid edge-code payload")

    rows: list[dict[str, str | int]] = []
    for index, filename in enumerate(filenames):
        codes = [ALPHABET.index(char) - radius for char in payload[4 * index : 4 * index + 4]]
        rows.append(
            {
                "stable_id": f"piece-{index + 1:02d}",
                "filename": filename,
                "top": codes[0],
                "right": codes[1],
                "bottom": codes[2],
                "left": codes[3],
            }
        )
    return rows


def solve(source: Path, output_dir: Path) -> None:
    rows = decoded_rows(source)
    lookup: dict[tuple[str, int], dict[str, str | int]] = {}
    for side in SIDES:
        for row in rows:
            code = int(row[side])
            if code == 0:
                continue
            key = (side, code)
            if key in lookup:
                raise SystemExit(f"non-unique edge code {key}")
            lookup[key] = row

    top_left = [row for row in rows if int(row["top"]) == 0 and int(row["left"]) == 0]
    if len(top_left) != 1:
        raise SystemExit(f"expected one top-left corner, found {len(top_left)}")

    grid: list[list[dict[str, str | int]]] = []
    for grid_row in range(8):
        current: list[dict[str, str | int]] = []
        for grid_col in range(8):
            if grid_row == 0 and grid_col == 0:
                piece = top_left[0]
            elif grid_col == 0:
                above = grid[grid_row - 1][0]
                piece = lookup[("top", -int(above["bottom"]))]
            else:
                left_piece = current[grid_col - 1]
                piece = lookup[("left", -int(left_piece["right"]))]

            if grid_row > 0:
                above = grid[grid_row - 1][grid_col]
                if int(piece["top"]) + int(above["bottom"]) != 0:
                    raise SystemExit(f"vertical mismatch at row {grid_row + 1}, col {grid_col + 1}")
            current.append(piece)
        grid.append(current)

    flattened = [piece for row in grid for piece in row]
    filenames = [str(piece["filename"]) for piece in flattened]
    if len(set(filenames)) != 64:
        raise SystemExit("grid traversal repeated or omitted pieces")
    for row_index, grid_line in enumerate(grid):
        for col_index, piece in enumerate(grid_line):
            if row_index == 0 and int(piece["top"]) != 0:
                raise SystemExit("non-flat top border")
            if row_index == 7 and int(piece["bottom"]) != 0:
                raise SystemExit("non-flat bottom border")
            if col_index == 0 and int(piece["left"]) != 0:
                raise SystemExit("non-flat left border")
            if col_index == 7 and int(piece["right"]) != 0:
                raise SystemExit("non-flat right border")

    layout_rows: list[dict[str, str | int]] = []
    for row_index, grid_line in enumerate(grid, start=1):
        for col_index, piece in enumerate(grid_line, start=1):
            layout_rows.append({"row": row_index, "col": col_index, **piece})
    with (output_dir / "layout.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=layout_rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(layout_rows)

    piece_size = 256
    cell = 128
    padding = 64
    canvas = Image.new("RGBA", (8 * cell + 2 * padding, 8 * cell + 2 * padding), (0, 0, 0, 0))
    pieces_dir = output_dir / "pieces"
    for row_index, grid_line in enumerate(grid):
        for col_index, piece in enumerate(grid_line):
            image = Image.open(pieces_dir / str(piece["filename"])).convert("RGBA")
            if image.size != (piece_size, piece_size):
                raise SystemExit(f"unexpected piece size for {piece['filename']}: {image.size}")
            canvas.alpha_composite(image, (col_index * cell, row_index * cell))
    assembled = canvas.crop((padding, padding, padding + 8 * cell, padding + 8 * cell))
    assembled.save(output_dir / "assembled.png")
    assembled.resize((256, 256), Image.Resampling.LANCZOS).save(output_dir / "assembled_thumb.png")
    assembled.filter(ImageFilter.GaussianBlur(radius=6)).save(output_dir / "assembled_blur.png")

    labeled = assembled.convert("RGBA")
    draw = ImageDraw.Draw(labeled, "RGBA")
    for offset in range(0, 8 * cell + 1, cell):
        draw.line((offset, 0, offset, 8 * cell), fill=(255, 255, 255, 110), width=1)
        draw.line((0, offset, 8 * cell, offset), fill=(255, 255, 255, 110), width=1)
    for row_index, grid_line in enumerate(grid):
        for col_index, piece in enumerate(grid_line):
            label = str(piece["stable_id"])
            x = col_index * cell + 4
            y = row_index * cell + 4
            draw.rectangle((x - 2, y - 2, x + 58, y + 12), fill=(0, 0, 0, 150))
            draw.text((x, y), label, fill=(255, 255, 255, 255))
    labeled.save(output_dir / "assembled_grid.png")
    print("assembled a unique 8x8 layout using all 64 pieces")
    print(f"top-left={grid[0][0]['stable_id']}; bottom-right={grid[7][7]['stable_id']}")


def rotate_codes(codes: list[int], quarter_turns: int) -> list[int]:
    quarter_turns %= 4
    return [codes[(direction - quarter_turns) % 4] for direction in range(4)]


def rotate_image(image: Image.Image, quarter_turns: int) -> Image.Image:
    operations = (
        None,
        Image.Transpose.ROTATE_270,
        Image.Transpose.ROTATE_180,
        Image.Transpose.ROTATE_90,
    )
    operation = operations[quarter_turns % 4]
    return image.copy() if operation is None else image.transpose(operation)


def canonical_rotation(codes: list[int]) -> tuple[int, int, int, int]:
    return min(tuple(rotate_codes(codes, rotation)) for rotation in range(4))


def fixed_layout_indices(rows: list[dict[str, str | int]]) -> list[int]:
    lookup: dict[tuple[int, int], int] = {}
    base_codes = [
        [int(row["top"]), int(row["right"]), int(row["bottom"]), int(row["left"])]
        for row in rows
    ]
    for piece_index, codes in enumerate(base_codes):
        for side, code in enumerate(codes):
            if code == 0:
                continue
            key = (side, code)
            if key in lookup:
                raise SystemExit(f"non-unique fixed-orientation edge code {key}")
            lookup[key] = piece_index

    top_left = [
        piece_index
        for piece_index, codes in enumerate(base_codes)
        if codes[0] == 0 and codes[3] == 0
    ]
    if len(top_left) != 1:
        raise SystemExit(f"expected one fixed-orientation top-left corner, found {len(top_left)}")

    grid: list[int] = []
    for position in range(64):
        row_index, col_index = divmod(position, 8)
        if position == 0:
            piece_index = top_left[0]
        elif col_index == 0:
            above_index = grid[position - 8]
            piece_index = lookup[(0, -base_codes[above_index][2])]
        else:
            left_index = grid[position - 1]
            piece_index = lookup[(3, -base_codes[left_index][1])]
        if row_index and base_codes[piece_index][0] != -base_codes[grid[position - 8]][2]:
            raise SystemExit(f"fixed-layout vertical mismatch at position {position}")
        grid.append(piece_index)
    if len(set(grid)) != 64:
        raise SystemExit("fixed layout repeats or omits pieces")
    return grid


def render_phase_layouts(source: Path, output_dir: Path) -> None:
    rows = decoded_rows(source)
    base_codes = [
        [int(row["top"]), int(row["right"]), int(row["bottom"]), int(row["left"])]
        for row in rows
    ]
    fixed_grid = fixed_layout_indices(rows)
    groups: dict[tuple[int, int, int, int], list[int]] = {}
    for piece_index, codes in enumerate(base_codes):
        groups.setdefault(canonical_rotation(codes), []).append(piece_index)

    group_rows: list[dict[str, str | int]] = []
    for group_index, (signature, members) in enumerate(sorted(groups.items()), start=1):
        for piece_index in members:
            phase_to_canonical = next(
                rotation
                for rotation in range(4)
                if tuple(rotate_codes(base_codes[piece_index], rotation)) == signature
            )
            group_rows.append(
                {
                    "group": group_index,
                    "group_size": len(members),
                    "canonical_top": signature[0],
                    "canonical_right": signature[1],
                    "canonical_bottom": signature[2],
                    "canonical_left": signature[3],
                    "stable_id": rows[piece_index]["stable_id"],
                    "filename": rows[piece_index]["filename"],
                    "phase_to_canonical": phase_to_canonical * 90,
                }
            )

    phase_dir = output_dir / "phase_layouts"
    phase_dir.mkdir(parents=True, exist_ok=True)
    with (phase_dir / "rotation_groups.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=group_rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(group_rows)

    all_placements: list[dict[str, str | int]] = []
    pieces_dir = output_dir / "pieces"
    phase_summaries: list[dict[str, int]] = []
    for phase in range(4):
        placements: list[dict[str, str | int]] = []
        used: set[int] = set()
        for position, target_piece_index in enumerate(fixed_grid):
            target_codes = base_codes[target_piece_index]
            matches = [
                piece_index
                for piece_index, codes in enumerate(base_codes)
                if piece_index not in used and rotate_codes(codes, phase) == target_codes
            ]
            if len(matches) != 1:
                raise SystemExit(
                    f"phase {phase}: target position {position} has {len(matches)} unused matches"
                )
            piece_index = matches[0]
            used.add(piece_index)
            codes = rotate_codes(base_codes[piece_index], phase)
            placement = {
                "phase": phase,
                "row": position // 8 + 1,
                "col": position % 8 + 1,
                "stable_id": rows[piece_index]["stable_id"],
                "filename": rows[piece_index]["filename"],
                "rotation": phase * 90,
                "top": codes[0],
                "right": codes[1],
                "bottom": codes[2],
                "left": codes[3],
            }
            placements.append(placement)
            all_placements.append(placement)
        if len(used) != 64:
            raise SystemExit(f"phase {phase}: used {len(used)} pieces")
        changed = sum(
            int(placement["stable_id"] != rows[fixed_grid[position]]["stable_id"])
            or int(placement["rotation"]) != 0
            for position, placement in enumerate(placements)
        )
        phase_summaries.append({"phase": phase, "rotation": phase * 90, "changed_cells": changed})
        render_rotating_solution(
            placements,
            pieces_dir,
            phase_dir / f"phase-{phase}-{phase * 90:03d}deg.png",
        )

    with (phase_dir / "phase_layouts.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=all_placements[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(all_placements)

    tile_size = 256
    label_height = 24
    orientation_sheet = Image.new(
        "RGB", (4 * tile_size, 4 * (tile_size + label_height)), (220, 220, 220)
    )
    sheet_draw = ImageDraw.Draw(orientation_sheet)
    for phase in range(4):
        base_image = Image.open(
            phase_dir / f"phase-{phase}-{phase * 90:03d}deg.png"
        ).convert("RGB")
        for global_rotation in range(4):
            view = rotate_image(base_image, global_rotation).resize(
                (tile_size, tile_size), Image.Resampling.LANCZOS
            )
            x = global_rotation * tile_size
            y = phase * (tile_size + label_height)
            orientation_sheet.paste(view, (x, y + label_height))
            sheet_draw.rectangle((x, y, x + tile_size, y + label_height), fill=(25, 25, 25))
            sheet_draw.text(
                (x + 6, y + 6),
                f"phase {phase}; whole +{global_rotation * 90} deg",
                fill=(255, 255, 255),
            )
    orientation_sheet.save(phase_dir / "phase_orientation_sheet.png")

    summary = {
        "rotation_group_count": len(groups),
        "rotation_group_sizes": sorted(len(members) for members in groups.values()),
        "phases": phase_summaries,
    }
    (phase_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False), flush=True)


def render_permutation_target(source: Path, output_dir: Path, permutation_file: Path) -> None:
    rows = decoded_rows(source)
    base_codes = [
        [int(row["top"]), int(row["right"]), int(row["bottom"]), int(row["left"])]
        for row in rows
    ]
    fixed_grid = fixed_layout_indices(rows)
    specification = json.loads(permutation_file.read_text(encoding="utf-8"))
    permutations = specification.get("permutations")
    if not isinstance(permutations, list) or len(permutations) != 16:
        raise SystemExit("permutation specification must contain 16 group permutations")

    group_positions: dict[tuple[int, int, int, int], list[int]] = {}
    for position, piece_index in enumerate(fixed_grid):
        signature = canonical_rotation(base_codes[piece_index])
        group_positions.setdefault(signature, []).append(position)
    if len(group_positions) != 16 or any(len(positions) != 4 for positions in group_positions.values()):
        raise SystemExit("expected 16 first-appearance groups of four positions")

    placements_by_position: list[dict[str, str | int] | None] = [None] * 64
    group_table: list[dict[str, str | int]] = []
    for group_index, ((signature, positions), permutation) in enumerate(
        zip(group_positions.items(), permutations), start=1
    ):
        if sorted(permutation) != [0, 1, 2, 3]:
            raise SystemExit(f"group {group_index} is not a permutation of 0,1,2,3")
        base_members = [fixed_grid[position] for position in positions]
        for slot, position in enumerate(positions):
            target_piece_index = fixed_grid[position]
            piece_index = base_members[int(permutation[slot])]
            rotations = [
                rotation
                for rotation in range(4)
                if rotate_codes(base_codes[piece_index], rotation) == base_codes[target_piece_index]
            ]
            if len(rotations) != 1:
                raise SystemExit(
                    f"group {group_index}, slot {slot}: expected one compatible rotation"
                )
            rotation = rotations[0]
            codes = rotate_codes(base_codes[piece_index], rotation)
            placement = {
                "group": group_index,
                "slot": slot,
                "row": position // 8 + 1,
                "col": position % 8 + 1,
                "stable_id": rows[piece_index]["stable_id"],
                "filename": rows[piece_index]["filename"],
                "rotation": rotation * 90,
                "top": codes[0],
                "right": codes[1],
                "bottom": codes[2],
                "left": codes[3],
            }
            placements_by_position[position] = placement
            group_table.append(
                {
                    "group": group_index,
                    "slot": slot,
                    "target_position": position,
                    "target_stable_id": rows[target_piece_index]["stable_id"],
                    "source_member_index": int(permutation[slot]),
                    "source_stable_id": rows[piece_index]["stable_id"],
                    "rotation": rotation * 90,
                    "canonical_signature": ",".join(map(str, signature)),
                }
            )

    if any(placement is None for placement in placements_by_position):
        raise SystemExit("recovered target has unfilled positions")
    placements = [placement for placement in placements_by_position if placement is not None]
    if len({str(placement["filename"]) for placement in placements}) != 64:
        raise SystemExit("recovered target repeats or omits pieces")

    target_dir = output_dir / "recovered_target"
    target_dir.mkdir(parents=True, exist_ok=True)
    render_rotating_solution(placements, output_dir / "pieces", target_dir / "assembled.png")
    with (target_dir / "layout.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=placements[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(placements)
    with (target_dir / "group_permutations.tsv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=group_table[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(group_table)
    payload = {
        "action": "validate",
        "pieces": [
            {
                "filename": placement["filename"],
                "row": int(placement["row"]) - 1,
                "col": int(placement["col"]) - 1,
                "rotation": placement["rotation"],
            }
            for placement in placements
        ],
    }
    (target_dir / "validation_payload.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    base_image = Image.open(target_dir / "assembled.png").convert("RGB")
    orientation_sheet = Image.new("RGB", (4 * 256, 280), (220, 220, 220))
    sheet_draw = ImageDraw.Draw(orientation_sheet)
    for global_rotation in range(4):
        oriented = rotate_image(base_image, global_rotation)
        oriented.save(target_dir / f"orientation-{global_rotation * 90:03d}deg.png")
        view = oriented.resize(
            (256, 256), Image.Resampling.LANCZOS
        )
        x = global_rotation * 256
        orientation_sheet.paste(view, (x, 24))
        sheet_draw.rectangle((x, 0, x + 256, 24), fill=(25, 25, 25))
        sheet_draw.text(
            (x + 6, 6), f"whole +{global_rotation * 90} deg", fill=(255, 255, 255)
        )
    orientation_sheet.save(target_dir / "orientation_sheet.png")
    summary = {
        "source": str(permutation_file),
        "group_order": specification.get("group_order"),
        "groups": len(group_positions),
        "pieces": len(placements),
    }
    (target_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False), flush=True)


def render_rotating_solution(
    placements: list[dict[str, str | int]], pieces_dir: Path, destination: Path
) -> None:
    piece_size = 256
    cell = 128
    padding = 64
    canvas = Image.new("RGBA", (8 * cell + 2 * padding, 8 * cell + 2 * padding), (0, 0, 0, 0))
    for placement in placements:
        image = Image.open(pieces_dir / str(placement["filename"])).convert("RGBA")
        image = rotate_image(image, int(placement["rotation"]) // 90)
        canvas.alpha_composite(
            image,
            ((int(placement["col"]) - 1) * cell, (int(placement["row"]) - 1) * cell),
        )
    assembled = canvas.crop((padding, padding, padding + 8 * cell, padding + 8 * cell))
    assembled.save(destination)
    assembled.resize((256, 256), Image.Resampling.LANCZOS).save(
        destination.with_name(destination.stem + "-thumb.png")
    )


def enumerate_rotating_solutions(
    source: Path,
    output_dir: Path,
    max_solutions: int,
    total_seconds: float,
    anchor_stable_id: str,
) -> None:
    import z3

    rows = decoded_rows(source)
    if len(rows) != 64:
        raise SystemExit(f"expected 64 pieces, found {len(rows)}")
    anchor_indices = [index for index, row in enumerate(rows) if row["stable_id"] == anchor_stable_id]
    if len(anchor_indices) != 1:
        raise SystemExit(f"anchor {anchor_stable_id!r} not found uniquely")
    anchor_index = anchor_indices[0]

    base_codes = [
        [int(row["top"]), int(row["right"]), int(row["bottom"]), int(row["left"])]
        for row in rows
    ]
    rotated_codes = [
        rotate_codes(base_codes[piece_index], rotation)
        for piece_index in range(64)
        for rotation in range(4)
    ]

    solver = z3.Solver()
    states = [z3.Int(f"cell_{position}") for position in range(64)]
    for state in states:
        solver.add(state >= 0, state < 256)
    solver.add(z3.Distinct([state / 4 for state in states]))

    edge_arrays = [z3.Array(f"edge_{side}", z3.IntSort(), z3.IntSort()) for side in range(4)]
    for state_index, codes in enumerate(rotated_codes):
        for side in range(4):
            solver.add(edge_arrays[side][state_index] == codes[side])

    solver.add(states[0] == 4 * anchor_index)
    for row_index in range(8):
        for col_index in range(8):
            position = 8 * row_index + col_index
            state = states[position]
            if row_index == 0:
                solver.add(edge_arrays[0][state] == 0)
            if col_index == 7:
                solver.add(edge_arrays[1][state] == 0)
            if row_index == 7:
                solver.add(edge_arrays[2][state] == 0)
            if col_index == 0:
                solver.add(edge_arrays[3][state] == 0)
            if col_index < 7:
                right_state = states[position + 1]
                solver.add(edge_arrays[1][state] != 0)
                solver.add(edge_arrays[1][state] + edge_arrays[3][right_state] == 0)
            if row_index < 7:
                below_state = states[position + 8]
                solver.add(edge_arrays[2][state] != 0)
                solver.add(edge_arrays[2][state] + edge_arrays[0][below_state] == 0)

    solutions_dir = output_dir / "rotating_solutions"
    solutions_dir.mkdir(parents=True, exist_ok=True)
    deadline = time.monotonic() + total_seconds
    all_placements: list[dict[str, str | int]] = []
    solution_count = 0
    terminal_status = "max_solutions"
    pieces_dir = output_dir / "pieces"

    while solution_count < max_solutions:
        remaining_ms = int(max(0.0, deadline - time.monotonic()) * 1000)
        if remaining_ms <= 0:
            terminal_status = "timeout"
            break
        solver.set(timeout=remaining_ms)
        result = solver.check()
        if result == z3.unsat:
            terminal_status = "exhausted"
            break
        if result != z3.sat:
            terminal_status = f"unknown:{solver.reason_unknown()}"
            break

        model = solver.model()
        values = [model.eval(state).as_long() for state in states]
        solution_count += 1
        placements: list[dict[str, str | int]] = []
        for position, state_value in enumerate(values):
            piece_index, rotation = divmod(state_value, 4)
            piece = rows[piece_index]
            codes = rotated_codes[state_value]
            placement = {
                "solution": solution_count,
                "row": position // 8 + 1,
                "col": position % 8 + 1,
                "stable_id": piece["stable_id"],
                "filename": piece["filename"],
                "rotation": rotation * 90,
                "top": codes[0],
                "right": codes[1],
                "bottom": codes[2],
                "left": codes[3],
            }
            placements.append(placement)
            all_placements.append(placement)

        render_rotating_solution(
            placements,
            pieces_dir,
            solutions_dir / f"solution-{solution_count:02d}.png",
        )
        solver.add(z3.Or([state != value for state, value in zip(states, values)]))
        corners = [placements[index]["stable_id"] for index in (0, 7, 56, 63)]
        rotation_counts = {
            rotation: sum(int(item["rotation"]) == rotation for item in placements)
            for rotation in (0, 90, 180, 270)
        }
        print(f"solution {solution_count}: corners={corners}, rotations={rotation_counts}")

    if all_placements:
        with (solutions_dir / "solutions.tsv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=all_placements[0].keys(), delimiter="\t")
            writer.writeheader()
            writer.writerows(all_placements)
    summary = {
        "anchor": anchor_stable_id,
        "max_solutions": max_solutions,
        "total_seconds": total_seconds,
        "solutions_found": solution_count,
        "terminal_status": terminal_status,
    }
    (solutions_dir / "enumeration_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False))


def enumerate_backtracking_solutions(
    source: Path,
    output_dir: Path,
    max_solutions: int,
    total_seconds: float,
    max_nodes: int,
    anchor_stable_id: str,
) -> None:
    rows = decoded_rows(source)
    anchor_indices = [index for index, row in enumerate(rows) if row["stable_id"] == anchor_stable_id]
    if len(anchor_indices) != 1:
        raise SystemExit(f"anchor {anchor_stable_id!r} not found uniquely")
    anchor_state = 4 * anchor_indices[0]
    base_codes = [
        [int(row["top"]), int(row["right"]), int(row["bottom"]), int(row["left"])]
        for row in rows
    ]
    rotated_codes = [
        rotate_codes(base_codes[piece_index], rotation)
        for piece_index in range(64)
        for rotation in range(4)
    ]

    position_states: list[list[int]] = []
    for position in range(64):
        row_index, col_index = divmod(position, 8)
        candidates: list[int] = []
        for state, codes in enumerate(rotated_codes):
            border_conditions = (
                (codes[0] == 0) == (row_index == 0)
                and (codes[1] == 0) == (col_index == 7)
                and (codes[2] == 0) == (row_index == 7)
                and (codes[3] == 0) == (col_index == 0)
            )
            if border_conditions:
                candidates.append(state)
        candidates.sort(key=lambda state: (state % 4 != 0, state // 4, state % 4))
        position_states.append(candidates)

    grid = [-1] * 64
    used = [False] * 64
    solutions: list[list[int]] = []
    nodes = 0
    deadline = time.monotonic() + total_seconds
    terminal_status = "exhausted"

    def search(position: int) -> bool:
        nonlocal nodes, terminal_status
        if len(solutions) >= max_solutions:
            terminal_status = "max_solutions"
            return False
        if nodes >= max_nodes:
            terminal_status = "max_nodes"
            return False
        if time.monotonic() >= deadline:
            terminal_status = "timeout"
            return False
        if position == 64:
            solutions.append(grid.copy())
            print(f"found solution {len(solutions)} after {nodes} nodes", flush=True)
            return True

        row_index, col_index = divmod(position, 8)
        top_required = None if row_index == 0 else -rotated_codes[grid[position - 8]][2]
        left_required = None if col_index == 0 else -rotated_codes[grid[position - 1]][1]
        any_solution = False
        for state in position_states[position]:
            piece_index = state // 4
            if used[piece_index]:
                continue
            if position == 0 and state != anchor_state:
                continue
            codes = rotated_codes[state]
            if top_required is not None and codes[0] != top_required:
                continue
            if left_required is not None and codes[3] != left_required:
                continue
            nodes += 1
            grid[position] = state
            used[piece_index] = True
            child_found = search(position + 1)
            any_solution = any_solution or child_found
            used[piece_index] = False
            grid[position] = -1
            if terminal_status in {"max_solutions", "max_nodes", "timeout"}:
                return any_solution
        return any_solution

    search(0)
    solutions_dir = output_dir / "rotating_solutions"
    solutions_dir.mkdir(parents=True, exist_ok=True)
    pieces_dir = output_dir / "pieces"
    all_placements: list[dict[str, str | int]] = []
    for solution_index, values in enumerate(solutions, start=1):
        placements: list[dict[str, str | int]] = []
        for position, state in enumerate(values):
            piece_index, rotation = divmod(state, 4)
            piece = rows[piece_index]
            codes = rotated_codes[state]
            placement = {
                "solution": solution_index,
                "row": position // 8 + 1,
                "col": position % 8 + 1,
                "stable_id": piece["stable_id"],
                "filename": piece["filename"],
                "rotation": rotation * 90,
                "top": codes[0],
                "right": codes[1],
                "bottom": codes[2],
                "left": codes[3],
            }
            placements.append(placement)
            all_placements.append(placement)
        render_rotating_solution(
            placements,
            pieces_dir,
            solutions_dir / f"solution-{solution_index:02d}.png",
        )
    if all_placements:
        with (solutions_dir / "solutions.tsv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=all_placements[0].keys(), delimiter="\t")
            writer.writeheader()
            writer.writerows(all_placements)
    summary = {
        "search_method": "row-major-backtracking",
        "anchor": anchor_stable_id,
        "max_solutions": max_solutions,
        "max_nodes": max_nodes,
        "total_seconds": total_seconds,
        "nodes_visited": nodes,
        "solutions_found": len(solutions),
        "terminal_status": terminal_status,
    }
    (solutions_dir / "enumeration_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False), flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract and solve the Pinduoduo jigsaw.")
    parser.add_argument("--source", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--max-solutions", type=int, default=32)
    parser.add_argument("--total-seconds", type=float, default=60.0)
    parser.add_argument("--max-nodes", type=int, default=5_000_000)
    parser.add_argument("--anchor", default="piece-36")
    parser.add_argument("--permutation-file", type=Path)
    parser.add_argument(
        "--mode",
        choices=(
            "extract",
            "analyze",
            "inspect-runtime",
            "decode",
            "solve",
            "enumerate",
            "enumerate-backtrack",
            "phase-layouts",
            "render-permutation",
        ),
        default="analyze",
    )
    args = parser.parse_args()

    if args.mode == "extract":
        if args.source is None:
            parser.error("--source is required in extract mode")
        extract(args.source, args.output_dir)
    elif args.mode == "analyze":
        analyze(args.output_dir)
    elif args.mode == "inspect-runtime":
        if args.source is None:
            parser.error("--source is required in inspect-runtime mode")
        inspect_runtime(args.source, args.output_dir)
    elif args.mode == "decode":
        if args.source is None:
            parser.error("--source is required in decode mode")
        decode_edges(args.source, args.output_dir)
    elif args.mode == "solve":
        if args.source is None:
            parser.error("--source is required in solve mode")
        solve(args.source, args.output_dir)
    elif args.mode == "enumerate":
        if args.source is None:
            parser.error("--source is required in enumerate mode")
        enumerate_rotating_solutions(
            args.source,
            args.output_dir,
            max_solutions=args.max_solutions,
            total_seconds=args.total_seconds,
            anchor_stable_id=args.anchor,
        )
    elif args.mode == "enumerate-backtrack":
        if args.source is None:
            parser.error("--source is required in enumerate-backtrack mode")
        enumerate_backtracking_solutions(
            args.source,
            args.output_dir,
            max_solutions=args.max_solutions,
            total_seconds=args.total_seconds,
            max_nodes=args.max_nodes,
            anchor_stable_id=args.anchor,
        )
    elif args.mode == "phase-layouts":
        if args.source is None:
            parser.error("--source is required in phase-layouts mode")
        render_phase_layouts(args.source, args.output_dir)
    elif args.mode == "render-permutation":
        if args.source is None or args.permutation_file is None:
            parser.error("--source and --permutation-file are required in render-permutation mode")
        render_permutation_target(args.source, args.output_dir, args.permutation_file)


if __name__ == "__main__":
    main()
