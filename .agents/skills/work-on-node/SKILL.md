---
name: work-on-node
description: Work on exactly one answer-producing Puzzle Hunt Node, including a normal puzzle, subpuzzle, Meta, Final Meta, or resumed investigation. Use when the user asks to solve, continue, investigate, or update a directory under rounds/ROUND_ID/nodes/NODE_ID/.
---

# Work on one Node

Require one assigned directory at `rounds/<round-id>/nodes/<node-id>/`. Do not
choose a Node implicitly.

## Start or resume

1. Read root `AGENTS.md`, `HUNT.md`, the assigned Round's `ROUND.md`, and the
   Node's `solution.md`.
2. Run `python tools/inspect_node.py <round-id>/<node-id>`.
3. Inspect `kind` in `solution.md`:
   - for `meta`, follow `META_TASK_PROMPT.md`;
   - for `puzzle` or `subpuzzle`, follow `PUZZLE_TASK_PROMPT.md`.
4. Resume from the recorded `Next action` and important failed routes. Do not
   restart merely because this is a new task.
5. Respect the Node and feeder read/write boundaries in `AGENTS.md`. Never
   start a subagent.

For visual, spatial, path, overlay, rotation, grid, PDF, HTML, video, or audio
evidence, use `$inspect-puzzle-visuals` and keep its derived material inside the
assigned Node's `work/`.

## Handle submission feedback

If the user reports an accepted or rejected submission, first append the
candidate, date, explicit result, and useful feedback to `Submission history`.
Create the section and its four-column table if an older Node lacks them, and
preserve prior rows. Then apply the status transition rules in `AGENTS.md`;
never infer a verdict or submit an answer yourself.

## Control experiments

- Keep one parameterized script and one result table for each hypothesis
  family. Modify or parameterize them instead of creating `v2`, `fresh`,
  `corrected`, `final`, or similar variants.
- Create a new experimental script only when the computational model changes,
  not merely when parameters change.
- Before a costly experiment, record the hypothesis, distinguishing signal,
  and finite search bound.
- After three bounded experiments in one family produce no new confirmed fact,
  no candidate-ranking change, and no mechanism update, stop that family.
  Record the negative evidence in `Important failed routes`, reassess the
  competing hypotheses, and choose a different discriminating test.
- Do not preserve large raw outputs in `solution.md`. Keep them in `work/` and
  promote only reproducibility-critical artifacts.

## Finish the turn

Follow the end-of-turn contract in `AGENTS.md`: update the one `solution.md`,
set its frontmatter and concrete `Next action`, run
`python tools/build_summary.py`, and report status, candidate, confidence,
evidence, and next action. Only user or Hunt-site confirmation permits
`accepted`.
