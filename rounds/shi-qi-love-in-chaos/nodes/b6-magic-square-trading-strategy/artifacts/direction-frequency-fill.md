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
| r07c07 | 结束本 / 部分的 / 关键词 | **BREAK** | 111 |
| r10c04 | 两根骨 / 头连接 / 根与尖 | 关节 | 111 |
| r10c10 | 记忆中 / 厕所里 / 的味道 | 氨气 | 212 |

The middle depth line is at the exact center of all three boards. Its clue
does answer **BREAK**, but the user explicitly rejected BREAK as the final
answer. It is therefore an internal stop word, not an extraction target. If
used only for the numeric check, a provisional `B / RE / AK` split has the
required `111` pattern; that split is not otherwise unique.

## Extraction consequence

In the natural visible-component fill, exactly four actual crossing trades
have value 2. Selecting character 2 of their three-Han blocks and applying the
repaired instruction `反切` reads `古筝 / 西北`. Independently, the only
repeated restored clue block is `关键词×2`; its trade partners read
`古代人的概念`. The rejected `路人甲` and `氨气` attempts show that this is not
a spatial choice among the five depth answers, and the rejected `闲钱` rules
out the unrelated conversions `古筝→弦` and `西北→乾`.  Instead, `古筝` fixes
the ancient five-tone domain; under five tones paired with five directions,
`西北→商羽`.  The pair's two fanqie orientations read `SHU/YANG`, and the
independent definition uniquely lands on `阳数`.  The complete extraction is
recorded in `artifacts/high-frequency-trade-extraction.md`.

## Reproduction

From the repository root:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

The command fails on any unequal crossing and otherwise prints all three
numeric boards and the five centered depth coordinates.
