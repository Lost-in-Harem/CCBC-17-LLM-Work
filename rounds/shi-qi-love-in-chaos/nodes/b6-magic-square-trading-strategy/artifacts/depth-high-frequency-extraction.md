# Depth-only high-frequency extraction

This is the direct extraction supported by Hint 3.  It uses only trades on
the depth/`里` dimension, which is the dimension absent from an ordinary
crossword.

## Selection rule

After restoring all 50 clues, split each answer into the ordered visible
components required by its entry length.  Count component frequency within
each statement direction (`横`, `纵`, `里`) and fill that number in the cell.
All 57 crossings agree.  The maximum frequency is 2.

There are four value-2/value-2 trades in the full three-dimensional grid, but
only two involve the depth dimension specified by Hint 3:

| Edge | Cell | Repaired directions | Value | Indexed pair | Fanqie |
| ---: | --- | --- | ---: | --- | --- |
| 55 | G1 r09c10 | 横 `气性不` / 里 `记忆中` | 2 | `性忆` | `XI` |
| 57 | G3 r09c10 | 横 `六百号` / 里 `的味道` | 2 | `百味` | `BEI` |

The order is fixed by the displayed boards G1 then G3.  Within each trade,
the restored pair is read in the statement's heading order, planar `横`
before depth `里`.  The frequency value 2 indexes the second character of
both traded three-Han blocks.  The separately restored keyword answer
`反切` supplies the phonetic operation:

```text
性 / 忆 -> XI
百 / 味 -> BEI
          西北
```

The other restored keyword is `END`; it says to stop the mechanical walk
here.  In particular, `西北` is not an instruction to select the northwest
depth line and start a second extraction.  In the three-dimensional stacked
grid it is a viewing direction—a **perspective**.  With the user's explicit
authorization to reverse-solve through the accepted Round Meta, the English
feeder answer is locked as **PERSPECTIVE**; see
`artifacts/meta-backsolve-perspective.md`.

## Reproduction

From the repository root, the complete numeric fill and the two selected
edges can be checked with:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --report rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md `
  --all-character-pairs rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

The second command reports edge 55 as repaired pair `性忆` and edge 57 as
repaired pair `百味`, both with value 2.
