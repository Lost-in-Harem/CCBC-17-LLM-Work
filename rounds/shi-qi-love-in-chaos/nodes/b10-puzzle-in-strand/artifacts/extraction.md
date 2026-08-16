# Reproducible extraction

Current answer candidate: **ECORI**.

## 1. The eight Strands

The eight grids have these complete non-crossing covers and unique left-right
spangrams:

| Board | Spangram | Other theme words |
| ---: | --- | --- |
| 1 | `APPREHENDING` | `ARRESTING`, `SEIZING`, `SEARCHING`, `SURVEILLING` |
| 2 | `BIATHLON` | `SNOWBOARDING`, `BOBSLEIGH`, `CURLING`, `SKELETON`, `LUGE` |
| 3 | `CARDIOLOGIST` | `PHYSICIAN`, `DIETICIAN`, `SURGEON`, `DOCTOR`, `NURSE` |
| 4 | `FLUCTUATION` | `WAVERING`, `SHIFT`, `VARIANCE`, `MUTATION`, `FLUIDITY` |
| 5 | `INCORPORATING` | `EMBRACING`, `CONCEALING`, `DEVOURING`, `PENNING` |
| 6 | `NEGATIVITY` | `DESPAIR`, `SORROW`, `MELANCHOLY`, `GLOOM`, `APATHY`, `BLUE` |
| 7 | `PANAFRICANISM` | `RUSSIA`, `HUNGARY`, `LUXEMBOURG`, `ESTONIA`, `GABON` |
| 8 | `STRATOLIFTER` | `GROWLER`, `SEAKNIGHT`, `PEGASUS`, `SUPERFORTRESS` |

Take the first two and last two letters in the spangram's actual left-to-right
path order. The eight four-circle strings are:

```text
1 APNG   2 BION   3 CAST   4 FLON
5 INNG   6 NETY   7 PASM   8 STER
```

Requiring each adjacent pair in the last image to share exactly two distinct
letters gives one Hamilton chain, up to reversal:

```text
4 - 2 - 5 - 1 - 7 - 3 - 8 - 6
FLON  BION  INNG  APNG  PASM  CAST  STER  NETY
```

The seven shared pairs are:

```text
NO / IN / GN / AP / AS / ST / ET
```

Repeated `N` in `INNG` is two separate circles; it does not force one circle
to be used twice.

## 2. The intermediate instruction

The overlap edges form the trails `ON`, `ING`, and `PASTE`; the unused two
letters at the left terminal are `FL`. Reading each trail in the opposite
direction (equivalently, using the whole-chain reversal) gives the grammatical
instruction:

```text
PASTE ING ON FL
```

The literal concatenation `FL + ING = FLING` was rejected by the user as a
final answer, but it is a useful intermediate clue. `Fling` means throw/cast;
among the eight path-order endpoint strings, the unique ordinary English word
matching that synonym is Board 3's `CAST`.

On the chain, `CAST` shares `AS` with its left neighbor and `ST` with its right
neighbor. Those matches consume `A`, `S`, and `T`, leaving exactly the physical
circle `C`.

## 3. DNA read and answer

The flavor explicitly mentions life, strands, and forward/reverse pairing.
Keep the literal DNA bases `A/C/G/T` in the seven overlap pairs. Each pair has
at most one such base, so the canonical chain reads:

```text
NO / IN / GN / AP / AS / ST / ET
-  / -  / G  / A  / A  / T  / T  = GAATT
```

The `C` selected from `CAST` closes the reverse-complement palindrome:

```text
5'-GAATTC-3'
3'-CTTAAG-5'
```

The forward and reversed chain therefore give the two orientations of the
same site. `GAATTC` is the canonical EcoRI recognition sequence, cut as
`G^AATTC`; the enzyme name, rather than the rejected raw sequence, is the
answer **`ECORI`**.

Reference: [EcoRI](https://en.wikipedia.org/wiki/EcoRI), which documents the
`G^AATTC` recognition/cut site and its `CTTAA^G` reverse complement. The
synonym step is the ordinary English relation *fling* = *cast/throw*.

## 4. Negative evidence

- Board 4 word transfer (`WAVERING -> WAVER`, `FLUCTUATION -> FLUCTUATING`)
  leaves `ION`, but that candidate was explicitly rejected and is not implied
  by the final diagram.
- Reading internally double-paired circles and appending the terminal `Y`
  gives `NASTY`, also explicitly rejected.
- `GAATTC` is the biochemical intermediate, not the answer string; the user
  explicitly rejected submitting that raw sequence.
- Binary, secondary-grid, ordinary-word, and literal connector-geometry
  interpretations have no unique output; they remain in the workbench audit.

Reproduce the extraction and all cover checks with:

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\artifacts\verify_solution.py
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\extraction_hypotheses.py --dna-overlap
```
