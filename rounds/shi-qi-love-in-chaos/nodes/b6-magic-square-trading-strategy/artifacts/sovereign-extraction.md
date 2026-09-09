# Rejected extraction: SOVEREIGN

**Verdict (2026-09-03): rejected by the user.** The reproducible calculations
below are retained as negative evidence, but joining them through Enterprise-E
and `class` is not licensed by the puzzle. Do not reuse this candidate or swap
in a nearby synonym/class name without new evidence.

## 1. Verified fill and the numeric high-frequency instruction

Undoing all 57 crossing trades restores the clues. Decomposing every answer
to the slot length and filling each component's frequency within its own
direction makes all 57 crossings agree. Exactly four actual trades have the
maximum value 2 on both sides.

The central depth entry is `END`, filled literally as `E / N / D`; those
letters name East, North and Depth and orient the direction cycle
`横→纵→里→横`. Taking character 2 from the two printed three-Han blocks at
the four double-2 trades, then applying the repaired keyword `反切`, gives:

```text
兔干 / 质锋 / 性忆 / 百味
 TAN / ZHENG / XI / BEI
 弹筝西北
```

The five depth entries are the five strings through the stacked boards.
Plucking the northwest string with the same direction cycle gives:

```text
去一 / 有的 / 的的
 QI / YE / DE
```

Read `QIYE` as `企业`, hence English **ENTERPRISE**. The other repaired
keyword is `END`; the end of the complete Romanized stream `QIYEDE` is `E`.
This branch therefore identifies **Enterprise-E** rather than merely the
generic adjective “corporate”.

## 2. The textual high-frequency trade supplies person and class

Among the 180 repaired three-Han blocks, `关键词` is uniquely most frequent
(two occurrences). Its two actual trade partners are exactly:

```text
古代人 / 的概念
```

The answers to the two keyword-bearing clues are `反切` and `END`. The five
depth answers occupy a quincunx with `END` at the center. Taking the ends of
the four outer answers preserves this square:

```text
路人甲 -> 甲        成精 -> 精

关节   -> 节        氨气 -> 气
```

Fanqie down and up the two columns:

| Direction | Pairs | Result | Required label |
| --- | --- | --- | --- |
| bottom→top | `节甲 / 气精` | `JIA / QING = 嘉庆` | 古代人 |
| top→bottom | `甲节 / 精气` | `JIE / JI = 阶级` | 概念 |

The two extracted labels thus say that the ancient person is **嘉庆** and the
relevant concept is **阶级 / class**. 嘉庆皇帝 was a sovereign.

## 3. Exact convergence

The two branches now give the same English headword without attaching an
arbitrary grid answer:

```text
嘉庆的身份／阶级          -> SOVEREIGN
Enterprise-E's class     -> SOVEREIGN class
```

The second line is the exact class name of the USS Enterprise-E. It also
distinguishes nearby landings:

| Landing | 嘉庆 branch | Enterprise + END(E) + class branch |
| --- | --- | --- |
| `SOVEREIGN` | exact ruler/status | exact Enterprise-E class |
| `ROYALTY` | broad class term | no Enterprise-E class |
| `GALAXY` | no 嘉庆 connection | requires D, contrary to taking the `END` |
| `MOGUL` | only via the incidental answer `权贵` | no Enterprise-E class; rejected |

As a permitted Meta back-check, `BO` and `SOVEREIGN` have exactly one
same-position equal letter, the required `O` at position 2. `SOVEREIGN` does
not itself explain the old row label `怪`; that semantic audio-to-feeder
assignment is known to be stale after b4=`PEEP` and b10=`INFLOOD`, so this is
only a positional check rather than semantic evidence.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 兔干 质锋 性忆 百味 去一 有的 的的 节甲 气精 甲节 精气

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\meta_actual_feeder_audit.py --b6 SOVEREIGN
```

The spatial positions used above are fixed in
`work/visual/canonical/extraction-geometry.png`; its annotation specification
is `work/visual/canonical/extraction-geometry.json`. No online answer or
solution lookup was used.
