---
node_id: c06-love-in-florence
title: 情迷翡冷翠
kind: puzzle
round: toringmoni
parent: 
source: 
round_feeder: yes
feeders: 
status: working
answer:
confidence: medium
summary: >-
  已复原题面的城市字母多重集/残余字母机制，并得到 Florence、Asti、Crema、Revere 等强例；
  但城市词典、载体范围与标记顺序仍多解，尚无可安全提交的最终答案。
updated: 2026-08-18
---

# 情迷翡冷翠

## Current conclusion

题面已从 WIG 附带的 SingleFile 中复原。当前最可信的解释是：句中的伪词（有时是相邻词的短语）是某个城市名加上若干额外字母的异序词；标记中的分母是城市名长度，方框数是额外字母数，黑/白方框记录额外字母是辅音/元音，分子索引城市名中的字母。这个解释有多个逐字可复核的强例，但还不能确定每一行应该选哪一个城市，也不能把 26 个输出唯一排序成答案。

## Observations

- 输入目录包含 `情迷翡冷翠.html`（只有题名/风味文字）以及 WIG 页面 `宣传页 - 旅行指南.html`、`天好 - 旅行指南.html`。实际题面是 `work/all_sfzip/宣传页 - 旅行指南/visible.txt`。
- 实际页面标题为 `CITY EDITION`，品牌为 Farbound Travel Guide，风味句为“快住手，洋味不是这样的！”。正文是六段故意夹入异常字母的英语，共 26 个方框/分数标记。
- 标记的方框只有黑色 `■` 和白色 `□`，分母出现 4、5、6、7、8、9、11；存在字面上异常的 `(3/4 4)` 和省略分母的 `(5)`，不能擅自规范化。
- 例如正文中有 `ceranflower`、`instead`、`ckerman`、`reversepar`、`linchoearth` 等明显非英语载体；HTML 原文和可见文本转录一致。

## Working hypotheses

- **城市异序词 + 残余字母（主路线）**：去掉标记分母长度的城市名后，剩余字母数量正好等于方框数；按正文载体中剩余字母的顺序，以 `■=辅音`、`□=元音` 可复现方框图样。分子取城市名（去空格、按常见英文拼写）的 1-based 字母。
- **为何可信**：标题“翡冷翠”本身指向 Florence；`ceranflower` = `FLORENCE` + `RAW`，图样 `■□■`，`(5/8)` 取 `E`。同一规则还给出 `instead` = `ASTI` + `NED`，`(3/4)` 取 `T`；`ckerman` = `CREMA` + `KN`，`(5/5)` 取 `A`；`reversepar` = `REVERE` + `RSPA`，`(1/6)` 取 `R`；`linchoearth` = `LOCHEARN` + `IHT`，`(5/8)` 取 `E`。这些不是只靠语义猜测，而是长度、字母多重集、黑白图样和索引同时吻合。
- **范围/选择仍未确定**：把载体扩展为所有连续词窗，并分别用 GeoNames、world-cities、意大利城市表、首都表等做穷举后，大多数标记仍有许多城市候选；有些单词必须与邻词合并（如 `sheyinterval`、`learn how`），有些载体可重复用于不同标记（如 `instead`、`If Draco`）。只按“意大利城市”、人口、PPLA 或文本顺序约束，均没有得到唯一的 26 字母串。
- **最有区分力的下一测**：从 WIG 其它已确认剧情/线索中找到题目采用的固定城市词典或城市属性，再对每个载体按同一多重集规则筛选；在没有这项外部约束前继续换城市数据库只会重复产生多解。

## Extraction

当前没有可提交候选答案。可复核的局部抽取如下（城市名均去空格计数）：

| 载体 | 城市 + 残余字母 | 方框/索引 | 输出 |
| --- | --- | --- | --- |
| `ceranflower` | `FLORENCE` + `RAW` | `■□■ (5/8)` | `E` |
| `instead` | `ASTI` + `NED` | `■□■ (3/4)`（原文还带多余 `4`） | `T` |
| `ckerman` | `CREMA` + `KN` | `■■ (5)`，按 5/5 解读 | `A` |
| `reversepar` | `REVERE` + `RSPA` | `■■■■ (1/6)` | `R` |
| `linchoearth` | `LOCHEARN` + `IHT` | `■□■ (5/8)` | `E` |
| `If Draco` | `CAIRO` + `FD` | `■■ (1/5)` 等多个标记 | `C` 等 |

这个表证明的是机制候选，不是最终答案；尚缺每个标记的规范载体/城市选择和 26 个输出的读取顺序。

## Candidate audit

未进入 `candidate`：没有唯一答案串，且 `(3/4 4)`、`(5)` 的精确定义与城市选择尚未解释。没有提交，也没有从网站反馈推断答案。

## Submission history

只记录用户或比赛网站明确反馈过的提交；不要把尚未提交的候选写进来。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |

## Evidence and artifacts

- 题面转录：`work/all_sfzip/宣传页 - 旅行指南/visible.txt`。
- 城市残余字母扫描：`work/city_mask_candidates.py`、`work/city_mask_out.txt`。
- 连续词窗扫描：`work/global_span_worldcities.py`、`work/global_span_worldcities_out.txt`。
- 意大利城市对照实验：`work/span_allitaly.py`、`work/span_allitaly_out.txt`。
- 单词/低频伪词检查：`work/carrier_sets.py`、`work/typo_token_candidates.py`。
- 运行方式示例：在本 Node 目录执行 `python work/global_span_worldcities.py`；所有实验输出均位于本 Node 的 `work/`，未修改输入或 Round shared 文件。

## Important failed routes

- 直接把方框当二进制、Morse、化学元素、键盘坐标或普通字符索引：有限枚举未产生稳定英文结果。
- 只对单个异常词做低频词典/英语异序匹配：多个标记无候选，且不能解释分母/黑白图样。
- 只用意大利城市、人口/PPLA、首都或严格文本顺序筛选：仍多解，或无完整单调路径；不能把“翡冷翠”直接当作全题城市范围的充分证据。
- 读取在线 puzzle app 的静态页面：只能看到题名、输入框和提示壳，未发现公开答案元数据；未进行提交或 hint 操作。

## Next action

确认 WIG 剧情中是否有一条明确给出国家/城市集合、城市属性或固定旅游网站词典的线索；得到集合后，按上述残余字母和方框规则重新筛选 26 个标记，并单独解析 `(3/4 4)` 与 `(5)`。在获得该约束或新的题面证据前保持 `working`，不要提交猜测答案。
