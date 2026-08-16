# Reproducible extraction

Current answer candidate: **ION**.

Each board has a complete non-crossing `8×6` Strands cover. Its sole theme
word spanning the left and right sides is the spangram below. Put its first
two and last two letters on the four-circle strand in the spangram's actual
left-to-right order.

| Board | Spangram | Four-circle strand |
| ---: | --- | --- |
| 1 | `APPREHENDING` | `APNG` |
| 2 | `BIATHLON` | `BION` |
| 3 | `CARDIOLOGIST` | `CAST` |
| 4 | `FLUCTUATION` | `FLON` |
| 5 | `INCORPORATING` | `INNG` |
| 6 | `NEGATIVITY` | `NETY` |
| 7 | `PANAFRICANISM` | `PASM` |
| 8 | `STRATOLIFTER` | `STER` |

Requiring adjacent strands to share exactly two distinct letters gives one
chain, up to reversal:

```text
4 - 2 - 5 - 1 - 7 - 3 - 8 - 6
FLON  BION  INNG  APNG  PASM  CAST  STER  NETY
```

The seven adjacent pairs are:

```text
NO / IN / GN / AP / AS / ST / ET
```

The seven overlap pairs form four consecutive blocks.  At the left end,
`FL` is the part of Board 4's four-circle string not used by `NO`.  Joining
successive two-letter overlaps as trails gives:

```text
left-to-right blocks:  FL | ON | ING | PASTE
reverse block order:   PASTE ING ON FL
```

`PASTE ING ON FL` is not asking for the rejected bare concatenation `FLING`.
`FL` selects the Board 4 spangram `FLUCTUATION`, while the same full Board 4
cover supplies the word `WAVERING`, whose suffix is `ING`.

Apply the instruction literally to the two Board 4 paths:

```text
WAVERING - ING             = WAVER
FLUCTUATION - ION + ING    = FLUCTUATING
```

Both new strings are valid paths in Board 4.  Holding the other four theme
words fixed, exhaustive path enumeration gives exactly one noncrossing
45-cell pack:

```text
WAVER / SHIFT / VARIANCE / MUTATION / FLUCTUATING / FLUIDITY
```

The three unused cells are all in the rightmost column:

```text
r8c6 = I
r6c6 = O
r5c6 = N
```

Reading the transfer upward—from the removed donor suffix toward the
displaced target suffix—gives **`ION`**.  Equivalently, `ION` is precisely the
old suffix displaced when `FLUCTUATION` becomes `FLUCTUATING`.  The unique
cover, exact path transfer, and coordinates are asserted by
`artifacts/verify_solution.py` and pictured in `artifacts/ion-extraction.svg`.

The most recent rejected route instead retained physical-circle reuse. For
each internal strand, compare its match to the left with its match to the
right. A letter is read only when the **same physical circle** is forced to
participate in both matches:

| Internal board | Left pair | Right pair | Forced twice-paired circle |
| ---: | --- | --- | --- |
| 2 | `NO` | `IN` | `N` |
| 5 | `IN` | `GN` | none: `INNG` has two different `N` circles |
| 1 | `GN` | `AP` | none |
| 7 | `AP` | `AS` | `A` |
| 3 | `AS` | `ST` | `S` |
| 8 | `ST` | `ET` | `T` |

This local rule reads `NAST`. It then paired the final `T` into the terminal
strand `NETY` and continued to its right endpoint, contributing `Y`:

```text
NAST + Y = NASTY
```

The whole-chain reversal reads `TSAN`, and its terminal strand `FLON` has no
letter after the final junction `N`. That asymmetry does not rescue the rule:
the diagram never instructs the solver to continue along only one terminal
spangram, and the user explicitly rejected `NASTY`.

The clue's “truth of life” made `NASTY` look semantically attractive, but this
is result-driven confirmation rather than extraction evidence.

Post-rejection geometry audits also failed to force a replacement.  The
wording-licensed interleaving order `a,d,b,c` was checked in both chain
directions under all 256 whole-strand reversals.  Its only all-gap noncrossing
orientation codes are the complementary `2` and `L`, with no diagrammatic way
to choose their absolute polarity.  The corresponding `4×8` letter board has
no exact secondary Strands cover or left-to-right spanning word.  Finally,
joining the two equal-letter circles at every `×2` yields three possible
topologies (from the duplicated `N`) and no unique readable trail.  Incidental
paths such as `NAMASTE` and `MATTERS` are therefore not candidates.

Reproduce the covers, unique chain, Board 4 paste, and negative audits:

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\artifacts\verify_solution.py
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\solve_strands.py 4 --paste-board4
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\solve_strands.py --extract
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\extraction_hypotheses.py --double-overlap
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\extraction_hypotheses.py --glyph-weave
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\nested_strands.py --endpoint-order adbc
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\pasted_graph.py
```

The user explicitly rejected **COPY AND PASTE**, **PASTE**, **CUT AND PASTE**,
**42**, **PASTEUR**, **GAATTC**, **FLYING**, **FLING**, and **NASTY**.  `FLING`
failed because it stopped after concatenating the instruction's source and
selector.  The new `ION` route instead executes the instruction on the full
Board 4 cover and is independently forced by a unique 45-cell path packing.
