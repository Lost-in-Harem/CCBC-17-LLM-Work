# Candidate extraction: CORPORATE STRUCTURE

> Status: candidate, not yet confirmed by the user. The earlier answer
> `CORPORATE` was rejected because it stopped after only the first of the two
> phonetic streams below.

## 1. Restore and fill the three-dimensional crossword

Undoing the three-Han clue-block trade at every intersection restores all 50
clues. There are 42 planar trades and 15 trades along the five depth entries,
57 in total.

Each answer is decomposed into the number of visible components required by
its entry. A cell contains that component's frequency within its own
direction (`横`, `纵`, or `里`). This gives equal values at all 57 crossings.
The complete ledger is `artifacts/direction-frequency-solution.json`.

## 2. Read the high-frequency trades

Exactly four trades have the maximum value 2 on both incident entries. The
central depth answer is `END`, placed directly as `E / N / D`; these letters
label East/North/Depth and fix the cycle `横→纵→里→横`.

Take character 2 of the two printed three-Han blocks at each selected trade,
orient them by that cycle, and use the independently clued operation `反切`:

| Crossing | Pair | Fanqie |
| --- | --- | --- |
| G1 r05c12 | `兔干` | `TAN` |
| G1 r07c02 | `质锋` | `ZHENG` |
| G1 r09c10 | `性忆` | `XI` |
| G3 r09c10 | `百味` | `BEI` |

The result is the instruction `弹筝西北`. The five depth entries are the five
strings through the displayed boards, so `西北` selects Z01. Its three cell
values are all 1. Apply the same indexing, cycle, and fanqie rule to its three
trades:

| Layer | Pair | Fanqie |
| --- | --- | --- |
| G1 | `去一` | `QI` |
| G2 | `有的` | `YE` |
| G3 | `的的` | `DE` |

This gives the incomplete possessive `企业的`.

## 3. Let the highest-frequency clue block make its trades

The 50 repaired clues contain 180 three-Han blocks and 179 distinct texts.
The unique maximum-frequency block is `关键词`, occurring twice. Put this
selected block first in each of its two real trades and use the cell value 1:

| Repaired host answer | Selected block / partner | Indexed pair | Fanqie |
| --- | --- | --- | --- |
| `反切` | `关键词 / 古代人` | `关古` | `GU` |
| `END` | `关键词 / 的概念` | `关的` | `GE` |

This post-trade stream is `GU/GE`. The state choice is independently checked
by the same two trades before repair: in the fixed direction cycle they read
`古关 / 的关 -> GUAN/DUAN = 关断`, exactly the meaning of the keyword answer
`END`. Performing the trades changes that checksum into the desired second
stream.

## 4. Jointly disambiguate the two streams

The local dictionary contains only these common two-Han landings:

```text
QI/YE: 企业、七夜、起夜、七叶、七爷、漆液
GU/GE: 骨骼、古格、古歌、雇个
```

Combining them with the fixed third syllable `DE` produces 24 equal-length
phrases. `企业的骨骼` is the only natural completion and also the only one
supported by the title/flavor's enterprise setting. As a bounded diagnostic,
the local Chinese model ranks it first at `-23.665`; the next phrase,
`七爷的骨骼`, scores `-28.019`.

Thus the extraction ends with the Chinese definition:

```text
企业的骨骼
```

The conventional English answer is:

```text
CORPORATE STRUCTURE
```

This does not restore the rejected one-word answer `CORPORATE`: that word was
only the unfinished first stream. The second stream supplies `STRUCTURE`.

## 5. Meta check and residual ambiguity

The old semantic assignments in the accepted Meta are stale after b4 and b10
were independently solved, so they cannot establish this answer. As a weak
positional check only, the unresolved suffix `BO` and normalized candidate
have exactly one same-position match, the required `O` at position 2:

```text
BO
CORPORATESTRUCTURE
 O
```

The Chinese definition can be paraphrased as *company structure* or
*organizational structure*. `CORPORATE STRUCTURE` is preferred because
`企业的` directly supplies *corporate* and the resulting English phrase is
standard; this answer-form choice is why confidence remains medium pending a
verdict.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json

& 'C:\Users\Lost\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -X utf8 `
  rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\keyword-operation-audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --model rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\gpt2_distil_zh `
  --vendor rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\vendor_lm `
  --candidate "CORPORATE STRUCTURE"
```
