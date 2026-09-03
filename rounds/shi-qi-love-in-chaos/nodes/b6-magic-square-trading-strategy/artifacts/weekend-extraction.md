# Rejected cyclic high-frequency extraction: WEEKEND

**Status: rejected.** The user explicitly rejected `WEEKEND`. The mechanical
second stream `QI / YE / DE` can be reproduced, but neither `企业的` nor
`七夜的` led to the answer. Two consecutive natural landings failing closes
the cyclic-direction/northwest-string family as a final extraction.

## 1. Read the four highest-frequency trades

After all 57 three-Han trades are undone, each clue answer is decomposed to
the length of its grid entry and each component is replaced by its frequency
within its statement direction.  All 57 crossings agree and the maximum cell
value is 2.  Exactly four trades occur at that value on both incident entries.

Order them by displayed board and coordinate.  The only one of the eight
global orientations of `横 / 纵 / 里` that makes ordinary Mandarin at both
extraction levels is the direction cycle

```text
横 → 纵 → 里 → 横
```

Index character 2 of the two printed blocks at each selected trade and apply
the separately clued operation `反切`:

| Crossing | Cyclic order | Indexed pair | Fanqie |
| --- | --- | --- | --- |
| G1 r05c12 | 横→纵 | `兔干` | `TAN` |
| G1 r07c02 | 横→纵 | `质锋` | `ZHENG` |
| G1 r09c10 | 里→横 | `性忆` | `XI` |
| G3 r09c10 | 里→横 | `百味` | `BEI` |

Thus:

```text
TAN / ZHENG / XI / BEI = 弹筝西北
```

## 2. Pluck the northwest depth string

Center-aligning the three boards creates five depth strings at four corners
and the center.  `西北` selects `Z01 / r04c04`.  Its three values are all 1,
so index character 1 of the three printed trades and reuse the same direction
cycle and fanqie operation:

| Layer | Cyclic order | Indexed pair | Fanqie |
| --- | --- | --- | --- |
| G1 | 里→横 | `去一` | `QI` |
| G2 | 纵→里 | `有的` | `YE` |
| G3 | 里→横 | `的的` | `DE` |

The fixed stream is therefore:

```text
QI / YE / DE
```

## 3. Use the other keyword as part of the answer

The second restored special clue is literal:

```text
结束本部分的关键词 -> END
```

A bounded scan of the local Han dictionary finds only six two-Han entries
with toneless pinyin `QI / YE`: `企业、七夜、起夜、七叶、七爷、漆液`.
`企业的` previously led to the explicitly rejected answers `BUSINESS END`,
`业`, `甲方`, `量化`, `高频交易`, and finally `CORPORATE`.  It is therefore
not rescued by another corporate synonym.

The alternate phrase `七夜的` makes `END` an exact operand rather than a stop
signal:

```text
七夜 = seven nights = one WEEK
七夜的 END = the WEEK's END = WEEKEND
```

This accounts for the otherwise unused `的` and uses the clue answer `END`
literally.  The high-frequency-trading setting gives a secondary surface
check: a trading week has an end, but that theme is not used to manufacture
the letters.

## 4. Meta check and disclosed contradiction

After accepted b4=`PEEP` replaces the Meta's former b4 guess, the two still
unresolved semantic rows are clip 6 (`BO`, wanted `O`) and clip 10
(`ZHIWANG`, wanted `N`).  `WEEKEND` has one exact target overlap with the
latter at position 6:

```text
ZHIWANG
WEEKEND
     N
```

It has no overlap with `BO`.  This does **not** corroborate the proposed b6
row assignment.  The accepted b10 answer `INFLOOD` also fails the old exact
clip-10 overlap and was previously represented there only by the unaccepted
semantic proxy `CURRENT`; hence the stale Meta row mapping cannot presently
decide this feeder.  The candidate rests on the local extraction above.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 兔干 质锋 性忆 百味 去一 有的 的的

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --reading QI YE
```

Expected mechanical outputs are `TAN/ZHENG/XI/BEI`, `QI/YE/DE`, and the six
bounded `QI/YE` dictionary entries listed above.
