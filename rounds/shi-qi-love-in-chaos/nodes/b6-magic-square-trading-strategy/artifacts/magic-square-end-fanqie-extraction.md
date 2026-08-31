# Rejected magic-square END/fanqie extraction: 季节

**Status: rejected.** The user explicitly reported `季节` is not the answer.
This file preserves the reproducible failed route; it does not authorize
treating title-word `幻方` as a generic opposite-corner pairing instruction or
executing central `END` as a last-character function. The active extraction is
`artifacts/depth-high-frequency-extraction.md`.

## 1. Select the two high-frequency keywords

After undoing all 57 crossing trades, the 50 clue rows contain 180
three-Han blocks but 179 distinct texts. The unique repeated block is
`关键词`, and its two repaired host clues answer the two extraction operations:

| Repaired host | Restored clue | Answer |
| --- | --- | --- |
| `G1-A07.4` | 西十五河海解谜中的关键词 | `反切` |
| `I05.3 / Z03.3` | 结束本部分的关键词 | `END` |

Thus `高频交易` selects the highest-frequency traded block, while the two
hosts supply `反切` and `END`. The blocks traded against these two occurrences
are `古代人 / 的概念`, which concatenate to the confirming phrase
`古代人的概念`; they are not separately fanqied into the rejected `GU/GE`.

## 2. Execute END on the four outer depth answers

Center-aligning the three boards creates five depth entries at four corners
and a center. The center entry is `END`; take the final Han character of each
of the other four answer words:

```text
路人甲 → 甲                     成精 → 精

                    END

关节   → 节                     氨气 → 气
```

This acts on the answers, not on the final G3 components of their decomposed
grid fills. That distinction preserves `精` rather than changing it to `青`.

## 3. Pair opposite corners as a magic square and fanqie

The title `幻方` supplies the spatial rule: pair corners opposite through the
center. Read the diagonals from their northern endpoints, west to east:

| Order | Opposite corners | Fanqie construction | Syllable | Character |
| ---: | --- | --- | --- | --- |
| 1 | northwest → southeast | `甲气`: `j + i4` | `ji4` | 季 |
| 2 | northeast → southwest | `精节`: `j + ie2` | `jie2` | 节 |

The exact but rejected result of this hypothesis was:

```text
JI4 / JIE2 = 季节
```

This used both selected keywords, all four noncentral depth answers, their
coordinate geometry, and the title, but the explicit verdict disproves the
claimed interpretation. Row-pairing had already produced the rejected
homophone family `经济 / 经纪`; neither pairing is licensed by the title.

## Reproduction

Validate the depth coordinates and answer decomposition:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

Reproduce the unique repeated block and its repaired hosts:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high_frequency.py `
  --input rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --output rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high-frequency-audit-current.md
```

Reproduce the two fanqie syllables:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 甲气 精节
```

Expected output: `ji4 / jie2`.
