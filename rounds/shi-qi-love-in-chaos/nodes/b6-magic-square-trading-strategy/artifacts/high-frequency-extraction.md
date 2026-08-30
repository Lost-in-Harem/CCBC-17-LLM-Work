# High-frequency block audit

> The block counts and counterpart table below remain reproducible.  The
> final paragraph's `嬴政／外滩` interpretation was explicitly rejected by the
> user and is retained only as a failed route.  The accepted working use of
> `反切` and `BREAK` is documented in `artifacts/extraction-loop.md`.

- reconstructed clue rows: `50`
- three-Han block occurrences: `180`
- distinct block texts: `179`
- maximum frequency: `2`

| Block | Frequency | Repaired-row positions |
| --- | ---: | --- |
| `关键词` | 2 | G1-A07.4, I05.3 |

## Rows containing a maximum-frequency block

- `G1-A07 -> G1-A07`: 西十五河海解谜中的关键词 (`西十五 / 河海解 / 谜中的 / 关键词`) -> **反切**
- `I05 -> Z03`: 结束本部分的关键词 (`结束本 / 部分的 / 关键词`) -> **BREAK**

## Trades involving maximum-frequency blocks

| Final repaired-row position | Original keyword source | Crossing | Counterpart source | Counterpart block |
| --- | --- | --- | --- | --- |
| `G1-A07.4` | `G1-D05.1` | `G1-D06.1 <-> G1-A07.4` | `G1-A07.4` | `古代人` |
| `I05.3` | `G3-A01.3` | `G3-A05.3 <-> Z03.3` | `I05.3` | `的概念` |

The two rows must retain their local trade associations:

| Host answer | Counterpart block | Interpretation |
| --- | --- | --- |
| **反切** | `古代人` | the fanqie extraction should produce an ancient person |
| **BREAK** | `的概念` | use the concept of a break rather than the literal word |

Concatenating the counterparts as `古代人的概念` loses this pairing.  With
the four high-frequency fanqie syllables fixed as
`TAN / ZHENG / YING / WAI`, the central break gives inner
`YING / ZHENG = 嬴政` and outer `WAI / TAN = 外滩`; the former matches the
`古代人` label and the latter checks the inner/outer orientation.
