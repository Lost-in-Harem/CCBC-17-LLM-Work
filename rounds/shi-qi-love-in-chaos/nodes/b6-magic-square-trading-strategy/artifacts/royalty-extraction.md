# Superseded partial extraction: ROYALTY

**Status: superseded without submission on 2026-09-03.** The column reading
`嘉庆/阶级` is retained, but `ROYALTY` explains only its broad royal-class
sense. It cannot also name the class of Enterprise-E. The later `MOGUL` route
that attached `企业的` to the incidental grid answer `权贵` was explicitly
rejected; the exact two-branch convergence is documented in
`sovereign-extraction.md`.

## 1. Find the highest-frequency traded block

After all 57 crossing trades are undone, the 50 clues contain 180 three-Han
block occurrences but 179 distinct block texts. The unique repeated block is
`关键词`, occurring twice. Its repaired hosts and the blocks occupying those
sites before the trades are:

| Repaired host | Host answer | Trade partner |
| --- | --- | --- |
| `西十五 / 河海解 / 谜中的 / 关键词` | `反切` | `古代人` |
| `结束本 / 部分的 / 关键词` | `END` | `的概念` |

Thus “高频交易” identifies one high-frequency block and its two trades. The
partners concatenate without modification to the single fill template
`古代人的概念`, while the two host answers globally supply the operations
`反切` and `END`.

## 2. Apply END to the four outer depth answers

Hint 3 makes the five common coordinates into depth entries. In the centered
square they form four corners plus a center:

```text
NW 路人甲       NE 成精

            END

SW 关节         SE 氨气
```

The center entry is the operation `END`. Take the end Han character of each
outer **answer** (not the last-layer component of its decomposition):

```text
甲   精

节   气
```

This distinction matters at the northeast corner: the answer is `成精`, so
its end is `精`; its G3 grid component is only the visible subcomponent `青`.

## 3. Use fanqie in both directions down the columns

The other repaired keyword is `反切`: take the initial of the first character
and the final (with tone) of the second. Reading the two columns in opposite
directions gives:

| Direction | Pairs | Fanqie | Landing | Template slot |
| --- | --- | --- | --- | --- |
| bottom to top | `节甲 / 气精` | `JIA3 / QING1` | `嘉庆` | `古代人` |
| top to bottom | `甲节 / 精气` | `JIE2 / JI4` | `阶级` | `的概念` |

The two slots in the concatenated template select the column pairing without
guessing. Row pairing produces `JING/JI`; diagonal pairing produces the
already rejected `JI/JIE`. Only the columns, read both ways, simultaneously
produce an ancient person and a concept.

Substituting the two mechanically obtained words into the partner phrase gives
an intermediate clue:

```text
古代人 的 概念
 嘉庆  的 阶级
```

The former route translated this immediately as **ROYALTY**. That stop was too
early: the other high-frequency branch retains `QIYEDE`, where
`QIYE=企业=ENTERPRISE` and the string's `END` is `E`. Only `SOVEREIGN` both
describes 嘉庆 as a ruler and names Enterprise-E's exact class.

## 4. Historical Meta check

With the accepted feeders installed, the spelling is compatible with the
still-unresolved clip 6 positional row:

```text
BO
ROYALTY
 O
```

The sole same-position match is `O` at position 2, the sixth character of the
accepted Meta `PARADOXXING`. The old semantic name assigned to that audio row
was speculative, and accepted b10=`INFLOOD` does not complete the old feeder
table. This could not distinguish `ROYALTY` from every answer-form synonym and
does not supply the exact Enterprise-E class name, so it no longer supports a
candidate.

## Reproduction

The two directional fanqie readings are reproduced by:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 节甲 气精 甲节 精气
```

Expected outputs are `JIA/QING/JIE/JI` with tones `3/1/2/4`.

The Meta positional check is reproduced by:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\meta_actual_feeder_audit.py --b6 ROYALTY
```
