# Rejected extraction: 清明

**Status:** rejected by the user on 2026-08-31. This artifact is retained only
to reproduce the closed route; neither `清明` nor any Chinese/English synonym
may be restored without genuinely new evidence.

## Fixed local mechanics

After all 57 three-Han clue-block trades are undone, the unique repeated
block `关键词` occurs in two repaired hosts. The host answers and the blocks
actually traded with those occurrences are fixed:

| Host answer | Actual trade partner |
| --- | --- |
| `反切` | `古代人` |
| `END` | `的概念` |

The five centered depth answers occupy four corners and a center. Applying
the central answer `END` to the four outer **answers** gives:

```text
甲   精
节   气
```

Direct row readings form the END family `嘉靖 / 节气`. Bidirectional fanqie
down the columns forms the fanqie family `嘉庆 / 阶级`.

## Preserve the two actual trade pairings

Each family contains exactly one ancient person and one concept. The original
one-to-one trade partners therefore select uniquely:

| Keyword host | Partner category | Selected family member |
| --- | --- | --- |
| `反切` | `古代人` | `嘉庆` |
| `END` | `的概念` | `节气` |

Keeping the repaired-host order, including the literal leading `的` in the
second partner block, yields:

```text
嘉庆的节气
```

The final syllable of `嘉庆` is `QING`. In the fixed set of 24 solar terms,
the unique term beginning with the homophonically matching `QING` is `清明`.
The route formerly proposed the direct Han landing:

```text
清明
```

## Rejected answer-form extension

The user explicitly rejected `TOMB SWEEPING DAY`. That form depended on an
incomplete Meta position match and is not restored here. This candidate does
not use the Meta or translate the locally extracted Han string.

## Reproduction

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --pairs 节甲 气精 甲节 精气
```

Expected toneless syllables are `JIA / QING / JIE / JI`, giving the two
label-checked column readings `嘉庆 / 阶级`; the direct rows give
`嘉靖 / 节气`.
