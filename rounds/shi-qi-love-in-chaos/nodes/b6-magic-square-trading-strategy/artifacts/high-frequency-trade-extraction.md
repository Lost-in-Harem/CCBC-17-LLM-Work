# Rejected four-high-frequency-trade extraction: 嬴政

> The user explicitly rejected **嬴政** on 2026-08-30.  The four
> value-2/value-2 crossings remain valid observations, but the center-out
> regrouping below has no puzzle-given traversal rule.  This artifact is kept
> only as negative evidence; the current extraction is the closed loop in
> `artifacts/extraction-loop.md`.

## 1. Select the four value-2 trades

The direction-local component-frequency fill agrees at all 57 crossings.
Exactly four actual clue-block trades have value 2 on both sides.  Since each
traded block has three Han characters, value 2 selects its middle character.

Use the puzzle as printed: order crossings by board, row, and column, and
order the two statement blocks by the displayed directions `横 / 纵 / 里`.
This removes the previously arbitrary choice between the two fanqie
orientations.

| Order | Crossing | Printed blocks in direction order | Middle pair | Fanqie |
| ---: | --- | --- | --- | --- |
| 1 | G1 r05c12 | `吃兔子` / `在干活` | 兔 / 干 | `TAN` |
| 2 | G1 r07c02 | `地质学` / `雷锋是` | 质 / 锋 | `ZHENG` |
| 3 | G1↔里 r09c10 | `记忆中` / `气性不` | 忆 / 性 | `YING` |
| 4 | G3↔里 r09c10 | `的味道` / `六百号` | 味 / 百 | `WAI` |

The fixed stream is:

```text
TAN / ZHENG / YING / WAI
```

As a control, using the repaired blocks with the same fixed direction order
would give `GU / FI / XI / BEI`.  The rejected route
`GU / ZHENG / XI / BEI -> 古筝 / 西北` mixed the two puzzle states pair by
pair and therefore had no consistent orientation rule.

## 2. Preserve the two keyword trades separately

Only the block `关键词` repeats among the 180 repaired three-Han blocks.  The
two occurrences answer different clues and trade with different blocks:

| Host clue answer | Counterpart traded with `关键词` | Role |
| --- | --- | --- |
| `反切` | `古代人` | the fanqie result is an ancient person |
| `BREAK` | `的概念` | use the concept of a break, not the literal word |

The old analysis concatenated the counterparts as `古代人的概念`.  That
discarded the local pairing and led to a chain of unsupported semantic
landings.  Keeping the associations explains both instructions directly.

## 3. Break at the center and read the nested pairs

The `BREAK` depth clue is at the exact common center of the three boards.
Place the break in the center of the four-syllable stream:

```text
TAN [ ZHENG | YING ] WAI
```

Read away from the break, right side before left side:

| Layer | Syllables | Result |
| --- | --- | --- |
| inner (`里`) | `YING / ZHENG` | **嬴政** |
| outer | `WAI / TAN` | **外滩** |

The outer result is an internal checksum: `外滩` literally begins with
“outside” and fixes the right-before-left orientation.  The inner result is
the one selected by `里` and by the paired counterpart `古代人`.
The bundled local dictionary independently lists `嬴政` as a person-name for
`YING/ZHENG` and `外滩` as a noun for `WAI/TAN`; no web lookup is involved.

The candidate answer is therefore **嬴政**.

## Reproduction

Validate the direction-local fill and list the four value-2 trades:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

Reproduce the two keyword trades:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high_frequency.py `
  --input rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --output rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high-frequency-audit-current.md
```

Reproduce the fixed fanqie orientations:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 兔干 质锋 忆性 味百

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --reading ying zheng

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --reading wai tan
```

The coordinate and orientation audit is retained at
`work/visual/high-frequency-orientation-audit.md`.
