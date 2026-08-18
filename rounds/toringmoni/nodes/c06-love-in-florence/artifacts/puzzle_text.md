# 情迷翡冷翠 — verified puzzle statement

Source: `input/宣传页 - 旅行指南.html` (a SingleFile **self-extracting ZIP** page;
run `python3 artifacts/extract_puzzle.py` to unpack it).  The poem lives in six
`<p class=tg-poem-stanza>` blocks; the first `<span>` of each block is the
sentence, the remaining `<span>`s are the markers.  Transcription below was
diffed byte-for-byte against the HTML.

Page chrome: brand `远迹旅行指南 / Farbound Travel Guide`, compass badge `N`,
tag `CITY EDITION`.  Puzzle page flavour text: 快住手，洋味不是这样的！

| # | sentence | markers |
| --- | --- | --- |
| 1 | A ushow's model should learn how to linchoearth tal or dress for phonegua shifting, such as adding a piece of outerni to highlight livelate. | ■□■(4/9) ■□■(3/4 4) ■■□(3/6) ■■■(7/11) |
| 2 | Dear ckerman, I do p mean to offend you but it's ther haman's to songssant na tacroi filled e rotles! | ■■(4/9) ■■■□(1/6) ■■(4/6) ■■(5) ■■(5) |
| 3 | Being kstar of tiredness, this product is dac a ronher's choice to help you maup enter a iman's state of funthon at kea at any sheyinterval. | ■□■(5/8) ■■(5/7) ■■(1/4) ■■■(6/6) ■■(4/4) |
| 4 | If Draco marfo meets sovie, ta is likely to be confused by the culture where soldiers da enemies with bullets gypt shells. | ■■■□(3/8) ■■(1/5) ■■(1/4) ■■□(3/7) |
| 5 | If he ate a ceranflower instead of that fruit, he might be presumed innocent in stf, which is disappointing ty the reversepar toaing cinth. | ■■■(3/6) ■■(4/5) □■■(5/8) ■■(2/5) |
| 6 | I mingb that a tidot with hailus and a menfast's vibe is ordinary, but what if it's right in the middle of dymiddlehe? | ■■□(2/9) ■■(2/5) ■□■(2/6) ■■(5) |

26 markers total (4/5/5/4/4/4).  Only two squares are used: `■` U+25A0 and
`□` U+25A1.  Two notations are literally irregular in the source and must not
be normalised away:

- stanza 1 marker 2 is `■□■(3/4 4)` — a space then a second `4`;
- three markers carry a single number with no slash: `■■(5)` twice in stanza 2
  and once in stanza 6.

## Non-English tokens ("pseudo-words")

| stanza | tokens |
| --- | --- |
| 1 | ushow, linchoearth, tal, phonegua, outerni, livelate |
| 2 | ckerman, p, ther, haman, songssant, na, tacroi, e, rotles |
| 3 | kstar, dac, ronher, maup, iman, funthon, kea, sheyinterval |
| 4 | marfo, sovie, ta, da, gypt |
| 5 | ceranflower, stf, ty, reversepar, toaing, cinth |
| 6 | mingb, tidot, hailus, menfast, dymiddlehe |

## Sibling WIG page

`input/天好 - 旅行指南.html` is the *other* Farbound article (枫叶国 / 天好市,
local food 柔枝薯条 — "柔枝主要用于增香，通常不会随薯条一起食用").  Its
"扩展阅读" link is `<a data-c17-open=foluo_travel_guide>` with the caption

- 其他国家的旅行地点？
- 引领远航者的方向
- `4.4.1.3`

`foluo` = 佛罗(伦萨) = Florence, i.e. that link opens **this** puzzle's page.
