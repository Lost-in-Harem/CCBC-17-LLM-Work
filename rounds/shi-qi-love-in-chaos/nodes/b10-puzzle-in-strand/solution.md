---
node_id: b10-puzzle-in-strand
title: 刻在strands里的谜题
kind: puzzle
round: shi-qi-love-in-chaos
parent:
source:
round_feeder: yes
feeders:
status: candidate
answer: ION
confidence: high
summary: "候选 ION：八条 spangram 的首末两字按相邻恰共享两字排成唯一链 4-2-5-1-7-3-8-6；公共边分块与左端余字给出 PASTE ING ON FL。FL 指向第 4 盘的 FLUCTUATION，供体 WAVERING 提供 ING；将 WAVERING/FLUCTUATION 改成 WAVER/FLUCTUATING 后，固定主题词只有一个合法 45 格覆盖，余下同列三格自下而上为 I-O-N。"
updated: 2026-08-16
---

# 刻在strands里的谜题

## Current conclusion

当前候选为 **`ION`**，置信度高。它保留此前已确认的八盘完整解与唯一链，但不再把 `PASTE ING ON FL` 停在用户已否定的裸拼接 `FLING`：`FL` 是对第 4 盘 spangram `FLUCTUATION` 的选择器，`ING` 则可从同盘完整主题词 `WAVERING` 取得。

执行移动后，`WAVERING → WAVER`，`FLUCTUATION → FLUCTUATING`。这六个固定主题词在第 4 盘所有合法路径中只有一个不相交、不交叉的 45 格覆盖；余下三格全在第 6 列，分别为 `r8c6=I、r6c6=O、r5c6=N`。沿移动方向自下向上读得 `ION`，也正是 `FLUCTUATION` 改为 `FLUCTUATING` 时被替换的原后缀。

此前的 `NASTY`、四圆几何、二次 `4×8` Strands 和普通连接图仍只作为负证据：它们都没有给出这一组“可执行指令 → 唯一重铺 → 同列余字”的三重闭合。

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

### 1. 每条 spangram 的两端各取两字，并保留原词方向

每条 spangram 都从盘面左边界走到右边界。取首二字与末二字，并按原词从左到右的次序放入四圆；即 `first, second, penultimate, last`。四圆的顺序不是任意排列，因为后续要判断同一个**字母出现位置**是否被左右两侧同时配到。

| Board | Spangram | 四圆 strand |
| ---: | --- | --- |
| 1 | `APPREHENDING` | `APNG` |
| 2 | `BIATHLON` | `BION` |
| 3 | `CARDIOLOGIST` | `CAST` |
| 4 | `FLUCTUATION` | `FLON` |
| 5 | `INCORPORATING` | `INNG` |
| 6 | `NEGATIVITY` | `NETY` |
| 7 | `PANAFRICANISM` | `PASM` |
| 8 | `STRATOLIFTER` | `STER` |

### 2. `×2` 强制唯一链

要求每对相邻 strand 恰有两个**不同**公共字母。枚举八条 strand 的所有排列只得到一条 Hamilton 链及其整体反转：

```text
4 - 2 - 5 - 1 - 7 - 3 - 8 - 6
FLON  BION  INNG  APNG  PASM  CAST  STER  NETY
```

相邻公共对依次为：

```text
NO / IN / GN / AP / AS / ST / ET
```

### 3. 公共边给出指令，并在第 4 盘重铺

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

### 4. 已否定：读取被左右两侧同时配到的同一个圆

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

### 5. 已否定：从最后的双配圆走到 spangram 右端

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
- 七个公共边连成的四块与左端余字给出 `FL | ON | ING | PASTE`；反向按块读成唯一通顺且可执行的命令 `PASTE ING ON FL`。
- `FL` 指向 Board 4 的 `FLUCTUATION`，同盘完整词 `WAVERING` 提供 `ING`。替换为 `WAVER/FLUCTUATING` 后，对所有合法路径穷举只得一个 45 格覆盖；余下 `r8c6/r6c6/r5c6` 同列向上为 `ION`。
- 四圆按 spangram 左到右的真实顺序放置为 `FLON/BION/INNG/APNG/PASM/CAST/STER/NETY`；这让“同字母集合”提升为“同一个圆的出现位置”。
- 六个内部 strand 的所谓强制双配读数为 `N/-/-/A/S/T`；它只是一个可重复的局部统计，不是已确认提取。
- “末个 `T` 配入 `NETY` 后继续取 `Y`”已被用户反馈否定，不能再用于确定链方向。
- 图形左右交替最自然地把四个端点排成 `a,d,b,c`。对唯一链两向各枚举 256 个整股翻转：要求七组配线均不交叉时只剩互补方向码 `00110010`（ASCII `2`）和反向的 `01001100`（ASCII `L`），但绝对朝向不受图示固定；更严格的距离/朝向最优解反而不可打印。`L/2` 只能视为局部巧合。
- 将 `a,d,b,c` 的 32 个字母排成 `4×8` 二次盘面，词库中虽可走出 `NAMASTE`、`MATTERS` 等普通词，却没有精确覆盖，也没有任何候选词横跨左右边界；这一族已停止。
- 按七个 `×2` 真正连接相同字母，并穷举 Board 5 两个 `N` 的物理配法，只得到 3 种不同拓扑；均无唯一长路径或与题意对应的目标串。把连接图继续当普通字谜只会制造短词噪声，因此也已停止。
- 旧的 `NORI/IRON` 冲突来自错误地把 `WAVERING` 截成 `WAVE`，于是多留了 `R`。按完整词真正移走后保留的是 `WAVER`，`R` 仍被覆盖，唯一余格因此从四个降为同列三个 `ION`；这是一条新的、可复核的机制证据，不恢复 `IRON`。
- 题句“生命的真相”与 Hobbes 语句的语义呼应属于诱导性的结果后验，不是机制证据。
- 用户否定 `FLING` 只否定了把 `FL+ING` 裸拼后停下。`PASTE ING ON FL` 现在由 Board 4 的 `WAVERING → WAVER`、`FLUCTUATION → FLUCTUATING` 以及唯一 45 格覆盖提供了独立闭合。

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

