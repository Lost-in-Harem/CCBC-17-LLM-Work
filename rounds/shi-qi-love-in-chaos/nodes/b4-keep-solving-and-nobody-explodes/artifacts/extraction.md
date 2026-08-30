# Extraction audit: PEEP

The user explicitly confirmed on 2026-08-29 that **PEEP is correct**.

## Hint-directed mechanism

The unlocked hints confirm the intended reconstruction:

1. The flavor word “奇迹” links the grid to a Miracle Sudoku and the seven
   pictures to the Seven Wonders of the Ancient World.
2. Use the rainbow-colored Sudoku values, in red-to-purple order, as one-based
   indices into the full English names of those Wonders.
3. Blue is the only color occupying two cells, so add its two values.
4. Some information is deliberately absent. Brute-force the missing values,
   using the common puzzle-hunt output prefix `ANS`.

The pictures need not be identified uniquely. Their descriptions supply
anchors such as Mausolus, Babylon, Alexandria, a Sphinx, Zeus, a Colossus, and
Temple/Artemis; together these determine the seven formal Wonder names in
picture order.

| # / color | Audio anchor | Full extraction name |
| --- | --- | --- |
| 1 / red | Mausolus, represented by a ruler's head | MAUSOLEUM AT HALICARNASSUS |
| 2 / orange | tiered rooftop gardens / Babylon | HANGING GARDENS OF BABYLON |
| 3 / yellow | Alexandria harbor and lighthouse | LIGHTHOUSE OF ALEXANDRIA |
| 4 / green | a blue flying Sphinx card / Giza | GREAT PYRAMID OF GIZA |
| 5 / cyan | player Zeus lifting a trophy at the O2 | STATUE OF ZEUS AT OLYMPIA |
| 6 / blue | a Colossus-named tracked land vehicle | COLOSSUS OF RHODES |
| 7 / purple | a Temple/Artemis-linked female game character | TEMPLE OF ARTEMIS AT EPHESUS |

## Sudoku facts

The Miracle Sudoku has a unique solution. The only color values recoverable
directly from the recording are:

- blue: r5c3=9 and r6c3=6;
- purple: r6c8=4.

The hint therefore fixes the blue extraction index as `9+6=15`, while purple
uses index 4. Red, orange, yellow, green, and cyan are each unknown digits from
1 through 9.

## One-based indexing

Delete spaces and punctuation and count only A-Z. The unique ordinary-English
closure produced by the bounded audit is:

| Color | Full name | Value / index | Letter |
| --- | --- | ---: | --- |
| red | MAUSOLEUM AT HALICARNASSUS | 2 | A |
| orange | HANGING GARDENS OF BABYLON | 3 or 6 | N |
| yellow | LIGHTHOUSE OF ALEXANDRIA | 9 | S |
| green | GREAT PYRAMID OF GIZA | 6 | P |
| cyan | STATUE OF ZEUS AT OLYMPIA | 6 | E |
| blue | COLOSSUS OF RHODES | 9+6=15 | E |
| purple | TEMPLE OF ARTEMIS AT EPHESUS | 4 | P |

Thus the reconstructed display is:

~~~text
ANS:PEEP
~~~

The answer field after the colon is **PEEP**.

## Bounded completion audit

The first-field hint constrains images 1-3 to `ANS`, giving red=2,
orange=3 or 6, and yellow=9. Images 4 and 5 then require only `9 × 9 = 81`
green/cyan value pairs. Blue and purple are already fixed. With the formal
Wonder names, the parameterized audit finds exactly one phrase whose two
fields both clear the low English-frequency threshold:

~~~text
ANS:PEEP    red=2; orange=3 or 6; yellow=9; green=6; cyan=6;
            blue=9+6=15; purple=4
~~~

Reproduce with:

~~~powershell
python rounds\shi-qi-love-in-chaos\nodes\b4-keep-solving-and-nobody-explodes\artifacts\test_indexing.py --rank-output rounds\shi-qi-love-in-chaos\nodes\b4-keep-solving-and-nobody-explodes\artifacts\wonders_phrase_results.tsv
~~~

The one-row result is stored in
[wonders_phrase_results.tsv](wonders_phrase_results.tsv). The orange ambiguity
does not affect the extracted letter. Common naming variants also leave all
used positions unchanged; the exact seven source pictures remain unknowable
from the recording, as the hint explicitly states.
