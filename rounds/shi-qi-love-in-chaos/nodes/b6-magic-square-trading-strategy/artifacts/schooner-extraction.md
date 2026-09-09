# Rejected candidate extraction: SCHOONER

**Verdict:** Rejected by the Hunt website on 2026-09-03 (“回答错误”).

## 1. Verified crossword and high-frequency instruction

Undoing all 57 three-Han crossing trades restores the clues. Splitting each
answer into the visible components required by its entry length and filling
each component's frequency within its own direction makes all 57 crossings
agree.

The central depth answer `END` fills as `E / N / D`, orienting the three
directions cyclically as East / North / Depth. Exactly four trades have the
maximum value 2 on both sides. Indexing their traded blocks by 2 and applying
the separately restored keyword `反切` gives:

```text
兔干 / 质锋 / 性忆 / 百味
 TAN / ZHENG / XI / BEI
 弹筝西北
```

The five depth entries are five strings through the stacked boards. Plucking
the northwest string and reusing its cell values (all 1) plus the same
direction cycle gives:

```text
去一 / 有的 / 的的
 QI / YE / DE
 企业的 = ENTERPRISE'S
```

## 2. The other high-frequency material supplies the date and lookup field

Among the 180 repaired three-Han blocks, `关键词` is the unique repeated
block. Its two trade partners are `古代人 / 的概念`, and its two host answers
are the operations `反切 / END`.

The five depth answers form a quincunx with `END` in the middle. Taking the
ends of the four outer answers leaves:

```text
甲   精

节   气
```

Fanqie in the two opposite column directions gives exactly:

```text
节甲 / 气精 -> JIA / QING -> 嘉庆   (古代人)
甲节 / 精气 -> JIE / JI  -> 阶级   (概念, CLASS)
```

These are not two independent definitions of a ruler. Together with the
first branch they form a lookup description:

```text
ENTERPRISE'S + [in the time of] JIAQING + CLASS/TYPE
```

The USS *Enterprise* launched in 1799, during the Jiaqing reign, was a
schooner. Its launch-era type therefore supplies the candidate:

```text
SCHOONER
```

This correction uses `嘉庆` to select the historical Enterprise instead of
discarding it after observing that Jiaqing was a sovereign. It also removes
the unlicensed `END(QIYEDE)=E` step that led to the rejected Enterprise-E
class `SOVEREIGN`.

## 3. Checks and disclosed ambiguity

- `SCHOONER` is the canonical initial type of USS *Enterprise* (1799). The
  vessel was rerigged as a brig in 1811, also during the Jiaqing reign; the
  candidate therefore relies on the launch identity rather than an arbitrary
  later state.
- As a permitted Meta positional check, `ZHIWANG / SCHOONER` has exactly one
  same-position match, `N` at position 6, the required tenth letter of the
  accepted Meta. The old semantic clip-to-feeder assignment is known to be
  stale, so this is supporting evidence only.
- No official answer, solution page, or search result was consulted. The
  live puzzle page was used only to read the already unlocked hints and the
  team's own answer log.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 兔干 质锋 性忆 百味 去一 有的 的的 节甲 气精 甲节 精气

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\meta_actual_feeder_audit.py --b6 SCHOONER
```
