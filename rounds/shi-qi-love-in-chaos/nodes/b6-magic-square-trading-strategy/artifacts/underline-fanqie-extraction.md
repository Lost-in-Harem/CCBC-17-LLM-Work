# Fixed-underline DAMAGE locator

> The user explicitly rejected `DAMAGE` as the final answer on 2026-08-29.
> It is instead a locator: among the 50 repaired clues, exactly one asks about
> damage, and its frequency-validated answer is **易伤**.  The later
> answer-length walk that continued past this row produced the rejected
> candidate `循环`; it is not needed for this shortest extraction.

This artifact records the intermediate extraction after the 57 geometric block
trades.  The three literal underline locations are treated as fixed marks on
the printed rows; the missing characters themselves travel with their
three-character blocks.

## Fixed marks after the trades

In statement order, the repaired block occupying each printed underline is:

| Mark | Printed source row | Assigned slot | Block at the fixed mark | Two marked characters |
| --- | --- | --- | --- | --- |
| B1 | `G1-D03` | `G1-D03` | `尔黛拉` | **黛拉** |
| B2 | `G2-D04` | `G2-D06` | `丽曼丽` | **曼丽** |
| B3 | `I01` | `Z05` | `记忆中` | **记忆** |

The travelling blank blocks separately complete ordinary clues as
`榜样 / 曼丽 / 气性`; those fills are needed for reconstruction but are not
what remains under the three fixed marks.

## Instruction and phonetic readout

After reconstruction, `关键词` is the unique highest-frequency three-Han
block.  Its two occurrences lie in clues whose answers are **反切** and
**BREAK**.  The blocks traded against those two occurrences, in repaired-row
order, are `古代人 / 的概念`.  Thus “古代人的概念” selects the ancient
phonological method **反切** from those two answers; **BREAK** is reserved for
the final step.  Applying ordinary modern fanqie to each marked pair—initial
of the first character plus final of the second—gives:

| Marked pair | First initial | Second final | Result |
| --- | --- | --- | --- |
| 黛拉 | `d-` | `-a` | `da` |
| 曼丽 | `m-` | `-i` | `mi` |
| 记忆 | `j-` | `-i` | `ji` |

The previously proposed statement-order reading was:

```text
DA / MI / JI  ->  DAMAGE
```

The English word is not the submission answer.  Translate it only far enough
to locate the matching repaired clue:

```text
发生后 / 伤害数 / 字变大  ->  易伤
          DAMAGE
```

No other repaired row contains `伤害`.  `易伤` is also not a loose semantic
guess: decomposing it as `日 / 勿 / 伤` gives `111` in the vertical direction
and preserves equality at every one of the 57 crossings.  Alternatives such
as `暴击` do not fit that completed frequency crossword.

The other clue answering **BREAK** is the last source clue and explicitly
says it ends this part.  The user also rejected `BREAK` as the answer.  Its
sound role is therefore a terminal marker, not permission to invent another
answer-length traversal.  The former continuation
`易伤 -> ζ电势 -> BREAK -> 数网格端 -> ...` ended in the rejected structural
guess `循环` and is retained only as negative evidence.

The missing characters themselves still travel with their three-Han blocks
and complete ordinary repaired clues as `榜样 / 曼丽 / 气性`; the fixed
locations are the visible extraction marks.

## Reproduction

The fixed-mark table appears in the first ranked state of
`work/all_crossings_unanchored.md`.  The phonetic syllables can be reproduced
from the repository root with:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\fanqie_audit.py --answers 黛拉 曼丽 记忆 --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt
```

Expected first two output lines:

```text
answers: 黛拉 / 曼丽 / 记忆
fanqie syllables: da1 / mi4 / ji4
```

The tones belong to the Chinese carrier characters; the final step is the
English phonetic rebus `da-mi-ji`, so only the segmental reading is used.

## Carrier and landing control

The literal underscores are embedded in the printed clue text, so the
alternative in which blank text travels with its block was checked rather
than silently discarded.  It gives `榜样 / 曼丽 / 气性`, whose direct fanqie
readings are `bang / mi / qing`; none of their six pair orders is a
three-character Chinese dictionary word.

Breaking and arbitrarily regrouping those six characters does produce seven
toneless dictionary hits among all 720 permutations, including
`丽性 / 样气 / 榜曼 -> 另一半`.  No row, column, reverse, or snake traversal of
the statement or spatial pair layout supplies that character order.  A
frequency-based construction also leaves unresolved ties (`丽=性=3` and
`榜=曼=气=1`).  It therefore needs extra choices that the direct fixed-site
reading does not.

The earlier comparison is recorded in `work/fanqie_landing_audit.md`.
`artifacts/final-perspective-extraction.md` and
`artifacts/round-robin-fanqie-extraction.md` preserve the two superseded
continuations as negative evidence.
