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
summary: "EQUALS SIGN 已被用户明确判错。稳定事实只保留八条 spangram、提示 12 顺序、A/C/G/T 片段与 DNA 翻译 MINIFYHAVE；四圆互补布局 FFRRRRFR 可复现，但把方向任意记成二进制并按 ASCII 读取为 '=' 的整条终答解释现已撤回。"
updated: 2026-08-30
---

# 刻在strands里的谜题

## Current conclusion

当前没有可提交候选。**`EQUALS SIGN` 与 `FALSE` 均已被用户明确判错**。

提示 10 明确要求使用每盘唯一、跨越两端的词，即八条 spangram，并在这些词中
寻找“生命的真相”。提示 11 图把最后的 strand 画成由氢键连接的蛋白质 β 股，
提示 12 则给出八词顺序。三条提示合起来给出一条不依赖旧端点链的完整遗传密码
提取：

1. 将每条 spangram **缩减（minify）**为其中的 `A/C/G/T`，保持原次序；
2. 六条结果已经是四碱基，Board 1 与 2 只有两碱基；按每股四圆的模板，将这两
   个二碱基片段各重复一次以补成四位；
3. 按提示 12 的 `2-6-7-8-4-5-3-1` 拼接；
4. 从首个生物学起始密码子 `ATG` 开始翻译成氨基酸单字母码；
5. 将八个四碱基股整体正读或反读，要求每个相邻 `x2` 恰有两处同位
   Watson-Crick 互补；固定第一股正读后，唯一方向为 `FFRRRRFR`；
6. 此前把正反方向任意记作 `0/1` 并按 ASCII 读取为 `=`，但 `EQUALS SIGN`
   已被判错；方向布局只保留为可复核观察，不再视作终答提取。

## Confirmed Strands solves

八盘都是标准 `8×6` Strands：主题词完整覆盖 48 格，词路径不复用格子且不自交、
不互交。每盘恰有一个主题词从左边界横跨到右边界。

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

Board 6 用 `BLUE` 的“忧郁”义统摄消极情绪；Board 7 的五面国家旗帜使用三色，
`PANAFRICANISM` 对应泛非三色；Board 8 的“音波”倒转为“波音”，主题词都是
Boeing 飞行器名称或绰号。

## Hint evidence supplied by the user

- 提示 1：八盘都是 NYT Strands；词可沿八邻接弯曲，每格恰属于一个主题词。
- 提示 10（2026-08-29 提供）：

  > 你需要用到那些“跨越思绪两端”的单词，这些单词在每个方阵中有且仅有一个。
  > 随后找出这些单词中“生命的真相”。

  “跨越两端且每盘唯一”指 spangram；“生命的真相”指从这些词中保留 DNA
  字母 `A/C/G/T`。
- 提示 11（2026-08-29 提供）：只有一张详细图。稳定副本为
  `work/visual/hint11/assets/image-001.jpg`，SHA-256 为
  `77d3828d90c69631fb91d4c4f434127af2691adb35c35039428ed18093c971f7`。
- 提示 12（2026-08-29 提供）：

  > 提取时八个词的顺序是什么？
  >
  > 按照如下的方阵顺序：来自二月的汗水、我的世界在下雨、我只给你三个颜色、
  > 凌云的倒转音波、唯有变是不变的、博采众长，兼容并蓄、十字军、
  > 放开人质，举起手来！

  对应 Board 顺序 `2,6,7,8,4,5,3,1`。

## Hint 11 visual audit

### Observed facts

坐标模型复核出：

- 五个错位水平层的圆数为 `6,6,7,6,6`，共 31 个可见圆；
- 23 段黑色斜向实线；
- 七条横向虚线；
- 圆环与填色只随垂直层级从中央黑色向外变浅，不按八个词分别着色。

稳定标注见 `artifacts/hint11-annotated.png`，全部坐标及边见
`work/visual/hint11/geometry.tsv`。因此这张图不应被当成一张可逐格填入 32 个
端点字母的字母方阵；31 只是该蛋白质示意图的可见节点数。

### Interpretation

锯齿实线对应多肽主链，链间虚线对应氢键，整体与蛋白质 β 股/β 折叠的画法一致。
这同时解释题面反复使用的 `strands`，并授权从 DNA 到蛋白质的标准翻译。

## DNA extraction

先只保留每条 spangram 里的 `A/C/G/T`：

