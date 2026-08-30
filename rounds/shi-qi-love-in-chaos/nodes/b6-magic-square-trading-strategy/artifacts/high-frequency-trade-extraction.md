# High-frequency trade extraction

## 1. Select the four repeated-frequency trades

The fixed component ledger in `direction-frequency-solution.json` fills every
cell with the frequency of its component inside its own direction (`横`, `纵`,
or `里`).  All 57 crossings agree.  Exactly four geometric clue-block trades
have value 2.  Since every traded block has three Han characters, value 2
selects the middle character on each side:

| Order | Crossing | Restored traded blocks | Middle pair | Fanqie |
| ---: | --- | --- | --- | --- |
| 1 | G1 r06c12 | `在干活` / `吃兔子` | 干 / 兔 | `GU` |
| 2 | G1 r08c02 | `地质学` / `雷锋是` | 质 / 锋 | `ZHENG` |
| 3 | G1↔里 r10c10 | `气性不` / `记忆中` | 性 / 忆 | `XI` |
| 4 | G3↔里 r10c10 | `六百号` / `的味道` | 百 / 味 | `BEI` |

Each trade pair permits two fanqie orientations.  After excluding invalid
Mandarin combinations, eight combinations remain; the only continuous
natural phrase is:

```text
GU / ZHENG / XI / BEI  ->  古筝 / 西北
```

## 2. Read the two maximum-frequency keyword blocks

Among all 180 restored three-Han blocks, only `关键词` repeats.  Its two host
clues answer `反切` and `BREAK`, supplying the phonetic operation above and a
split between `古筝` and `西北`.  The two blocks traded against `关键词`, in
restored-row order, are:

```text
古代人 / 的概念  ->  古代人的概念
```

This is the definition for the final landing.

## 3. Use the ancient five-tone/direction correspondence

`古筝` fixes the relevant ancient domain as the five tones.  In the
traditional five-tone/five-direction correspondence:

| Direction | East | South | Center | West | North |
| --- | --- | --- | --- | --- | --- |
| Tone | 角 | 徵 | 宫 | 商 | 羽 |

Therefore `西北` maps in its stated order to `商羽`.  Reading the pair in the
two directions available to a trade gives:

| Pair | Fanqie construction | Toneless syllable |
| --- | --- | --- |
| 商羽 | `sh-` from 商 + `-u` from 羽 | `SHU` |
| 羽商 | `y-` from 羽 + `-ang` from 商 | `YANG` |

A bounded scan of the local two-Han dictionary for `SHU/YANG` in either order
returns only `杨树、输氧、沭阳、样书、阳数、杨淑`.  Only **阳数** means an
ancient concept: in the traditional yin-yang classification, odd numbers are
yang numbers.  The extracted definition fixes both character choice and
order:

```text
YANG / SHU  ->  阳数
```

The candidate answer is **阳数**.

## Controls

- `古筝→弦、西北→乾、弦乾→闲钱` used two unrelated conversion systems and
  an extra homophone; the user explicitly rejected `闲钱`.
- Selecting a northwest or southeast depth answer produced the explicitly
  rejected `路人甲` and `氨气`.
- Indexing all fifteen planar/depth crossings gives fixed pair streams with
  several invalid syllables in both global orientations; that negative audit
  is in `work/visual/depth-character-state-audit.md`.

## Reproduction

Validate the direction-local frequency fill and list the four value-2 trades:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\component_crossword.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --render-direction-fill rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json
```

Reproduce `关键词×2 -> 古代人的概念`:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high_frequency.py `
  --input rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --output rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\high-frequency-audit-current.md
```

Reproduce both `商羽` fanqie syllables and the bounded local landing scan:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --two-way-pair 商羽
```
