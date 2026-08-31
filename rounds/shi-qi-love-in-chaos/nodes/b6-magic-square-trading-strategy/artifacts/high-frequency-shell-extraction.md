# Rejected high-frequency END rebus extraction: 古今中外

**Status: rejected.** The user explicitly rejected `古今中外`.  The linear
orientation and `外［嬴政］滩` construction below are retained only as a bounded
failed route; neither its subwords nor a semantic/positional rebus reading may
be restored without new evidence.

## Four high-frequency trades

The direction-local component-frequency fill has values only 1 and 2.  Exactly
four geometric trades have value 2 on both incident entries.  Order them by
the displayed boards (`G1`, `G2`, `G3`) and local row/column; within a trade,
keep the statement direction order `横 / 纵 / 里`.  Since the value is 2,
take character 2 from each *printed* three-Han block:

| Order | Crossing | Printed blocks | Indexed pair | Fanqie |
| ---: | --- | --- | --- | --- |
| 1 | G1 r05c12 | `吃兔子 / 在干活` | `兔干` | `TAN` |
| 2 | G1 r07c02 | `地质学 / 雷锋是` | `质锋` | `ZHENG` |
| 3 | G1 r09c10 | `记忆中 / 气性不` | `忆性` | `YING` |
| 4 | G3 r09c10 | `的味道 / 六百号` | `味百` | `WAI` |

The repaired orientation would give `GU/FI/XI/BEI`, including invalid `FI`;
the printed orientation is therefore independently checked.  The repaired
clue “西十五河海解谜中的关键词” answers `反切`, authorizing the phonetic
operation.

## Read from END

The other repaired `关键词` clue answers `END`.  Start at the literal end of
the fixed stream and read the whole stream backward:

```text
TAN / ZHENG / YING / WAI
 WAI / YING / ZHENG / TAN
  外 /   嬴    政   / 滩
```

This preserves a rebus rather than two independent words:

```text
外［嬴政］滩
```

The endpoints make `外滩`, fixing the right-to-left orientation because
`TAN/WAI` is not a local two-Han word.  The middle makes `嬴政`.

## Name the represented concept

The two repeated `关键词` blocks traded with `古代人` and `的概念`; in repaired
host order these concatenate exactly to `古代人的概念`.  This confirms that
the middle is the ancient person and asks for the concept represented by the
whole rebus.  Preserve the two nested objects rather than replacing the scene
with the rejected loose idea “time travel”:

| Object, inner to outer | Time attribute | Position attribute |
| --- | --- | --- |
| `嬴政` | `古` | `中` |
| `外滩` | `今` | `外` |

Read the attribute columns in their displayed order:

```text
古 今 / 中 外 = 古今中外
```

This uses every stable feature of `外［嬴政］滩`: both identities, their
ancient/present contrast, and their inner/outer relation.  The local dictionary
contains both `古今中外` and rare reordered `中外古今`; their frequencies are
108 and 6 respectively, and the table's semantic-then-positional reading gives
the canonical former order. The rejected `穿越` used only the first column;
`上海皇帝` discarded the layout entirely. No online answer or solution lookup
was used.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 兔干 质锋 忆性 味百
```
