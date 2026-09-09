# Direction-frequency fill

## Rule

1. Undo the three-Han clue-block trade at every geometric crossing: 42 planar
   crossings plus 15 depth crossings, for 57 trades total.
2. Answer each repaired clue and split Chinese characters into ordered visible
   components until the component count equals the entry length.
3. Count each component separately within the three statement directions
   `横`, `纵`, and `里`.  Put that direction-local frequency in its cell.

The fixed decomposition ledger is in
`artifacts/direction-frequency-solution.json`.  It gives 57/57 equal numeric
crossings.  The only repeated components are:

| Direction | Components of frequency 2 |
| --- | --- |
| 横 | 凵、月、队、木、又、气 |
| 纵 | 艹、小、㇏、又、田 |
| 里 | 气 |

Every other component has frequency 1.  Several ambiguous clue answers are
fixed by this condition: `莱尔`, `易伤`, `名著`, `权贵`, `东京优骏`, and
`氨气` all participate in the exact crossing closure.

## Depth lines

Center-aligning the three boards in a 13 by 13 frame gives five positions open
on all three layers:

| Centered coordinate | Restored depth clue | Answer | Frequency pattern |
| --- | --- | --- | --- |
| r04c04 | 一个可 / 有可无 / 的影子 | 路人甲 | 111 |
| r04c10 | 学狐狸 / 能达成 / 这件事 | 成精 | 111 |
| r07c07 | 结束本 / 部分的 / 关键词 | **END** | 111 |
| r10c04 | 两根骨 / 头连接 / 根与尖 | 关节 | 111 |
| r10c10 | 记忆中 / 厕所里 / 的味道 | 氨气 | 212 |

The middle depth line is at the exact center of all three boards.  Its clue
answers **END**, whose three letters fill the three cells directly as
`E / N / D`.  The former `BREAK` fill required the arbitrary merger
`B / RE / AK`, contrary to the decomposition rule, and has been discarded.

## Cyclic extraction prefix

Hint 3 adds the depth/`里` dimension absent from an ordinary crossword. It
does not discard the planar directions. The complete fill has four
value-2/value-2 trades. Read each printed traded pair in the single global
direction cycle `横→纵→里→横`:

```text
edge 06: 横 吃兔子 / 纵 在干活, index 2 -> 兔干 -> TAN
edge 09: 横 地质学 / 纵 雷锋是, index 2 -> 质锋 -> ZHENG
edge 55: 里 气性不 / 横 记忆中, index 2 -> 性忆 -> XI
edge 57: 里 六百号 / 横 的味道, index 2 -> 百味 -> BEI
```

The restored keyword `反切` supplies the operation. Reading central `E/N/D`
as East/North/Depth fixes `横→纵→里→横`, producing
`弹筝西北→QI/YE/DE`. The direct landings `CORPORATE`, `HIGH FLYER`,
`LANG/WOLF`, `PHILOSOPHY`, `CONCUBINE`, `CORPORATE STRUCTURE`, and `MOGUL`
were explicitly rejected. The current route instead keeps the Romanized
structure: `QIYE=企业=ENTERPRISE`, while `END(QIYEDE)=E`, giving
**Enterprise-E**. The independently extracted concept `阶级=class` then
identifies its exact class name, `SOVEREIGN`.

## Reproduction

From the repository root:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

The command fails on any unequal crossing and otherwise prints all three
numeric boards and the five centered depth coordinates.
