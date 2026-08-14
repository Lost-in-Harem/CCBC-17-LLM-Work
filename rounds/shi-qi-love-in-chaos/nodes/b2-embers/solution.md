---
node_id: b2-embers
title: 余烬
kind: puzzle
round: shi-qi-love-in-chaos
parent: 
source: 
round_feeder: yes
feeders: 
status: accepted
answer: DEFLAGRATE
confidence: high
summary: "把残缺题面复原为 12×12 方阵并定位 10 个十字形火源；继续燃烧后只剩‘暴、然’，给两字同加火字旁得‘爆燃’，对应十字母 DEFLAGRATE，已获用户确认。"
updated: 2026-08-15
---

# 余烬

## Current conclusion

已确认答案为 **DEFLAGRATE**。

关键订正是题面末句应复原为“它们会指向一个与本题**有关**的十字母词”，而不是“无关”。继续燃烧留下 `暴`、`然`；给两字同加火字旁：

```text
火 + 暴 = 爆
火 + 然 = 燃
爆燃 = DEFLAGRATE
```

`DEFLAGRATE` 恰为 10 个英文字母。用户于 2026-08-15 明确确认这是正确答案。

## Observations

- 题面风险警告明确说“发现10个火源”。
- 原题正文只剩 100 个字符，多数语句是若干字符被删除后的残句。
- 完整题面恰为 144 字，可按行排成 12×12 方阵：

```text
一场大火把这道题烧成了残
骸。这些字本应该被排成一
个方阵，但题中所有字都发
生了位移。想要解开这道谜
题，你可能需要暴力穷举来
复原这道题的题面。每团火
都烧毁了自身和周围四个格
子。为了得到答案，你应该
先定位每团火所在的位置，
然后，让盘面继续燃烧直到
只剩两个字，它们会指向一
个与本题有关的十字母词。
```

- 末行 `R12C5` 的“有”恰好在 `R12C4` 火源烧掉的范围内，因此残文只能看到“与……关”，无法仅靠未烧文字区分“有关”和“无关”。最终偏旁机制和用户确认共同确定应为“有关”。
- 单文件网页中只有一个 80×80 头像图片；它不参与机制。

## Working hypotheses

- 机制与答案均已解决并确认，没有仍在检验的竞争路线。
- 若以后复核，只需保持三个彼此独立的层次：题面复原、火源几何、`暴/然 → 爆燃 → DEFLAGRATE` 提取。

## Extraction

1. 按行优先把复原文字写入 12×12 方阵。
2. 每个火源烧掉自身、上、下、左、右五格；要求恰有 10 个火源，烧后按行读出的未烧文字必须与网页现存的 100 字完全一致。
3. 求解器枚举出唯一一组火源位置（坐标均为 1 起始）：

```text
R1C4   R1C9   R3C11  R4C4   R6C12
R7C3   R9C6   R10C9  R10C10 R12C4
```

4. 初始十字共烧掉 44 格，留下原题中的 100 字。随后从相同火源继续按曼哈顿距离扩张：

| 燃烧半径 | 剩余格数 |
| ---: | ---: |
| 1 | 100 |
| 2 | 50 |
| 3 | 16 |
| 4 | 2 |
| 5 | 0 |

5. 半径 4 时仅剩 `R5C8 = 暴` 与 `R10C1 = 然`。
6. 两字同加题目核心偏旁“火”：`暴 → 爆`，`然 → 燃`，得到 **爆燃**。
7. “爆燃”对应英语动词 **DEFLAGRATE**，共 10 个字母。

## Candidate audit

- **格式：** `DEFLAGRATE` 为 10 个英文字母，符合复原题面的明示要求。
- **机制覆盖：** 12×12 方阵、10 个火源、十字燃烧、继续燃烧、末两字、题目相关性和偏旁变换均得到解释。
- **独立检查：** 程序重新生成的烧毁掩码留下 100 字，与网页正文逐字相同；继续扩张的末两格也由程序直接计算。
- **未用信息：** 网页头像无需使用；除此之外没有影响答案的未解释信息。
- **确认：** 用户明确报告 `DEFLAGRATE` 为正确答案。

## Submission history

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-15 | DEFLAGRATE | accepted | 用户明确确认正确，并订正题面为“与本题有关”。 |

## Evidence and artifacts

- [`artifacts/restored_grid.md`](artifacts/restored_grid.md)：稳定的 12×12 坐标表示、火源、最终剩余字与偏旁提取。
- [`artifacts/fire_solver.py`](artifacts/fire_solver.py)：参数化求解与复核脚本。
- [`artifacts/fire_results.tsv`](artifacts/fire_results.tsv)：唯一模型的结果表。
- 复现命令：

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b2-embers\artifacts\fire_solver.py --grid 12 --sources 10 --mode exact --combine union --timeout-ms 60000 --max-models 100 --layout row --shape plus --result rounds\shi-qi-love-in-chaos\nodes\b2-embers\work\fire_results-recheck.tsv
```

## Important failed routes

- 未完整复原题面时凭语感补入“所有的空格”等文字，十字燃烧约束无解；错误在补文，不在火源数量。
- 蛇形、螺旋、环绕边界、对角邻接及 XOR 等变体均没有同时给出通顺题面与可复核提取；标准行优先、有限边界、正交十字即可唯一满足。
- 曾把末句误补成“与本题无关”，因而把 `暴然` 当作罕见词并猜测 `REGARDLESS`、`BOISTEROUS`。`R12C5` 本来就是烧毁格，残文不约束“有/无”；正确偏旁机制要求“有关”，这些词义路线均作废。
- 网页搜索还曾把旧《国语辞典》的“暴桀”OCR 成“暴然”；高分辨率核对原页后确认是 OCR 错误，不能作为词义证据。

## Next action

无；答案已由用户确认，可将 **DEFLAGRATE** 作为本 Round 的已解 feeder 使用。
