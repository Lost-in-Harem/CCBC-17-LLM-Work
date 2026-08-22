# Failed HART/CRANE/LINER and ORIZABA audit

Run from the Node directory:

```powershell
python artifacts/reproduce_candidate.py
```

Expected checkpoints:

| Stage | Result |
| --- | --- |
| Rows 10–20 | `XENA'S AT BASE / V / TEAM YES` |
| Rows 27–28 set aside | `Xe Na` = `XENA` |
| Remaining team sizes | astronomY/racE/mineralS = 5/4/6 |
| Four base-5 recombinations | `112/243/212/244` = `Ge/Ta/La/W` = `GET A LAW` |
| `LAWLESS − LAW` | `LESS`, hence `LUCY LESS` |
| `Hf/Pu/Ra − Lu/C/Y` | `H/Ra/In`, values `001/323/144` in base 5 |
| Zero-based indices into `ALIEN/RACER/STONE` | `ART/ECN/LRE` |
| Uninstructed anagram with element symbols | `HART/CRANE/LINER`; not validated as intermediate answers |
| Failed association | Hart Crane + liner points to Orizaba, but does not satisfy “mix into one thing” |

Sensitivity controls:

- `--row2 31` replaces Croix/FIA `33 As` with Sepang/FIA `31 Ga`; the first selected base-5 digit remains 1 and the output is unchanged.
- `--row26 89` reproduces the discarded Ureyite homophone branch; it yields `H/Ra/Sn` and does not even reproduce all three old words.

This artifact is retained only to reproduce and prevent repetition of the
failed route. Its final two stages are not a candidate extraction.
