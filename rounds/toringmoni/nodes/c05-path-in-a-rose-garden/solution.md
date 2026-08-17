---
node_id: c05-path-in-a-rose-garden
title: 玫瑰花园的小径
kind: puzzle
round: toringmoni
parent:
source:
round_feeder: yes
feeders:
status: rejected
answer:
confidence:
summary: Rows Garden 与三条 garden-path sentences 已完整交叉验证；先前从 13 朵余花自由选字所得 DECELERATIONS 已被用户明确否定，正确提取仍待确定。
updated: 2026-08-17
---

# 玫瑰花园的小径

## Current conclusion

先前候选 **DECELERATIONS** 已被明确否定，不能继续使用。当前可靠进展是完整 Rows Garden 填字与三条入口—出口 garden-path sentences；错误集中在余花提取规则。

题面是一盘标准全尺寸 Rows Garden。填完横行与 38 朵六字母花后，从三支指入棋盘的箭头出发、每步走到共享一条边的三角格，可分别读出三句 garden-path sentences。三条句子路径本身证据充分；“剩余 13 朵花后自由挑字母”的做法缺少显式索引，现已由拒绝结果证实为错误路线。

## Observations

- 实际题页只给出标题、答案长度 `(13)`、一句主题文字和一个文件入口；用户下载的宣传单才是题面主体。
- 宣传单矩阵是 12 行、38 朵花的标准 Rows Garden：14 粉、14 白、10 灰。矩阵另有三支入箭头和三支出箭头。
- 横行填字如下；斜线只表示题目给出的横向分词。

| Row | Fill |
| --- | --- |
| A | `HTA / WREATH` |
| B | `LYCEE / RI / DESK / CHASM / LEONE` |
| C | `PMO / RB / SHP / LG / EREN / OLED / LAM` |
| D | `UPLOAD / TORNADO / TROOP / LUA` |
| E | `OC / EX / SANE / IMO / TO BE / TENANT` |
| F | `PATH / OSIRIS / ROHIT / OPTICS` |
| G | `MO / CAUSUS / SG / IE / POPULAR / ET` |
| H | `AN / INAE / SUCH / THOM / SMARTER` |
| I | `POLISH / TEH / ITOOL / BELEM / US` |
| J | `CANLER / OKI / HIM / MAI / HANDEL` |
| K | `ADAMEC / LINEN / COD / NO VOCAL` |
| L | `ENA / HWEI / DS` |

- 38 朵花按图上从上到下、同层从左到右的位置为：

| Band | Color | Blooms |
| --- | --- | --- |
| A–B | pink | `THE ERA`, `WRECKS`, `THELMA` |
| B–C | white | `COMPLY`, `DELPHI`, `ONE HAS`, `MALONE` |
| C–D | gray | `BROADS`, `DANGER`, `POOLED` |
| D–E | pink | `COUPLE`, `ORIENT`, `REBOOT`, `LANTAU` |
| E–F | white | `XHOSAS`, `MOTORS`, `POTENT` |
| F–G | gray | `COMPAT`, `SIRIUS`, `POP HIT`, `STERIC` |
| G–H | pink | `NAUSEA`, `HEIGHT`, `AL-UMAR` |
| H–I | white | `POLINA`, `SUCHET`, `BLOOMS`, `SUMTER` |
| I–J | gray | `RELISH`, `HITOMI`, `HELENA` |
| J–K | pink | `CANADA`, `NIKOLI`, `DOMAIN`, `CALLED` |
| K–L | white | `MENACE`, `WHENCE`, `OVOIDS` |

- 每朵花均通过上下两个三字母块交叉验证。例如 `GER + reverse(NAD) = GERDAN` 是 `DANGER` 的循环排列；脚本验证了全部 38 朵花。
- J 行首题意看似可能是 `CANNER`，但灰花 `RELISH` 要求其后三字母块严格为 `LER`，因此全交叉网格只能保留 `CANLER`。这个题面/答案异常不在三条路径及最终 13 朵花中，不影响候选。

## Working hypotheses

- **采用共享边移动：确认。** 三角格中心组成三度蜂窝图；只允许跨共享边时会出现下述完整英文句。仅共享顶点也可移动时分支骤增，且不再唯一支持句子。
- **三条路径覆盖全盘：否定。** 把六支箭头当作三条覆盖全部 228 格的 Numberlink，即使只保留局部度数条件也为 `unsat`，所以路径只负责读句子，不覆盖全盘。
- **第三句的同字母微分支：由答案长度消歧。** 两条路线都拼出同一句；第一条经过 25 朵花，恰剩 13 朵，第二条只经过 24 朵而剩 14 朵。题面枚举 `(13)` 因而选第一条。

## Extraction

三条入口到出口的路径为：

