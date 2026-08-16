---
node_id: b10-puzzle-in-strand
title: 刻在strands里的谜题
kind: puzzle
round: shi-qi-love-in-chaos
parent:
source:
round_feeder: yes
feeders:
status: rejected
answer:
confidence:
summary: "用户明确否定 FLOUNDERING。八盘 spangram、唯一链和中间指令 PASTE ING ON FL 仍确认；共享 N 后构造 FLO UNDER ING 的 rebus 也不是官方提取，需重新审计 ×2 的配对位置和正反交织规则。"
updated: 2026-08-17
---

# 刻在strands里的谜题

## Current conclusion

用户已明确否定 **`FLOUNDERING`**。此前把 `PASTE ING ON FL` 解释成共享 `N`
移动后的空间 rebus；这一步仍是未经图示明确授权的语义补全。`BINGO`、`ECORI`、
`ION`、`FLING` 等也均已否定，当前没有可提交候选。

八条 spangram 的端点四字按最后一图的 `×2` 关系排成唯一链
`4-2-5-1-7-3-8-6`（整体反向等价）。相邻交叠对是
`NO / IN / GN / AP / AS / ST / ET`。这些边的连续轨迹和左端余字给出中间指令
`PASTE ING ON FL`。此前将 `ON` 与 `ING` 的字母值 `N` 合并，搬走 `ING` 后留下
`O`，再把 `ING` 放在 `FLO` 上方并读作 `FLO UNDER ING`；用户已明确否定该结果。
这说明公共字母的集合关系不能直接当作一个可移动的物理节点，最后图的 `×2` 必须
按实际配对位置或另一种正反交织规则解释。

## Confirmed Strands solves

八盘都是标准的 `8×6` Strands：主题词完整覆盖 48 格，词不能占用同一格，线段也不能自交或互交。每盘恰有一个主题词从左边界横跨到右边界，即题句所说跨越“两端”的 spangram。

| Board | 完整主题词 | Spangram |
| ---: | --- | --- |
| 1 放开人质，举起手来 | `APPREHENDING / ARRESTING / SEIZING / SEARCHING / SURVEILLING` | `APPREHENDING` |
| 2 来自二月的汗水 | `SNOWBOARDING / BOBSLEIGH / BIATHLON / CURLING / SKELETON / LUGE` | `BIATHLON` |
| 3 十字军 | `CARDIOLOGIST / PHYSICIAN / DIETICIAN / SURGEON / DOCTOR / NURSE` | `CARDIOLOGIST` |
| 4 唯有变是不变的 | `WAVERING / SHIFT / VARIANCE / MUTATION / FLUCTUATION / FLUIDITY` | `FLUCTUATION` |
| 5 博采众长，兼容并蓄 | `INCORPORATING / EMBRACING / CONCEALING / DEVOURING / PENNING` | `INCORPORATING` |
| 6 我的世界在下雨 | `DESPAIR / SORROW / NEGATIVITY / MELANCHOLY / GLOOM / APATHY / BLUE` | `NEGATIVITY` |
| 7 我只给你三个颜色 | `RUSSIA / HUNGARY / LUXEMBOURG / ESTONIA / GABON / PANAFRICANISM` | `PANAFRICANISM` |
| 8 凌云的倒转音波 | `STRATOLIFTER / GROWLER / SEAKNIGHT / PEGASUS / SUPERFORTRESS` | `STRATOLIFTER` |

Board 6 用 `BLUE` 的“忧郁”义统摄消极情绪；Board 7 的五个国家旗帜使用三色，`PANAFRICANISM` 对应泛非三色；Board 8 的“音波”倒转为“波音”（Boeing），其主题词均为 Boeing 飞行器名称或绰号。

## Hint evidence supplied by the user

- 已解锁提示 1 明确确认：八盘都是 NYT Strands；词可沿八邻接任意弯曲，每格恰属于一个主题词。
- 用户还提供了提示 10–12 的标题，但没有正文：分别询问完成小题后做什么、最后一图的更多细节、以及提取时八个词的顺序。
- 因而可以确认最终对象是八条 spangram 及其顺序；不能把未提供的提示正文当作已知，也不能据此臆造四圆箭头或编码。

