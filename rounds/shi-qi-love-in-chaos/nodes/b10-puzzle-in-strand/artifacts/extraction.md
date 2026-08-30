# Reproducible extraction after Hints 10, 11, and 12

Current candidate: **`EQUALS SIGN`** (the standard name of `=`).

## 1. Confirmed spangrams

| Board | Spangram |
| ---: | --- |
| 1 | `APPREHENDING` |
| 2 | `BIATHLON` |
| 3 | `CARDIOLOGIST` |
| 4 | `FLUCTUATION` |
| 5 | `INCORPORATING` |
| 6 | `NEGATIVITY` |
| 7 | `PANAFRICANISM` |
| 8 | `STRATOLIFTER` |

Hint 12 fixes their extraction order as:

```text
2, 6, 7, 8, 4, 5, 3, 1
```

## 2. What Hint 11 adds

The supplied detailed picture has solid zigzag backbones and horizontal
dotted bonds between them.  Its protein-beta-sheet-like visual language
changes the interpretation of the original strands: use DNA bases and then
translate codons to one-letter amino-acid codes.  It is not evidence for the
former equal-endpoint chain.

The persistent coordinate audit is:

- `artifacts/hint11-annotated.png` -- 31 labelled circle centres and seven
  labelled dotted bonds;
- `work/visual/hint11/geometry.tsv` -- the same geometry as a table;
- `work/hint11_model.py` -- regenerates the table and annotation spec.

## 3. Minify to DNA

Hint 10 explicitly says to use the one word in each board that spans its two
ends (the spangram), then find the "truth of life" in those words.  Therefore,
keep only `A/C/G/T` in each spangram, preserving letter order.  Six results
already have four bases. Boards 1 and 2 have two bases, so repeat each
two-base string once to occupy the four pictured circles. This is the
four-slot completion; the seven printed `x2` labels are separately used as
the two-complementary-match constraint.

| Hint-12 position | Board | Filtered | Four-base strand |
| ---: | ---: | --- | --- |
| 1 | 2 | `AT` | `ATAT` |
| 2 | 6 | `GATT` | `GATT` |
| 3 | 7 | `AACA` | `AACA` |
| 4 | 8 | `TATT` | `TATT` |
| 5 | 4 | `CTAT` | `CTAT` |
| 6 | 5 | `CATG` | `CATG` |
| 7 | 3 | `CAGT` | `CAGT` |
| 8 | 1 | `AG` | `AGAG` |

Concatenation gives 32 DNA bases:

```text
ATATGATTAACATATTCTATCATGCAGTAGAG
```

The first start codon `ATG` begins at base 3.  From there the remaining 30
bases divide exactly into ten codons:

```text
ATG ATT AAC ATA TTC TAT CAT GCA GTA GAG
 M   I   N   I   F   Y   H   A   V   E
```

The peptide message is therefore:

```text
MINIFY HAVE
```

Now use the original four-circle columns and the `x2` links literally. Anchor
the first strand in the forward reading direction; for each of the remaining
seven strands try forward or reverse, and require every adjacent pair to have
exactly two same-row Watson-Crick complements. The bound is only `2^7 = 128`,
and one anchored orientation survives:

| Position | Board | Oriented bases | Direction | Complementary rows to next |
| ---: | ---: | --- | :---: | --- |
| 1 | 2 | `ATAT` | F | `2,3` |
| 2 | 6 | `GATT` | F | `3,4` |
| 3 | 7 | `ACAA` | R | `1,4` |
| 4 | 8 | `TTAT` | R | `2,3` |
| 5 | 4 | `TATC` | R | `2,3` |
| 6 | 5 | `GTAC` | R | `1,2` |
| 7 | 3 | `CAGT` | F | `1,4` |
| 8 | 1 | `GAGA` | R | `-` |

Encode forward/reverse as `0/1` in Hint 12 order:

```text
FFRRRRFR -> 00111101 -> ASCII 61 -> =
```

Here `x2` has already done its job: it is the requirement that each adjacent
gap have **two** complementary rows. It must not be applied again to duplicate
the extracted character. Python's local Unicode character database gives the
standard name of `=` as:

```text
EQUALS SIGN
```

The current candidate is therefore **`EQUALS SIGN`**. The peptide text
`MINIFY HAVE` is best retained as a self-check/instruction to reduce what the
solver has to the life alphabet; it is not licensed as two program identifiers
on either side of an equality operator.

Without fixing the first strand, the complement layout has the expected global
mirror `RRFFFFRF`. Swapping the 0/1 convention or reversing Hint 12's expressly
given order yields `194`, `188`, or `C`, so the readable `=` specifically uses
the normal puzzle conventions “a reversal is a marked bit” and “read in the
given order.” Direct encodings of the seven matched row pairs give
`63966C9`, while circles paired on both sides read `T/A/-/AT/T/C`; neither is a
word. This symmetry/direct-read audit is included rather than hidden.

The now-rejected continuation was:

```text
= x2 -> ==; MINIFY == HAVE -> FALSE
```

The user explicitly rejected `FALSE`; `x2` is not a second operation.

As an independent check on the `x2` links, the eight undoubled DNA fragments
contain 28 bases in total, exactly `7 gaps × 2 pairs × 2 bases`. Requiring
every occurrence to be used once in Watson-Crick pairs gives one base-count
partition in Hint 12 order. Expanding repeated letters gives 72 occurrence
matchings, but none admits literal equal-spacing horizontal bonds. This
distinguishes that count-only checksum from the four-circle same-row model;
both audits are reproduced by `work/dna_pairing.py` and tabulated in
`work/visual/dna_pairing.tsv`.

## 4. Reproduction

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\artifacts\verify_solution.py
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\amino_minification.py
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\dna_pairing.py --output rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\visual\dna_pairing.tsv
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\hint11_model.py --table rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\visual\hint11\geometry.tsv --spec rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\visual\hint11\annotations.json
```

The verifier also retains all explicitly rejected historical candidates as
negative evidence.  In particular, Hint 12 disproves the old
`4-2-5-1-7-3-8-6` equal-endpoint chain, so none of its `PASTE`, `FLING`, or
`FLEETING` descendants are used here.  The former `I/A -> CURRENT`, `HALVE`,
and `L -> LEUCINE` steps are retained only as rejected evidence. The former
pairwise-mass result `NAVE` and the boolean result `FALSE` were also explicitly
rejected; their audits remain only to prevent those routes from being restored.
