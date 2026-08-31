# Rejected underline-frequency Morse route: CFD

The user explicitly rejected `CFD`.  The three marked frequency strings below
remain reproducible, but the puzzle never authorizes interpreting them as
Morse; this artifact is retained only as negative evidence.

The three literal underline runs are the puzzle's extraction markers.  After
all 57 clue-block trades are undone, the missing text in statement order is:

1. `好□□` -> `榜样`
2. `丽□□` -> `曼丽`
3. `□□不` -> `气性`

Each filled word is also the answer to the repaired clue containing it.  Split
those answers by the same component rule used to fill the crossword, then use
the direction-local frequency of each component:

| Underline order | Answer | Filled slot | Components | Frequencies | Morse (`1=.` / `2=-`) |
| ---: | --- | --- | --- | --- | --- |
| 1 | 榜样 | `G1-A06` | 木 / 旁 / 木 / 羊 | `2121` | `-.-.` = **C** |
| 2 | 曼丽 | `G2-D06` | 曰 / 罒 / 又 / 丽 | `1121` | `..-.` = **F** |
| 3 | 气性 | `G1-A09` | 气 / 心 / 生 | `211` | `-..` = **D** |

The polarity is forced: reversing dot and dash makes the first marked answer
`.-.-`, which is not a standard Morse letter.  The marked stream is therefore:

```text
CFD
```

The former route expanded the letters as Contract for Difference（差价合约）
from the trading flavor.  The explicit rejection closes both the acronym and
that semantic expansion.  No online answer or solution lookup was used.

## Reproduction

The fixed decomposition ledger and the 57/57 crossing check are reproduced by:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

The Morse rendering, including the three rows above, is reproduced by:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-morse rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```
