# Rejected cyclic-direction landing: CORPORATE

**Status: rejected landing, retained upstream.** The user explicitly rejected
both **CORPORATE** and the alternate **WEEKEND** landing.  The later strict
central fill `E / N / D` independently authorizes the direction cycle, so the
phonetic prefix `弹筝西北 -> 企业的` remains reproducible.  Only the direct
English landings documented here are closed. A later continuation read the
two trades of the unique repeated `关键词` block as `GU/GE=骨骼` and proposed
`企业的骨骼 -> CORPORATE STRUCTURE`; the user rejected that answer as well.
The later `企业的权贵 -> MOGUL` join was also explicitly rejected. The current
candidate keeps the Romanized form: `QIYE=企业=ENTERPRISE` and
`END(QIYEDE)=E`, identifying Enterprise-E rather than another Chinese
possessive completion.

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

## 3. Stop at the complete definition `企业的`

The unique repeated traded block `关键词` occurs in two restored clues. Their
answers are `反切`, used above, and `END`:

```text
结束本部分的关键词 -> END
```

The old route treated `企业的` as an incomplete possessive phrase. That was
the grammatical mistake: the feeder answer is English, so Chinese `企业的`
is a complete adjective definition:

```text
企业的 = CORPORATE
```

The clue for the other keyword literally says that it is the keyword that
ends this part. Thus `END` is a stop signal once this complete definition has
been obtained; it is not an instruction to reverse the previous stream, take
a last letter, or append an English fixed phrase.

The title and flavor text independently place the speaker inside an
algorithmic high-frequency-trading enterprise and therefore support the
corporate sense. No company-name lookup is required.

## 4. Rejected extensions

The former company-name completion was:

```text
企业：幻方量化
END：      量化
```

It proposed **量化**, which the user explicitly rejected. `BUSINESS END`,
`业`, `甲方`, and directly copying `高频交易` were also rejected. None of
those verdicts rejects the mechanically obtained `QI/YE/DE`; they rule out
adding another semantic operation after it.

## 5. Meta positional check

After accepted feeder b4=`PEEP` takes the `PUSA` row formerly assigned to b6,
the unresolved sixth Meta row uses suffix `BO` and needs `O`. Left-align:

```text
BO
CORPORATE
 O
```

The only same-position equal letter is `O` at position 2, exactly the sixth
letter of accepted Meta `PARADOXXING`. The Chinese name proposed for that
audio row has not been independently re-established, so this remains
corroboration rather than the primary derivation.

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
