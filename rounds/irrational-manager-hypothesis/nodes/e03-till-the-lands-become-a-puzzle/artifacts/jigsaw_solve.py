"""Analyze and partially assemble the 8x8 satellite-image jigsaw.

The script keeps one stable model for the hypothesis family:
1. find each piece's 140 px logical cell inside its cropped RGBA image;
2. classify each side as flat, tab, or hole;
3. score every geometrically compatible pair in all four rotations using the
   RGB discontinuity along the shared irregular boundary;
4. emit stable TSV/JSON tables for manual audit and later assembly.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


SIDES = ("top", "right", "bottom", "left")
COMPLEMENT = {"tab": "hole", "hole": "tab", "flat": "flat"}


@dataclass
class Piece:
    piece_id: str
    path: Path
    rgba: np.ndarray
    pitch: int
    anchor_x: int
    anchor_y: int
    anchor_score: float


@dataclass
class OrientedPiece:
    piece_id: str
    rotation: int
    rgba: np.ndarray
    pitch: int
    anchor_x: int
    anchor_y: int
    sides: dict[str, str]
    normalized: np.ndarray


def rect_sum(integral: np.ndarray, x0: int, y0: int, x1: int, y1: int) -> int:
    if x1 <= x0 or y1 <= y0:
        return 0
    return int(
        integral[y1, x1]
        - integral[y0, x1]
        - integral[y1, x0]
        + integral[y0, x0]
    )


def anchor_cost(
    mask: np.ndarray,
    integ: np.ndarray,
    x0: int,
    y0: int,
    pitch: int,
) -> float:
    """Score a candidate logical-cell rectangle; lower is better."""
    height, width = mask.shape
    q = 28
    center_margin = 42

    guaranteed = [
        (x0, y0, x0 + q, y0 + q),
        (x0 + pitch - q, y0, x0 + pitch, y0 + q),
        (x0, y0 + pitch - q, x0 + q, y0 + pitch),
        (x0 + pitch - q, y0 + pitch - q, x0 + pitch, y0 + pitch),
        (
            x0 + center_margin,
            y0 + center_margin,
            x0 + pitch - center_margin,
            y0 + pitch - center_margin,
        ),
    ]
    missing = 0
    for ax0, ay0, ax1, ay1 in guaranteed:
        area = (ax1 - ax0) * (ay1 - ay0)
        missing += area - rect_sum(integ, ax0, ay0, ax1, ay1)

    # Outside the logical cell, opaque pixels are allowed only in a centered
    # tab corridor. Any opacity near an outside corner indicates a bad anchor.
    lo = int(round(pitch * 0.24))
    hi = pitch - lo
    forbidden = 0
    if y0 > 0:
        forbidden += rect_sum(integ, 0, 0, x0 + lo, y0)
        forbidden += rect_sum(integ, x0 + hi, 0, width, y0)
    if y0 + pitch < height:
        forbidden += rect_sum(integ, 0, y0 + pitch, x0 + lo, height)
        forbidden += rect_sum(integ, x0 + hi, y0 + pitch, width, height)
    if x0 > 0:
        forbidden += rect_sum(integ, 0, 0, x0, y0 + lo)
        forbidden += rect_sum(integ, 0, y0 + hi, x0, height)
    if x0 + pitch < width:
        forbidden += rect_sum(integ, x0 + pitch, 0, width, y0 + lo)
        forbidden += rect_sum(integ, x0 + pitch, y0 + hi, width, height)

    # Encourage the four cell-boundary corner segments to be solid.
    boundary_expected = 0
    boundary_opaque = 0
    segments = [
        (x0, y0, x0 + q, y0 + 2),
        (x0 + pitch - q, y0, x0 + pitch, y0 + 2),
        (x0, y0 + pitch - 2, x0 + q, y0 + pitch),
        (x0 + pitch - q, y0 + pitch - 2, x0 + pitch, y0 + pitch),
        (x0, y0, x0 + 2, y0 + q),
        (x0, y0 + pitch - q, x0 + 2, y0 + pitch),
        (x0 + pitch - 2, y0, x0 + pitch, y0 + q),
        (x0 + pitch - 2, y0 + pitch - q, x0 + pitch, y0 + pitch),
    ]
    for ax0, ay0, ax1, ay1 in segments:
        boundary_expected += (ax1 - ax0) * (ay1 - ay0)
        boundary_opaque += rect_sum(integ, ax0, ay0, ax1, ay1)

    return float(missing * 5 + forbidden * 4 + (boundary_expected - boundary_opaque) * 3)


def find_anchor(rgba: np.ndarray, pitch_hint: int) -> tuple[int, int, int, float]:
    mask = rgba[:, :, 3] >= 96
    height, width = mask.shape
    integ = cv2.integral(mask.astype(np.uint8), sdepth=cv2.CV_32S)
    best: tuple[float, int, int, int] | None = None
    # Every piece comes from one source grid. A common pitch makes normalized
    # edge signatures directly comparable across the full collection.
    for pitch in [pitch_hint]:
        if pitch > width or pitch > height:
            continue
        for y0 in range(height - pitch + 1):
            for x0 in range(width - pitch + 1):
                cost = anchor_cost(mask, integ, x0, y0, pitch)
                candidate = (cost, pitch, x0, y0)
                if best is None or candidate < best:
                    best = candidate
    if best is None:
        raise ValueError(f"image {width}x{height} is smaller than pitch {pitch_hint}")
    cost, pitch, x0, y0 = best
    return x0, y0, pitch, cost


def rotated_anchor(piece: Piece, rotation: int) -> tuple[int, int]:
    rotation %= 4
    h, w = piece.rgba.shape[:2]
    x0, y0, s = piece.anchor_x, piece.anchor_y, piece.pitch
    if rotation == 0:
        return x0, y0
    if rotation == 1:  # 90 degrees counter-clockwise
        return y0, w - x0 - s
    if rotation == 2:
        return w - x0 - s, h - y0 - s
    return h - y0 - s, x0


def classify_sides(rgba: np.ndarray, x0: int, y0: int, pitch: int) -> dict[str, str]:
    mask = rgba[:, :, 3] >= 96
    h, w = mask.shape
    lo = int(round(pitch * 0.28))
    hi = pitch - lo
    depth = min(48, pitch // 3)

    measurements: dict[str, tuple[int, int]] = {}
    measurements["top"] = (
        int(mask[:y0, x0 + lo : x0 + hi].sum()),
        int((~mask[y0 : y0 + depth, x0 + lo : x0 + hi]).sum()),
    )
    measurements["bottom"] = (
        int(mask[y0 + pitch :, x0 + lo : x0 + hi].sum()),
        int((~mask[y0 + pitch - depth : y0 + pitch, x0 + lo : x0 + hi]).sum()),
    )
    measurements["left"] = (
        int(mask[y0 + lo : y0 + hi, :x0].sum()),
        int((~mask[y0 + lo : y0 + hi, x0 : x0 + depth]).sum()),
    )
    measurements["right"] = (
        int(mask[y0 + lo : y0 + hi, x0 + pitch :].sum()),
        int((~mask[y0 + lo : y0 + hi, x0 + pitch - depth : x0 + pitch]).sum()),
    )

    result: dict[str, str] = {}
    for side, (outside, missing_inside) in measurements.items():
        if outside >= 80:
            result[side] = "tab"
        elif missing_inside >= 80:
            result[side] = "hole"
        else:
            result[side] = "flat"
    return result


def normalize_orientation(piece: Piece, rotation: int, extension: int) -> OrientedPiece:
    rgba = np.rot90(piece.rgba, rotation).copy()
    x0, y0 = rotated_anchor(piece, rotation)
    sides = classify_sides(rgba, x0, y0, piece.pitch)
    size = piece.pitch + 2 * extension
    canvas = np.zeros((size, size, 4), dtype=np.uint8)
    dst_x = extension - x0
    dst_y = extension - y0
    h, w = rgba.shape[:2]
    canvas[dst_y : dst_y + h, dst_x : dst_x + w] = rgba
    return OrientedPiece(
        piece_id=piece.piece_id,
        rotation=(rotation * 90) % 360,
        rgba=rgba,
        pitch=piece.pitch,
        anchor_x=x0,
        anchor_y=y0,
        sides=sides,
        normalized=canvas,
    )


def contact_color_differences(
    mask_a: np.ndarray,
    rgb_a: np.ndarray,
    mask_b: np.ndarray,
    rgb_b: np.ndarray,
) -> np.ndarray:
    differences: list[np.ndarray] = []
    # A pixel followed by a B pixel in each of the four cardinal directions.
    contacts = [
        (mask_a[:, :-1] & mask_b[:, 1:], rgb_a[:, :-1], rgb_b[:, 1:]),
        (mask_a[:, 1:] & mask_b[:, :-1], rgb_a[:, 1:], rgb_b[:, :-1]),
        (mask_a[:-1, :] & mask_b[1:, :], rgb_a[:-1, :], rgb_b[1:, :]),
        (mask_a[1:, :] & mask_b[:-1, :], rgb_a[1:, :], rgb_b[:-1, :]),
    ]
    for contact, colors_a, colors_b in contacts:
        if np.any(contact):
            delta = colors_a[contact].astype(np.float32) - colors_b[contact].astype(np.float32)
            differences.append(np.sqrt(np.sum(delta * delta, axis=1)))
    if not differences:
        return np.empty((0,), dtype=np.float32)
    return np.concatenate(differences)


def pair_score(
    a: OrientedPiece,
    b: OrientedPiece,
    direction: str,
    extension: int,
    require_complement: bool = True,
) -> dict[str, float] | None:
    if direction == "right":
        side_a, side_b = a.sides["right"], b.sides["left"]
    else:
        side_a, side_b = a.sides["bottom"], b.sides["top"]
    if require_complement and (side_a == "flat" or side_b != COMPLEMENT[side_a]):
        return None

    s = a.pitch
    if b.pitch != s:
        return None
    if direction == "right":
        patch_a = a.normalized[:, s : s + 2 * extension]
        patch_b = b.normalized[:, : 2 * extension]
        seam_union_slice = (slice(extension, extension + s), slice(extension - 2, extension + 3))
    else:
        patch_a = a.normalized[s : s + 2 * extension, :]
        patch_b = b.normalized[: 2 * extension, :]
        seam_union_slice = (slice(extension - 2, extension + 3), slice(extension, extension + s))

    alpha_a = patch_a[:, :, 3]
    alpha_b = patch_b[:, :, 3]
    mask_a = alpha_a >= 96
    mask_b = alpha_b >= 96
    overlap = int((mask_a & mask_b).sum())
    union = mask_a | mask_b
    gap = int((~union[seam_union_slice]).sum())
    diffs = contact_color_differences(mask_a, patch_a[:, :, :3], mask_b, patch_b[:, :, :3])
    contact_count = int(diffs.size)
    if contact_count < 20:
        return None

    median = float(np.median(diffs))
    mean = float(np.mean(diffs))
    p90 = float(np.percentile(diffs, 90))
    score = median + 0.18 * mean + 0.05 * p90 + 1.2 * overlap + 0.8 * gap
    return {
        "score": score,
        "median_rgb": median,
        "mean_rgb": mean,
        "p90_rgb": p90,
        "contact_count": float(contact_count),
        "overlap": float(overlap),
        "gap": float(gap),
    }


def load_pieces(directory: Path, pitch_hint: int) -> list[Piece]:
    pieces: list[Piece] = []
    for path in sorted(directory.glob("*.png")):
        rgba = np.array(Image.open(path).convert("RGBA"))
        x0, y0, pitch, score = find_anchor(rgba, pitch_hint)
        pieces.append(
            Piece(
                piece_id=path.stem[:8],
                path=path,
                rgba=rgba,
                pitch=pitch,
                anchor_x=x0,
                anchor_y=y0,
                anchor_score=score,
            )
        )
    if not pieces:
        raise SystemExit(f"no PNG files in {directory}")
    return pieces


def render_anchor_sheet(pieces: list[Piece], output_path: Path) -> None:
    cell_w, cell_h = 300, 290
    columns = 4
    rows = math.ceil(len(pieces) / columns)
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "#ececec")
    font = ImageFont.load_default()
    for index, piece in enumerate(pieces):
        col, row = index % columns, index // columns
        tile = Image.fromarray(piece.rgba)
        scale = min(1.0, 220 / max(tile.size))
        if scale < 1:
            tile = tile.resize((round(tile.width * scale), round(tile.height * scale)), Image.Resampling.LANCZOS)
        x = col * cell_w + (cell_w - tile.width) // 2
        y = row * cell_h + 38 + (220 - tile.height) // 2
        sheet.paste(tile, (x, y), tile)
        draw = ImageDraw.Draw(sheet)
        ax = x + round(piece.anchor_x * scale)
        ay = y + round(piece.anchor_y * scale)
        size = round(piece.pitch * scale)
        draw.rectangle((ax, ay, ax + size - 1, ay + size - 1), outline="#ff3050", width=2)
        sides = classify_sides(piece.rgba, piece.anchor_x, piece.anchor_y, piece.pitch)
        draw.text((col * cell_w + 8, row * cell_h + 8), f"{piece.piece_id}  {piece.rgba.shape[1]}x{piece.rgba.shape[0]}", fill="black", font=font)
        draw.text((col * cell_w + 8, row * cell_h + 23), f"anchor=({piece.anchor_x},{piece.anchor_y}) S={piece.pitch} cost={piece.anchor_score:.0f}", fill="black", font=font)
        draw.text((col * cell_w + 8, row * cell_h + 258), " ".join(f"{side[0]}:{sides[side][0]}" for side in SIDES), fill="black", font=font)
    sheet.save(output_path)


def write_tables(
    pieces: list[Piece],
    orientations: list[OrientedPiece],
    matches: list[dict[str, object]],
    output_dir: Path,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "pieces.tsv").open("w", encoding="utf-8", newline="") as handle:
        fields = ["piece_id", "filename", "width", "height", "pitch", "anchor_x", "anchor_y", "anchor_score", *SIDES]
        writer = csv.DictWriter(handle, fields, delimiter="\t")
        writer.writeheader()
        for piece in pieces:
            sides = classify_sides(piece.rgba, piece.anchor_x, piece.anchor_y, piece.pitch)
            writer.writerow(
                {
                    "piece_id": piece.piece_id,
                    "filename": piece.path.name,
                    "width": piece.rgba.shape[1],
                    "height": piece.rgba.shape[0],
                    "pitch": piece.pitch,
                    "anchor_x": piece.anchor_x,
                    "anchor_y": piece.anchor_y,
                    "anchor_score": f"{piece.anchor_score:.1f}",
                    **sides,
                }
            )

    match_fields = [
        "score", "direction", "a", "a_rotation", "a_side", "b", "b_rotation", "b_side",
        "median_rgb", "mean_rgb", "p90_rgb", "contact_count", "overlap", "gap",
    ]
    with (output_dir / "matches.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, match_fields, delimiter="\t")
        writer.writeheader()
        for row in matches:
            writer.writerow(row)

    model = {
        "pitch_hint": int(round(np.median([piece.pitch for piece in pieces]))),
        "pieces": [
            {
                "piece_id": piece.piece_id,
                "filename": piece.path.name,
                "width": piece.rgba.shape[1],
                "height": piece.rgba.shape[0],
                "pitch": piece.pitch,
                "anchor": [piece.anchor_x, piece.anchor_y],
                "anchor_score": piece.anchor_score,
            }
            for piece in pieces
        ],
        "orientations": [
            {
                "piece_id": oriented.piece_id,
                "rotation": oriented.rotation,
                "anchor": [oriented.anchor_x, oriented.anchor_y],
                "sides": oriented.sides,
            }
            for oriented in orientations
        ],
        "matches": matches,
    }
    (output_dir / "model.json").write_text(json.dumps(model, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rotate_grid_vector(vector: tuple[int, int], degrees: int) -> tuple[int, int]:
    """Rotate a screen-coordinate grid vector counter-clockwise."""
    x, y = vector
    return {
        0: (x, y),
        90: (y, -x),
        180: (-x, -y),
        270: (-y, x),
    }[degrees % 360]


def assemble_exact_components(
    pieces: list[Piece],
    orientations: list[OrientedPiece],
    matches: list[dict[str, object]],
    output_dir: Path,
    extension: int,
    exact_threshold: float,
    grid_size: int,
) -> None:
    """Assemble connected components from shape-exact, image-continuous seams."""
    best_by_pair: dict[tuple[str, str], dict[str, object]] = {}
    for match in matches:
        if int(match["overlap"]) != 0 or int(match["gap"]) != 0:
            continue
        if float(match["score"]) > exact_threshold:
            continue
        key = tuple(sorted((str(match["a"]), str(match["b"]))))
        incumbent = best_by_pair.get(key)
        if incumbent is None or float(match["score"]) < float(incumbent["score"]):
            best_by_pair[key] = match
    exact_edges = sorted(best_by_pair.values(), key=lambda row: float(row["score"]))

    edge_fields = [
        "score", "direction", "a", "a_rotation", "b", "b_rotation",
        "median_rgb", "mean_rgb", "p90_rgb", "contact_count",
    ]
    with (output_dir / "exact-edges.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, edge_fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(exact_edges)

    # Each directed relation stores the source/target pose in the edge's local
    # frame plus a one-cell target offset. Rotating that entire relation to the
    # source's assigned pose yields a global constraint.
    adjacency: dict[str, list[tuple[str, int, int, tuple[int, int], float]]] = {
        piece.piece_id: [] for piece in pieces
    }
    for edge in exact_edges:
        a, b = str(edge["a"]), str(edge["b"])
        ra, rb = int(edge["a_rotation"]), int(edge["b_rotation"])
        delta = (1, 0) if edge["direction"] == "right" else (0, 1)
        score = float(edge["score"])
        adjacency[a].append((b, ra, rb, delta, score))
        adjacency[b].append((a, rb, ra, (-delta[0], -delta[1]), score))

    assigned: dict[str, tuple[int, int, int]] = {}
    components: list[list[str]] = []
    conflicts: list[str] = []
    for root in sorted(adjacency):
        if root in assigned:
            continue
        assigned[root] = (0, 0, 0)
        queue = [root]
        component: list[str] = []
        while queue:
            source = queue.pop(0)
            component.append(source)
            sx, sy, source_rotation = assigned[source]
            for target, local_source_rotation, local_target_rotation, offset, score in adjacency[source]:
                frame_rotation = (source_rotation - local_source_rotation) % 360
                dx, dy = rotate_grid_vector(offset, frame_rotation)
                proposal = (
                    sx + dx,
                    sy + dy,
                    (local_target_rotation + frame_rotation) % 360,
                )
                if target not in assigned:
                    assigned[target] = proposal
                    queue.append(target)
                elif assigned[target] != proposal:
                    conflicts.append(
                        f"{source}->{target} score={score:.4f}: {assigned[target]} != {proposal}"
                    )
        components.append(sorted(component))

    # Larger connected islands first; stable ID order breaks ties.
    components.sort(key=lambda members: (-len(members), members))
    # Remove stale component renders from earlier runs with fewer pieces or a
    # different threshold, so the output directory stays a canonical view.
    for stale_path in output_dir.glob("component-*.png"):
        stale_path.unlink()
    oriented_lookup = {(item.piece_id, item.rotation): item for item in orientations}
    assembly_rows: list[dict[str, object]] = []
    font = ImageFont.load_default()
    for component_index, members in enumerate(components, start=1):
        xs = [assigned[piece_id][0] for piece_id in members]
        ys = [assigned[piece_id][1] for piece_id in members]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        pitch = pieces[0].pitch
        width = (max_x - min_x + 1) * pitch + 2 * extension
        height = (max_y - min_y + 1) * pitch + 2 * extension
        canvas = Image.new("RGBA", (width, height), (22, 22, 22, 255))
        labeled = Image.new("RGBA", (width, height), (22, 22, 22, 255))
        for piece_id in members:
            grid_x, grid_y, rotation = assigned[piece_id]
            oriented = oriented_lookup[(piece_id, rotation)]
            tile = Image.fromarray(oriented.normalized)
            paste_x = (grid_x - min_x) * pitch
            paste_y = (grid_y - min_y) * pitch
            canvas.alpha_composite(tile, (paste_x, paste_y))
            labeled.alpha_composite(tile, (paste_x, paste_y))
            assembly_rows.append(
                {
                    "component": component_index,
                    "piece_id": piece_id,
                    "x": grid_x - min_x,
                    "y": grid_y - min_y,
                    "rotation": rotation,
                }
            )
        label_draw = ImageDraw.Draw(labeled)
        for piece_id in members:
            grid_x, grid_y, rotation = assigned[piece_id]
            text_x = extension + (grid_x - min_x) * pitch + 4
            text_y = extension + (grid_y - min_y) * pitch + 4
            caption = f"{piece_id} r{rotation}"
            box = label_draw.textbbox((text_x, text_y), caption, font=font)
            label_draw.rectangle((box[0] - 2, box[1] - 1, box[2] + 2, box[3] + 1), fill=(255, 255, 255, 210))
            label_draw.text((text_x, text_y), caption, fill=(0, 0, 0, 255), font=font)
        canvas.convert("RGB").save(output_dir / f"component-{component_index:02d}.png")
        labeled.convert("RGB").save(output_dir / f"component-{component_index:02d}-labeled.png")

    with (output_dir / "assembly.tsv").open("w", encoding="utf-8", newline="") as handle:
        fields = ["component", "piece_id", "x", "y", "rotation"]
        writer = csv.DictWriter(handle, fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(assembly_rows)

    # Place every connected component into the known square source grid.  A
    # true flat edge must lie on the corresponding outer border, and every
    # occupied border cell must expose a flat edge.  Missing pieces may fill
    # arbitrary other cells, so this produces all placements justified by the
    # currently collected pieces without guessing any seam.
    placement_rows: list[dict[str, object]] = []
    placement_summary_rows: list[dict[str, object]] = []
    all_component_candidates: dict[int, list[dict[str, object]]] = {}
    for component_index, members in enumerate(components, start=1):
        component_candidates: list[dict[str, object]] = []
        for whole_rotation in (0, 90, 180, 270):
            rotated_poses: dict[str, tuple[int, int, int]] = {}
            for piece_id in members:
                x, y, rotation = assigned[piece_id]
                rx, ry = rotate_grid_vector((x, y), whole_rotation)
                rotated_poses[piece_id] = (
                    rx,
                    ry,
                    (rotation + whole_rotation) % 360,
                )
            min_x = min(pose[0] for pose in rotated_poses.values())
            max_x = max(pose[0] for pose in rotated_poses.values())
            min_y = min(pose[1] for pose in rotated_poses.values())
            max_y = max(pose[1] for pose in rotated_poses.values())
            for offset_y in range(-min_y, grid_size - max_y):
                for offset_x in range(-min_x, grid_size - max_x):
                    poses: dict[str, tuple[int, int, int]] = {}
                    valid = True
                    for piece_id, (rx, ry, rotation) in rotated_poses.items():
                        x, y = rx + offset_x, ry + offset_y
                        sides = oriented_lookup[(piece_id, rotation)].sides
                        border_checks = {
                            "top": y == 0,
                            "right": x == grid_size - 1,
                            "bottom": y == grid_size - 1,
                            "left": x == 0,
                        }
                        if any((sides[side] == "flat") != on_border for side, on_border in border_checks.items()):
                            valid = False
                            break
                        poses[piece_id] = (x, y, rotation)
                    if valid:
                        component_candidates.append(
                            {
                                "whole_rotation": whole_rotation,
                                "offset_x": offset_x,
                                "offset_y": offset_y,
                                "poses": poses,
                            }
                        )

        for candidate_index, candidate in enumerate(component_candidates, start=1):
            poses = candidate["poses"]
            placement_rows.append(
                {
                    "component": component_index,
                    "component_size": len(members),
                    "candidate": candidate_index,
                    "whole_rotation": candidate["whole_rotation"],
                    "offset_x": candidate["offset_x"],
                    "offset_y": candidate["offset_y"],
                    "poses": ";".join(
                        f"{piece_id}@{poses[piece_id][0]},{poses[piece_id][1]},r{poses[piece_id][2]}"
                        for piece_id in sorted(poses)
                    ),
                }
            )
        placement_summary_rows.append(
            {
                "component": component_index,
                "component_size": len(members),
                "candidate_count": len(component_candidates),
                "whole_rotations": ",".join(
                    str(value)
                    for value in sorted({int(row["whole_rotation"]) for row in component_candidates})
                ),
            }
        )
        all_component_candidates[component_index] = component_candidates

    with (output_dir / "grid-placement-candidates.tsv").open("w", encoding="utf-8", newline="") as handle:
        fields = [
            "component", "component_size", "candidate", "whole_rotation",
            "offset_x", "offset_y", "poses",
        ]
        writer = csv.DictWriter(handle, fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(placement_rows)
    with (output_dir / "grid-placement-summary.tsv").open("w", encoding="utf-8", newline="") as handle:
        fields = ["component", "component_size", "candidate_count", "whole_rotations"]
        writer = csv.DictWriter(handle, fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(placement_summary_rows)

    # Combine the strongly border-anchored multi-piece components.  Fixing the
    # first placement of the largest component removes the fourfold global
    # rotation symmetry while preserving every relative layout.
    anchored_components = [
        int(row["component"])
        for row in placement_summary_rows
        if int(row["component_size"]) > 1 and 0 < int(row["candidate_count"]) <= 20
    ]
    layout_components = anchored_components + [
        int(row["component"])
        for row in placement_summary_rows
        if int(row["component_size"]) > 1
        and int(row["component"]) not in anchored_components
        and int(row["candidate_count"]) > 0
    ]
    layouts: list[dict[str, object]] = []

    def fit_candidate(
        candidate: dict[str, object],
        occupied: dict[tuple[int, int], tuple[str, int]],
    ) -> tuple[dict[tuple[int, int], tuple[str, int]], float, int, int] | None:
        """Validate a component placement and score seams to occupied cells."""
        candidate_cells = {
            (pose[0], pose[1]): (piece_id, pose[2])
            for piece_id, pose in candidate["poses"].items()
        }
        if not set(occupied).isdisjoint(candidate_cells):
            return None
        added_score = 0.0
        added_count = 0
        mismatch_count = 0
        for (x, y), (piece_id, rotation) in candidate_cells.items():
            piece = oriented_lookup[(piece_id, rotation)]
            neighbor_tests = [
                ((x - 1, y), "right", False),
                ((x + 1, y), "right", True),
                ((x, y - 1), "down", False),
                ((x, y + 1), "down", True),
            ]
            for neighbor_cell, direction, candidate_first in neighbor_tests:
                neighbor_pose = occupied.get(neighbor_cell)
                if neighbor_pose is None:
                    continue
                neighbor = oriented_lookup[neighbor_pose]
                details = (
                    pair_score(piece, neighbor, direction, extension)
                    if candidate_first
                    else pair_score(neighbor, piece, direction, extension)
                )
                if details is None:
                    mismatch_count += 1
                    details = (
                        pair_score(piece, neighbor, direction, extension, require_complement=False)
                        if candidate_first
                        else pair_score(neighbor, piece, direction, extension, require_complement=False)
                    )
                if details is None:
                    added_score += 5000.0
                    added_count += 1
                    continue
                added_score += details["score"]
                added_count += 1
        return candidate_cells, added_score, added_count, mismatch_count

    def extend_layout(
        component_offset: int,
        chosen: dict[int, dict[str, object]],
        occupied: dict[tuple[int, int], tuple[str, int]],
        cross_seam_score: float,
        cross_seam_count: int,
        cross_seam_mismatches: int,
    ) -> None:
        if component_offset == len(layout_components):
            layouts.append(
                {
                    "chosen": dict(chosen),
                    "cross_seam_score": cross_seam_score,
                    "cross_seam_count": cross_seam_count,
                    "cross_seam_mismatches": cross_seam_mismatches,
                }
            )
            return
        component_index = layout_components[component_offset]
        candidates = all_component_candidates[component_index]
        if component_offset == 0:
            candidates = candidates[:1]
        for candidate in candidates:
            fit = fit_candidate(candidate, occupied)
            if fit is None:
                continue
            candidate_cells, added_score, added_count, added_mismatches = fit
            if cross_seam_mismatches + added_mismatches > 2:
                continue
            chosen[component_index] = candidate
            extend_layout(
                component_offset + 1,
                chosen,
                occupied | candidate_cells,
                cross_seam_score + added_score,
                cross_seam_count + added_count,
                cross_seam_mismatches + added_mismatches,
            )
            del chosen[component_index]

    if layout_components:
        extend_layout(0, {}, {}, 0.0, 0, 0)
    total_layout_count = len(layouts)
    layouts.sort(
        key=lambda row: (
            int(row["cross_seam_mismatches"]),
            float(row["cross_seam_score"]) / max(1, int(row["cross_seam_count"])),
            float(row["cross_seam_score"]),
        )
    )
    layouts = layouts[:512]

    layout_rows: list[dict[str, object]] = []
    for layout_index, layout_record in enumerate(layouts, start=1):
        layout = layout_record["chosen"]
        merged_poses: dict[str, tuple[int, int, int]] = {}
        selections: list[str] = []
        for component_index in layout_components:
            candidate = layout[component_index]
            candidate_number = all_component_candidates[component_index].index(candidate) + 1
            selections.append(f"C{component_index}={candidate_number}")
            merged_poses.update(candidate["poses"])
        layout_rows.append(
            {
                "layout": layout_index,
                "components": ",".join(str(value) for value in layout_components),
                "selections": ";".join(selections),
                "piece_count": len(merged_poses),
                "cross_seam_count": layout_record["cross_seam_count"],
                "cross_seam_mismatches": layout_record["cross_seam_mismatches"],
                "cross_seam_score": f"{float(layout_record['cross_seam_score']):.3f}",
                "poses": ";".join(
                    f"{piece_id}@{pose[0]},{pose[1]},r{pose[2]}"
                    for piece_id, pose in sorted(merged_poses.items())
                ),
            }
        )
    with (output_dir / "grid-layouts.tsv").open("w", encoding="utf-8", newline="") as handle:
        fields = [
            "layout", "components", "selections", "piece_count",
            "cross_seam_count", "cross_seam_mismatches", "cross_seam_score", "poses",
        ]
        writer = csv.DictWriter(handle, fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(layout_rows)
    with (output_dir / "grid-layout-search-summary.tsv").open("w", encoding="utf-8", newline="") as handle:
        fields = ["components", "total_layouts", "retained_layouts", "minimum_mismatches"]
        writer = csv.DictWriter(handle, fields, delimiter="\t")
        writer.writeheader()
        writer.writerow(
            {
                "components": ",".join(str(value) for value in layout_components),
                "total_layouts": total_layout_count,
                "retained_layouts": len(layouts),
                "minimum_mismatches": min(
                    (int(row["cross_seam_mismatches"]) for row in layouts),
                    default="",
                ),
            }
        )

    conditional_rows: list[dict[str, object]] = []
    conditional_summary_rows: list[dict[str, object]] = []
    if len(layouts) == 1:
        base_layout = layouts[0]["chosen"]
        base_occupied: dict[tuple[int, int], tuple[str, int]] = {}
        for component_index in layout_components:
            for piece_id, pose in base_layout[component_index]["poses"].items():
                base_occupied[(pose[0], pose[1])] = (piece_id, pose[2])
        for component_index, candidates in sorted(all_component_candidates.items()):
            if component_index in layout_components:
                continue
            members = components[component_index - 1]
            valid_options: list[dict[str, object]] = []
            for candidate_number, candidate in enumerate(candidates, start=1):
                fit = fit_candidate(candidate, base_occupied)
                if fit is None:
                    continue
                _, seam_score, seam_count, seam_mismatches = fit
                row = {
                    "component": component_index,
                    "component_size": len(members),
                    "candidate": candidate_number,
                    "cross_seam_count": seam_count,
                    "cross_seam_mismatches": seam_mismatches,
                    "cross_seam_score": f"{seam_score:.3f}",
                    "poses": ";".join(
                        f"{piece_id}@{pose[0]},{pose[1]},r{pose[2]}"
                        for piece_id, pose in sorted(candidate["poses"].items())
                    ),
                }
                valid_options.append(row)
                conditional_rows.append(row)
            touching = [row for row in valid_options if int(row["cross_seam_count"]) > 0]
            best_touching = min(
                (float(row["cross_seam_score"]) / int(row["cross_seam_count"]) for row in touching),
                default=float("inf"),
            )
            conditional_summary_rows.append(
                {
                    "component": component_index,
                    "component_size": len(members),
                    "valid_candidates": len(valid_options),
                    "touching_candidates": len(touching),
                    "best_touching_mean_score": "" if not math.isfinite(best_touching) else f"{best_touching:.3f}",
                }
            )
    with (output_dir / "conditional-placement-options.tsv").open("w", encoding="utf-8", newline="") as handle:
        fields = [
            "component", "component_size", "candidate", "cross_seam_count",
            "cross_seam_mismatches", "cross_seam_score", "poses",
        ]
        writer = csv.DictWriter(handle, fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(conditional_rows)
    with (output_dir / "conditional-placement-summary.tsv").open("w", encoding="utf-8", newline="") as handle:
        fields = [
            "component", "component_size", "valid_candidates",
            "touching_candidates", "best_touching_mean_score",
        ]
        writer = csv.DictWriter(handle, fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(conditional_summary_rows)

    # A compact persistent visual lets later turns compare all justified
    # relative layouts without mentally rotating disconnected screenshots.
    render_layouts = layouts[:64]
    unique_layout_path = output_dir / "grid-layout-unique.png"
    best_layout_path = output_dir / "grid-layout-best.png"
    if unique_layout_path.exists():
        unique_layout_path.unlink()
    if best_layout_path.exists():
        best_layout_path.unlink()
    thumb_size = 280
    columns = 4
    rows = max(1, math.ceil(len(render_layouts) / columns))
    contact = Image.new("RGB", (columns * thumb_size, rows * (thumb_size + 18)), "#181818")
    for layout_offset, layout_record in enumerate(render_layouts):
        layout = layout_record["chosen"]
        board_size = grid_size * pieces[0].pitch + 2 * extension
        board = Image.new("RGBA", (board_size, board_size), (22, 22, 22, 255))
        for component_index in layout_components:
            for piece_id, (x, y, rotation) in layout[component_index]["poses"].items():
                tile = Image.fromarray(oriented_lookup[(piece_id, rotation)].normalized)
                board.alpha_composite(tile, (x * pieces[0].pitch, y * pieces[0].pitch))
        if layout_offset == 0:
            board.convert("RGB").save(best_layout_path)
        if len(layouts) == 1:
            board.convert("RGB").save(unique_layout_path)
        thumb = board.convert("RGB").resize((thumb_size, thumb_size), Image.Resampling.LANCZOS)
        col, row = layout_offset % columns, layout_offset // columns
        x0, y0 = col * thumb_size, row * (thumb_size + 18)
        contact.paste(thumb, (x0, y0))
        score = float(layout_record["cross_seam_score"])
        count = int(layout_record["cross_seam_count"])
        mismatches = int(layout_record["cross_seam_mismatches"])
        caption = f"layout {layout_offset + 1}  seams={count} bad={mismatches} score={score:.0f}"
        ImageDraw.Draw(contact).text((x0 + 4, y0 + thumb_size + 3), caption, fill="white", font=font)
    contact.save(output_dir / "grid-layouts-contact.png")
    (output_dir / "assembly-conflicts.txt").write_text(
        ("\n".join(conflicts) + "\n") if conflicts else "none\n",
        encoding="utf-8",
    )


def match_reference_image(
    pieces: list[Piece],
    orientations: list[OrientedPiece],
    reference_path: Path,
    output_dir: Path,
    grid_size: int,
    extension: int,
) -> None:
    """Test whether a proposed aerial reference is the source imagery."""
    reference = cv2.imread(str(reference_path), cv2.IMREAD_COLOR)
    if reference is None:
        raise ValueError(f"cannot read reference image: {reference_path}")
    reference_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create(nfeatures=12000, contrastThreshold=0.015)
    reference_keypoints, reference_descriptors = sift.detectAndCompute(reference_gray, None)
    if reference_descriptors is None:
        raise ValueError(f"no reference features found in {reference_path}")
    matcher = cv2.BFMatcher(cv2.NORM_L2)
    rows: list[dict[str, object]] = []
    annotated = reference.copy()
    palette = [
        (42, 211, 255), (255, 120, 80), (80, 230, 110), (230, 80, 230),
        (90, 170, 255), (255, 210, 65),
    ]
    color_index = 0
    for piece in pieces:
        rgb = cv2.cvtColor(piece.rgba[:, :, :3], cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
        mask = np.where(piece.rgba[:, :, 3] >= 128, 255, 0).astype(np.uint8)
        mask = cv2.erode(mask, np.ones((5, 5), dtype=np.uint8), iterations=1)
        keypoints, descriptors = sift.detectAndCompute(gray, mask)
        good: list[cv2.DMatch] = []
        inliers = 0
        median_distance = float("inf")
        homography = None
        reference_center_x: float | None = None
        reference_center_y: float | None = None
        reference_x_axis_deg: float | None = None
        reference_cell_width: float | None = None
        reference_cell_height: float | None = None
        if descriptors is not None and len(descriptors) >= 2:
            pairs = matcher.knnMatch(descriptors, reference_descriptors, k=2)
            good = [first for first, second in pairs if first.distance < 0.72 * second.distance]
            if good:
                median_distance = float(np.median([match.distance for match in good]))
            if len(good) >= 4:
                source_points = np.float32([keypoints[match.queryIdx].pt for match in good]).reshape(-1, 1, 2)
                target_points = np.float32([reference_keypoints[match.trainIdx].pt for match in good]).reshape(-1, 1, 2)
                homography, inlier_mask = cv2.findHomography(source_points, target_points, cv2.RANSAC, 5.0)
                if inlier_mask is not None:
                    inliers = int(inlier_mask.sum())
        if homography is not None and inliers >= 4:
            x0 = float(piece.anchor_x)
            y0 = float(piece.anchor_y)
            pitch = float(piece.pitch)
            core_points = np.float32(
                [
                    [x0 + pitch / 2.0, y0 + pitch / 2.0],
                    [x0 + pitch, y0 + pitch / 2.0],
                    [x0 + pitch / 2.0, y0 + pitch],
                ]
            ).reshape(-1, 1, 2)
            projected_core = cv2.perspectiveTransform(core_points, homography).reshape(-1, 2)
            if np.all(np.isfinite(projected_core)):
                center, right_midpoint, bottom_midpoint = projected_core
                x_vector = right_midpoint - center
                y_vector = bottom_midpoint - center
                reference_center_x = float(center[0])
                reference_center_y = float(center[1])
                reference_x_axis_deg = float(
                    math.degrees(math.atan2(float(x_vector[1]), float(x_vector[0]))) % 360.0
                )
                reference_cell_width = float(np.linalg.norm(x_vector) * 2.0)
                reference_cell_height = float(np.linalg.norm(y_vector) * 2.0)
        rows.append(
            {
                "piece_id": piece.piece_id,
                "piece_features": len(keypoints),
                "good_matches": len(good),
                "homography_inliers": inliers,
                "median_distance": "" if not math.isfinite(median_distance) else f"{median_distance:.3f}",
                "reference_center_x": "" if reference_center_x is None else f"{reference_center_x:.3f}",
                "reference_center_y": "" if reference_center_y is None else f"{reference_center_y:.3f}",
                "reference_x_axis_deg": "" if reference_x_axis_deg is None else f"{reference_x_axis_deg:.3f}",
                "reference_cell_width": "" if reference_cell_width is None else f"{reference_cell_width:.3f}",
                "reference_cell_height": "" if reference_cell_height is None else f"{reference_cell_height:.3f}",
            }
        )
        if homography is not None and inliers >= 6:
            height, width = piece.rgba.shape[:2]
            corners = np.float32([[0, 0], [width, 0], [width, height], [0, height]]).reshape(-1, 1, 2)
            projected = cv2.perspectiveTransform(corners, homography).reshape(-1, 2)
            if np.all(np.isfinite(projected)):
                color = palette[color_index % len(palette)]
                color_index += 1
                polygon = np.round(projected).astype(np.int32)
                cv2.polylines(annotated, [polygon], True, color, 4, cv2.LINE_AA)
                origin = tuple(polygon[0])
                cv2.putText(annotated, piece.piece_id, origin, cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2, cv2.LINE_AA)
    rows.sort(key=lambda row: (-int(row["homography_inliers"]), -int(row["good_matches"]), str(row["piece_id"])))
    with (output_dir / "reference-matches.tsv").open("w", encoding="utf-8", newline="") as handle:
        fields = [
            "piece_id", "piece_features", "good_matches", "homography_inliers", "median_distance",
            "reference_center_x", "reference_center_y", "reference_x_axis_deg",
            "reference_cell_width", "reference_cell_height",
        ]
        writer = csv.DictWriter(handle, fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    cv2.imwrite(str(output_dir / "reference-annotated.jpg"), annotated)

    # The large exact-edge component supplies a stable 8x8 coordinate frame.
    # Feature homographies then place every disconnected component as a rigid
    # body. This also locates a featureless water piece through its two
    # feature-rich neighbors, without guessing from colour alone.
    assembly_path = output_dir / "assembly.tsv"
    if not assembly_path.exists():
        return
    with assembly_path.open(encoding="utf-8", newline="") as handle:
        assembly_rows = list(csv.DictReader(handle, delimiter="\t"))
    if not assembly_rows:
        return

    pitch = pieces[0].pitch
    match_by_piece = {str(row["piece_id"]): row for row in rows}
    component_rows: dict[int, list[dict[str, object]]] = {}
    for raw in assembly_rows:
        component = int(raw["component"])
        component_rows.setdefault(component, []).append(
            {
                "piece_id": str(raw["piece_id"]),
                "x": int(raw["x"]),
                "y": int(raw["y"]),
                "rotation": int(raw["rotation"]),
            }
        )

    main_rows = component_rows[min(component_rows)]
    origin_samples_x: list[float] = []
    origin_samples_y: list[float] = []
    for row in main_rows:
        match = match_by_piece.get(str(row["piece_id"]))
        if not match or int(match["homography_inliers"]) < 6 or match["reference_center_x"] == "":
            continue
        width = float(match["reference_cell_width"])
        height = float(match["reference_cell_height"])
        if not (110.0 <= width <= 170.0 and 110.0 <= height <= 170.0):
            continue
        origin_samples_x.append(float(match["reference_center_x"]) - int(row["x"]) * pitch)
        origin_samples_y.append(float(match["reference_center_y"]) - int(row["y"]) * pitch)
    if len(origin_samples_x) < 4:
        return
    origin_x = float(np.median(origin_samples_x))
    origin_y = float(np.median(origin_samples_y))

    reference_targets: dict[str, tuple[int, int, int, int, float]] = {}
    residuals: list[float] = []
    for piece_id, match in match_by_piece.items():
        if int(match["homography_inliers"]) < 6 or match["reference_center_x"] == "":
            continue
        width = float(match["reference_cell_width"])
        height = float(match["reference_cell_height"])
        if not (110.0 <= width <= 170.0 and 110.0 <= height <= 170.0):
            continue
        center_x = float(match["reference_center_x"])
        center_y = float(match["reference_center_y"])
        grid_x = int(round((center_x - origin_x) / pitch))
        grid_y = int(round((center_y - origin_y) / pitch))
        residual = math.hypot(
            center_x - (origin_x + grid_x * pitch),
            center_y - (origin_y + grid_y * pitch),
        )
        if not (0 <= grid_x < grid_size and 0 <= grid_y < grid_size and residual <= 12.0):
            continue
        reference_angle = float(match["reference_x_axis_deg"]) % 360.0
        rotation = (-int(round(reference_angle / 90.0)) * 90) % 360
        reference_targets[piece_id] = (
            grid_x,
            grid_y,
            rotation,
            int(match["homography_inliers"]),
            residual,
        )
        residuals.append(residual)

    def rotate_grid(x: int, y: int, quarter_turns: int) -> tuple[int, int]:
        quarter_turns %= 4
        if quarter_turns == 0:
            return x, y
        if quarter_turns == 1:
            return y, -x
        if quarter_turns == 2:
            return -x, -y
        return -y, x

    placements: dict[str, dict[str, object]] = {}
    occupied: dict[tuple[int, int], str] = {}
    for row in main_rows:
        piece_id = str(row["piece_id"])
        x, y = int(row["x"]), int(row["y"])
        placements[piece_id] = {
            **row,
            "component": min(component_rows),
            "source": "exact-main-component",
        }
        occupied[(x, y)] = piece_id

    for component in sorted(component_rows):
        if component == min(component_rows):
            continue
        members = component_rows[component]
        matched_members = [row for row in members if str(row["piece_id"]) in reference_targets]
        candidates: set[tuple[int, int, int]] = set()
        for anchor in matched_members:
            target_x, target_y, target_rotation, _, _ = reference_targets[str(anchor["piece_id"])]
            for quarter_turns in range(4):
                if (int(anchor["rotation"]) + quarter_turns * 90) % 360 != target_rotation:
                    continue
                rotated_x, rotated_y = rotate_grid(int(anchor["x"]), int(anchor["y"]), quarter_turns)
                candidates.add((quarter_turns, target_x - rotated_x, target_y - rotated_y))

        valid: list[tuple[int, int, int]] = []
        for quarter_turns, translate_x, translate_y in sorted(candidates):
            transformed: list[tuple[str, int, int, int]] = []
            rejected = False
            for member in members:
                piece_id = str(member["piece_id"])
                local_x, local_y = rotate_grid(int(member["x"]), int(member["y"]), quarter_turns)
                x, y = local_x + translate_x, local_y + translate_y
                rotation = (int(member["rotation"]) + quarter_turns * 90) % 360
                if not (0 <= x < grid_size and 0 <= y < grid_size):
                    rejected = True
                    break
                if (x, y) in occupied:
                    rejected = True
                    break
                target = reference_targets.get(piece_id)
                if target and (x, y, rotation) != target[:3]:
                    rejected = True
                    break
                transformed.append((piece_id, x, y, rotation))
            if not rejected:
                valid.append((quarter_turns, translate_x, translate_y))
        if len(valid) != 1:
            continue
        quarter_turns, translate_x, translate_y = valid[0]
        for member in members:
            piece_id = str(member["piece_id"])
            local_x, local_y = rotate_grid(int(member["x"]), int(member["y"]), quarter_turns)
            x, y = local_x + translate_x, local_y + translate_y
            rotation = (int(member["rotation"]) + quarter_turns * 90) % 360
            placements[piece_id] = {
                "piece_id": piece_id,
                "x": x,
                "y": y,
                "rotation": rotation,
                "component": component,
                "source": f"rigid-reference-fit:{len(matched_members)}-matched",
            }
            occupied[(x, y)] = piece_id

    placement_rows: list[dict[str, object]] = []
    for placement in placements.values():
        piece_id = str(placement["piece_id"])
        target = reference_targets.get(piece_id)
        placement_rows.append(
            {
                **placement,
                "homography_inliers": "" if target is None else target[3],
                "grid_residual_px": "" if target is None else f"{target[4]:.3f}",
            }
        )
    placement_rows.sort(key=lambda row: (int(row["y"]), int(row["x"]), str(row["piece_id"])))
    with (output_dir / "reference-grid-placements.tsv").open("w", encoding="utf-8", newline="") as handle:
        fields = [
            "piece_id", "x", "y", "rotation", "component", "source",
            "homography_inliers", "grid_residual_px",
        ]
        writer = csv.DictWriter(handle, fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(placement_rows)

    oriented_lookup = {(item.piece_id, item.rotation): item for item in orientations}
    board_size = grid_size * pitch + 2 * extension
    board = Image.new("RGBA", (board_size, board_size), (34, 34, 34, 255))
    for placement in placement_rows:
        key = (str(placement["piece_id"]), int(placement["rotation"]))
        tile = Image.fromarray(oriented_lookup[key].normalized)
        board.alpha_composite(tile, (int(placement["x"]) * pitch, int(placement["y"]) * pitch))
    board.convert("RGB").save(output_dir / "reference-assisted-layout.png")

    missing = [
        (x, y)
        for y in range(grid_size)
        for x in range(grid_size)
        if (x, y) not in occupied
    ]
    annotated_board = board.convert("RGB")
    draw = ImageDraw.Draw(annotated_board)
    font = ImageFont.load_default()
    for x, y in missing:
        x0, y0 = extension + x * pitch, extension + y * pitch
        draw.rectangle((x0, y0, x0 + pitch, y0 + pitch), outline=(255, 70, 70), width=4)
        draw.text((x0 + 8, y0 + 8), f"missing ({x},{y})", fill=(255, 70, 70), font=font)
    annotated_board.save(output_dir / "reference-assisted-layout-annotated.png")
    rmse = math.sqrt(float(np.mean(np.square(residuals)))) if residuals else float("nan")
    crop_left = int(round(origin_x - pitch / 2.0))
    crop_top = int(round(origin_y - pitch / 2.0))
    crop_right = crop_left + grid_size * pitch
    crop_bottom = crop_top + grid_size * pitch
    source_crop_status = "outside-reference-bounds"
    if (
        crop_left >= 0
        and crop_top >= 0
        and crop_right <= reference.shape[1]
        and crop_bottom <= reference.shape[0]
    ):
        source_crop = reference[crop_top:crop_bottom, crop_left:crop_right].copy()
        cv2.imwrite(str(output_dir / "reference-source-grid.jpg"), source_crop)
        source_crop_annotated = source_crop.copy()
        for grid_line in range(grid_size + 1):
            offset = grid_line * pitch
            cv2.line(source_crop_annotated, (offset, 0), (offset, grid_size * pitch), (60, 220, 255), 2)
            cv2.line(source_crop_annotated, (0, offset), (grid_size * pitch, offset), (60, 220, 255), 2)
        for x, y in missing:
            cv2.rectangle(
                source_crop_annotated,
                (x * pitch + 3, y * pitch + 3),
                ((x + 1) * pitch - 3, (y + 1) * pitch - 3),
                (60, 60, 255),
                4,
            )
        cv2.imwrite(str(output_dir / "reference-source-grid-annotated.jpg"), source_crop_annotated)
        source_crop_status = f"({crop_left},{crop_top})-({crop_right},{crop_bottom})"
    (output_dir / "reference-grid-summary.txt").write_text(
        "\n".join(
            [
                f"reference={reference_path}",
                f"grid_origin_center_px=({origin_x:.3f},{origin_y:.3f})",
                f"reference_targets={len(reference_targets)}",
                f"reference_grid_rmse_px={rmse:.3f}",
                f"placed_pieces={len(placements)}",
                f"missing_cells={','.join(f'({x},{y})' for x, y in missing)}",
                f"reference_source_crop_px={source_crop_status}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pieces", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pitch", type=int, default=140)
    parser.add_argument("--extension", type=int, default=55)
    parser.add_argument("--keep-matches", type=int, default=500)
    parser.add_argument("--exact-threshold", type=float, default=90.0)
    parser.add_argument("--grid-size", type=int, default=8)
    parser.add_argument("--reference", type=Path)
    args = parser.parse_args()

    pieces = load_pieces(args.pieces, args.pitch)
    orientations = [
        normalize_orientation(piece, rotation, args.extension)
        for piece in pieces
        for rotation in range(4)
    ]
    by_piece: dict[str, list[OrientedPiece]] = {}
    for oriented in orientations:
        by_piece.setdefault(oriented.piece_id, []).append(oriented)

    matches: list[dict[str, object]] = []
    for a in orientations:
        for b in orientations:
            if a.piece_id == b.piece_id:
                continue
            for direction in ("right", "down"):
                details = pair_score(a, b, direction, args.extension)
                if details is None:
                    continue
                side_a = "right" if direction == "right" else "bottom"
                side_b = "left" if direction == "right" else "top"
                matches.append(
                    {
                        "score": round(details["score"], 4),
                        "direction": direction,
                        "a": a.piece_id,
                        "a_rotation": a.rotation,
                        "a_side": a.sides[side_a],
                        "b": b.piece_id,
                        "b_rotation": b.rotation,
                        "b_side": b.sides[side_b],
                        "median_rgb": round(details["median_rgb"], 4),
                        "mean_rgb": round(details["mean_rgb"], 4),
                        "p90_rgb": round(details["p90_rgb"], 4),
                        "contact_count": int(details["contact_count"]),
                        "overlap": int(details["overlap"]),
                        "gap": int(details["gap"]),
                    }
                )
    matches.sort(key=lambda row: (float(row["score"]), str(row["a"]), int(row["a_rotation"])))
    matches = matches[: args.keep_matches]

    args.output.mkdir(parents=True, exist_ok=True)
    render_anchor_sheet(pieces, args.output / "anchors.png")
    write_tables(pieces, orientations, matches, args.output)
    assemble_exact_components(
        pieces,
        orientations,
        matches,
        args.output,
        args.extension,
        args.exact_threshold,
        args.grid_size,
    )
    if args.reference:
        match_reference_image(
            pieces,
            orientations,
            args.reference,
            args.output,
            args.grid_size,
            args.extension,
        )
    print(f"pieces={len(pieces)} orientations={len(orientations)} retained_matches={len(matches)}")
    if matches:
        print(f"best_score={matches[0]['score']} {matches[0]['a']}->{matches[0]['b']} {matches[0]['direction']}")


if __name__ == "__main__":
    main()