## Extraction

### 1. 每条 spangram 的两端各取两字

每条 spangram 都从盘面左边界走到右边界。取首二字与末二字，并按原词从左到右的次序放入四圆；即 `first, second, penultimate, last`。四圆的顺序不是任意排列，因为后续要判断同一个**字母出现位置**是否被左右两侧同时配到。

先得到原词方向的端点四字；按题句“正反”实际填图时，后两字从另一端向内读，
所以圆的顶到底顺序是 `first, second, last, penultimate`：

| Board | Spangram | 原词端点 | 圆的顶到底填入 |
| ---: | --- | --- | --- |
| 1 | `APPREHENDING` | `APNG` | `APGN` |
| 2 | `BIATHLON` | `BION` | `BINO` |
| 3 | `CARDIOLOGIST` | `CAST` | `CATS` |
| 4 | `FLUCTUATION` | `FLON` | `FLNO` |
| 5 | `INCORPORATING` | `INNG` | `INGN` |
| 6 | `NEGATIVITY` | `NETY` | `NEYT` |
| 7 | `PANAFRICANISM` | `PASM` | `PAMS` |
| 8 | `STRATOLIFTER` | `STER` | `STRE` |

### 2. `×2` 强制唯一链

要求每对相邻 strand 恰有两个**不同**公共字母。枚举八条 strand 的所有排列只得到一条 Hamilton 链及其整体反转：

```text
4 - 2 - 5 - 1 - 7 - 3 - 8 - 6
FLNO  BINO  INGN  APGN  PAMS  CATS  STRE  NEYT
```

相邻公共对依次为：

```text
NO / IN / GN / AP / AS / ST / ET
```

### 3. 已否定：共享 N 的 `FLOUNDERING` rebus

七个公共对按链的位置分成 `1 / 2 / 4` 条边；分别可以走成：

```text
ON | ING | PASTE
```

链首 Board 4 未用于第一个 `NO` 交叠的两个字母是 `FL`。从右往左读取这些块，
得到完整操作 `PASTE ING ON FL`，而不是把 `FL+ING` 裸拼成已否定的 `FLING`。

关键是 `ON` 与 `ING` 并非完全独立：在按字母值建立的公共边图上，它们共用
`N`。搬动完整路径 `I-N-G` 时，连接点 `N` 必须一起搬走；原来的 `O-N` 支路只
留下 `O`。这个 `O` 仍接在左端余字 `FL` 之后，因此下方材料变成：

```text
FL + O = FLO
```

把 `ING` “on”在该目标上，即放在它的上方：

```text
ING
FLO
```

此前据此读出：

```text
FLO UNDER ING = FLOUNDERING
```

用户明确报告 `FLOUNDERING` 不是答案。失败点是把公共边中相同的字母值 `N` 当作
同一个可移动物理圆，并把英文 `on` 自行升级为“上下排版”指令；题图只标出每个
相邻 strand 有两个匹配，未授权这两个额外操作。

