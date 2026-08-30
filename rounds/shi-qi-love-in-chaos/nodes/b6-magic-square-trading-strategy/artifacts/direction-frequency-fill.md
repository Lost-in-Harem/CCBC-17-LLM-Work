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

The numeric fill fixes ambiguous repaired answers, especially `易伤`, `名著`,
and `氨气`.  This matters at the final locator: the three fixed underlines
read `DA/MI/JI = DAMAGE`, and the unique repaired clue containing its Chinese
counterpart is `发生后伤害数字变大`.  Its answer **易伤** decomposes as
`日 / 勿 / 伤` and participates in the exact 57/57 crossing closure; the old
semantic alternative `暴击` does not.

The former answer-length chain `易伤 -> ζ电势 -> BREAK` and its return to
`数网格端` produced the user-rejected candidate `循环`.  It is preserved only
as negative evidence in `artifacts/extraction-loop.md` because the puzzle does
not state that answer character counts should index clue blocks.

The former selection of only the four value-2/value-2 crossings led to
`TAN/ZHENG/YING/WAI` and then to the user-rejected `嬴政`; that extraction is
not part of the current route.

## Reproduction

From the repository root:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

The command fails on any unequal crossing and otherwise prints all three
numeric boards and the five centered depth coordinates.
