# Rejected extraction: CONCEPT

**Status: rejected by the user on 2026-08-31.** The mechanical reading below
is retained as negative evidence. It shows that the two host operations can be
paired locally, but the verdict proves that this one-to-one pairing is not the
intended terminal extraction. Do not replace `CONCEPT` with a synonym.

## 1. Select the literal high-frequency traded block

After all 57 crossing trades are undone, the 50 repaired clues contain 180
three-Han blocks and 179 distinct block texts.  The unique repeated block is
`关键词`, with frequency 2.  Its two repaired hosts and the blocks that had
occupied those positions are:

| Repaired host clue | Host answer | Trading partner |
| --- | --- | --- |
| `西十五 / 河海解 / 谜中的 / 关键词` | `反切` | `古代人` |
| `结束本 / 部分的 / 关键词` | `END` | `的概念` |

The two partner blocks concatenate in repaired-host order to the grammatical
check `古代人的概念`.

## 2. Apply each keyword to its own trading partner

`反切` is a two-character operation, so apply it to the first adjacent pair
of its three-character partner, `古代`:

```text
古代 = initial(古) + final-and-tone(代)
     = g + ai4
     = GAI4
```

Apply the other host answer literally to its partner:

```text
END(的概念) = 念 = NIAN4
```

The resulting tone-preserving reading is uniquely lexical in the local Han
dictionary:

```text
GAI4 / NIAN4 = 概念
```

The other adjacent pair in `古代人`, `代人`, gives `DEN2`; the bounded check
finds no `DEN2/NIAN4` entry.  The full partner phrase already ends in `概念`,
so it independently disambiguates the homophone rather than requiring a
semantic synonym choice.

The Round's feeder answers are submitted in English.  The direct English
noun for `概念` is therefore:

```text
CONCEPT
```

## 3. Checks and disclosed limitation

- `CONCEPT` is not a replacement synonym for the rejected `PERSPECTIVE`:
  `概念` is produced character by character before translation.
- In the accepted Meta's still-unresolved positional audit, `BO` and
  `CONCEPT` have exactly one same-position match, the required second-position
  `O`.  This is corroboration only; accepted b10=`INFLOOD` proves the old Meta
  proxy table cannot determine feeder spellings on its own.
- The four value-2/value-2 component crossings are essential checks on the
  direction-frequency fill, but their 384 possible order/orientation streams
  contain no four-Han local-dictionary match.  Their previously selected
  cyclic readings led to rejected `CORPORATE` and `WEEKEND`, so they are not
  reused to choose this candidate.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high_frequency.py `
  --input rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --output rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high-frequency-audit-current.md

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 古代 代人

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --reading gai4 nian4 --reading-exact
```

Expected final check: one match, `概念 gai4/nian4`.
