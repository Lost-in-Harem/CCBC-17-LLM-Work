# Rejected extraction: MOGUL

**Status: rejected.** The user explicitly reported that `MOGUL` is incorrect.
The reproducible upstream strings `企业的` and `嘉庆 / 阶级` remain useful,
but joining `企业的` to the incidental grid answer `权贵` was not authorized by
the puzzle. The geometric crossing with `权贵[3]=贵` is therefore recorded as
an overfit, and `TYCOON / MAGNATE / POWER BROKER / CORPORATE MOGUL` must not be
substituted for the rejected landing.

## 1. Numeric high-frequency trades give a modifier

The direction-frequency fill has exactly four crossings whose two incidences
both have the maximum value 2. Index character 2 in the two printed three-Han
blocks, orient every pair by the central `E/N/D` direction cycle
`横→纵→里→横`, and apply the repaired clue answer `反切`:

| Indexed pairs | Fanqie stream | Landing |
| --- | --- | --- |
| `兔干 / 质锋 / 性忆 / 百味` | `TAN / ZHENG / XI / BEI` | `弹筝西北` |

The five depth entries are the five strings through the three boards. Pluck
the northwest string and apply the same rule at its three value-1 trades:

```text
去一 / 有的 / 的的
 QI / YE / DE
 企业的
```

The trailing `的` shows that this is a modifier awaiting a noun. The rejected
`CORPORATE` route stopped here; the rejected `CORPORATE STRUCTURE` route added
an independently guessed `骨骼`.

## 2. Textual high-frequency trades identify the noun

Among all 180 repaired three-Han clue blocks, `关键词` is uniquely most
frequent, occurring twice. Its two real trade partners concatenate directly:

```text
古代人 / 的概念 -> 古代人的概念
```

The two keyword-host answers are `END` and `反切`. The five centered depth
answers form four corners around central `END`; taking the ends of the four
outer answers gives:

```text
甲   精

节   气
```

Apply `反切` to the two columns in both directions:

| Direction | Pairs | Result | Template slot |
| --- | --- | --- | --- |
| bottom to top | `节甲 / 气精` | `嘉庆` | 古代人 |
| top to bottom | `甲节 / 精气` | `阶级` | 概念 |

Thus the template becomes `嘉庆的阶级`. This is a precise second clue for the
already filled G2 down answer `权贵`, whose repaired clue is `居高位 / 有权势 /
的人物`. It is not necessary to choose among `ROYALTY/NOBILITY/MONARCH`.

This answer is also geometrically singled out: its third component `贵` is the
G2 planar entry crossing the same northwest depth string selected by
`弹筝西北`. The other branch therefore does not choose a noun arbitrarily from
the fifty answers.

## 3. Rejected join of the two results

```text
企业的 + 权贵 = 企业的权贵
```

The standard one-word English description of a powerful business person is
**MOGUL**. This uses the noun located inside the crossword and the modifier
from the numeric-frequency branch; neither branch is translated in isolation.

As a permitted Meta back-check, left-aligning the remaining suffix `BO` with
the headword gives exactly the needed sixth Meta letter:

```text
BO
MOGUL
 O
```

Nearby business-person answers `TYCOON`, `MAGNATE`, and `BARON` do not produce
`O` in this same-position comparison. The old semantic assignment of the
audio row is not used because accepted b4=`PEEP` and b10=`INFLOOD` invalidate
that table.

## Reproduction

The direction fill and both fanqie stages are reproduced by the existing
parameterized scripts:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 兔干 质锋 性忆 百味 去一 有的 的的 节甲 气精 甲节 精气
```
