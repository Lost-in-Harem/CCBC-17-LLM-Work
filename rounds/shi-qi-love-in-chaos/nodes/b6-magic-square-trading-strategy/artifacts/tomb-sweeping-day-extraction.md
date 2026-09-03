# Rejected extraction: TOMB SWEEPING DAY

**Status: rejected.** The user explicitly rejected `TOMB SWEEPING DAY` on
2026-08-31. The `BO` position match from the incomplete Meta cannot determine
this feeder's answer form. A subsequent local pairing audit retains the direct
Han candidate `嘉庆的节气→清明` without Meta assistance; see
`artifacts/qingming-extraction.md`. No alternate English name is restored.

## 1. Highest-frequency trades supply paired instructions

After all 57 crossing trades are undone, `关键词` is the unique repeated
three-Han block among 180 occurrences. Its two repaired hosts and their
individual trade partners are:

| Host answer | Trade partner |
| --- | --- |
| `反切` | `古代人` |
| `END` | `的概念` |

The pairing in this table is evidence: the two partner labels must not be
detached from the operations that traded with them.

## 2. Use the five depth answers in their fixed coordinates

The central depth answer `END` acts on the four outer depth answers:

```text
NW 路人甲 → 甲        NE 成精 → 精

                    END

SW 关节   → 节        SE 氨气 → 气
```

The four ends therefore form the fixed square:

```text
甲   精
节   气
```

Direct rows provide `嘉靖 / 节气`; applying `反切` down the columns in both
directions provides `嘉庆 / 阶级`.

## 3. Preserve each operation's original trade partner

Each family contains one ancient person and one concept. The original trade
pairings select across the two families:

```text
反切 ↔ 古代人  : choose 嘉庆 from 嘉庆 / 阶级
END  ↔ 的概念  : choose 节气 from 嘉靖 / 节气
```

This yields the exact final clue:

```text
嘉庆的节气
```

The rejected `奇迹` route instead paired outputs within each family and then
reused `END/反切` without a new instruction.

`嘉庆` ends in the syllable `QING`. Of the 24 solar terms, only `清明` begins
with that homophonically matching syllable. The local Chinese landing is
therefore `清明`.

## 4. Meta-assisted answer form

Every currently accepted feeder in this Round has a Latin-letter answer.
The user authorized a Meta backsolve; the still unresolved clip-6 suffix is
`BO`, whose required extracted letter is `O`. The common English name of
`清明` that satisfies this positional constraint is `TOMB SWEEPING DAY`:

```text
BO
TOMBSWEEPINGDAY
 O
```

The sole same-position match is `O` at position 2. The alternative forms
`QINGMING`, `PURE BRIGHTNESS`, and `CLEAR AND BRIGHT` do not satisfy that
row. Since accepted b10=`INFLOOD` still leaves the old Meta table incomplete,
this positional check fixes answer form but is not treated as an independent
proof of the local extraction.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 节甲 气精 甲节 精气

python rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\meta_actual_feeder_audit.py --b6 "TOMB SWEEPING DAY"
```

Expected local outputs are `嘉庆 / 阶级` and `嘉靖 / 节气`; expected Meta
overlap is clip 6 `BO`, position 2 `O` only.
