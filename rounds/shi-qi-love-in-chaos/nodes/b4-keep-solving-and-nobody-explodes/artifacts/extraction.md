# Coordinate extraction audit

The current seven-image coordinate chain is:

| Color | Image identification | Number source | Coordinate | Solved digit |
| --- | --- | --- | --- | --- |
| Red | Richard II portrait | page title **Plate 1.4** | `r1c4` | 3 |
| Orange | Shunchang Museum rooftop | section **2.4 Urban terrace** | `r2c4` | 9 |
| Yellow | Luzhou port construction | caption **Photo 3.4** | `r3c4` | 6 |
| Green | *Dream Eater*, a blue mythic flying Nightmare Sphinx | printed power/toughness **4/3** | `r4c3` | 3 |
| Cyan | Faker lifting the trophy at the O2 | fifth Worlds title; T1 won three games | `r5c3` | 9 |
| Blue | Morden's Battleship | Mission **6** of *Metal Slug 3D* | `r6c3` | 6 |
| Purple | green Medusa image on the Dota patch page | version **6.80**, with the zero discarded for a 1–9 grid | `r6c8` | 4 |

Read in the spoken rainbow order, the coordinates and digits are:

```text
red     orange  yellow  green   cyan    blue    purple
r1c4    r2c4    r3c4    r4c3    r5c3    r6c3    r6c8
3       9       6       3       9       6       4
                       396:3964
```

Run the retained solver from the repository root:

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b4-keep-solving-and-nobody-explodes\artifacts\miracle_sudoku.py --extract r1c4 r2c4 r3c4 r4c3 r5c3 r6c3 r6c8
```

Expected final lines:

```text
unique: True
extract: 3963964 (r1c4=3 r2c4=9 r3c4=6 r4c3=3 r5c3=9 r6c3=6 r6c8=4)
```

The bottom answer pattern is `___:____`, and the user explicitly clarified that
the extracted digits themselves are the answer. Therefore no ISO lookup or word
extraction follows this table.

## Corrections to the rejected 397:1964 chain

| Image | Rejected match | Why it was wrong | Corrected match |
| --- | --- | --- | --- |
| 3 / yellow | World Bank **Photo 3.6**, a three-panel set of barges and locks | It was selected after noticing that `397:1964` matched an ISO number; visually it is not a single port. | **Photo 3.4 — Construction of Luzhou port**, a single port image with a crane and pier. |
| 4 / green | *Blue Dragon*, **5/5** | It is uncommon, obviously a dragon, and was not uniquely supported by the spoken description. | *Dream Eater*, a blue mythic flying Nightmare Sphinx with a bat-like silhouette, **4/3**. |

Those two changes turn:

```text
r1c4 r2c4 r3c6 r5c5 r5c3 r6c3 r6c8 -> 397:1964 (rejected)
```

into:

```text
r1c4 r2c4 r3c4 r4c3 r5c3 r6c3 r6c8 -> 396:3964 (candidate)
```

The exact ISO/R 397:1964 hit was post-hoc coincidence, not independent image
evidence. `WIRES` and `COPPER` were explicitly rejected; `WRAPPING` was an
unsubmitted guess that was withdrawn when the user clarified the numeric
mechanism.

## Sources

- [Miracle Sudoku rules and the original two-given puzzle](https://ethmcc.github.io/miracle-sudoku/)
- [Plate 1.4: Portrait of Richard II](https://scalar.missouri.edu/vm/vol1plate4-colorprints)
- [Shunchang Museum — section 2.4 “Urban terrace”](https://www.world-architects.com/de/uad-zhejiang/project/shunchang-museum)
- [World Bank, *Blue Routes for a New Era* — Photo 3.4](https://documents1.worldbank.org/curated/en/908191600317351237/pdf/Blue-Routes-for-a-New-Era-Developing-Inland-Waterways-Transportation-in-China.pdf)
- [*Dream Eater* — flying, mythic, 4/3](https://scryfall.com/card/grn/38/dream-eater)
- [Riot photo: Faker at the 2024 Worlds final in the O2](https://www.flickr.com/photos/lolesports/54112369706)
- [T1 won the final 3–2 and Faker earned his fifth title](https://www.cna.com.tw/news/aspt/202411030005.aspx)
- [Morden's Battleship — Mission 6 boss in *Metal Slug 3D*](https://metalslug.fandom.com/wiki/Morden%27s_Battleship)
- [Dota 6.80 analysis page containing the Medusa image](https://game8review.blogspot.com/2014/01/dota-680-changelog-reviewanalysis.html)
