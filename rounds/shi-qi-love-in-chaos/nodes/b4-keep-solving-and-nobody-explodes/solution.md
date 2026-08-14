---
node_id: b4-keep-solving-and-nobody-explodes
title: 保持解谜就无人爆炸
kind: puzzle
round: shi-qi-love-in-chaos
parent: 
source: 
round_feeder: yes
feeders: 
status: candidate
answer: WIRES
confidence: medium
summary: 被拒的 `397:1964` 应是内层查询码而非最终答案：它精确定位 ISO/R 397:1964“铜及铜合金线材缠绕试验”，而题名指向的 Keep Talking and Nobody Explodes 官方模块名为 Wires；故新候选为 WIRES。
updated: 2026-08-15
---

# 保持解谜就无人爆炸

## Current conclusion

新候选是 **`WIRES`**。用户明确拒绝了 **`397:1964` 作为最终答案**，但这串数字仍是高度可信的内层查询码：它与 [ISO/R 397:1964](https://www.iso.org/standard/4397.html) 的官方参考号完全一致，标题是 “Wrapping test for copper and copper alloy **wire**”。外层题名明确仿作 *Keep Talking and Nobody Explodes*；该游戏的[官方手册](https://www.bombmanual.com/web/index.html)将对应模块命名为 **Wires**。因此题名与 ISO 查询结果的交集给出最终词 `WIRES`。

这个解释也消除了先前的结构矛盾：音频里的 `___:____` 是室友正在解的“内层题”的输出格式；本题网页自身只有录音和一个不限字数的通用答案框。

## Observations

以下为音频中稳定听清、并被多次本地转写一致支持的事实；时间戳和清理后的转录见 [`artifacts/audio_transcript.md`](artifacts/audio_transcript.md)。

- 标题为“残酷天使的行动纲领”，下面歌词含“……创造奇迹”；“奇迹”提示 Miracle Sudoku。
- 页面有一张大数独图和七张小图，最下面格式为三格、冒号、四格：`___:____`。
- 数独只报出两个给定数：`r5c3=9`、`r6c7=8`。
- 9 所在格及正下方一格是青、蓝两格；8 右边是紫格。因此后三种颜色的格为 `r5c3`、`r6c3`、`r6c8`。
- 七张小图依次描述为：陌生国王头像；屋顶露台突出的大楼；港口；蓝色万智牌上的飞行神话生物；英国 O2 场馆内举杯的戴眼镜亚洲电竞选手；有履带、在地面行驶的巨大“船”游戏建模；带绿色女角色和魔兽式技能栏的老游戏截图。
- MP3 为 137.4 秒人声录音，左右声道相同；频谱、波形和元数据没有支持音频隐写路线的异常。

## Mechanism and Sudoku

[Miracle Sudoku](https://ethmcc.github.io/miracle-sudoku/) 的规则是普通数独，加上反王步、反马步、以及正交相邻格数字不得连续。著名原题只有两个给定数；本题的 9、8 是原题 1、2 的 `d → 10-d` 对称版本。

保留的 Z3 脚本 [`artifacts/miracle_sudoku.py`](artifacts/miracle_sudoku.py) 实现全部规则、验证唯一性并可参数化取格。它给出的唯一解为：

```text
6 2 7 | 3 8 4 | 9 5 1
3 8 4 | 9 5 1 | 6 2 7
9 5 1 | 6 2 7 | 3 8 4
------+-------+------
2 7 3 | 8 4 9 | 5 1 6
8 4 9 | 5 1 6 | 2 7 3
5 1 6 | 2 7 3 | 8 4 9
------+-------+------
7 3 8 | 4 9 5 | 1 6 2
4 9 5 | 1 6 2 | 7 3 8
1 6 2 | 7 3 8 | 4 9 5
```

复现命令：

```powershell
python rounds\shi-qi-love-in-chaos\nodes\b4-keep-solving-and-nobody-explodes\artifacts\miracle_sudoku.py --extract r1c4 r2c4 r3c6 r5c5 r5c3 r6c3 r6c8
```

脚本输出 `unique: True`，并取出 `3971964`。

## Intermediate extraction

完整的证据表见 [`artifacts/extraction.md`](artifacts/extraction.md)。核心提取如下：

| 色 | 小图给出的编号 | 数独格 | 格中数字 |
| --- | --- | --- | --- |
| 红 | [Richard II 肖像页标题为 Plate **1.4**](https://scalar.missouri.edu/vm/vol1plate4-colorprints) | `r1c4` | 3 |
| 橙 | [顺昌博物馆页面第 **2.4** 节正是 “Urban terrace”](https://www.brazilian-architects.com/zh/uad-zhejiang/project/shunchang-museum) | `r2c4` | 9 |
| 黄 | [World Bank 报告的 Photo **3.6** 是内河航运/船闸图](https://documents1.worldbank.org/curated/en/908191600317351237/pdf/Blue-Routes-for-a-New-Era-Developing-Inland-Waterways-Transportation-in-China.pdf)，与口述的“港口”大致吻合，但未有原图逐像素确认 | `r3c6` | 7 |
| 绿 | 蓝色飞行神话生物万智牌为 **5/5**；[Blue Dragon](https://www.cardkingdom.com/mtg/adventures-in-the-forgotten-realms/blue-dragon) 与描述及数据相符 | `r5c5` | 1 |
| 青 | O2 举杯者是 Faker：第 **5** 个世界冠军，决赛 **3–2** | `r5c3` | 9 |
| 蓝 | 履带陆行舰截图来自 [Airships **6.3**](https://www.zarkonnen.com/airships/airships_6_3/) | `r6c3` | 6 |
| 紫 | 老 Dota **6.8** 截图；且紫格已由口述固定 | `r6c8` | 4 |

青色图的外部核对完整吻合：[Riot 确认 2024 决赛在 The O2](https://lolesports.com/en-US/news/your-ticket-guide-to-the-world-final)，[Riot 确认这是 Faker 的第五座 Worlds 奖杯](https://www.leagueoflegends.com/en-us/news/esports/worlds-2024-winners/)，[中央社记录 T1 以 3–2 获胜](https://www.cna.com.tw/news/aspt/202411030005.aspx)。

所以依彩虹顺序得到内层查询码：

```text
r1c4 r2c4 r3c6 r5c5 r5c3 r6c3 r6c8
  3     9     7     1     9     6     4
                    397:1964
```

`397:1964` 精确定位 ISO/R 397:1964，其标题的核心对象是 `wire`。再用外层题名指向的官方游戏手册规范化为模块名，得最终候选：

```text
WIRES
```

## Candidate audit

- **可复现性：** 保留脚本证明 Miracle Sudoku 唯一解，并可按七个坐标复现 `397:1964`。
- **独立校验：** `397:1964` 不只是格式像 ISO 号，而是精确查到一个主题为 `wire` 的 ISO 条目；外层题名又独立指向拆弹游戏的 `Wires` 模块。这个双重命中远强于随机 ISO 语义巧合。
- **答案形式：** 官方英文模块名是复数 `Wires`，因此优先于 ISO 标题里的单数 `WIRE`和中文本地化 `线路`。
- **未用信息/风险：** 黄色港口图与绿色万智牌仍没有原图级匹配；因此保留中等置信度。数字串作为最终答案已被拒绝，不得再提交。

## Submission history

只记录用户或比赛网站明确反馈过的提交。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-14 | `397:1964` | rejected | 用户明确报告“答案错误”。 |

## Evidence and artifacts

- [`artifacts/audio_transcript.md`](artifacts/audio_transcript.md)：带时间戳的清理转录和不确定项。
- [`artifacts/extraction.md`](artifacts/extraction.md)：七图坐标、取值、证据强度、来源和复现命令。
- [`artifacts/miracle_sudoku.py`](artifacts/miracle_sudoku.py)：唯一解与取格脚本。
- 音频波形、频谱、ASR 模型输出及试验记录留在 `work/`，属于可丢弃调查材料。

## Important failed routes

- **已拒绝的最终答：`397:1964`。** 用户于 2026-08-14 明确报告答案错误；不得再把它恢复为最终答案。新证据只支持它作为内层查询码：题面快照显示 `___:____` 是录音中的内层格式，ISO 官方页与拆弹官方手册共同给出之后的 `WIRES` 提取层。
- 音频隐写路线没有证据：左右声道重复、内容为普通人声、元数据只有 Adobe Audition 记录。没有继续在该路线消耗搜索。
- ASR 在第四张牌的最后一个视觉短语上始终不稳定；多次有界转写没有产生新的可确认事实后已停止该实验族，不把该短语用于结论。
- 港口图一度考虑 `3.7`，会导向 `393:1964`；该 ISO 编号语义完全不合题材，而 `397:1964` 是 wire wrapping test，因此将其降为重要反例而非并列候选。
- 第七张图的具体截图页面匹配不够可靠，但这不影响取格：紫格由音频直接固定为 `r6c8`，Dota 6.8 只提供冗余确认。

## Next action

建议下一次只提交 **`WIRES`**。若仍被拒绝，请带回判题器的完整反馈；再根据反馈区分“单复数/中文本地化”与“黄、绿坐标仍错”，不要穷举提交 `WIRE`、`线路`、`WRAPPING TEST` 等变体，也不得再提交 `397:1964`。
