---
node_id: b10-puzzle-in-strand
title: 刻在strands里的谜题
kind: puzzle
round: shi-qi-love-in-chaos
parent:
source:
round_feeder: yes
feeders:
status: accepted
answer: INFLOOD
confidence: high
summary: "用户已明确确认 INFLOOD 正确。将 28 个 A/C/G/T 出现位置映回提示 12 顺序下的八个完整 spangram，并要求每处 ×2 为水平 Watson-Crick 配对，只剩两个布局；提示 11 详细图的可见圆数和七条虚线唯一选中 FRFRFRFR、偏移 0,-3,-3,-2,2,5,7,7。七个相邻词各恰有一个相同普通字母交叠，依次读出 INFLOOD。"
updated: 2026-08-30
---

# 刻在strands里的谜题

## Current conclusion

答案 **`INFLOOD`**（自然分词 **`IN FLOOD`**）已由用户明确确认正确，状态为
`accepted`。

提示 10 选出八条 spangram 并从中保留生命字母 `A/C/G/T`；提示 12 固定顺序
`2-6-7-8-4-5-3-1`。八段长度正好是 `2,4,4,4,4,4,4,2`，所以 28 个碱基出现
恰可各用一次，填满图中 `7 间隙 × 2 对 × 2 端点`。把这些碱基映回完整
spangram 的原位置并让整词正读或反读，只剩两个水平配对布局。

提示 11 的详细图不是泛化的蛋白质示意：它的八股可见圆数
`3,2,5,5,5,5,3,3` 与七条可见虚线，逐项唯一匹配布局
`FRFRFRFR`、纵向偏移 `0,-3,-3,-2,2,5,7,7` 的第 `9..5` 行裁窗。
在这个被图唯一指定的完整单词对齐中，每个相邻词对还恰有一个相同普通字母：

```text
I / N / F / L / O / O / D  ->  INFLOOD
```

`WAY` 已由用户判错；弱/强互补键—七位 ASCII—`WY` 补词家族停止，只在后文
保留为负证据。四圆端股翻译出的 `MINIFYHAVE` 仍是 DNA/蛋白质语境的独立校验，
但不是当前终答。

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
`work/visual/hint11/geometry.tsv`。31 个圆不是八股的总长度，而是完整错位布局
在连续五个纵坐标中的裁窗；因此应按八个连通实线分量的可见数
`3,2,5,5,5,5,3,3` 比对候选布局。

### Interpretation

锯齿实线对应正读或反读的完整 spangram，链间虚线对应选中的 Watson-Crick
配对。穷举所得两个完整词布局中，只有 `FRFRFRFR`、偏移
`0,-3,-3,-2,2,5,7,7` 在全局行 `9..5` 上产生详细图的八股可见数；它在这个
窗口内的七条选中配对也与图上七条虚线逐一同位。因而详细图同时给出了方向、
错位与哪些偶然互补位置实际连线，不能只当成 β 折叠的气氛提示。

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

