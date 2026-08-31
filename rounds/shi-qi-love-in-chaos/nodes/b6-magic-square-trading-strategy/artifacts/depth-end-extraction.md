# Depth extraction: END as an instruction

## Why the third direction is the extraction

Hint 3 says to compare the contents of cells in the same positions on the
three boards; they correspond to the dimension absent from an ordinary
crossword.  Center-aligning the boards produces exactly five three-cell depth
entries:

| Centered coordinate | Repaired depth clue | Answer | Three cell contents | Direction-frequency pattern |
| --- | --- | --- | --- | --- |
| r04c04 | 一个可有可无的影子 | 路人甲 | 路 / 人 / 甲 | 111 |
| r04c10 | 学狐狸能达成这件事 | 成精 | 成 / 米 / 青 | 111 |
| r07c07 | 结束本部分的关键词 | **END** | **E / N / D** | 111 |
| r10c04 | 两根骨头连接根与尖 | 关节 | 丷 / 天 / 节 | 111 |
| r10c10 | 记忆中厕所里的味道 | 氨气 | 气 / 安 / 气 | 212 |

The middle entry lies at the unique common center of all three boards.  Its
clue directly gives the keyword **END**, but the user rejected it as the final
answer.  It instead selects the end layer G3 at all five depth columns:
`甲 / 青 / D / 节 / 气`.  The other restored `关键词` clue answers `反切`, so
the top pair `甲青` reads `jing1`; central `D` represents “的”, while the
bottom pair already spells `节气`.  The complete rebus is “JING 的节气”,
which uniquely clues `惊蛰`.  The complete extraction is recorded in
`artifacts/depth-endpoint-fanqie.md`.

## Why BREAK was wrong

The former provisional answer `BREAK` has five letters.  Making it fit the
three-cell depth entry required the arbitrary grouping `B / RE / AK`.  That
operation combines letters, whereas Hint 2 tells the solver to *decompose*
answers.  `END` instead contributes one written symbol to each cell, with no
extra convention:

```text
G1 center = E
G2 center = N
G3 center = D
```

Replacing `BREAK` by `END` leaves every direction-local count equal at all
57 crossings.  Each of E, N, and D occurs once in the depth direction, so the
center pattern remains `111`.

The three visible blank runs are not extraction marks.  After the trades they
complete clues whose answers would otherwise appear literally in their clue
texts (`榜样`, `曼丽`, and `气性`).  Treating the fixed underline locations as
marks created the rejected `DAMAGE` continuation and is unnecessary here.

## Reproduction

From the repository root:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

The command validates all 57 crossings and reports the center as
`END[1]=E`, `END[2]=N`, and `END[3]=D` on G1, G2, and G3 respectively.  It
also reports all five G3 contents used next: `甲 / 青 / D / 节 / 气`.
