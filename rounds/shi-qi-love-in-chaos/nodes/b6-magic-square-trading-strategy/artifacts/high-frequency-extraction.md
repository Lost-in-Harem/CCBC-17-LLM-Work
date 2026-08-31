# High-frequency block audit

> The block counts and counterpart table below remain reproducible.  The
> former `嬴政／外滩` shell interpretation and its `杜月笙` continuation were
> explicitly rejected.  Reading the two trades directly also led to the
> explicitly rejected `谷歌 / GOOGLE`; see
> `artifacts/high-frequency-trade-extraction.md`.

- reconstructed clue rows: `50`
- three-Han block occurrences: `180`
- distinct block texts: `179`
- maximum frequency: `2`

| Block | Frequency | Repaired-row positions |
| --- | ---: | --- |
| `关键词` | 2 | G1-A07.4, I05.3 |

## Rows containing a maximum-frequency block

- `G1-A07 -> G1-A07`: 西十五河海解谜中的关键词 (`西十五 / 河海解 / 谜中的 / 关键词`) -> **反切**
- `I05 -> Z03`: 结束本部分的关键词 (`结束本 / 部分的 / 关键词`) -> **END**

## Trades involving maximum-frequency blocks

| Final repaired-row position | Original keyword source | Crossing | Counterpart source | Counterpart block |
| --- | --- | --- | --- | --- |
| `G1-A07.4` | `G1-D05.1` | `G1-D06.1 <-> G1-A07.4` | `G1-A07.4` | `古代人` |
| `I05.3` | `G3-A01.3` | `G3-A05.3 <-> Z03.3` | `I05.3` | `的概念` |

Both crossing cells have direction-local frequency value 1.  Put the selected
maximum-frequency block first and index character 1 of it and its partner:

| Host answer | Indexed pair | Fanqie |
| --- | --- | --- |
| **反切** | `关古` | `GU` |
| **END** | `关的` | `GE` |

The fixed stream under this hypothesis is `GU/GE`, but the attempted
`关键词 -> 谷歌 / GOOGLE` homophone landing was explicitly rejected.  The
stream has no题面-internal reason to select another homophone, so this route
is retained only as a bounded negative audit.
