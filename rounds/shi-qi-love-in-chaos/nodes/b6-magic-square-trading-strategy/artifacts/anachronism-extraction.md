# Four high-frequency trades to ANACHRONISM

> **Status: rejected.** The user explicitly rejected `ANACHRONISM` on
> 2026-08-31. The failure is upstream of the concept synonym: reading the
> three directions as a linear order and treating `END` as whole-stream
> reversal is not the active extraction. The current route selects the unique
> repeated block `关键词` and uses the four outer depth-answer ends; see
> `artifacts/qingming-extraction.md`.

## 1. Hint 3 completes the three-dimensional crossword

Hint 3 explains that corresponding cells of the three displayed boards form
the `里` direction absent from an ordinary crossword.  It therefore adds the
five depth entries and their fifteen crossings to the same fill; it does not
say to discard the ordinary `横/纵` high-frequency trades.

After the 50 clues are restored, answers are decomposed and their component
frequencies are counted within `横/纵/里`.  The resulting values agree at all
57 crossings.  Exactly four trades occur at the maximum cell value 2.

## 2. Read all four high-frequency trades

The objects that actually underwent the trades are the blocks in the printed,
scrambled statement.  Within a crossing, use the displayed direction order
`横`, then `纵`, then `里`; order crossings by board and coordinate.  Value 2
indexes the second Han character of both incident three-Han blocks:

| Order | Crossing | Printed direction-order blocks | Indexed pair | Fanqie |
| ---: | --- | --- | --- | --- |
| 1 | G1 r05c12 | `吃兔子 / 在干活` | `兔干` | `TAN` |
| 2 | G1 r07c02 | `地质学 / 雷锋是` | `质锋` | `ZHENG` |
| 3 | G1 r09c10 | `记忆中 / 气性不` | `忆性` | `YING` |
| 4 | G3 r09c10 | `的味道 / 六百号` | `味百` | `WAI` |

The repaired clue `西十五河海解谜中的关键词` answers `反切`, supplying the
initial-of-first plus final-of-second operation.  This produces the fixed
stream:

```text
TAN / ZHENG / YING / WAI
```

The other repaired keyword clue answers `END`.  Read the stream from its end:

```text
WAI / YING / ZHENG / TAN
 外 /   嬴    政   / 滩

外［嬴政］滩
```

The endpoints form the modern Shanghai landmark `外滩`; the middle forms the
ancient person `嬴政`.

## 3. Name the represented concept

`关键词` is also the only repeated repaired three-Han block.  Its two actual
trade partners, in repaired-host order, are:

```text
古代人 / 的概念
```

This independently identifies `嬴政` as the ancient person and asks for the
concept represented by the complete placement.  An ancient historical figure
placed inside a modern landmark is an **ANACHRONISM**: a person or thing shown
in a historical period where it does not belong.

The rejected `穿越` names a possible fictional cause, not the represented
concept.  The rejected `古今中外` merely labels two attribute pairs and is not
the name of the temporal-placement phenomenon.  `ANACHRONISM` is the specific
noun requested by `的概念` and preserves both identities in the rebus.

No online answer or official solution was consulted.

## Reproduction

The four rows can be reproduced from the fixed fill and crossing ledger with:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --report rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md `
  --all-character-pairs rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

The unique repeated block and partners are reproduced by:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high_frequency.py `
  --input rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --output rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high-frequency-audit-current.md
```
