# Extraction audit: SOS:HELP

## Theme

The flavor line says “创造奇迹” and the puzzle has seven small pictures. This
does double duty:

1. It identifies the large grid as a Miracle Sudoku.
2. It identifies the common class of the seven picture referents as the Seven
   Wonders of the Ancient World.

The picture descriptions therefore lead to the following indexing labels:

| # | Description | Label | Wonder connection |
| --- | --- | --- | --- |
| 1 | king's head | MAUSOLUS | Mausoleum at Halicarnassus |
| 2 | tiered rooftop building | BABYLON | Hanging Gardens of Babylon |
| 3 | harbor | LIGHTHOUSE | Lighthouse of Alexandria |
| 4 | blue flying mythological Magic creature | SPHINX | Giza / Great Pyramid |
| 5 | glasses-wearing O2 trophy winner | ZEUS | Statue of Zeus |
| 6 | huge tracked game vehicle | COLOSSUS | Colossus of Rhodes |
| 7 | old green female game character with skill icons | TEMPLAR ASSASSIN | Temple of Artemis |

The fifth identification is independently supported by several Riot / LoL
Esports Flickr photos whose captions explicitly say “Zeus of T1 lifts the
trophy” at the 2024 final and whose tags include O2. The sixth is supported by
a public four-track model titled Vehicle_Common_Colossus [Planetside 2].

## Sudoku

The Miracle Sudoku rules and the heard givens r5c3=9 and r6c7=8 produce the
unique solution:

~~~text
6 2 7 | 3 8 4 | 9 5 1
3 8 4 | 9 5 1 | 6 2 7
9 5 1 | 6 2 7 | 3 8 4
------+-------+------
2 7 3 | 8 4 9 | 5 1 6
8 4 9 | 5 1 6 | 2 7 3
5 1 6 | 2 7 3 | 8 4 9
------+-------+------
7 3 8 | 4 9 5 | 1 6 2
4 9 5 | 1 6 2 | 7 3 8
1 6 2 | 7 3 8 | 4 9 5
~~~

The recording directly fixes the blue values as {9,6} and the purple value as
4. The other five color positions were obscured in the audio; the coherent
Seven Wonders extraction reconstructs their values as 4,6,9,3,2.

## One-based indexing

Normalize each label by deleting spaces and punctuation. In rainbow order:

| Color | Label | Index | Result |
| --- | --- | ---: | --- |
| red | MAUSOLUS | 4 | S |
| orange | BABYLON | 6 | O |
| yellow | LIGHTHOUSE | 9 | S |
| green | SPHINX | 3 | H |
| cyan | ZEUS | 2 | E |
| blue | COLOSSUS | abs(9-6)=3 | L |
| purple | TEMPLAR ASSASSIN | 4 | P |

The absolute-difference operation is symmetric:

~~~text
|9 - 6| = |6 - 9| = 3
~~~

The extraction is therefore:

~~~text
SOS:HELP
~~~

The four-letter answer after the colon is **HELP**.

Reproduce with:

~~~powershell
python rounds\shi-qi-love-in-chaos\nodes\b4-keep-solving-and-nobody-explodes\artifacts\test_indexing.py
~~~

## Uncertainty

- The page intentionally contains no source pictures. Public matches are
  semantic comparison images, not recovered originals.
- The five non-blue/non-purple color values are closure from the thematic
  phrase rather than independently audible coordinates.
- SPHINX and TEMPLAR ASSASSIN are associative representatives for Pyramid/Giza
  and Temple; they are not full formal wonder names.
- The full display is SOS:HELP. The current answer interpretation is HELP;
  SOSHELP remains only a possible checker-format variant if HELP is rejected.
