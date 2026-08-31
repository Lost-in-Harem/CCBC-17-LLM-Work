# Rejected cyclic-direction extraction: 量化

**Status: rejected.** The user explicitly rejected both `高频交易` and the
later terminal `量化`. The bounded streams below remain reproducible, but the
cycle orientation was chosen because it makes Mandarin rather than by a
题面-specified ordering; `QI/YE/DE` also has several homophonic landings.
This route is no longer used by the active extraction.

## 1. Orient the three dimensions cyclically

The direction-local component-frequency fill has values only 1 and 2.  Exactly
four actual trades have value 2 on both incident entries.  Order those trades
by displayed board (`G1`, `G2`, `G3`) and local row/column, and take character
2 of both *printed* three-Han blocks.

The three directions form the cyclic order

```text
横 → 纵 → 里 → 横
```

so a 横/纵 trade is read 横→纵, while a 横/里 trade is read 里→横.
This one orientation rule gives:

| Order | Crossing | Directions | Oriented pair | Fanqie |
| ---: | --- | --- | --- | --- |
| 1 | G1 r05c12 | 横 / 纵 | `兔干` | `TAN` |
| 2 | G1 r07c02 | 横 / 纵 | `质锋` | `ZHENG` |
| 3 | G1 r09c10 | 横 / 里 | `性忆` | `XI` |
| 4 | G3 r09c10 | 横 / 里 | `百味` | `BEI` |

The repaired clue “西十五河海解谜中的关键词” answers `反切`, authorizing
initial-of-first plus final-of-second.  The four syllables read:

```text
TAN / ZHENG / XI / BEI = 弹筝西北
```

## 2. Pluck the northwest depth string

Center-aligning the three boards produces five depth strings.  “西北” selects
the unique northwest one, `Z01` at centered coordinate r04c04.  Rather than
stopping at its fill `路人甲`, inspect its three trades with the planar boards.
Apply the same cyclic orientation.  Each of these three selected trades has
direction-local frequency 1, so take character 1 of both printed blocks:

| Layer | Directions | Cyclic order | Frequency/index | Indexed pair | Fanqie |
| --- | --- | --- | ---: | --- | --- |
| G1 | 横 / 里 | 里→横 | 1 | `去一` | `QI` |
| G2 | 纵 / 里 | 纵→里 | 1 | `有的` | `YE` |
| G3 | 横 / 里 | 里→横 | 1 | `的的` | `DE` |

This yields:

```text
QI / YE / DE = 企业的
```

The direction rule has therefore been reused at two extraction levels; no
pair is individually reversed to force a legal syllable.

## 3. Rejected completion `企业的 END`

The unique repeated traded block `关键词` occurs in two restored clues. Their
answers are `反切`, used above, and `END`:

```text
结束本部分的关键词 -> END
```

The extracted fragment `企业的` is deliberately possessive and incomplete.
Place the second keyword after it exactly as supplied:

```text
企业的 END
```

This means the **ending of the enterprise's name**, not `END(企业)=业` and not
the English phrase `BUSINESS END`.  The title identifies the enterprise by
its short name `幻方`; its full name is `幻方量化`.  Therefore:

```text
企业：幻方量化
END：      量化
```

This proposed **量化**. The user explicitly rejected it, so the following
thematic checks are insufficient to authorize the completion:

1. The title “幻方的交易策略” defines `量化` as the hidden modifier of its
   trading strategy and as the omitted suffix of `幻方量化`.
2. The main fill literally turns decomposed answer components into numerical
   frequencies: it *quantifies* them.
3. “算法工程师 / 高频交易” describes the quantitative-finance setting without
   itself being the answer.

The earlier rejected `业` took the end of the generic word `企业`; `甲方` took
ends from two unrelated short strings.  Neither identified the enterprise's
full name, so those verdicts do not collapse this more specific operation.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 兔干 质锋 性忆 百味 去一 有的 的的
```

Expected fanqie output, in order:

```text
TAN ZHENG XI BEI QI YE DE
```
