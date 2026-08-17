# Reproducible extraction

Current candidate: **`FLUCTUATING`**.

## 1. Solve the eight Strands

The complete non-crossing covers give these spangrams. Each is the unique
theme word crossing from the left edge of its board to the right edge.

| Board | Spangram | First two + last two inward |
| ---: | --- | --- |
| 1 | `APPREHENDING` | `APGN` |
| 2 | `BIATHLON` | `BINO` |
| 3 | `CARDIOLOGIST` | `CATS` |
| 4 | `FLUCTUATION` | `FLNO` |
| 5 | `INCORPORATING` | `INGN` |
| 6 | `NEGATIVITY` | `NEYT` |
| 7 | `PANAFRICANISM` | `PAMS` |
| 8 | `STRATOLIFTER` | `STRE` |

The final diagram's `x2` condition means that neighboring four-letter strands
have exactly two distinct letters in common. There is one Hamilton chain, up
to reversing the whole chain:

```text
4 - 2 - 5 - 1 - 7 - 3 - 8 - 6
FLNO  BINO  INGN  APGN  PAMS  CATS  STRE  NEYT
```

The seven common pairs are:

```text
NO / IN / GN / AP / AS / ST / ET
```

## 2. Read the intermediate instruction

The first three shared-pair edges split into the ordinary trails `ON` and
`ING`; the last four make the trail `PASTE`. The two unused circles at the
left terminal are `FL`:

```text
FL | ON | ING | PASTE
```

Reading the blocks from the other end gives:

```text
PASTE ING ON FL
```

This is an instruction. `FLING` was explicitly rejected as the final answer,
so no synonym or rebus continuation is used.

## 3. Execute the instruction on the strand identified by `FL`

`FL` is the unmatched endpoint of Board 4's spangram `FLUCTUATION`. It therefore
identifies the complete strand, rather than serving as a two-letter base for
the already rejected `FLING`. Paste the suffix `ING` over the old suffix `ION`:

```text
FLUCTUATION = FLUCTUAT + ION
FLUCTUATING = FLUCTUAT + ING
```

The exact output is **`FLUCTUATING`**. Board 4 independently validates the
rewrite. Re-solving with `WAVERING` shortened to `WAVER` gives exactly one
noncrossing 45-cell cover:

```text
WAVER / SHIFT / VARIANCE / MUTATION / FLUCTUATING / FLUIDITY
```

The new `FLUCTUATING` path keeps the first nine cells of `FLUCTUATION` and then
uses the `N,G` cells formerly at the end of `WAVERING`. The three unused cells
spell `ION` up the last column, but `ION` was explicitly rejected and is only
the displaced old suffix, not another extraction. Board 4's theme, "the only
constant is change," also matches the flavour's truth-of-life clue without a
further synonym step.

Reproduce the extraction with:

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\artifacts\verify_solution.py
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\solve_strands.py 4 --paste-board4
```

The stable path overlay is `artifacts/ion-extraction.svg` and its rendered PNG;
the filename is retained because it also documents why the old `ION` reading
was rejected.

## 4. Rejected continuations

- `FLOUNDERING`: merging the letter value `N` across physically different
  circles and turning `on` into an above/below rebus were unsupported; the
  user explicitly rejected it.
- `BINGO`: overwriting Board 4 and retaining an obsolete connector were not
  licensed by the picture; explicitly rejected.
- `MEANING`: extending the fixed `ING` in a reconstructed endpoint matrix had
  no extraction instruction and was explicitly rejected.
- `ION`: this is only the suffix displaced by the instructed rewrite; it was
  explicitly rejected as an answer, while `FLUCTUATING` itself was not.
- `ECORI` / `GAATTC`: the DNA observation depended on the extra
  `FLING -> CAST` synonym step; both candidates were explicitly rejected.
- `NASTY`, `FLYING`, `FLING`, `42`, `PASTE`, and the other entries in
  `solution.md` remain negative evidence only.