| Hint-12 position | Board | Spangram | A/C/G/T | 四圆片段 |
| ---: | ---: | --- | --- | --- |
| 1 | 2 | `BIATHLON` | `AT` | `ATAT` |
| 2 | 6 | `NEGATIVITY` | `GATT` | `GATT` |
| 3 | 7 | `PANAFRICANISM` | `AACA` | `AACA` |
| 4 | 8 | `STRATOLIFTER` | `TATT` | `TATT` |
| 5 | 4 | `FLUCTUATION` | `CTAT` | `CTAT` |
| 6 | 5 | `INCORPORATING` | `CATG` | `CATG` |
| 7 | 3 | `CARDIOLOGIST` | `CAGT` | `CAGT` |
| 8 | 1 | `APPREHENDING` | `AG` | `AGAG` |

Board 2 与 Board 1 的两字串各重复两次，使八股都恰有四个碱基。拼接为：

```text
ATATGATTAACATATTCTATCATGCAGTAGAG
```

首个 `ATG` 在第 3 个碱基开始；其后恰为 30 个碱基、10 个完整密码子：

```text
ATG ATT AAC ATA TTC TAT CAT GCA GTA GAG
 M   I   N   I   F   Y   H   A   V   E
```

标准氨基酸单字母码给出：

```text
MINIFY HAVE
```

原始图还直接要求使用八个四圆股的“正反、配对、交叠”。固定第一股按提取顺序
正读，枚举其余七股的 `2^7=128` 种整体方向；仅保留每个相邻间隙都恰有两处
同一圆位呈 Watson-Crick 互补的布局。唯一结果为：

| 位置 | Board | 定向后碱基 | 方向 | 与右邻互补的圆位 |
| ---: | ---: | --- | :---: | --- |
| 1 | 2 | `ATAT` | F | `2,3` |
| 2 | 6 | `GATT` | F | `3,4` |
| 3 | 7 | `ACAA` | R | `1,4` |
| 4 | 8 | `TTAT` | R | `2,3` |
| 5 | 4 | `TATC` | R | `2,3` |
| 6 | 5 | `GTAC` | R | `1,2` |
| 7 | 3 | `CAGT` | F | `1,4` |
| 8 | 1 | `GAGA` | R | `-` |

将 F/R 分别记作 `0/1`：

```text
FFRRRRFR -> 00111101 -> ASCII 61 -> =
```

这里的 `x2` 已经用于要求每个相邻间隙有两处互补圆位，不应再作用一次。
Python 本地 Unicode 字符数据库把 `=` 命名为：

```text
EQUALS SIGN
```

因此当前候选为 **`EQUALS SIGN`**。此前曾把 `x2` 错当成“将所得字符重复”，
再把 `==` 置于蛋白质译文的自然两词分界：

```text
MINIFY == HAVE  ->  FALSE
```

用户已明确判错 `FALSE`，所以该布尔解释只作负证据。方向、互补圆位、全局镜像
与编码对称性由 `work/dna_pairing.py` 穷举复核，结果见
`work/visual/dna_pairing.tsv`。

### Disclosed residual details

- 32 碱基串有两个前导碱基；首个 `ATG` 自然且唯一地选出第三阅读框，另外两框都
  很快遇到终止密码子并不成英文。
- 编码区末尾没有终止密码子，但从 `ATG` 到串尾正好是 30 个碱基，不影响十个
  氨基酸单字母码的唯一读取。
- `MINIFYHAVE` 没有空格编码；`MINIFY | HAVE` 是唯一自然的两词切分。
- 不固定首股时还有全局镜像 `RRFFFFRF`。提示 12 固定从左到右的词序，以首股
  正读作图的纵向锚，并把“发生反转”记为 1，才得到 `=`；交换 0/1 或反转提示
  顺序分别得到十进制 `194`、`188` 或字符 `C`。这项约定依赖已明确披露，故
  候选置信度暂不升至 high。
- 七个匹配圆位的组合序号为 `4,6,3,4,4,1,3`，四位掩码为 `63966C9`；内部
  同时向左右配对的圆读作 `T/A/-/AT/T/C`。两种直接几何读数都不成词，未拿来
  反选答案。
- 裸 `A`、蛋白质扩写 `ALANINE` 和 DNA 扩写 `ADENINE` 均已被判错；三者都不再
  是可提交候选。
