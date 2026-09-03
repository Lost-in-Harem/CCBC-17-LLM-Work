# Rejected Meta synonym fill: PERSPECTIVE

> **Status: rejected.** The user explicitly rejected `PERSPECTIVE` on
> 2026-08-31.  The accepted Meta constrains this feeder's semantic key to
> `观=VIEW` and its overlap letter to initial `P`; it does not authorize this
> particular synonym.  The exact replacement supported by the local
> `西北=compass POINT` extraction is documented in
> `artifacts/point-of-view-extraction.md`.

The user explicitly authorized reverse-solving this feeder through its Round
Meta.  The Meta `八音盒里的潘多拉` is accepted with answer `PARADOXXING`.
Its first audio object is `观音菩萨`; the semantic prefix `观` selects this
feeder, while the suffix `PUSA` is left-aligned with the feeder answer.

The Meta solution had recorded the unverified feeder guess `PERSPECTIVE`:

```text
PUSA
PERSPECTIVE
P
```

Only the first aligned position agrees, supplying the accepted Meta's first
letter `P`.

## Independent evidence inside this puzzle

Two local observations converge on the same concept.

1. Hint 3 restricts extraction to the depth/`里` dimension.  The two
   maximum-frequency depth trades are indexed by value 2 and, after clue
   restoration, read `性忆 / 百味`.  The repaired keyword `反切` converts
   them to `XI / BEI = 西北`.  In the three-dimensional stacked-grid setting,
   northwest is a viewing direction or **perspective**, not an answer-form
   English word by itself.
2. The unique highest-frequency repaired three-Han block is `关键词`, occurring
   twice.  Its two actual trade partners, in repaired-host order, are
   `古代人 / 的概念`, concatenating exactly to `古代人的概念`.  A person's
   conception/view is their **perspective**.  The restored clue beginning
   `古代人 / 观测天 / ...` also places the literal character `观` immediately
   after `古代人`, matching the Meta's semantic key.

The former artifact that reached `视角` through answer-length endpoints was
also invalid because it used the wrong clue answer `暴击` and the wrong
central fill `BREAK`.  Neither that route nor this broad semantic fill may be
used to restore `PERSPECTIVE`.  No online answer or official solution was
consulted.

## Reproduction

The two local trades are edges 55 and 57 in the complete character-pair
ledger produced by `work/component_crossword.py`; see
`artifacts/depth-high-frequency-extraction.md`.  The repeated block and its
partners are reproduced by `work/high_frequency.py` and recorded in
`artifacts/high-frequency-extraction.md`.

The Meta overlap can be checked read-only from the repository root with:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b-meta-pandora-that-is-trapped\work\positional_overlap.py
```

Its b6 row is the now-rejected guess
`观音菩萨 / PUSA / PERSPECTIVE / position 1 / P`; only the semantic key
`观=VIEW` and the overlap requirement `position 1 / P` survive.
