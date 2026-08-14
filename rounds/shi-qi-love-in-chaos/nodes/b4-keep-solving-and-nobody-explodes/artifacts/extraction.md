# Rejected coordinate hypothesis

This file preserves the former `397:1964` route so it can be audited without
being repeated. Both `397:1964` and the derived guess `WIRES` were explicitly
rejected by the user. None of the seven rows below should now be treated as a
complete verified image chain; see `solution.md` for the full manual checklist.

| Color | Picture identification / number source | Coordinate | Solved digit | Strength |
| --- | --- | --- | --- | --- |
| Red | Former guess: Richard II portrait headed **Plate 1.4** | `r1c4` | 3 | Generic spoken match only; exact image unavailable |
| Orange | Former guess: Shunchang Museum section **2.4 “Urban terrace”** | `r2c4` | 9 | Generic spoken match only; exact image unavailable |
| Yellow | [World Bank Photo **3.6**](https://documents1.worldbank.org/curated/en/908191600317351237/pdf/Blue-Routes-for-a-New-Era-Developing-Inland-Waterways-Transportation-in-China.pdf), a three-panel inland-shipping/lock image | `r3c6` | 7 | Weak: not an obvious single port image; exact source unavailable |
| Green | Blue Magic card with a flying mythical creature; a 5/5 creature (e.g. **Blue Dragon** or **Keiga**) supplies **5/5** | `r5c5` | 1 | Weak and non-unique; exact artwork unavailable |
| Cyan | O2/Faker trophy image: Faker's **5th** Worlds title, final score **3–2** | `r5c3` | 9 | Strong; also fixed by the spoken cyan cell |
| Blue | Former guess: tracked landship screenshot from **Airships 6.3** | `r6c3` | 6 | Rejected source match: official chronology places tracked landships after 6.3; the cell itself is fixed by audio |
| Purple | Former guess: old **Dota 6.8** screenshot | `r6c8` | 4 | Rejected source match: the located page shows Invoker, not the spoken green female character; the cell itself is fixed by audio |

Thus the rejected coordinate hypothesis produced:

```text
r1c4 r2c4 r3c6 r5c5 r5c3 r6c3 r6c8
  3     9     7     1     9     6     4
                    397:1964
```

The exact [ISO/R 397:1964](https://www.iso.org/standard/4397.html) match was
post-hoc evidence, not an independent picture identification. Inferring
`WIRES` from that standard and the puzzle title added an unsupported semantic
step; the user explicitly rejected it on 2026-08-15. Do not submit
`397:1964`, `WIRES`, `WIRE`, `线路`, or `WRAPPING TEST` from this route.

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
- [Airships 6.3 release page](https://www.zarkonnen.com/airships/airships_6_3/) — retained as a rejected source match
- [Later Airships tracked-landship development](https://www.zarkonnen.com/airships/landcruisers)
- [ISO/R 397:1964 — Wrapping test for copper and copper alloy wire](https://www.iso.org/standard/4397.html)
- [Official *Keep Talking and Nobody Explodes* manual — Wires](https://www.bombmanual.com/web/index.html)
- [ISO/R 393:1964 alternative, in the asbestos-cement product family](https://www.iso.org/standard/4384.html)
