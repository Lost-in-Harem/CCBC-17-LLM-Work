# Rejected highest-frequency-block route: 谷歌 / GOOGLE

The user explicitly rejected both `谷歌` and `GOOGLE`.  This artifact retains
the reproducible `GU/GE` observation but no longer treats every non-Google
landing as unsupported: comparison with the printed state now gives the exact
pair `GUAN/DUAN=关断` and repaired `GU/GE≈骨骼`. The rejected `CONCUBINE` route
used the host `反切` and the complete partners `古代人 / 的概念` as a type
constraint. A later attempt joined `GU/GE` to the independent
`QI/YE/DE=企业的` stream as `企业的骨骼`, but the user rejected
`CORPORATE STRUCTURE`; both semantic landings are now closed.

The former four-value-2 shell route produced the user-rejected intermediates
`嬴政 / 外滩` and then the user-rejected candidate `杜月笙`.  The phrase
“高频交易” has a more literal and more tightly anchored reading: find the
highest-frequency repaired clue block and inspect the trades made by that
block.

## 1. The unique highest-frequency block

After all 57 crossing trades are undone, the 50 clues contain 180 three-Han
block occurrences and 179 distinct texts.  Exactly one block occurs twice:

| Block | Frequency | Repaired host | Host answer |
| --- | ---: | --- | --- |
| `关键词` | 2 | `G1-A07.4` | `反切` |
| `关键词` | 2 | `I05.3 / Z03.3` | `END` |

The first host supplies the operation.  The second says that this is the end
of the extraction rather than another answer to follow.

## 2. Inspect its two trades

At each repaired host, put the selected high-frequency block first and the
block it traded with second.  The direction-local component-frequency fill
gives value 1 at both crossing cells, so index character 1 of both three-Han
blocks:

| Order | Repaired host | Crossing | High-frequency block | Trade partner | Cell value | Indexed pair | Fanqie |
| ---: | --- | --- | --- | --- | ---: | --- | --- |
| 1 | `G1-A07.4` | G1 r07c12 / edge 12 | `关键词` | `古代人` | 1 | `关古` | `GU` |
| 2 | `I05.3` | G3 r06c07 / edge 51 | `关键词` | `的概念` | 1 | `关的` | `GE` |

The order is fixed by the repaired hosts in statement order: the G1 across
host precedes the final depth host.  The orientation is also fixed: the
selected high-frequency block is the object whose two trades are being
examined, so it precedes its partner in each pair.

The referenced CCBC 15 “河海解谜” explicitly establishes fanqie as the
operation and allows tone changes.  Thus the fixed reading is:

```text
GU / GE
```

## 3. Rejected landing

Toneless `GU/GE` has multiple possible spellings, including `骨骼`. The
former Google route tried to resolve the homophone from the repeated block
`关键词`, because keywords can be submitted to Google searches.  It proposed:

```text
谷歌
```

The user rejected both this Chinese spelling and `GOOGLE`. The semantic step
was therefore not a valid disambiguator. `GU/GE` alone also did not justify
switching to another homophone such as `骨骼`. The later independent
`QI/YE/DE` stream made `企业的骨骼` linguistically natural, but the explicit
rejection of `CORPORATE STRUCTURE` shows that natural completion was not an
authorized extraction. The later `企业的 + 权贵 -> MOGUL` join was rejected as
well. The current route instead keeps each complete trade partner, yielding
the labels `古代人 / 的概念` without an extra character index.

No online answer or solution lookup was used.

## Reproduction

Reproduce the unique repeated block and its two partners:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high_frequency.py `
  --input rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --output rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high-frequency-audit-current.md
```

Reproduce the numeric fill and verify that edges 12 and 51 both have value 1:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --report rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md `
  --all-character-pairs rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

Reproduce the two fanqie pairs:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 关古 关的
```
