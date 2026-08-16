# Reproducible extraction

Current candidate: **`FLOUNDERING`**. The `BINGO` circle-overlay route is
retained below only as an explicitly rejected experiment.

## 1. Solve the eight Strands

The complete non-crossing covers give these spangrams (the other theme words
are omitted here because only the spangram crosses both grid edges):

| Board | Spangram | Endpoint letters (first two, then last two inward) |
| ---: | --- | --- |
| 1 | `APPREHENDING` | `APGN` |
| 2 | `BIATHLON` | `BINO` |
| 3 | `CARDIOLOGIST` | `CATS` |
| 4 | `FLUCTUATION` | `FLNO` |
| 5 | `INCORPORATING` | `INGN` |
| 6 | `NEGATIVITY` | `NEYT` |
| 7 | `PANAFRICANISM` | `PAMS` |
| 8 | `STRATOLIFTER` | `STRE` |

The last picture says that adjacent strands have exactly two letters in
common. The only Hamilton chain (up to reversing the whole chain) is:

```text
4 - 2 - 5 - 1 - 7 - 3 - 8 - 6
FLNO  BINO  INGN  APGN  PAMS  CATS  STRE  NEYT
```

Its shared pairs are:

```text
NO / IN / GN / AP / AS / ST / ET
```

Treat the repeated `N` in `INGN` as two physical circles. The endpoint order
is fixed by the wording "forward and reverse": the first two letters are read
forward and the final two are read inward (backward).

## 2. Read the intermediate instruction

The shared pairs form three edge trails: `ON`, `ING`, and `PASTE`. The two
unused circles at the left terminal are `FL`. Reversing the trail/block order
gives the literal instruction:

```text
PASTE ING ON FL
```

This is an operation, not the answer `FLING`. In particular, `FL + ING` and
the old `FLING -> CAST -> EcoRI` continuation are rejected routes.

## 3. Execute the instruction as a shared-node rebus

The extracted edge trails are not independent strings. `ON` and `ING` meet at
the same letter-value vertex `N`:

```text
ON intersect ING = N
```

Move the complete `ING` trail when carrying out `PASTE ING ...`. Its shared
`N` moves with it, so the `ON` arm leaves only `O`. That `O` remains beside the
left residue `FL`, producing `FLO`:

```text
before:  FL + ON, with N also belonging to ING
move:         ING  (including the shared N)
left:    FL + O = FLO
```

The word `ON` supplies the placement relation: paste `ING` above `FL`. After
the shared `N` has moved, the actual lower row is `FLO`:

```text
       ING
       FLO
```

The lower text is under the upper text, so the rebus reads:

```text
FLO UNDER ING = FLOUNDERING
```

This operation does not preserve an overwritten connector and does not invent
a new path start. Its remaining ambiguity is that the last diagram has no
arrow fixing an absolute up/down direction; the reading uses ordinary English
`on` to put the pasted text above its target.

Reproduce the extraction with:

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\extraction_hypotheses.py --paste-rebus
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\artifacts\verify_solution.py
```

The stable layout is `artifacts/floundering-extraction.svg` (and its rendered
PNG).

## 4. Rejected literal circle-overlay experiment (`BINGO`)

The source of the three-circle segment is visible in Board 5's endpoint strand:

```text
Board 5: I N G N
            ^ ^ ^   (the contiguous ING segment)
```

The target named by `FL` is the start of Board 4:

```text
before: Board 4  F L N O       beside Board 2  B I N O
paste:             I N G       onto the FL start
after:  Board 4  I N G O       beside Board 2  B I N O
```

Because the pasted segment has three circles, its `G` occupies the old third
circle (`N`); this is why the instruction must be executed on the pictured
circles rather than by concatenating text. Keep the existing Board 4/Board 2
strand junction and trace from the top of `BINO`: `B-I-N`, cross at the changed
old `N` junction to the new `G`, then continue down the target strand to `O`:

```text
B I N  +  G O  =  BINGO
```

Equivalently, after the paste the adjacent strings `BINO` and `INGO` merge on
their ordered common subsequence `I-N-O`; their shortest common supersequence is
the same `BINGO`.

The parameterized audit tries all 24 endpoint orders. The wording-licensed
`abdc` order produces `BINGO` under this overlay experiment, but the user
explicitly rejected it. The final picture does not say to retain the old
`N/N` junction after overwriting a circle or to start the read at `BINO`.

Reproduce this rejected experiment with:

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\extraction_hypotheses.py --paste-ing-on-fl
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\artifacts\verify_solution.py
```

## 5. Other rejected routes

- `ECORI` / `GAATTC`: the DNA overlap observation was real, but the extra
  `FLING -> CAST` and enzyme-name step is not licensed by the diagram; the user
  explicitly rejected both candidates.
- `ION`: Board 4 can be repathed as `FLUCTUATING`, leaving an `ION` column, but
  the final picture does not authorize that grid rewrite; explicitly rejected.
- `NASTY`, `FLING`, `FLYING`, `42`, and the other submitted strings were also
  explicitly rejected and remain only as negative evidence.