第一条读法按原图每股四圆，将 Board 2 与 Board 1 的两字串各重复一次，使八股
都恰有四个碱基。拼接为：

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
MINIFYHAVE
```

这是一条精确的英文指令 `MINIFY HAVE`，不是答案本身。

### Current full-spangram alignment and extraction

原始八段总长恰为 28：

```text
AT / GATT / AACA / TATT / CTAT / CATG / CAGT / AG
```

原图七处 `×2` 正好需要 `7 × 2 × 2 = 28` 个碱基。要求每个出现位置只进入
一对 Watson-Crick 键，得到唯一的左右侧碱基多重集分配：

| Board | 原串 | 向左配对 | 向右配对 |
| ---: | --- | --- | --- |
| 2 | `AT` | — | `AT` |
| 6 | `GATT` | `AT` | `GT` |
| 7 | `AACA` | `AC` | `AA` |
| 8 | `TATT` | `TT` | `AT` |
| 4 | `CTAT` | `AT` | `CT` |
| 5 | `CATG` | `AG` | `CT` |
| 3 | `CAGT` | `AG` | `CT` |
| 1 | `AG` | `AG` | — |

关键修正是：水平配对的坐标应是这些碱基在**完整 spangram** 中的位置，而不是
压缩后的 A/C/G/T 串下标。区分重复字母出现位置、允许整词正读或反读并固定首词
正读后，只有两个全局水平布局：

| 方向 | 偏移 | 每个相邻词对唯一的相同普通字母 |
| --- | --- | --- |
| `FRFFRFRF` | `0,-3,-3,-4,-7,-12,-13,-13` | `I/N/I/L/O/O/D` |
| `FRFRFRFR` | `0,-3,-3,-2,2,5,7,7` | `I/N/F/L/O/O/D` |

提示 11 详细图唯一选中第二行：其连续五行裁窗恰为全局行 `9..5`，八股可见圆
数为 `3,2,5,5,5,5,3,3`；窗口中七条实际绘出的配对依次是
`g5@9, g4@8, g6@8, g7@7, g4@6, g3@5, g5@5`，与坐标模型完全相同。

在选中的完整单词对齐里，各相邻词对除了两处生命字母配对，还恰有一个位置上的
普通字母完全相同：

| Gap | 对齐词对 | 两个选中配对行 | 相同字母行 | 提取 |
| ---: | --- | --- | ---: | :---: |
| 1 | `BIATHLON / YTIVITAGEN` | `2,3` | 1 | `I` |
| 2 | `YTIVITAGEN / PANAFRICANISM` | `-2,4` | 6 | `N` |
| 3 | `PANAFRICANISM / RETFILOTARTS` | `0,5` | 1 | `F` |
| 4 | `RETFILOTARTS / FLUCTUATION` | `6,8` | 3 | `L` |
| 5 | `FLUCTUATION / GNITAROPROCNI` | `5,9` | 11 | `O` |
| 6 | `GNITAROPROCNI / CARDIOLOGIST` | `8,15` | 14 | `O` |
| 7 | `CARDIOLOGIST / GNIDNEHERPPA` | `7,18` | 10 | `D` |

按间隙从左到右读：

```text
I / N / F / L / O / O / D  ->  INFLOOD
```

因此答案是 **`INFLOOD`**，自然分词为 **`IN FLOOD`**。完整枚举见
`work/dna_pairing.py`，稳定坐标图见 `artifacts/in-flood-extraction.svg/.png`。

### Rejected four-circle STOP/F branch

以下四圆同位模型仍是可复核的观察，但其终止码解释已被用户判错。把八个四碱基
片段依次放入原图八股，并固定第一股按提取
次序自上而下。每一股可正读或反读；要求相邻两股在同一圆位恰有两个
Watson-Crick 互补，唯一得到：

```text
方向      F     F     R     R     R     R     F     R
四圆股    ATAT  GATT  ACAA  TTAT  TATC  GTAC  CAGT  GAGA
向右配对位 23    34    14    23    23    12    14    -
```

题面说答案出现在“交叠之处”。对六条内部股，只有同一个物理圆既参与左侧配对、
又参与右侧配对时才算双重交叠。按股从左到右、每股从上到下读取：

```text
T / A / - / AT / T / C  ->  TAATTC
```

继续按同一遗传密码分组：

```text
TAA | TTC  ->  STOP | F
```

主编码区中 `TTC` 恰是 `MINIFYHAVE` 唯一 `F` 的密码子。把它换成前面的 `TAA`
终止密码子，等价于在 `F` 之前停止翻译：

```text
M I N I | STOP | Y H A V E  ->  MINI
```

该路线曾给出 **`MINI`**，但用户已明确判错。问题在于 `TAATTC` 只是一种圆位
读数，图中没有箭头授权把 `TAA` 当成对主串 `TTC` 的替换指令。

### Rejected direction and mirror audit

将八个补成四位的片段强制在同一圆位恰有两处互补，固定首股按提取次序自上而下
后唯一得到 `FFRRRRFR`。若连首股也反转，会出现全局镜像 `RRFFFFRF`；但这违反
了初始书写锚点。方向布局本身用于读取物理圆位，而不是当二进制。此前的
`00111101 -> '=' -> EQUALS SIGN` 仍因 F/R→0/1 没有题面授权且已被用户判错，
整个 ASCII 方向位假设族停止。穷举保存在 `work/dna_pairing.py` 与
`work/visual/dna_pairing.tsv`。

### Disclosed residual details

- 当前 28 碱基模型在多重集层面唯一；扩展重复字母发生位置共有 72 种配法。
  把碱基映回完整词位置并要求每处两键同高后只剩两个布局；详细图再唯一选择
  `FRFRFRFR`。这三层都不依赖字典择词。
- 选中布局在第 5、8 行有额外的偶然互补碱基相邻，但提示图没有画出所有偶然
  互补；它只画每个碱基出现恰用一次的 14 条选中键。尤其第 8 行中央 A–T 没有
  虚线，正与单次使用约束吻合。
- 七个 `I/N/F/L/O/O/D` 都是完整词对齐后的**同字母**重合，不是互补碱基、
  ASCII 映射或语义补词；每个间隙恰有一个，因此读序由提示 12 的横向次序直接给定。
- 答案保留原样 `INFLOOD`；`IN FLOOD` 只是自然空格，不把 `FLOOD` 再换同义词、
  删字或扩成未经提取的格言。
- 32 碱基旁证串有两个前导碱基；首个 `ATG` 自然选出第三阅读框，之后恰为
  30 个碱基并译成 `MINIFYHAVE`。串尾无终止码不影响十个单字母氨基酸码。
- 四圆模型的双重交叠串 `TAATTC -> TAA/TTC -> STOP/F` 及结果 `MINI` 已判错；
  方向位 `FFRRRRFR -> '='` 也因没有 F/R→比特授权且答案判错而停止。
- 旧 28 碱基非交叉配对可稳定读出 `WWWSWWW|WSWWSSW -> w/Y`，但 `WAVY`、
  `WAY` 均被用户判错。按预设分界，整个弱/强键—七位 ASCII—`WY` 补词家族
  停止；不得恢复 `WHY/WHEY/WAVY/WAY`。
- 氨基酸质量、名称长度、普通一编辑、逻辑值、碱基全名与 `HAVE` 局部重排等
  解释族均已有明确判错结果，继续只作负证据。

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
| 2026-08-30 | TRUE | rejected | 用户明确报告答案不正确；将 A-T 配对所得 `T` 按逻辑真值展开为 `TRUE` 的规范化撤回。 |
| 2026-08-30 | THYMINE | rejected | 用户明确报告答案不正确；把图示 `x2` 解释为 A-T 两个氢键并将所得 `T` 扩写为 DNA 碱基全名的路线撤回。 |
| 2026-08-30 | MINI | rejected | 用户明确报告答案不正确；将双重交叠串 `TAATTC` 解释为 `TAA/TTC = STOP/F` 并在主肽串唯一 `F` 前终止的路线撤回。 |
| 2026-08-30 | WAVY | rejected | 用户明确报告答案不正确；将 28 个原始碱基按严格正反交替和不交叉配对读成弱/强二进制 `wY`，再把 `HAVE` 两端裁成 `AV` 的路线撤回。 |
| 2026-08-30 | WAY | rejected | 用户明确报告答案不正确；弱/强键七位 ASCII `WY` 加 `HAVE -> A` 的补词路线撤回，并停止整个 `WY` 补词家族。 |
| 2026-08-30 | INFLOOD | accepted | 用户明确确认答案正确。 |

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
  肽串 `MINIFYHAVE` 的图示终操作。
- **把 `MINIFY | HAVE` 拆开后直接提交 `HAVE`**：`HAVE` 已被用户明确判错。
  `MINIFYHAVE` 当前只作 DNA/蛋白质语境的独立校验；终答直接来自完整词对齐的
  七个相同字母交叠，不能把操作数原样当答案，也不再把它拼进 `WY`。
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
  可由初始书写顺序锚定，但 F/R 到 0/1 仍没有题面规定；交换映射会改变字节。
  因此方向布局保留，`=` 的字符名不是终答，ASCII 假设族停止。
- **`MINIFY HAVE -> A -> T -> TRUE` 的逻辑展开**：用户已明确判错。即使把图中
  `x2` 解释为 A-T 的两个氢键，`T` 也不能再凭“真相”一词扩成逻辑值 `TRUE`；
  上游生物学中间量与这一错误规范化分开审计。
- **`MINIFY HAVE -> A -> T -> THYMINE` 的两氢键路线**：用户已明确判错。这不只
  否定碱基全名，还使“图示 `x2` 专指单个 A-T 的两个氢键”失去候选支撑；当前
  路线把每个 `x2` 统一建模为相邻两股之间两对被图选中的互补碱基。
- **`TAATTC -> STOP/F -> MINI`**：用户已明确判错。`TAATTC` 是首股正读布局下
  同时向左右配对圆的真实读数，但把相邻两个密码子当成“用 STOP 替换 F”的指令
  没有图示箭头授权；该终止替换与答案 `MINI` 均撤回。
- **弱/强键七位 ASCII—`WY` 补词家族**：`WAVY` 与 `WAY` 均被用户明确判错。
  前者把 `MINIFY` 临时改释为两端裁字，后者虽复用 `A/C/G/T` 过滤得到 `A`，仍需
  把弱/强键任意指定为比特并以成词性把字母塞入 `WY`。按预设分界，
  `WHY/WHEY/WAVY/WAY` 等整个补词家族停止；独立计算结果仅作负证据。

## Evidence and artifacts

- `artifacts/extraction.md`：答案 `INFLOOD` 的 28 碱基唯一分配、两个完整词布局、
  详细图裁窗判别与七个同字母交叠的精简复现版。
- `artifacts/verify_solution.py`：复核八盘完整覆盖、DNA 片段、密码子旁证、完整词
  `FRFRFRFR` 对齐、提示图可见圆/虚线以及 `I/N/F/L/O/O/D`；旧 `WAVY/WAY`、
  `TAATTC -> STOP/F -> MINI` 及更早结果只作负证据。
- `artifacts/in-flood-extraction.svg/.png`：已确认答案的稳定完整坐标图；显示八词
  正反方向、纵向偏移、14 条选中互补键、提示 11 裁窗及七个相同字母交叠。
- `artifacts/way-extraction.svg/.png`：已判错 `HAVE -> A; W+A+Y -> WAY` 的历史图，
  已明确标成 rejected，不代表当前答案。
- `artifacts/wavy-extraction.svg/.png`：已判错 `HAVE -> AV -> WAVY` 的历史图，
  已明确标成 rejected，不代表当前答案。
- `artifacts/hint11-annotated.png`：提示 11 的稳定坐标标注。
- `artifacts/stop-f-extraction.svg/.png`：已判错 `TAATTC -> STOP/F -> MINI`
  路线的历史标注图，不代表当前答案。
- `work/hint11_model.py`：提示 11 几何模型生成器。
- `work/visual/hint11/geometry.tsv`：31 圆、23 实线段、七虚线的坐标表。
- `work/visual/final_diagram_audit.md`：提示 11/12 后的视觉审计。
- `work/minify_have.py` 与 `work/visual/minify_have.tsv`：一次编辑词族的参数化
  负证据；“保留 HAVE、前置尺寸码 S、具有 reduction sense”虽唯一选出
  `SHAVE`，但已被用户明确判错。
- `work/reduce_have.py` 与 `work/visual/reduce_have.tsv`：四种自然读向及共享 `Y`
  前后位置的八项有界审计；其唯一普通词 `HEAVY` 已被判错，现为负证据。
- `work/dna_pairing.py` 与 `work/visual/dna_pairing.tsv`：28 碱基唯一多重集
  分配、72 个出现位置级配法、两个完整词水平布局、提示 11 唯一裁窗与
  `INFLOOD`；同时保留 `WWWSWWW|WSWWSSW -> w/Y`、四圆 `FFRRRRFR`、
  600 项直接翻译和 `STOP/F -> MINI` 的负证据。
- `work/amino_minification.py` 与 `work/visual/amino_minification.tsv`：质量与
  名称长度的旧全局对照，以及两股正反、三个完整交叠偏移的 12 项逐对质量
  负审计；其唯一普通词 `NAVE` 已被明确判错。
- `work/visual/hint12_*.tsv`：旧端点机制在官方顺序下的有界负证据。
- `artifacts/*-extraction.*`、`dna-overlap.*`、`overlap-binary.*`、
  `endpoint-chain.*`：均是明确标记的历史失败路线，不代表当前机制。

## Next action

无需继续求解；**`INFLOOD`** 已由用户确认正确。保留当前验证脚本、坐标图与
失败路线，供 Round feeder 或后续复核使用。
