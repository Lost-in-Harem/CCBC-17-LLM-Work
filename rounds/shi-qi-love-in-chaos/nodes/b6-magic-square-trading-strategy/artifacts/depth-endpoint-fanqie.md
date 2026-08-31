# Rejected depth rebus extraction: 惊蛰

> The user explicitly rejected `惊蛰` on 2026-08-30.  The five G3 characters
> below remain reproducible, but `D -> 的` is not a licensed rebus step.  This
> artifact is retained only as negative evidence.

Hint 3 creates five three-cell entries in the direction through the three
boards.  Their fixed centered layout and decomposed contents are:

| Coordinate | Depth answer | G1 | G2 | G3 |
| --- | --- | --- | --- | --- |
| r04c04 | 路人甲 | 路 | 人 | **甲** |
| r04c10 | 成精 | 成 | 米 | **青** |
| r07c07 | END | E | N | D |
| r10c04 | 关节 | 丷 | 天 | **节** |
| r10c10 | 氨气 | 气 | 安 | **气** |

The center clue is “结束本部分的关键词”.  `END` is therefore an instruction,
not the final answer: select the end layer G3 at all five common coordinates.
Their fixed geometry is:

```text
甲   青
   D
节   气
```

The only other restored clue containing the repeated block `关键词` answers
`反切`.  Apply it to the top pair:

```text
甲青 = j + ing1 = JING1
```

Keep the center: `D` reads as Chinese `的` (`de`).  Keep the bottom row
literal: it already spells `节气`.  The complete rebus is therefore
`JING1 的节气`, whose unique completion is:

```text
惊蛰
```

## Why the previous route failed

Deleting `D` and fanqie-reading the bottom row changed the diagram into
`JING1/JI4`, leading to the rejected `经济/经纪` guesses.  It also discarded
one of the five cells selected by Hint 3.  The complete five-cell layout needs
no homophone ranking: the center and bottom row literally supply `的节气`.

## Reproduction

From the repository root:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 甲青
```

The first command verifies all 57 frequency crossings and prints the five
depth columns.  The second prints `甲青=jing1`.