## Evidence and artifacts

- `artifacts/extraction.md`：精简记录完整 spangram、唯一链、`PASTE ING ON FL` 与 Board 4 的 `ION` 重铺提取。
- `artifacts/ion-extraction.svg/png`：候选提取的坐标示意，标出 `WAVER`、`FLUCTUATING`、移入的 `NG` 与同列余字 `ION`。
- `artifacts/nasty-extraction.svg` 与渲染后的 PNG：已否定路线的可视化，仅作防重复负证据。
- `artifacts/fling-extraction.svg/png`：已判错 `FLING` 的旧词图分块，现已明确标为 `REJECTED`。
- `artifacts/flying-extraction.svg/png`：已判错 `FLYING` 的旧最短交织，仅作防重复负证据。
- `artifacts/verify_solution.py`：标准库复核八盘精确覆盖、唯一链、Board 4 唯一 45 格重铺与候选 `ION`，并保留用户否定路线的负证据审计。
- `work/solve_strands.py`：探索阶段的铺盘搜索器；`--full` 输出完整路径，`4 --paste-board4` 穷举候选重铺。
- `work/extraction_hypotheses.py`：`--double-overlap` 参数化复核当前提取；其余参数保留已停止路线的有界审计。
- `work/extraction_hypotheses.py --glyph-weave`：复核 `a,d,b,c` 四圆交织与 256 个整股翻转的几何负证据。
- `work/endpoint_grid_search.py` 与 `work/nested_strands.py --endpoint-order adbc`：复核二次 `4×8` 盘面没有精确覆盖或横跨词。
- `work/pasted_graph.py`：复核相同字母圆连接/合并后的 3 种拓扑均无唯一读串。
- `work/visual/diagram_inventory/`：题面八条四圆 strand 和七个 `×2` 的稳定原图证据。
- `work/visual/final_diagram_audit.md`：提示标题与最后一图的可见/不可见信息审计。
- `work/visual/flying_scs.tsv`：已判错路线中四种端点方向及最短交织结果。
- `work/visual/endpoint_geometry.tsv`：原盘端点纵坐标不能唯一决定四圆上下次序的负证据。
- `work/visual/paste_4_on_2.tsv`：把已判错的 `42` 当作 `PASTE 4 ON 2` 参数也不能闭合的负证据。
- `artifacts/dna-overlap.svg/png`、`overlap-binary.svg/png`、`endpoint-chain.svg/png`：分别保留已判错的 `GAATTC`、`42` 与旧交叉读 `PASTE`，仅作防重复负证据。

## Important failed routes

- **`NASTY`**：用户明确报告不是答案。内部 strand 的单一物理圆若同时参与左右公共对，确实依次给出 `N/A/S/T`，但从最后一个 `T` 沿终端 `NETY` 续取 `Y` 没有图示依据；题句与 Hobbes 语句的对应也只是后验联想。整条路线不再恢复。
- **`FLING`**：用户明确报告不是答案，因此 `FL+ING` 的裸拼结果不得恢复。新证据只复用 `PASTE ING ON FL` 作为中间指令：它作用于 Board 4 的完整词并留下 `ION`，不是把 `FLING` 改名重报。
- **`FLYING`**：用户明确报告不是答案。旧路线把右端 `NY` 反读为 `YN`，再对 `FL / YN / ING` 做最短公共超序列；“把两端都作为材料”和 SCS 均非图上指令。
- **`GAATTC`**：用户明确报告不是答案。该路线从公共对筛 `A/C/G/T` 得 `GAATT`，再取唯一未配对碱基 `C` 并补成反向互补回文；“只留 DNA 字母”“把 PASTE 当补字操作”“要求回文闭合”均非题面逐字强制。不得改猜 `ECORI`。
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

## Next action

请用户手动提交候选 **`ION`**。若判对，将状态改为 `accepted`；若判错，记录反馈并回到“公共边分块为何选择反向指令语序”这一唯一尚可能受提示 11/12 正文影响的环节，不再扩展已停止的几何、二次方阵或普通词库搜索。
