# Extraction audit: `ANS:MENU` candidate

## Reproducible calculation

The Miracle Sudoku with givens `r5c3=9` and `r6c7=8` has the unique solution
recorded by `miracle_sudoku.py`.  Under the current seven-cell reconstruction,
the spoken rainbow order gives:

```text
red     orange  yellow  green   cyan    blue    purple
r1c4    r2c4    r3c4    r3c2    r5c2    r6c3    r6c8
3       9       6       5       4       6       4
                       396:5464
```

Run from the repository root:

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b4-keep-solving-and-nobody-explodes\artifacts\miracle_sudoku.py --extract r1c4 r2c4 r3c4 r3c2 r5c2 r6c3 r6c8
```

Expected final lines:

```text
unique: True
extract: 3965464 (r1c4=3 r2c4=9 r3c4=6 r3c2=5 r5c2=4 r6c3=6 r6c8=4)
```

Treat the seven digits as one-based indices into normalized English proper
names (uppercase, spaces and punctuation deleted):

| # / color | Picture candidate | Coordinate evidence | Digit | Index result | Confidence |
| --- | --- | --- | ---: | --- | --- |
| 1 / red | King **Charles** | `r1c4` is reconstructed, not heard | 3 | `CHARLES[3]=A` | weak until portrait comparison |
| 2 / orange | **Sky Garden** rooftop | `r2c4` is reconstructed, not heard | 9 | `SKYGARDEN[9]=N` | weak until building comparison |
| 3 / yellow | Port of **Santos** | `r3c4` is reconstructed, not heard | 6 | `SANTOS[6]=S` | weak until port comparison |
| 4 / green | **Serum Raker** Magic card | card P/T is directly `3/2`, hence `r3c2=5` | 5 | `SERUMRAKER[5]=M` | strong candidate |
| 5 / cyan | **Faker** lifting the trophy at the O2 | picture 5 + O2 suggests `r5c2=4` | 4 | `FAKER[4]=E` | identity strong; coordinate inferred |
| 6 / blue | **Morden's Battleship** from *Metal Slug 3D* | its source identifies it as the Mission 6 boss of a `3D` game, hence `r6c3`; this is also the lower spoken blue cell | 6 | `MORDENSBATTLESHIP[6]=N` | strong coordinate/name loop |
| 7 / purple | Dota **Medusa** | the matching old guide is explicitly for Dota `6.78`, echoing the spoken given `r6c7=8`; the purple extraction cell is immediately right at `r6c8` | 4 | `MEDUSA[4]=U` | strong candidate |

This gives:

```text
CHARLES[3]      = A
SKY GARDEN[9]   = N
SANTOS[6]       = S
SERUM RAKER[5]  = M
FAKER[4]        = E
MORDEN'S BATTLESHIP[6] = N
MEDUSA[4]       = U

display = ANS:MENU
answer  = MENU
```

Reproduce the indexing with:

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b4-keep-solving-and-nobody-explodes\artifacts\test_indexing.py
```

## Why the fourth coordinate changed

The rejected `HEAD` route assumed a generic `SPHINX` and `r4c3=3`.  A bounded
Scryfall search instead found the specific blue flying card *Serum Raker*.
Its printed power/toughness is `3/2`, so it naturally identifies the Sudoku cell
`r3c2`; that cell contains 5, and the fifth letter of `SERUMRAKER` is M.

*Dream Strix* and *Shimmerwing Chimera* are remaining `3/2` alternatives with M
as the fifth letter, but *Serum Raker* best matches the uncertain audio impression
of a bat-like blue flying creature.  Only comparison with the original card can
choose among them.

## Unresolved evidence

- The saved SingleFile page contains the title, flavor text, and MP3, but not the
  Sudoku screenshot or seven source pictures.
- Only the blue and purple positions are directly recoverable from the recording.
  The red/orange/yellow coordinates, and the `(5,2)` reading for Faker/O2, remain
  hypotheses.
- Charles, Sky Garden, and Santos are not uniquely determined by the broad audio
  descriptions.  `ANS` is a useful fit, but is not independent proof of those
  names.
- Morden's Battleship is independently documented as the Mission 6 boss of
  *Metal Slug 3D*, so its source supplies `(6,3)` while its normalized proper
  name supplies the extracted N.  Cocoon remains a close visual alternative
  and also has N as its sixth letter, but it does not supply the coordinate.
- The Medusa guide title says Dota `6.78`, which independently mirrors the
  spoken given `r6c7=8`; its old guide banner also has the four Warcraft-style
  skill icons described in the recording.  Lady Vashj remains an image-level
  alternative, but lacks this numeric cross-check.
- The competing `EASY` chain is not a clean extraction: under this file's
  normalization `WORLD CHAMPION[9]=M`, not A, and using `T1 WORLD CHAMPION`
  solely to force A is not the exact Flickr title.  It also mixes the
  Richard/Shunchang/Luzhou coordinate sources with Charles/Sky Garden/Santos
  labels from different candidate pictures.

Therefore `MENU` is a medium-confidence candidate for manual visual checking,
not a confirmed answer.

## Rejected alternatives

- Literal `397:1964`, `396:3964`, and `396:3464` were rejected.
- `WIRES`, `COPPER`, `DEF:USER`, `WAR:HEAD`, `CRUELTY`, and `HEAD` were rejected.
- `ANS:HEAD` depended on a generic `SPHINX`, generic `LAND BATTLESHIP`, and
  target-selected `WINDRUNNER`; it must not be restored.

## Public references for manual comparison

- [King Charles III coronation portraits](https://www.royal.uk/coronation-portraits)
- [Sky Garden at 20 Fenchurch Street](https://skygarden.london/)
- [Port of Santos](https://www.portodesantos.com.br/en/)
- [Serum Raker](https://scryfall.com/card/mbs/31/serum-raker)
- [Faker at the 2024 Worlds final in the O2](https://www.flickr.com/photos/lolesports/54112369706)
- [Morden's Battleship: Metal Slug 3D, Mission 6](https://metalslug.fandom.com/wiki/Morden%27s_Battleship)
- [Old Dota 6.78 Medusa guide](https://blogdota.ru/gajdy-po-geroyam/medusa.html)
