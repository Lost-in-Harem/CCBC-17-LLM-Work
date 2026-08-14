# Reproducible extraction

The seven small pictures are in rainbow order and each identifies a colored
Sudoku coordinate. Read the solved digit in each coordinate in that same order.

| Color | Picture identification / number source | Coordinate | Solved digit | Strength |
| --- | --- | --- | --- | --- |
| Red | Richard II portrait headed **Plate 1.4** | `r1c4` | 3 | Strong text-and-image match |
| Orange | Shunchang Museum building; the pictured rooftop feature is section **2.4 “Urban terrace”** | `r2c4` | 9 | Strong text-and-image match |
| Yellow | [World Bank Photo **3.6**](https://documents1.worldbank.org/curated/en/908191600317351237/pdf/Blue-Routes-for-a-New-Era-Developing-Inland-Waterways-Transportation-in-China.pdf), showing inland shipping/locks, plausibly matches the spoken port description | `r3c6` | 7 | Plausible caption match; original puzzle image unavailable |
| Green | Blue Magic card with a flying mythical creature; a 5/5 creature (e.g. **Blue Dragon**) supplies **5/5** | `r5c5` | 1 | Stat fits, exact artwork not confirmed from audio alone |
| Cyan | O2/Faker trophy image: Faker's **5th** Worlds title, final score **3–2** | `r5c3` | 9 | Strong; also fixed by the spoken cyan cell |
| Blue | Tracked landship screenshot from **Airships 6.3** | `r6c3` | 6 | Strong; also fixed by the spoken blue cell |
| Purple | Old **Dota 6.8** screenshot | `r6c8` | 4 | Medium; coordinate is independently fixed by the spoken purple cell |

Thus the rainbow extraction gives the inner lookup key:

```text
r1c4 r2c4 r3c6 r5c5 r5c3 r6c3 r6c8
  3     9     7     1     9     6     4
                    397:1964
```

The user explicitly reported that `397:1964` was rejected as the final answer,
so it must not be resubmitted. It remains a strong intermediate: [ISO/R
397:1964](https://www.iso.org/standard/4397.html) is “Wrapping test for copper
and copper alloy wire,” an exact `___:____` reference. The outer puzzle title
points to *Keep Talking and Nobody Explodes*, whose [official manual names the
matching module **Wires**](https://www.bombmanual.com/web/index.html). Therefore
the current final candidate is:

```text
WIRES
```

`WIRES` uses the official module name. `WIRE` (the singular wording in the ISO
title) and the Simplified-Chinese localization `线路` remain form variants, not
parallel candidates to submit speculatively. If the harbor were misread as
`r3c7`, the intermediate would instead be `393:1964`, an unrelated
asbestos-cement standard.

Run the retained solver from the repository root:

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b4-keep-solving-and-nobody-explodes\artifacts\miracle_sudoku.py --extract r1c4 r2c4 r3c6 r5c5 r5c3 r6c3 r6c8
```

Expected final lines:

```text
unique: True
extract: 3971964 (r1c4=3 r2c4=9 r3c6=7 r5c5=1 r5c3=9 r6c3=6 r6c8=4)
```

## Sources

- [Miracle Sudoku rules and the original two-given puzzle](https://ethmcc.github.io/miracle-sudoku/)
- [Plate 1.4: Portrait of Richard II](https://scalar.missouri.edu/vm/vol1plate4-colorprints)
- [Shunchang Museum — section 2.4 “Urban terrace”](https://www.brazilian-architects.com/zh/uad-zhejiang/project/shunchang-museum)
- [World Bank, *Blue Routes for a New Era* — Photo 3.6](https://documents1.worldbank.org/curated/en/908191600317351237/pdf/Blue-Routes-for-a-New-Era-Developing-Inland-Waterways-Transportation-in-China.pdf)
- [Blue Dragon card — flying, 5/5](https://www.cardkingdom.com/mtg/adventures-in-the-forgotten-realms/blue-dragon)
- [Riot: the 2024 final was held at The O2](https://lolesports.com/en-US/news/your-ticket-guide-to-the-world-final)
- [Riot: Faker's fifth Worlds trophy](https://www.leagueoflegends.com/en-us/news/esports/worlds-2024-winners/)
- [Central News Agency: T1 won 3–2 and Faker earned his fifth title](https://www.cna.com.tw/news/aspt/202411030005.aspx)
- [Airships 6.3 release page and screenshots](https://www.zarkonnen.com/airships/airships_6_3/)
- [ISO/R 397:1964 — Wrapping test for copper and copper alloy wire](https://www.iso.org/standard/4397.html)
- [Official *Keep Talking and Nobody Explodes* manual — Wires](https://www.bombmanual.com/web/index.html)
- [ISO/R 393:1964 alternative, in the asbestos-cement product family](https://www.iso.org/standard/4384.html)
