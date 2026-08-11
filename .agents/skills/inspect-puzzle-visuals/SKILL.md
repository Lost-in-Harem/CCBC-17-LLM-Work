---
name: inspect-puzzle-visuals
description: Create reproducible, persistent representations of Puzzle Hunt images, HTML or SingleFile pages, PDFs, video, audio, layouts, grids, overlays, routes, and OCR. Use when solving a Node depends on visual or spatial evidence, asset extraction, transcription with coordinates, image layers, or multimedia inspection.
---

# Inspect puzzle visuals

Work only with inputs readable under the assigned Node's scope. Never modify an
original file. Write derived material under
`rounds/<round>/nodes/<node>/work/visual/`; promote only the few files needed to
reproduce a candidate into `artifacts/`.

The bundled script requires Pillow for raster operations. Run
`python tools/doctor.py` to see which optional media capabilities are available.

Set the script path in commands below to:

```text
.agents/skills/inspect-puzzle-visuals/scripts/visual_workbench.py
```

## Build a stable inventory

Start with an inventory when several images, HTML assets, or archive members
are involved:

```text
python <script> inventory <input-file-or-directory> --output <node>/work/visual/inventory
```

This extracts bounded HTML data images and archive images, deduplicates by
SHA-256, and writes numbered contact sheets, `index.tsv`, and `manifest.json`.
Refer to stable IDs such as `image-003`, not visual memory or file-list order.

## Derive only what tests a hypothesis

```text
python <script> crop IMAGE OUTPUT --box LEFT,TOP,RIGHT,BOTTOM --scale 3 --grid 10
python <script> channels IMAGE OUTPUT_DIR --threshold 96 --threshold 160
python <script> annotate IMAGE SPEC.json OUTPUT
python <script> ocr IMAGE OUTPUT_DIR --lang chi_sim+eng --psm 11
python <script> render MEDIA OUTPUT_DIR
```

- `crop` preserves original-image coordinates in a JSON sidecar.
- `channels` emits RGB, CMYK, grayscale, alpha when present, and requested
  thresholds.
- `annotate` accepts JSON annotations of type `box`, `line`, `point`,
  `polyline`, or `text`; all coordinates refer to the source image.
- `ocr` keeps raw TSV, reconstructed text, word confidence, coordinates, and
  an overlay. Treat OCR as uncertain observation, not source truth.
- `render` uses `pdftoppm` for bounded PDF pages and FFmpeg/FFprobe for bounded
  video frames, waveform, spectrum, and media metadata.

Use `python <script> <command> --help` for the exact bounded options.

A minimal annotation specification is:

```json
{
  "annotations": [
    {"type": "box", "xy": [10, 20, 80, 90], "label": "A"},
    {"type": "line", "xy": [20, 30, 120, 130], "label": "edge"},
    {"type": "point", "xy": [45, 60], "label": "P"},
    {"type": "polyline", "points": [[0, 0], [30, 20], [60, 10]]},
    {"type": "text", "xy": [100, 40], "label": "uncertain"}
  ]
}
```

## Maintain reasoning integrity

1. Record what transformation was applied and what signal would support or
   reject the current hypothesis.
2. Keep at least one untouched or direct rendering beside transformed views.
3. Check suspicious OCR characters against the image at useful scale.
4. For routes, overlays, rotations, and grids, maintain one canonical
   coordinate system and update a single annotation specification.
5. Do not generate every transformation automatically. Generate only views
   that discriminate among live hypotheses.
6. Link the final stable representation and exact reproduction command from
   `solution.md`.