复核命令与稳定图示：

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\extraction_hypotheses.py --paste-rebus
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\artifacts\verify_solution.py
```

该路线的图示 `artifacts/floundering-extraction.svg` / `.png` 仅保留作负证据。

### 4. 已否定：保留旧连接读 `BINGO`

此前实验把 Board 5 的 `ING` 覆盖到 Board 4 的 `FLNO` 开头，得到 `INGO`，再
保留被覆盖前的 `N/N` 配对并从相邻 `BINO` 顶端起读：

```text
B-I-N -> G-O = BINGO
```

用户明确否定 `BINGO`。最后一图既未授权覆盖后保留旧连接，也未指定从 `BINO`
顶端开始；因此该读法不可恢复。参数化负证据仍可用
`work/extraction_hypotheses.py --paste-ing-on-fl` 复核。

### 5. 已否定：DNA / EcoRI 路线

以下只记录已被用户否定的 `ECORI` 路线，不是当前提取。

把相邻公共对中首尾相接的边连成字母路径，并保留左端 Board 4 未参与
`NO` 的 `FL`。块结构为：

```text
FL | ON | ING | PASTE
```

沿每个块的反向轨迹读出唯一通顺的中间指令：

```text
PASTE ING ON FL
```

裸拼结果 `FLING` 已被用户否定为终答，但它有明确的同义线索作用：
*fling* = throw/cast。八个按 spangram 原方向的端点串中，唯一普通英文词是
Board 3 的 `CAST`（不要把图形内向读法 `CATS` 当作字母顺序）。`CAST` 与两侧
分别共享 `AS`、`ST`，所以 `A/S/T` 已被配对，剩余圆是 `C`。

题句中的“生命”“strands”“正反配对”共同指定 DNA 字母筛选。七个公共对各至多
含一个 `A/C/G/T`，正向链读为：

```text
NO / IN / GN / AP / AS / ST / ET
-  / -  / G  / A  / A  / T  / T  = GAATT
```

把 `CAST` 的剩余 `C` 接上，得到互为反向互补的双链：

```text
5'-GAATTC-3'
3'-CTTAAG-5'
```

这是 EcoRI 的经典识别位点 `G^AATTC`（反向写作 `CTTAA^G`）。所以 `GAATTC`
是中间生化标记，最终答案是酶名 **`ECORI`**。复核命令：

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\artifacts\verify_solution.py
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\extraction_hypotheses.py --dna-overlap
```

### 6. 已否定：Board 4 的后缀重铺

以下只记录曾试验并被用户否定的 `ION` 路线，不是当前提取。

把相邻公共对中首尾相接的边连成字母路径，并保留左端 Board 4 未参与 `NO` 的 `FL`，整条链从左到右分成：

```text
FL | ON | ING | PASTE
```

按指令语序反读四块，得到：

```text
PASTE ING ON FL
```

这不是把裸字符串拼成用户已经否定的 `FLING`。`FL` 选择同盘的 `FLUCTUATION`；Board 4 的完整铺法还恰有 `WAVERING`，可作为 `ING` 的供体：

```text
WAVERING - ING             = WAVER
FLUCTUATION - ION + ING    = FLUCTUATING
```

`WAVER` 在盘上只有一条路径；`FLUCTUATING` 虽有两条路径，但与其余固定主题词同时要求不占同格、线段不交叉后，只剩一个 45 格覆盖：

```text
WAVER / SHIFT / VARIANCE / MUTATION / FLUCTUATING / FLUIDITY
```

相对于原 48 格完整铺法，新的 `FLUCTUATING` 保留旧 `FLUCTUATION` 的前九格，并接过旧 `WAVERING` 末尾的 `N,G` 两格。唯一未覆盖的三格为：

```text
r8c6 = I   （原 WAVERING 的 I）
r6c6 = O   （原 FLUCTUATION 的 O）
r5c6 = N   （原 FLUCTUATION 的 N）
```

三格同在第 6 列；由供体位置向目标位置自下而上读为：

```text
I O N
```

这也正好恢复被 `ING` 替换的原后缀 `ION`。复核命令：

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\solve_strands.py 4 --paste-board4
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\artifacts\verify_solution.py
```

### 7. 已否定：读取被左右两侧同时配到的同一个圆

对每个内部 strand，把它与左邻的公共对、与右邻的公共对进行比较。若两对含有同一个字母，而且该 strand 中这个字母只有一个物理圆，那么该圆被左右两组配对强制复用，正是题句“交叠之处”所指的二次交叠。

| Internal board | 左侧公共对 | 右侧公共对 | 强制双配圆 |
| ---: | --- | --- | --- |
| 2 | `NO` | `IN` | `N` |
| 5 | `IN` | `GN` | 无：`INNG` 的两个 N 分别服务左右 |
| 1 | `GN` | `AP` | 无 |
| 7 | `AP` | `AS` | `A` |
| 3 | `AS` | `ST` | `S` |
| 8 | `ST` | `ET` | `T` |

该局部规则从左到右读出：

```text
N A S T
```

Board 5 的重复 `N` 说明字母出现位置不能随意压成集合；但题图未明确指示“被两侧同时使用的圆就是提取位”，因此 `NAST` 只保留为负证据。

### 8. 已否定：从最后的双配圆走到 spangram 右端

最后一个双配圆是 Board 8 `STER` 中的 `T`；它通过末组 `ET` 配入终端 Board 6 的 `NETY`。沿这条已固定为左到右的 spangram，从 `T` 继续到右边界，恰剩末字 `Y`：

```text
NAST + Y = NASTY
```

整体反转的审计结果是 `TSAN`，且终端 `FLON` 的最后一个交叠字母 `N` 已经位于词尾。这个不对称曾被用来支持正向，但用户明确否定 `NASTY`，说明“沿终端词补尾字”是未经图示授权的后验规则。复核这条失败路线的命令：

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b10-puzzle-in-strand\work\extraction_hypotheses.py --double-overlap
```

