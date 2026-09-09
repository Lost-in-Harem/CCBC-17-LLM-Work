# Rejected extraction: CONCUBINE

> Status: rejected by the user on 2026-09-03. This file preserves the failed
> reasoning for audit only; it must not be used to restore `CONCUBINE` or a
> synonym without new evidence.

## 1. Reach the northwest-string output

The fully repaired 3-D component crossword has exactly four trades whose two
direction-local frequencies are both 2.  The central depth answer `END`,
written `E / N / D`, labels East/North/Depth and fixes the cycle
`横 -> 纵 -> 里 -> 横`.  Indexing the printed traded blocks by 2 and applying
the separately repaired keyword `反切` gives:

```text
兔干 / 质锋 / 性忆 / 百味
 TAN / ZHENG / XI / BEI
 弹筝西北
```

The five depth entries are the five strings through the displayed boards, so
`西北` selects the unique northwest string.  Repeating the same operation at
its three frequency-1 trades gives:

```text
去一 / 有的 / 的的
 QI / YE / DE
 企业的
```

The two streams and every selected crossing are reproduced by
`artifacts/direction-frequency-fill.md`.

## 2. Complete the possessive with the题内 operation

`企业的` was previously mistranslated as the rejected adjective `CORPORATE`.
It is instead an unfinished instruction.  One of the only two repaired clues
containing the unique highest-frequency block `关键词` answers `反切`, so the
exact grammatical completion is:

```text
企业的反切 = the fanqie of 企业
```

Use the initial of `企 qǐ` and the phonological final plus tone of `业 yè`:

```text
q + iè = qiè
```

This is stricter than a toneless homophone choice: the fourth tone is inherited
from the lower fanqie character `业`.

## 3. Use the actual keyword-trade partners as the type constraint

The two `关键词` occurrences traded with the complete blocks, in repaired-host
order:

```text
古代人 / 的概念
```

They are not an English charade.  They tell what kind of `qiè` concept is
wanted.  The local one-character `qiè` set includes `切 / 鍥 / 妾 / 窃 / 怯`;
only **`妾`** denotes an ancient social-person role.  The other keyword clue
answers `END`, so the extraction stops at this uniquely typed landing instead
of translating `企业的` or recursing through the grids again.

The proposed English feeder form was:

```text
妾 = CONCUBINE
```

## 4. Meta check and disclosed residue

This positional check did not validate the candidate. The accepted Meta was
used only as a positional check. Its old semantic audio
labels are stale after b4 and b10 were solved, but the unresolved `BO` suffix
needs an `O` and the candidate has exactly one same-position match:

```text
BO
CONCUBINE
 O
```

The same two keyword trades also have the exact state pair
`GUAN/DUAN -> 关断` before repair and `GU/GE -> 骨骼` after repair.  This is a
strong checksum involving `END`, but it did not by itself specify a unique
English landing. The later `GU/GE + QI/YE/DE` join was rejected as
`CORPORATE STRUCTURE`, and the later join to grid answer `权贵` was rejected as
`MOGUL`. The current route instead keeps the spelling structure
`QIYE=ENTERPRISE`, `END(QIYEDE)=E`; that does not validate the `qiè -> 妾`
claim or the rejected answer recorded here.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\keyword-operation-audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt
```
