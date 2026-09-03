# Rejected endpoint trade-chain extraction: 伤势

**Status: rejected.** The user explicitly rejected `伤势`.  The chain below
is reproducible but stacks several unlicensed interpretations of `END` and
the underline marks; it is retained only as negative evidence. The current
extraction is in `artifacts/wolf-extraction.md`.

## 1. Count the ends of all 50 entries

For an answer written with `N` characters or symbols, its end lies at cell
`N` of its assigned entry. `END` has three letters and is included normally;
its endpoint is `D` on G3. Center-aligning the three boards and counting all
50 endpoints gives one coordinate of maximum frequency:

| Centered coordinate | Direction | Entry answer | End |
| --- | --- | --- | --- |
| r10c04 | 横 | 中冲穴 | 穴 |
| r10c04 | 纵 | 翼 | 翼 |
| r10c04 | 里 | 关节 | 节 |

The maximum is 3; every other coordinate has frequency at most 2. In the
statement's direction order `横 / 纵 / 里`, the carriers are `穴 / 翼 / 节`.
The repaired clue “西十五河海解谜中的关键词” answers `反切`, so `穴翼`
gives `XI`; the following `节` fixes the homophone as:

```text
穴 / 翼 / 节 -> XI / 节 -> 细节
```

The full 50-end ledger, including `END`, is generated in
`artifacts/answer-endpoint-extraction.md`.

## 2. The three marked details give DAMAGE

The page has exactly three underline runs. After all crossing trades are
undone, the characters occupying those fixed printed locations are:

| Mark | Pair | Fanqie |
| ---: | --- | --- |
| 1 | 黛拉 | DA |
| 2 | 曼丽 | MI |
| 3 | 记忆 | JI |

Thus the marked `细节` read `DA / MI / JI`, the phonetic English locator
`DAMAGE`. This is an instruction to enter the repaired clue containing
“伤害”, not a submission answer.

## 3. Follow answer ends through their trades

The unique repaired clue containing “伤害” is
`发生后 / 伤害数 / 字变大`, whose crossing-locked answer is `易伤`.
Go to the end of that answer: its written length 2 selects block 2 of its
assigned entry. Follow the actual trade at that block. Repeat once:

| Current answer | End / selected block | Trade | Partner block | Next clue answer |
| --- | --- | ---: | --- | --- |
| 易伤 | **伤** / `伤害数` | 35 | `物理化` | ζ电势 |
| ζ电势 | **势** / `的概念` | 51 | `关键词` | END |

The second destination clue is `结束本部分的关键词`, so `END` terminates the
walk. The two nonterminal answer ends collected on the way are:

```text
易[伤] -> ζ电[势] -> END
             伤势
```

The candidate answer is **伤势**.

## 4. Closed mechanical check

Both traversed trades have direction-frequency value 1. Index character 1
of the two traded three-Han blocks and read each trade in the natural
printed-before-repair order. Applying the same `反切` keyword gives:

| Trade | Printed pair | Reading | Repaired pair | Reading |
| ---: | --- | --- | --- | --- |
| 35 | `伤物` | SHU = 数 | `物伤` | WANG = 网 |
| 51 | `关的` | GE = 格 | `的关` | DUAN = 端 |

This spells `数网格端`, exactly the operation that starts step 1. It is a
self-check, not the final answer; the terminal `END` makes the carried endpoint
characters `伤 / 势` the output.

## Reproduction

From the repository root:

```powershell
python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\selection_frequency.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --report rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md `
  --output rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\answer-endpoint-extraction.md

python -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\answer_trade_graph.py `
  --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json `
  --report rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md `
  --dict rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\jieba-dict.txt `
  --components rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\artifacts\direction-frequency-solution.json `
  --output rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\answer_trade_graph.md
```