## Mechanism audit

- 可复核事实：八盘完整铺法、八条左右横跨的 spangram、首末各两字、唯一 `×2` 链及七个公共对。
- 公共边分成 `FL | ON | ING | PASTE`；反向按块读成唯一通顺的中间指令 `PASTE ING ON FL`。
- `ON` 与 `ING` 的字母值确实都含 `N`，但这不证明它们在图中共用同一物理圆。
- `FLO UNDER ING` 的空间 rebus 已被用户明确否定，不能再列为候选。
- `FLING`、Board 4 的 `ION`、DNA/`ECORI`、内部双配的 `NASTY` 以及二进制/几何/二次方阵均保留为已否定或非唯一的负证据。

## Submission history

只记录用户或比赛网站明确反馈过的提交；不要把尚未提交的候选写进来。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-16 | COPY AND PASTE | rejected | 用户明确报告不是答案。 |
| 2026-08-16 | PASTE | rejected | 用户明确报告也不是答案。 |
| 2026-08-16 | CUT AND PASTE | rejected | 用户明确报告也不是答案。 |
| 2026-08-16 | 42 | rejected | 用户明确报告不是答案。 |
| 2026-08-16 | PASTEUR | rejected | 用户明确报告不是答案，并指出该路线属于无字母依据的联想。 |
| 2026-08-16 | GAATTC | rejected | 用户明确报告不是答案。 |
| 2026-08-16 | FLYING | rejected | 用户明确报告不是答案，并提供了提示列表；提示标题明确最终提取依赖八个词的顺序与最后一张图。 |
| 2026-08-16 | FLING | rejected | 用户明确报告不是答案；裸拼 `FL+ING` 不是终答。后续新证据表明整句可能是作用于 Board 4 完整词的中间指令。 |
| 2026-08-16 | NASTY | rejected | 用户明确报告不是答案；因此“强制双配圆读 NAST，再沿终端 NETY 续 Y”不是官方终提取。 |
| 2026-08-16 | ION | rejected | 用户明确报告不是答案；Board 4 的后缀搬移与余格读取不是官方终提取。 |
| 2026-08-16 | ECORI | rejected | 用户明确报告不是答案；`FLING → CAST → GAATTC → ECORI` 的后续补充操作不成立。 |
| 2026-08-16 | BINGO | rejected | 用户明确报告不是答案；Board 5 `ING` 覆盖 Board 4 `FLNO` 的圆位读法不是官方终提取。 |
| 2026-08-17 | FLOUNDERING | rejected | 用户明确报告不是答案；把共享字母 `N` 移动并将 `ING` 置于 `FLO` 上方的 rebus 不是官方终提取。 |

## Evidence and artifacts

