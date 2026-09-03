# Rejected extraction: HIGH-FLYER

**Status:** rejected by the user on 2026-08-31.  This artifact is retained
only to reproduce the closed title-company landing.  Neither `HIGH-FLYER`
nor another company, product, or fund-type name may be substituted without a
new mechanical extraction.

## 1. Orient trades with the central depth answer

The repaired center depth clue answers `END`, filling the three displayed
layers as `E / N / D`.  These letters label the three statement directions
East/across, North/down, and Depth/inside, and fix the cycle:

```text
横(E) -> 纵(N) -> 里(D) -> 横(E)
```

There are exactly four crossings at which both direction-local component
frequencies are the maximum value 2.  Use 2 to index the two printed
three-Han blocks, orient the pair by the cycle, and apply the repaired keyword
answer `反切`:

| Crossing | Oriented pair | Fanqie |
| --- | --- | --- |
| G1 r05c12 | `兔干` | TAN |
| G1 r07c02 | `质锋` | ZHENG |
| G1 r09c10 | `性忆` | XI |
| G3 r09c10 | `百味` | BEI |

This gives the instruction:

```text
弹筝西北
```

The alternative claim that statement-source order gives `古筝西北` is
false: true printed source order gives `TAN/ZHENG/YING/WAI`.  The cycle above
is the only retained orientation rule.

## 2. Pluck the northwest depth string

The three centered grids have five depth strings.  `西北` uniquely selects
Z01 at centered coordinate r04c04.  Its three crossing frequencies are all
1.  Index and orient its three trades by the same rule:

| Layer | Oriented pair | Fanqie |
| --- | --- | --- |
| G1 | `去一` | QI |
| G2 | `有的` | YE |
| G3 | `的的` | DE |

The unique natural title-relevant landing is:

```text
企业的
```

`CORPORATE` and `WEEKEND` were rejected because they treated this as a final
definition or respelled it.  Here it remains a locator.

## 3. Resolve the title's double meaning

The title is `幻方的交易策略`.  The extracted possessive `企业的` identifies
the occurrence `幻方的`: `幻方` is to be understood as an enterprise name,
not merely the mathematical object “magic square.”  The flavor text gives an
independent check by placing the speaker among algorithm engineers doing
high-frequency trading.

The English name of the enterprise `幻方` is:

```text
HIGH-FLYER
```

That is the candidate.  No endpoint of the company name, English adjective,
Meta homophone, or company product is appended.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 兔干 质锋 性忆 百味 去一 有的 的的
```

Expected toneless syllables are:

```text
TAN ZHENG XI BEI QI YE DE
```

The coordinate and direction proof is retained in
`work/visual/cyclic-direction-audit.md`.
