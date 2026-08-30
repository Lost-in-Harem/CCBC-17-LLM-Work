# Reproducible extraction after Hints 10, 11, and 12

Accepted answer: **`INFLOOD`** (naturally spaced **`IN FLOOD`**).

## 1. Confirmed spangrams and life-letter fragments

Hint 10 selects each board's unique left-to-right spangram. Hint 12 fixes the
board order as `2,6,7,8,4,5,3,1`. Keep the DNA letters `A/C/G/T` from each:

| Position | Board | Spangram | A/C/G/T |
| ---: | ---: | --- | --- |
| 1 | 2 | `BIATHLON` | `AT` |
| 2 | 6 | `NEGATIVITY` | `GATT` |
| 3 | 7 | `PANAFRICANISM` | `AACA` |
| 4 | 8 | `STRATOLIFTER` | `TATT` |
| 5 | 4 | `FLUCTUATION` | `CTAT` |
| 6 | 5 | `INCORPORATING` | `CATG` |
| 7 | 3 | `CARDIOLOGIST` | `CAGT` |
| 8 | 1 | `APPREHENDING` | `AG` |

The fragment lengths are `2,4,4,4,4,4,4,2`, exactly what the schematic needs:
the two end strands contribute to one `×2` link, while every internal strand
contributes two bases to each of its two neighbouring links. Thus all 28 base
occurrences fill `7 gaps × 2 pairs × 2 endpoints` once.

## 2. Watson-Crick allocation

Requiring the two bases across every gap to be Watson-Crick complements gives
one base-multiset allocation:

```text
          AT   GATT   AACA   TATT   CTAT   CATG   CAGT   AG
left       -    AT     AC     TT     AT     AG     AG    AG
right     AT    GT     AA     AT     CT     CT     CT     -
```

Map these occurrences back to their positions in the **complete spangrams**,
allow each whole word to run forward or backward, and require each gap's two
drawn bonds to be horizontal. With the first word fixed forward, only two
layouts survive:

| Directions | Vertical offsets | One equal non-base letter per gap |
| --- | --- | --- |
| `FRFFRFRF` | `0,-3,-3,-4,-7,-12,-13,-13` | `I/N/I/L/O/O/D` |
| `FRFRFRFR` | `0,-3,-3,-2,2,5,7,7` | `I/N/F/L/O/O/D` |

## 3. Hint 11 selects the second layout exactly

The detailed image is not a generic beta-sheet illustration. It is a crop of
global rows `9..5` in the second full-word layout:

- its eight visible strand lengths are exactly `3,2,5,5,5,5,3,3`;
- its seven visible dotted bonds are exactly
  `g5@9, g4@8, g6@8, g7@7, g4@6, g3@5, g5@5`;
- no five-row window of the other surviving layout has those strand lengths.

Thus the picture uniquely fixes:

```text
directions  F  R  F  R  F  R  F  R
offsets     0 -3 -3 -2  2  5  7  7
```

The complete coordinate drawing is in
`artifacts/in-flood-extraction.svg/.png`.

## 4. Read the ordinary-letter overlaps

After the fourteen life-letter pairs place the words, every adjacent word pair
has exactly one further position where the two ordinary letters are identical:

| Gap | Aligned word pair | Selected base-pair rows | Equal-letter row | Read |
| ---: | --- | --- | ---: | :---: |
| 1 | `BIATHLON / YTIVITAGEN` | `2,3` | 1 | `I` |
| 2 | `YTIVITAGEN / PANAFRICANISM` | `-2,4` | 6 | `N` |
| 3 | `PANAFRICANISM / RETFILOTARTS` | `0,5` | 1 | `F` |
| 4 | `RETFILOTARTS / FLUCTUATION` | `6,8` | 3 | `L` |
| 5 | `FLUCTUATION / GNITAROPROCNI` | `5,9` | 11 | `O` |
| 6 | `GNITAROPROCNI / CARDIOLOGIST` | `8,15` | 14 | `O` |
| 7 | `CARDIOLOGIST / GNIDNEHERPPA` | `7,18` | 10 | `D` |

Read the gaps in Hint-12 order:

```text
I / N / F / L / O / O / D  ->  INFLOOD
```

So the accepted answer is **`INFLOOD`**, naturally **`IN FLOOD`**.

## 5. Independent codon check and rejected branches

Repeating only the two short endpoint fragments to fill four circles gives:

```text
ATAT / GATT / AACA / TATT / CTAT / CATG / CAGT / AGAG
```

Starting at the first `ATG`, standard one-letter amino-acid translation gives:

```text
ATG ATT AAC ATA TTC TAT CAT GCA GTA GAG
 M   I   N   I   F   Y   H   A   V   E
```

`MINIFYHAVE` is a strong independent confirmation of the DNA/protein mechanism,
but it is not the current answer. The user explicitly rejected `WAY`, so the
weak/strong-bond seven-bit ASCII `WY` completion family is stopped. The former
`TAATTC -> STOP/F -> MINI` route and `HAVE -> AV -> WAVY` route were also
explicitly rejected.

## 6. Reproduction

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\artifacts\verify_solution.py
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\dna_pairing.py --output rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\visual\dna_pairing.tsv --svg rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\artifacts\in-flood-extraction.svg
```

`artifacts/way-extraction.svg/.png` and
`artifacts/wavy-extraction.svg/.png` are explicitly marked rejected.