| Entry → exit | Path text | Geometric matches |
| --- | --- | --- |
| 左上 → 左下 | `THE COMPLEX HOUSES THREE MEN` | 1 |
| 右上 → 右下 | `THE OLD PLANT PLUMS BEHIND` | 1 |
| 下中 → 上中 | `WHEN I HIT THE PHOTO ANGLED` | 2；取留下 13 朵花的第一条 |

三句都需要在后半句出现后重新分析前文：`houses`、`plant` 及 `hit the photo` 的最初句法读法会把读者带错。这解释了标题、实体花园中的三条路径，以及题面“迷茫后意义明朗”的描述。

三条选定路径经过 25 朵花，未经过的 13 朵按网格常规顺序倒读，逐花选字如下：

| # | Unused bloom | Letter |
| --- | --- | --- |
| 1 | `OVOI[D]S` | D |
| 2 | `CALL[E]D` | E |
| 3 | `[C]ANADA` | C |
| 4 | `SUMT[E]R` | E |
| 5 | `PO[L]INA` | L |
| 6 | `ST[E]RIC` | E |
| 7 | `SI[R]IUS` | R |
| 8 | `COMP[A]T` | A |
| 9 | `REBOO[T]` | T |
| 10 | `OR[I]ENT` | I |
| 11 | `BR[O]ADS` | O |
| 12 | `O[N]E HAS` | N |
| 13 | `WRECK[S]` | S |

这条自由选字路线曾给出 **DECELERATIONS**，但现已被用户明确否定。

脚本曾在常用英语词频表前 50 万项中寻找“依次从每朵余花取一个字母”的 13 字母词：正序无结果；倒序只有 `DENUNCIATIONS` 与 `DECELERATIONS`。这种做法没有从题面推出逐花索引，拒绝结果说明主题吻合不足以补上机制缺口；两词都不得作为候选。

## Candidate audit

- **已保留：** 38 朵花交叉、共享边移动与三条 garden-path sentences 均可复算。
- **已推翻：** “反向排列 13 朵余花，再凭主题自由选字”没有索引依据；`DECELERATIONS` 已被明确拒绝。
- **仍需解释：** 第三句两条同字母微分支、路径相对花心的左右关系、以及 `(13)` 应如何产生有索引的 13 个字母。

## Submission history

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-17 | DECELERATIONS | rejected | 用户明确反馈“不是答案”；无额外反馈。 |

## Evidence and artifacts

- `artifacts/rows_garden.py`：横行/花朵交叉、三角格坐标、共享边图及精确文字路径。
- `artifacts/extract_paths.py`：统计路径经过的花、选定第三句分支并生成余花提取。
- `artifacts/path-sentences.tsv`：三条句子的精确格子序列与左右转向序列。
- `artifacts/final-extraction.tsv`：13 朵余花、所选字母、原答案位置及具体花瓣格。
- `artifacts/three-paths.png`：在持久坐标系上的三条已填路径标注图。
- Rows Garden 格式核对：[A Muse Labs Rows Garden overview](https://amuselabs.com/docs/puzzles/rows-garden/overview/)。
- Garden-path 阅读中的回视/重读现象参考：[Retracing the garden-path: Nonselective rereading and no reanalysis](https://www.sciencedirect.com/science/article/pii/S0749596X24000184)。

复算命令（从仓库根目录执行）：

```powershell
python rounds\toringmoni\nodes\c05-path-in-a-rose-garden\artifacts\rows_garden.py --path-query "left|A01|L01|THE COMPLEX HOUSES THREE MEN" --path-query "right|A07|K13|THE OLD PLANT PLUMS BEHIND" --path-query "middle|L04|B07|WHEN I HIT THE PHOTO ANGLED"
python rounds\toringmoni\nodes\c05-path-in-a-rose-garden\artifacts\extract_paths.py --middle-match 1
```

## Important failed routes

- 不能把矩阵当成三条覆盖全盘的 Numberlink；度数约束本身已不可满足。
- 不能允许只碰顶点的三角格相邻；它产生大量偶然文字路径，失去句子唯一性。
- `THE OLD POOR TOO ...`、`THE COMPLEX HOUSES US ...` 是在分叉处可读出的诱饵/偶然延伸，不通向对应出口；完整入口—出口句分别要求 `PLANT PLUMS BEHIND` 与 `THREE MEN`。
- 不应把 J 行强改成 `CANNER`；这样会立即破坏 `RELISH` 的交叉。
- `DECELERATIONS` 来自对 13 朵余花的无索引自由选字；虽与“放慢脚步”主题吻合，但已被明确拒绝，不能在没有新证据时恢复。`DENUNCIATIONS` 使用同一失效机制，也一并排除。

## Next action

从三条已确认路径的几何关系中寻找显式的 13 次取字事件，优先检查句法消歧点所触发的回退/改道及路径两侧花瓣，而不是继续对余花自由挑字。
