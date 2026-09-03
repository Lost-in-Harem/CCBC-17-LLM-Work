# Rejected Meta translation: WONDER

**Status: rejected.** The user explicitly rejected `WONDER` on 2026-08-31.
The local recursive extraction through `QI2/JI4 = 奇迹` remains reproducible,
but the user later rejected the literal Chinese result as well as both English
translations. In particular,
accepted b10=`INFLOOD` also needs the non-answer proxy `CURRENT` in that old
Meta table, so positional overlap cannot determine a feeder's submitted word.
See `artifacts/qingming-extraction.md` for the current paired-trade
candidate.

## 1. The highest-frequency block supplies two labels and two operations

After all 57 three-Han crossing trades are undone, the 50 clues contain 180
block occurrences but 179 distinct texts. The unique repeated/highest-
frequency block is `关键词`. Its two repaired hosts and trade partners are:

| Repaired host | Host answer | Trade partner |
| --- | --- | --- |
| `西十五 / 河海解 / 谜中的 / 关键词` | `反切` | `古代人` |
| `结束本 / 部分的 / 关键词` | `END` | `的概念` |

Thus the literal “高频交易” gives the template `古代人的概念` and the two
operations `反切/END`. Indexing the first characters of these complete labels
into `GU/GE` was the rejected GOOGLE route and is not used.

## 2. END the four outer depth answers

Hint 3 creates five depth entries at four corners and the center:

```text
NW 路人甲       NE 成精

            END

SW 关节         SE 氨气
```

Use the central answer `END` on the four outer **answers**:

```text
甲   精

节   气
```

The northeast end is `精` from the answer `成精`, not the last-layer visible
component `青`.

## 3. The square contains two instances of “古代人的概念”

Read the rows directly:

- `甲精` has toneless reading `JIA/JING`, landing as the historical person
  `嘉靖`;
- `节气` is already a concept.

Now use the other keyword `反切` on the two columns in both directions:

| Direction | Pairs | Fanqie | Result | Type |
| --- | --- | --- | --- | --- |
| bottom to top | `节甲 / 气精` | `JIA / QING` | `嘉庆` | 古代人 |
| top to bottom | `甲节 / 精气` | `JIE / JI` | `阶级` | 概念 |

The four ends therefore create two checked instances of the exact trade-
partner template:

```text
嘉靖 的 节气
嘉庆 的 阶级
```

This second instance is why stopping at `嘉庆的阶级 -> ROYALTY` is premature:
it ignores the equally exact row instance.

## 4. Repeat END and fanqie on the two instances

Take the ends of the ancient-person word and concept word in each instance:

| Instance | Ends | Fanqie |
| --- | --- | --- |
| fanqie-derived `嘉庆 / 阶级` | `庆级` | `QI2` |
| direct-row `嘉靖 / 节气` | `靖气` | `JI4` |

There are only two possible group orders. `QI2/JI4` preserves both fanqie
tones and lands exactly as:

```text
QI2 / JI4 = 奇 / 迹 = 奇迹
```

The reverse `JI4/QI2` has no ordinary two-Han landing with those tones;
`机器` would require `JI1/QI4`, so it is not a tone-preserving alternative.

## 5. Rejected Meta disambiguation

This route claimed that clip 6 (`怪`, suffix `BO`) fixed `WONDER`:

```text
BO
WONDER
 O
```

The same-position `O` is real, but the conclusion is not. The user rejected
`WONDER`, and the old Meta mapping is known to use semantic proxy words rather
than every accepted feeder answer: b10=`INFLOOD` has no target overlap with
`ZHIWANG`, whereas its old proxy `CURRENT` does. This section is therefore a
failed backsolve, not answer-form evidence.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 节甲 气精 甲节 精气 庆级 靖气

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\meta_actual_feeder_audit.py --b6 WONDER
```

Expected terminal syllables: `庆级=QI2`, `靖气=JI4`; expected Meta overlap:
clip 6 `BO`, position 2 `O` only.
