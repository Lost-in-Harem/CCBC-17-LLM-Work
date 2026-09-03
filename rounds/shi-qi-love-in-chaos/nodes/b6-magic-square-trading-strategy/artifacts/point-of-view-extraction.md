# Rejected depth-subset interpretation: POINT OF VIEW

> **Status: rejected.** The user explicitly rejected `POINT OF VIEW` on
> 2026-08-31.  The error is upstream: Hint 3 adds the `里` direction to the
> same three-dimensional crossword; it does not authorize discarding the two
> planar maximum-frequency trades.  This file is retained only as negative
> evidence.

## 1. Puzzle-internal `POINT`

Hint 3 restricts the frequency extraction to the `里` direction formed by
corresponding cells of the three boards.  The only two `里` trades whose two
incident values are both the maximum value 2 are edges 55 and 57.  In repaired
direction order, character 2 of each three-Han block gives:

```text
性 / 忆 -> XI
百 / 味 -> BEI
          西北
```

The repaired clue whose answer is `反切` supplies the phonetic operation.  The
other repeated keyword clue answers `END`, so the mechanical extraction stops
at `西北`; the rejected routes that used it to select another string are not
needed.  `西北` is specifically a compass **POINT**, not merely a generic
perspective.

## 2. Puzzle/Meta `VIEW`

The only repeated repaired three-Han block is `关键词`.  Its two trade partners
concatenate to `古代人 / 的概念`, pointing to an ancient person's conception or
view.  More concretely, the repaired clue containing the first fragment is:

```text
古代人 / 观测天 / 体运动 / 的学问
```

so the character immediately after `古代人` is literally `观`.

With the user's authorization to reverse-solve through the Round Meta, clip 1
is `观音菩萨`: the character before `音` is again `观`, whose required English
semantic value is **VIEW**.  Thus the local compass **POINT** and the Meta/local
**VIEW** identify the exact idiom **POINT OF VIEW**, rather than its rejected
synonym `PERSPECTIVE`.

## 3. Positional Meta check

The Meta normalizes spaces away and left-aligns the suffix `PUSA` with the
English feeder.  The exact comparison is:

```text
PUSA
POINTOFVIEW
P
```

Only position 1 agrees (`P`), reproducing the first letter of the accepted Meta
answer `PARADOXXING`.  The comparison is mechanically verified by:

```powershell
$key='PUSA'; $answer='POINTOFVIEW'; 0..([Math]::Min($key.Length,$answer.Length)-1) |
  ForEach-Object { if ($key[$_] -eq $answer[$_]) { '{0} {1}' -f ($_+1),$key[$_] } }
```

Expected output: `1 P`.