- `SHAVE` 已被判错；普通字谜补入 `S` 的路线停止。
- 对两个整词分别取全局最小质量会得到 `I/A`，其扩写 `CURRENT` 已被判错；逐位
  质量比较得到的 `NAVE` 也已被判错。整个氨基酸质量指标族停止。
- 四种 `HAVE` 读向与共享 `Y` 的前后位置共八种虽只有 `HEAVY` 是普通词，但
  `HEAVY` 已被判错；结果见 `work/reduce_have.py` 与
  `work/visual/reduce_have.tsv`，仅作负证据。
- 八条未补齐的 DNA 片段共有 28 个碱基，恰为 `7×2×2`。若要求七个相邻间隙
  各形成两对 Watson-Crick 互补碱基并让每个碱基恰用一次，按提示 12 顺序只有
  一个碱基计数分配。扩展重复字母的发生位置后有 72 种配对，但没有一种能实现
  所有横键等距；它是计数校验，不是当前四圆同位模型。两者均见
  `work/dna_pairing.py` 与 `work/visual/dna_pairing.tsv`。
- 把 `=` 当作 Base64 填充补到 `MINIFYHAVE` 后只得到不可读字节；对四碱基股做
  两位后缀—前缀的同一、互补或反向互补交叠也都无布局。这两个分支均已停止。
- 提示 11 的 31 个可见圆是蛋白质结构线索，不与 32 个碱基一一对应；强行逐圆
  填字曾产生大量无规则输出，现已停止。

## Submission history

只记录用户或比赛网站明确反馈过的提交。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-16 | COPY AND PASTE | rejected | 用户明确报告不是答案。 |
| 2026-08-16 | PASTE | rejected | 用户明确报告也不是答案。 |
| 2026-08-16 | CUT AND PASTE | rejected | 用户明确报告也不是答案。 |
| 2026-08-16 | 42 | rejected | 用户明确报告不是答案。 |
| 2026-08-16 | PASTEUR | rejected | 用户明确报告不是答案，并指出该路线属于无字母依据的联想。 |
| 2026-08-16 | GAATTC | rejected | 用户明确报告不是答案。 |
| 2026-08-16 | FLYING | rejected | 用户明确报告不是答案，并提供提示列表。 |
| 2026-08-16 | FLING | rejected | 用户明确报告不是答案。 |
| 2026-08-16 | NASTY | rejected | 用户明确报告不是答案。 |
| 2026-08-16 | ION | rejected | 用户明确报告不是答案。 |
| 2026-08-16 | ECORI | rejected | 用户明确报告不是答案。 |
| 2026-08-16 | BINGO | rejected | 用户明确报告不是答案。 |
| 2026-08-17 | FLOUNDERING | rejected | 用户明确报告不是答案。 |
| 2026-08-17 | MEANING | rejected | 用户明确报告答案不对。 |
| 2026-08-17 | FLUCTUATING | rejected | 用户明确报告不是答案。 |
| 2026-08-29 | FLEETING | rejected | 用户明确报告答案错误；该路线依赖错误端点链且缺少图示授权。 |
| 2026-08-29 | A | rejected | 用户明确报告不是答案，并提供提示 10；`A` 现保留为执行 `MINIFY HAVE` 后的中间 DNA 符号，而非完整提交答案。 |
| 2026-08-29 | HAVE | rejected | 用户明确报告答案不正确；`MINIFYHAVE` 不能简单切成“已执行的方法 + 终答”。 |
| 2026-08-29 | CONTRACT | rejected | 用户明确报告不是答案；`MINIFY/HAVE` 的双定义解释撤回。 |
| 2026-08-29 | ALANINE | rejected | 用户明确报告答案不正确，并给出完整提示列表；按 H/A/V/E 残基大小选 A 没有提示授权。 |
| 2026-08-29 | ADENINE | rejected | 用户明确报告不是答案；把递归过滤所得 `A` 扩写为 DNA 碱基名没有进一步授权。 |
| 2026-08-29 | VALINE | rejected | 用户明确报告不是答案；按 H/A/V/E 氨基酸全名长度选四者最短不成立。 |
| 2026-08-30 | CURRENT | rejected | 用户明确报告不正确；`I/A` 的量符号—单位符号扩写不是终答。 |
| 2026-08-30 | HALVE | rejected | 用户明确报告不正确；不能把原图的 `x2` 反向解释成对 `HAVE` 插入 `L` 的终答。 |
| 2026-08-30 | LEUCINE | rejected | 用户明确报告不是答案；`HALVE` 的新增字母 `L` 不能再扩写为氨基酸名。 |
| 2026-08-30 | LIGHTEN | rejected | 用户明确报告不正确；`MINIFY HEAVY` 不能直接释为及物动词 `LIGHTEN`。 |
| 2026-08-30 | HEAVY | rejected | 用户明确报告不正确；`HAVE -> HEAV + Y` 的整条尾解撤回。 |
| 2026-08-30 | SHAVE | rejected | 用户明确报告不正确；`S(small) + HAVE` 的普通字谜解释撤回。 |
| 2026-08-30 | NAVE | rejected | 用户明确报告不正确；按分子量逐位取较小残基并以成词性选择右对齐的路线撤回。 |
| 2026-08-30 | FALSE | rejected | 用户明确报告答案不正确；将 ASCII `=` 按图示 `x2` 扩成 `==` 并比较 `MINIFY` 与 `HAVE` 的布尔真值路线撤回。 |
| 2026-08-30 | EQUALS SIGN | rejected | 用户明确报告答案不正确；将四圆方向任意编码为二进制并按 ASCII 字符名提交的路线撤回。 |