- `artifacts/extraction.md`：精简记录完整 spangram、唯一链及已否定的共享 `N` rebus。
- `artifacts/floundering-extraction.svg/png`：保留已判错的 `ING` 搬移、`FLO` 和上下 rebus，仅作负证据。
- `artifacts/bingo-extraction.svg/png`：保留已判错的 `BINGO` 圆位覆盖，仅作防重复负证据。
- `artifacts/ion-extraction.svg/png`：候选提取的坐标示意，标出 `WAVER`、`FLUCTUATING`、移入的 `NG` 与同列余字 `ION`。
- `artifacts/nasty-extraction.svg` 与渲染后的 PNG：已否定路线的可视化，仅作防重复负证据。
- `artifacts/fling-extraction.svg/png`：已判错 `FLING` 的旧词图分块，现已明确标为 `REJECTED`。
- `artifacts/flying-extraction.svg/png`：已判错 `FLYING` 的旧最短交织，仅作防重复负证据。
- `artifacts/verify_solution.py`：标准库复核八盘精确覆盖、唯一链和各失败路线；`FLOUNDERING` 断言仅作已否定路线审计。
- `work/solve_strands.py`：探索阶段的铺盘搜索器；`--full` 输出完整路径，`4 --paste-board4` 穷举候选重铺。
- `work/extraction_hypotheses.py --paste-rebus`：复核已否定的 `ON ∩ ING = N`、搬走 `ING` 后留下 `O` 及 `FLO UNDER ING`；`--paste-ing-on-fl` 保留已判错的 `BINGO` 实验。
- `work/extraction_hypotheses.py --glyph-weave`：复核 `a,d,b,c` 四圆交织与 256 个整股翻转的几何负证据。
- `work/endpoint_grid_search.py` 与 `work/nested_strands.py --endpoint-order adbc`：复核二次 `4×8` 盘面没有精确覆盖或横跨词。
- `work/pasted_graph.py`：复核相同字母圆连接/合并后的 3 种拓扑均无唯一读串。
- `work/visual/diagram_inventory/`：题面八条四圆 strand 和七个 `×2` 的稳定原图证据。
- `work/visual/final_diagram_audit.md`：提示标题与最后一图的可见/不可见信息审计。
- `work/visual/flying_scs.tsv`：已判错路线中四种端点方向及最短交织结果。
- `work/visual/endpoint_geometry.tsv`：原盘端点纵坐标不能唯一决定四圆上下次序的负证据。
- `work/visual/paste_4_on_2.tsv`：把已判错的 `42` 当作 `PASTE 4 ON 2` 参数也不能闭合的负证据。
- `artifacts/dna-overlap.svg/png`：保留已否定的 DNA/`ECORI` 路线，仅作负证据。
- `artifacts/overlap-binary.svg/png`、`endpoint-chain.svg/png`：保留已判错的 `42` 与旧交叉读 `PASTE`，仅作防重复负证据。

## Important failed routes

- **`BINGO`**：用户明确报告不是答案。把 Board 5 的前三圆 `ING` 覆盖到 Board 4
  `FLNO` 的前三圆可机械得到 `INGO`，再沿旧 `N/N` 配对读出 `BINGO`，但最终图没有
  授权保留被覆盖的配对或指定从 `BINO` 顶端起读；该操作不能恢复。
- **`FLOUNDERING`**：用户明确报告不是答案。把 `ON` 与 `ING` 的相同字母值 `N`
  当作一个可移动节点，留下 `O`，再把 `ING` 排在 `FLO` 上方，确实能构成
  `FLO UNDER ING`，但题图没有授权这种物理合并或空间 rebus；不得恢复。
