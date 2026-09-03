# Superseded answer-length trade-chain hypothesis

> Hint 3 invalidates the premise of this extraction.  The contents of
> corresponding cells across the three boards are three-Han clue blocks along
> the depth/`里` axis; the puzzle never instructs solvers to use repaired
> answer lengths as cell indices.  This derivation of `PERSPECTIVE / 视角` is
> withdrawn and the file is retained only as negative evidence; `PERSPECTIVE`
> has since also been explicitly rejected by the user.  The later exact phrase
> `POINT OF VIEW` was also explicitly rejected; neither route is active, and
> does not rehabilitate this chain.  This old route also uses the superseded
> five-letter central fill `BREAK`; the strict three-cell answer is `END`.

This artifact records the former post-reconstruction hypothesis that
continued past the explicitly rejected readings `细节` and `DAMAGE`.

## 1. The maximum-frequency cell gives an instruction

Placing each repaired clue answer from the start of its assigned line makes
an N-character answer end at position N.  After the three planes are
center-aligned, the unique maximum-frequency coordinate is `r10c04` with one
endpoint from each direction:

| Direction | Answer | Character at the endpoint |
| --- | --- | --- |
| 横 | 中冲穴 | 穴 |
| 纵 | 翼 | 翼 |
| 里 | 关节 | 节 |

The repaired keyword clue supplies `反切`.  `穴翼` gives `xi`; the following
`节` resolves that syllable as `细`, so this stage reads `细节`.  It is an
instruction to inspect the three literal underline details, not the answer.

## 2. The fixed underline view gives a locator

After all 57 block trades, the three printed underline positions contain:

```text
黛拉 / 曼丽 / 记忆
```

Their fanqie readings are `da / mi / ji`, the English phonetic locator
`DAMAGE`.  `DAMAGE` is not the final answer; it points to the repaired clue
`发生后伤害数字变大`, whose answer is `暴击`.  The final character `击` also
matches the third fixed-site reading `ji`, uniquely anchoring the third
underline rather than either of the first two.

## 3. Follow the answer-length trade chain to `BREAK`

An answer of N characters selects block N on its assigned repaired line.  If
that block lies at a geometric crossing, follow the other incidence of that
actual trade to the clue occupying the counterpart line:

| Clue answer | Length-selected block | Trade counterpart | Next clue answer | Selected answer character |
| --- | --- | --- | --- | --- |
| 暴击 | `伤害数` | `物理化` | ζ电势 | 击 |
| ζ电势 | `的概念` | `关键词` | BREAK | 势 |

The second repaired keyword clue answers `BREAK`, so the chain stops there.
Reading the selected answer characters back from the stop gives `势—击`.

## 4. Take the other view of the anchored underline

The `ji`/`击` match anchors the third printed underline, source row `I01`.
That row is assigned to depth line `Z05`, position 1.  The repaired clue on
that line is `记忆中厕所里的味道`, answered by `尿骚味`; at the same first
answer cell, the character is `尿`.

Thus the fixed clue-text view supplied `记忆 -> ji -> 击`, while the answer-grid
view of the same marked cell supplies its counterpart `尿`.  Appending that
other-view character to the reversed trade chain gives the overlapping
carrier:

```text
势 — 击 — 尿
```

## 5. Overlapping fanqie

Apply the repaired `反切` instruction to adjacent pairs:

| Pair | Initial from first | Final from second | Reading |
| --- | --- | --- | --- |
| 势击 | `sh-` | `-i` | `shi` |
| 击尿 | `j-` | `-iao` | `jiao` |

The local two-Han dictionary's toneless `shi / jiao` hits are led by `视角`
(frequency 425), ahead of `市郊` (261) and all other hits.  `视角` also
describes the puzzle's central operation: the same positions are read through
clue-block, answer-grid, and three-plane views.

This obsolete route therefore proposed Chinese **视角** and English
**PERSPECTIVE**.  Both the derivation and the English answer are rejected.

## Reproduction pointers

- `work/answer_trade_graph.md` contains all 50 answer-length transitions and
  shows `暴击 -> ζ电势 -> BREAK` mechanically.
- `artifacts/answer-endpoint-extraction.md` records the unique frequency-3
  coordinate and `穴 / 翼 / 节` carriers.
- `artifacts/underline-fanqie-extraction.md` preserves the fixed underline
  positions, now explicitly labelled as a rejected intermediate rather than a
  final answer.
