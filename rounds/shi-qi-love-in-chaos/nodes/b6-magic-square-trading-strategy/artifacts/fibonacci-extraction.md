# Rejected Fibonacci extraction

> The user explicitly rejected **斐波那契数列** on 2026-08-30.  More
> importantly, the central depth clue should answer `END`, which fits its
> three cells directly; the `BREAK -> B/RE/AK` grouping used below was an
> unsupported merger.  This file is retained only as negative evidence.

The rejected route treated `DAMAGE`, `易伤`, and `BREAK` as intermediate
controls in one deterministic path and named the resulting numeric pattern
as the Fibonacci sequence.  The submission verdict and corrected `END` fill
invalidate that landing.

## 1. The first edge is located, not guessed

The three fixed underlines give `DA / MI / JI = DAMAGE`.  In all 50 repaired
clues, the only literal Chinese counterpart is the middle block of:

```text
发生后 / 伤害数 / 字变大  ->  易伤
```

Thus `DAMAGE` identifies `伤害数`, block 2 of the entry answered by `易伤`.
That block is one endpoint of trade edge 35 at `G3 r06c05`; no answer-length
rule is needed to choose the initial edge.

## 2. The filled crossing supplies the seeds

The direction-frequency fill gives value 1 to both incidences at edge 35:

| Edge / coordinate | Incidence | Repaired block | Filled value |
| --- | --- | --- | ---: |
| 35 / G3 r06c05 | `G3-D03[2]`, answer `易伤` | `伤害数` | 1 |
| 35 / G3 r06c05 | `G3-A05[1]`, answer `ζ电势` | `物理化` | 1 |

These are the two initial terms `1,1`.  Adding adjacent terms then gives the
successive written answer lengths and the block positions needed to continue
the same trade walk:

| Fibonacci step | Current answer | Written length / selected block | Trade target |
| --- | --- | --- | --- |
| `1+1=2` | 易伤 | 2: `伤害数` | ζ电势 |
| `1+2=3` | ζ电势 | 3: `的概念` (edge 51, `G3 r06c07`) | BREAK |
| `2+3=5` | BREAK | 5 Latin letters; its depth entry has only 3 cells | stop |

The complete numeric readout is therefore:

```text
1, 1, 2, 3, 5
```

`BREAK` is both the answer to “结束本部分的关键词” and the exact point where
the next index no longer fits the three-cell entry.  It terminates the
extraction instead of sending it around the previously rejected loop.

## 3. Finite control

`work/answer_trade_graph.py` checks all 50 answer nodes.  Only two graph
sources have a five-term Fibonacci prefix when the first crossing's two
direction-frequency values are used as seeds:

```text
易伤 -> ζ电势 -> BREAK    1,1,2,3,5
元音 -> ζ电势 -> BREAK    1,1,2,3,5
```

The preceding `DAMAGE` locator selects the former uniquely: only the `易伤`
row contains `伤害`, whereas the `元音` row does not.

The algorithm-engineer flavor confirms the recurrence, while the trading
title is consistent with Fibonacci-based trading terminology.  The sequence
itself is mechanically present; no retracement ratios or separate operation
are supplied, so the direct answer is **斐波那契数列**.

## Reproduction

From the repository root:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\answer_trade_graph.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --report rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings.md `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --components rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json `
  --output rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\answer_trade_graph.md
```

The final report section prints the anchor stream and every graph source with
an exact Fibonacci prefix of at least five terms.
