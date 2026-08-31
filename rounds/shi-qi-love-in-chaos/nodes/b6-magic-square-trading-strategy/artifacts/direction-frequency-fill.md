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

## Extraction consequence

Hint 3 restricts extraction to the depth/`里` dimension absent from an
ordinary crossword.  Among the four value-2/value-2 trades in the complete
fill, exactly two involve that dimension:

```text
edge 55: 横 气性不 / 里 记忆中, index 2 -> 性忆 -> XI
edge 57: 横 六百号 / 里 的味道, index 2 -> 百味 -> BEI
                                                   西北
```

The pair order is fixed by the statement directions `横` before `里`; the
trade order is fixed by the displayed boards G1 before G3.  The separately
restored keyword `反切` supplies the operation, and the other keyword `END`
says to stop rather than use `西北` as a second-stage line selector.  In the
stacked three-dimensional grid, `西北` is the extracted viewing direction or
**perspective**.  The accepted Round Meta fixes the English feeder form as
**PERSPECTIVE**; details are in
`artifacts/depth-high-frequency-extraction.md` and
`artifacts/meta-backsolve-perspective.md`.

## Reproduction

From the repository root:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

The command fails on any unequal crossing and otherwise prints all three
numeric boards and the five centered depth coordinates.
