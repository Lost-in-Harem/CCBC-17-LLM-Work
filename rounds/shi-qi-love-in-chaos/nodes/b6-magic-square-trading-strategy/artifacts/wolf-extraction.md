# Rejected extraction: WOLF

> Verdict (2026-08-31): the user explicitly reported `WOLF` is not the
> answer. Sections 1–3 preserve the reproducible upstream route to `LANG`;
> section 4 is the rejected Meta-assisted homophone landing and must not be
> reused without new evidence.

## 1. Use `END` as the three direction labels

The two repaired clues that literally contain `关键词` answer `反切` and
`END`. The central depth answer is not merely an English word: its direct
three-cell decomposition puts `E / N / D` on the three displayed layers.
These letters label the three crossword directions:

```text
E = East = 横
N = North = 纵
D = Depth = 里
```

Treating the written order cyclically gives one global trade orientation,
`横→纵→里→横`. This supplies the independent rule that the earlier cyclic
audit lacked.

## 2. Read the maximum-frequency trades

Exactly four geometric trades have direction-local frequency 2 on both
sides. Take character 2 of both printed three-Han blocks, order their two
directions by the `E→N→D→E` cycle, and use the other keyword, `反切`:

| Crossing | Oriented indexed pair | Fanqie |
| --- | --- | --- |
| G1 r05c12 | `兔干` | TAN |
| G1 r07c02 | `质锋` | ZHENG |
| G1 r09c10 | `性忆` | XI |
| G3 r09c10 | `百味` | BEI |

This gives the complete instruction `弹筝西北`. The five depth entries are
five strings through the three boards, and only Z01 at centered coordinate
r04c04 is northwest. Pluck/read its three trades with the same direction
cycle and each cell's frequency 1:

| Layer | Pair | Fanqie |
| --- | --- | --- |
| G1 | `去一` | QI |
| G2 | `有的` | YE |
| G3 | `的的` | DE |

The unique natural stream is `企业的`. Rejected answers `CORPORATE` and
`WEEKEND` stopped here; this phrase is instead an instruction to identify the
possessive structure already printed in the title.

## 3. Return to the title

The title is `幻方的交易策略`, and the flavor establishes `幻方` as the
enterprise in this reading. Thus `企业的` identifies:

```text
幻方 的 交易策略
```

Take `END` of the enterprise name and its strategy: `方 / 略`. Their title
order forms `方略`, itself a synonym of `策略`, which checks the scope. Apply
the title's trade and then the repaired `反切` keyword:

```text
方略 --交易--> 略方
略方 --反切--> l + ang = LANG
```

## 4. Meta-assisted homophone landing

`LANG` alone has several Han homophones. The user authorized a Meta
backsolve. After accepted b4=`PEEP` occupies the old `观` row, b6 is the
remaining feeder for the `怪 / BO` row. The creature reading `狼` gives the
English answer `WOLF`, and the positional overlap is exact:

```text
BO
WOLF
 O
```

Only the second-position `O` matches, producing the sixth letter of accepted
Meta `PARADOXXING`. This is a final disambiguator, not an independent answer
source; accepted b10=`INFLOOD` still shows that the old proxy table is not a
complete proof of actual feeder spellings.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 兔干 质锋 性忆 百味 去一 有的 的的 略方

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\meta_actual_feeder_audit.py --b6 WOLF
```

Expected final phonetic result: `略方 -> LANG`; expected Meta result:
`b6?=WOLF@2` on clip 06.
