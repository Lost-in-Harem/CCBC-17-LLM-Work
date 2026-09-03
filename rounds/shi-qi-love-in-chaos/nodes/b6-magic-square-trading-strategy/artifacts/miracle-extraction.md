# Rejected recursive extraction: 奇迹

**Status: rejected.** After rejecting the English strings `WONDER` and
`MIRACLE`, the user explicitly rejected the literal Chinese `奇迹` on
2026-08-31. This closes the recursive step that takes the ends of
`嘉庆/阶级；嘉靖/节气` and fanqies them again. The upstream 2×2 square and its
two checked `古代人 / 概念` pairs remain reproducible.

## 1. Select the literal highest-frequency traded block

Undoing all 57 crossing trades restores 50 clues containing 180 three-Han
block occurrences and 179 distinct texts. The unique repeated block is
`关键词`; its hosts and the blocks traded against it are:

| Repaired host | Host answer / operation | Trade partner / label |
| --- | --- | --- |
| `西十五 / 河海解 / 谜中的 / 关键词` | `反切` | `古代人` |
| `结束本 / 部分的 / 关键词` | `END` | `的概念` |

Thus the literal “高频交易” supplies two operations, `反切/END`, and two
column labels, `古代人 / 的概念`.

## 2. Use the central END on the depth answers

The five coordinates open on all three boards form four corners and a center:

```text
NW 路人甲       NE 成精

            END

SW 关节         SE 氨气
```

Take the end of each outer **answer**. This yields:

```text
甲   精

节   气
```

The northeast character is `精` from the answer `成精`, not the last-layer
component `青`.

## 3. Read two rows under the supplied labels

The square has a direct row reading:

```text
甲精 -> JIA/JING -> 嘉靖    (古代人)
节气 -> 节气               (概念)
```

Apply the other operation, `反切`, to each column in both directions:

| Direction | Pairs | Tone-preserving result | Label |
| --- | --- | --- | --- |
| bottom to top | `节甲 / 气精` | `JIA3 / QING1 -> 嘉庆` | 古代人 |
| top to bottom | `甲节 / 精气` | `JIE2 / JI4 -> 阶级` | 概念 |

The labels therefore check two complete rows:

```text
嘉靖 | 节气
嘉庆 | 阶级
```

## 4. Apply END and fanqie to the checked rows

Take the two word ends in each row and fanqie them. Put the fanqie-derived row
first, matching the statement order of the two keyword hosts (`反切`, then
`END`):

| Row | Ends | Fanqie |
| --- | --- | --- |
| `嘉庆 / 阶级` | `庆级` | `QI2` |
| `嘉靖 / 节气` | `靖气` | `JI4` |

The tones discriminate the order and landing:

```text
QI2 / JI4 = 奇 / 迹 = 奇迹
```

The reverse order does not form an ordinary word with those tones; `机器`
would require `JI1/QI4`.

## 5. Exact answer form and the failed English substitutions

The repeated operation mechanically produces the Han string `奇迹`, but the
user has now rejected that exact string as well as both English translations.
The old Meta table cannot rescue the route: accepted b10=`INFLOOD` has no
target overlap with `ZHIWANG`, and that row works only after replacing the
real answer by the semantic proxy `CURRENT`. The following is retained only
as rejected evidence:

```text
奇迹
```

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 节甲 气精 甲节 精气 庆级 靖气

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\meta_actual_feeder_audit.py --b6 MIRACLE
```

Expected local terminal syllables: `庆级=QI2`, `靖气=JI4`. The Meta audit is
expected **not** to assign `MIRACLE` to clip 6; that negative result is the
reason the obsolete Meta spelling constraint is no longer used.
