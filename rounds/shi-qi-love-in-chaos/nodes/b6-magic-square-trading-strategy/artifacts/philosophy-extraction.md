# Rejected extraction: PHILOSOPHY

**Verdict (2026-08-31): rejected by the user.**  This file is retained only
to reproduce the failed route.  The step `企业的 + 观念 -> 企业理念` has no
authorized exchange operation, and changing the English noun to `ETHOS`,
`IDEOLOGY`, `VALUES`, or another synonym would not repair that defect.

## 1. The numeric high-frequency trades give a possessive

The verified direction-frequency fill contains exactly four crossings whose
two incidences both have the maximum value `2`.  Index the two printed
three-Han blocks by `2`, order the directions by the central
`E/N/D = East/North/Depth` cycle, and apply the repaired keyword `反切`:

```text
兔干 / 质锋 / 性忆 / 百味
 TAN    ZHENG    XI     BEI
 弹       筝      西      北
```

`弹筝西北` selects the northwest one of the five depth strings.  Applying the
same cell-frequency indexing, direction cycle, and fanqie operation to its
three trades gives:

```text
去一 / 有的 / 的的
 QI     YE      DE
 企      业      的
```

So this branch ends in the incomplete possessive **`企业的`**.  The rejected
answers `CORPORATE` and `HIGH FLYER` stopped here without supplying its noun.

## 2. The textual high-frequency trades supply the noun sense

After all 57 clue-block trades are undone, `关键词` is the unique repeated
three-Han block: it occurs twice, while every other block occurs once.  Its
two actual trading partners, in occurrence order, are:

```text
古代人 / 的概念
```

Together they specify **an ancient person's concept**, i.e. an `观念`.  This
reading is also present literally in the repaired material rather than being
only a synonym guess:

- the first partner begins `古代人 / 观测天 / ...`, placing `观` immediately
  after `古代人`;
- the second keyword clue answers `END`, and the end of `的概念` is `念`.

Thus the previously unused textual high-frequency branch supplies **`观念`**.
Combining the two branches gives:

```text
企业的 + 观念 = 企业的观念 / 企业理念
```

The route guessed the core English noun **PHILOSOPHY** (as in *corporate
philosophy*), which the user rejected.  It differed from the rejected `PERSPECTIVE` and
`POINT OF VIEW`: those translated `观` while discarding the possessive
`企业的`; it also differs from rejected `CONCEPT`, which stopped at `观念`
and discarded the possessive.

## 3. Read-only Meta check

The user authorized reverse-checking through the accepted Round Meta.  Its
clip 1 object is `观音菩萨`, so the semantic prefix is `观`, and the suffix
`PUSA` must be left-aligned with this feeder's English answer.  For the
candidate:

```text
PUSA
PHILOSOPHY
P
```

Only position 1 agrees, reproducing the accepted Meta answer's first letter
`P`; the rejection proves this one-letter agreement was too weak to validate
the feeder.

## Reproduction pointers

- `artifacts/direction-frequency-fill.md` validates the complete 57-crossing
  numeric fill.
- `work/visual/cyclic-direction-audit.md` lists the two successive cyclic
  fanqie streams `弹筝西北 -> 企业的`.
- `artifacts/high-frequency-extraction.md` lists the two `关键词` occurrences
  and their exact partners `古代人 / 的概念`.
- In the all-character-pair ledger, edges 12 and 51 are the two keyword
  trades; their value is `1` and their printed/repaired indexed pairs are
  `古关↔关古` and `关的↔的关`.

No online answer or official solution was consulted.