- **`NASTY`**：用户明确报告不是答案。内部 strand 的单一物理圆若同时参与左右公共对，确实依次给出 `N/A/S/T`，但从最后一个 `T` 沿终端 `NETY` 续取 `Y` 没有图示依据；题句与 Hobbes 语句的对应也只是后验联想。整条路线不再恢复。
- **`FLING`**：用户明确报告不是答案。错误在于把 “paste ... on ...” 当成字符串拼接；当前候选改为移动共用 `N` 的完整 `ING` 路径并读取空间 rebus，不再使用 `fling = cast` 的同义跳转。
- **`FLYING`**：用户明确报告不是答案。旧路线把右端 `NY` 反读为 `YN`，再对 `FL / YN / ING` 做最短公共超序列；“把两端都作为材料”和 SCS 均非图上指令。
- **`GAATTC / ECORI`**：用户明确否定序列和酶名。DNA 字母筛选本身可重复，但 `FLING → CAST`、补 `C` 和把识别位点命名为答案都不是题图强制步骤。
- **`PASTEUR`**：用户明确报告不是答案；`UR` 没有任何字母级来源，只是借“生命”补成人名。
- **`PASTE / COPY AND PASTE / CUT AND PASTE` 作为答案**：用户均已明确否定。`PASTE` 现在只作为七条公共边中可复核的操作词，不恢复为终答。
- **`42`**：用户明确报告不是答案。取“右侧新 strand 顶圆是否属于重叠”可造出 `0101010₂`，但选右侧、选顶排和二进制极性都未受充分指示。
- 每盘只覆盖 44 格并留下四字是伪机制；它依赖截短词或错误复数。正确机制是完整覆盖 48 格后取 spangram 两端。
- Board 4 的 `IFHT/RING/NORI` 剩余格、Board 5 的 `GNIN`、Board 8 的伪复数 `STRATOLIFTERS` 均属于 44 格失败路线；后者还会自交。
- Board 6 的 Minecraft、Rain World、Pokémon、天气词表和通用词频覆盖未闭合；正确主题是 `BLUE` 的忧郁义。Board 7 只搜国家名不完整，须加入 `PANAFRICANISM`。Board 8 是 Boeing 双关。
- 四圆上下次序不能从题图箭头、编号或颜色确定；原盘纵坐标检验在 8 盘中有 6 盘出现同行并列，仍产生 2–4 种次序。
- 四排 7-bit ASCII 可在自然参数下排出 `UP/*` 或其互补/倒序，但“取左侧还是右侧、重叠为 0 还是 1、上下方向”都未由图固定；相邻列 8-bit、Braille、位置映射 DNA、Watson–Crick 配对、翻译密码、最短公共超序列、行列换位与普通词路径也均无唯一结果，同类编码不再扩大。
- 完整 spangram 的固定/D4 叠合、端点双锚刚体配准、`4×8` 二级 Strands、普通 PASTE 精确对齐和新增字母分词均未闭合。
- 把已判错 `42` 解释为 `PASTE 4 ON 2`：固定叠盘只有无读序的 `U/H/S/R` 四个同位同字格；两条 spangram 同占三格却没有同字，双端锚配准为 0。
- 七个公共对各选一字共有 `2^7=128` 种；链正反两向在固定十万词表中均为 0 个七字词命中。
- 相邻完整 spangram 扣除端点公共对后，每对都留下 2–5 个额外共同字母，没有任何一对恰留一个强制字母。
- 合并 `×2` 后的 18 字按奇偶拆为两条 9 字 strand：四种自然端点次序、链正反、全部整股正反和重复 `N` 选择共 2304 个贡献串，双词和单词命中均为 0。
- **四圆交织几何**：自然的 `a,d,b,c` 放置不能固定绝对朝向；无交叉配线仅给出互补的 `2/L` 方向码，四排 7-bit 掩码也不成唯一文字。不得把 `2`、`L` 或它们的组合升级为候选。
- **二次方阵与连接图**：`a,d,b,c` 的 `4×8` 盘没有精确 Strands 覆盖、没有横跨词；`NAMASTE/MATTERS` 是高密度字母盘中的偶然路径。三种同字母连接拓扑也没有唯一长读串；不再从其中挑普通词或做语义补全。
- **`FLUCTUATING → NORI/IRON`**：旧路线错误保留 `WAVE`，因而让 `RING` 的 `R,I` 都落空，得到不连通的 `N,O,R,I` 并任意反读 `IRON`。正确执行会把 `WAVERING` 只截成 `WAVER`，保留 `R` 的覆盖，余格是同列 `ION`；`IRON` 仍不得恢复。
- **`ION`**：用户明确报告不是答案；Board 4 的 45 格重铺虽可复核，但没有题图或提示授权把该余格升级为终提取。
- **`ECORI`**：用户明确报告不是答案；此前把中间 DNA 识别位点升级为酶名，属于无授权的语义补全。

## Next action

重新审计最后图的 `×2`：不要把公共字母集合当作物理连接；为每个相邻 strand
保留两个匹配字母的**具体圆位**，枚举正向/反向交织后的配对位置，并从题句“正反
交织配对、交叠之处”寻找直接字母读法。需要一个不依赖英文同义词或 rebus 的候选；
不得恢复已否定的 `FLOUNDERING`、`BINGO`、`ION`、`FLING`、`GAATTC` 或 `ECORI`。