## Important failed routes

- **旧 `x2` 端点链全家族**：`4-2-5-1-7-3-8-6` 虽是“相邻四字集合恰有两个
  公共字母”的唯一 Hamilton 链及反向，但提示 12 指定了不同顺序。由它导出的
  `PASTE ING ON FL`、`FLEETING`、`FLOUNDERING`、`BINGO`、`NASTY`、
  `FLING/FLYING`、DNA/`ECORI`、Board 4 重铺及余格 `ION` 均不得恢复。
- **官方顺序下的端点路线**：相邻公共数为 `1/0/1/0/1/0/1`；端点二次 Strands、
  整词/整盘叠合、双交叉、普通换位和 `42` 二进制联想均无唯一输出。
- **31 圆逐格填字**：图的实线组件含 `3/2/5/5/5/5/3/3` 个圆，不是八条四圆
  字槽；将 31 个端点字母按行列蛇形填入，再读虚线端点也不能形成统一路径。
- **把中间符号 `A` 直接提交**：用户已明确判错；递归保留 `A/C/G/T` 不是
  `MINIFY HAVE` 在蛋白质层级中的终操作。
- **把 `MINIFY | HAVE` 直接拆成方法与答案**：`HAVE` 已被用户明确判错；它是
  `MINIFY` 的操作数，而不是可直接提交的答案。
- **`MINIFY/HAVE -> CONTRACT` 双定义**：虽然 `contract` 可表示缩小，也可表示
  染上疾病，但用户已明确判错，不能再作为终答。
- **`H/A/V/E` 中最小残基 -> ALANINE**：用户已明确判错；提示列表没有要求查询
  氨基酸质量或侧链体积，该步骤属于额外解释。
- **`HAVE -> A -> ADENINE`**：用户已明确判错；即使 `HAVE -> A` 可复现，把中间
  符号扩写为碱基全名仍是未受提示授权的语义补全。
- **只按“一次编辑 + 宽泛近义词”排序**：本地 WordNet 同时得到 `HALVE`、
  `SHAVE`、`SAVE`，裸条件不唯一；此前用 `x2` 偏向 `HALVE`、再用原位字谜
  `S(small) + HAVE` 偏向 `SHAVE` 均已被判错，不能恢复这一词族。
- **`H/A/V/E` 全名中选最短 -> VALINE**：四个名称长度确为 `9/7/6/12`，但用户
  已明确判错；`MINIFY HAVE` 不是一个从四个残基名称中选四选一的指令。
- **对两个肽词按平均分子量最小化 -> `I/A -> CURRENT`**：计算本身可复现，
  但用户已明确判错；提示没有指定质量指标，从量符号和单位符号扩写物理量也是
  第二次未授权语义跳跃。
- **把一编辑结果 HALVE 直接提交**：虽然 `HALVE` 是 `HAVE` 插入 `L` 且表示
  除以二，但用户已明确判错；不得再把整词或 `+L` 恢复到现路线。
- **`HALVE` 的新增码 `L -> LEUCINE`**：用户已明确判错；这说明一编辑近义词族
  不能通过“再扩写氨基酸名”挽救，`SERINE` 等平行候选也不应直接提交。
- **`MINIFY HEAVY -> LIGHTEN`**：`HEAVY` 的字母构造可复现，但用户明确判错
  `LIGHTEN`；把命令改写成另一个同义动作动词，没有说明操作后的结果词形。
- **`HAVE -> HEAV + Y -> HEAVY`**：用户已明确判错；即使八种局部读法中只有
  `HEAVY` 成词，题面也未授权只交织 `HAVE`、只取 `MINIFY` 的末字。整条尾解
  作废，不能再由它改猜 `LIGHT/LIGHTER`。
- **`S(small) + HAVE -> SHAVE`**：用户已明确判错；即使它唯一满足“保留 HAVE、
  前置尺寸码 S、具有 reduction sense”，`S` 仍不是图示直接提取的字母。普通
  字谜补字路线停止。
- **`MINIFY/NIFY` 与 `HAVE` 逐位取轻残基 -> NAVE**：用户已明确判错；分子量
  指标及右端对齐都不是题图直接指定的约束，“12 项中唯一成词”只是字典筛选，
  不能作为机制。整个氨基酸质量比较族停止。
- **`FFRRRRFR -> '=' -> '==' -> FALSE`**：用户已明确判错。四圆同位互补约束确实
  唯一给出方向串，但把 F/R 指派为 0/1、再把图中 `x2` 当成重复等号、最后对两
  个英文词求程序语言布尔值，是连续三层未受题面授权的解释。保留方向布局和
  `=` 这一可复核观察，撤回 `==` 与 `FALSE`。
- **`FFRRRRFR -> 00111101 -> '=' -> EQUALS SIGN`**：用户已明确判错。首股正读
  只是人为锚点，F/R 到 0/1 也没有题面规定；交换映射或镜像会改变字节。因此
  `=` 的字符名不是终答，ASCII 方向位假设族停止。

## Evidence and artifacts

- `artifacts/extraction.md`：候选 `EQUALS SIGN` 的 DNA、肽译文、四圆定向与
  对称性精简复现版；旧 `FALSE` 结论只作负证据。
- `artifacts/verify_solution.py`：复核八盘完整覆盖、DNA 片段、起始阅读框、密码子
  翻译、首股锚定下唯一四圆方向 `FFRRRRFR`、ASCII `=` 与标准名称
  `EQUALS SIGN`；旧 `MINIFY == HAVE -> FALSE` 及 `NAVE`、`SHAVE`、
  `HEAVY/LIGHTEN` 等只作负证据。
- `artifacts/hint11-annotated.png`：提示 11 的稳定坐标标注。
- `work/hint11_model.py`：提示 11 几何模型生成器。
- `work/visual/hint11/geometry.tsv`：31 圆、23 实线段、七虚线的坐标表。
- `work/visual/final_diagram_audit.md`：提示 11/12 后的视觉审计。
- `work/minify_have.py` 与 `work/visual/minify_have.tsv`：一次编辑词族的参数化
  负证据；“保留 HAVE、前置尺寸码 S、具有 reduction sense”虽唯一选出
  `SHAVE`，但已被用户明确判错。
- `work/reduce_have.py` 与 `work/visual/reduce_have.tsv`：四种自然读向及共享 `Y`
  前后位置的八项有界审计；其唯一普通词 `HEAVY` 已被判错，现为负证据。
- `work/dna_pairing.py` 与 `work/visual/dna_pairing.tsv`：28 个原始 DNA 字母的
  唯一互补计数分配、72 项发生位置负审计，以及四圆同位模型的全局镜像、首股
  锚定方向 `FFRRRRFR -> 00111101 -> '=' -> EQUALS SIGN` 和直接圆位负审计。
- `work/amino_minification.py` 与 `work/visual/amino_minification.tsv`：质量与
  名称长度的旧全局对照，以及两股正反、三个完整交叠偏移的 12 项逐对质量
  负审计；其唯一普通词 `NAVE` 已被明确判错。
- `work/visual/hint12_*.tsv`：旧端点机制在官方顺序下的有界负证据。
- `artifacts/*-extraction.*`、`dna-overlap.*`、`overlap-binary.*`、
  `endpoint-chain.*`：均是明确标记的历史失败路线，不代表当前机制。

## Next action

保留 `MINIFYHAVE` 与互补布局，但撤回全部 ASCII/字符命名。下一步只审计
`MINIFYHAVE` 是否应整体作为答案，或应作为“minify what you have”的自指指令
作用于八个已提取片段；优先寻找无需新增语义、物性指标或字典反选的直接结果，
不恢复 `=/==/FALSE`、语义近义词或分子量尾解。
