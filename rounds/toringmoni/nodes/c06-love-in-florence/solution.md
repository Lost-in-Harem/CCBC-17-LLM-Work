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
- WIG 提示 4 已解锁：本题主题是“与翡冷翠（Firenze）属于同一类型的词”，即城市名；它确认了城市异序词方向，但没有给出国家、城市名单、载体范围或句子间的读取规则。
- 用户进一步确认这里的“城市”指现实世界中的城市/地名，而非普通词或虚构地点；这仍未限定国家、人口级别、行政层级或固定城市表。

## Working hypotheses

- **城市异序词 + 残余字母（主路线）**：去掉标记分母长度的城市名后，剩余字母数量正好等于方框数；按正文载体中剩余字母的顺序，以 `■=辅音`、`□=元音` 可复现方框图样。分子取城市名（去空格、按常见英文拼写）的 1-based 字母。
- **为何可信**：标题“翡冷翠”本身指向 Florence；`ceranflower` = `FLORENCE` + `RAW`，图样 `■□■`，`(5/8)` 取 `E`。同一规则还给出 `instead` = `ASTI` + `NED`，`(3/4)` 取 `T`；`ckerman` = `CREMA` + `KN`，`(5/5)` 取 `A`；`reversepar` = `REVERE` + `RSPA`，图样为原文的 `■■■□(1/6)`，取 `R`；`linchoearth` = `LOCHEARN` + `IHT`，`(5/8)` 取 `E`。这些不是只靠语义猜测，而是长度、字母多重集、黑白图样和索引同时吻合。
- **范围/选择仍未确定**：把载体扩展为所有连续词窗，并分别用 GeoNames、world-cities、意大利城市表、首都表等做穷举后，大多数标记仍有许多城市候选；有些单词必须与邻词合并（如 `sheyinterval`、`learn how`），有些载体可重复用于不同标记（如 `instead`、`If Draco`）。只按“意大利城市”、人口、PPLA 或文本顺序约束，均没有得到唯一的 26 字母串。
- **伪词短窗的有界核验**：只保留包含低频/明显伪词、至多四个相邻词的载体，并要求 26 个标记使用不同载体。world-cities 词典下前 21 个标记仍有候选，但到第 22 个无完美分配；弱语言模型的前缀也只是 `eithninon...` 一类噪声，不能作为答案证据。
- **载体范围的局部审计**：逐字母检查显示，载体不一定是单个伪词，跨词窗口也能精确吻合同一规则，例如 `A ushow's` = `SUSA` + `HOW`、`linchoearth tal` = `CALLIANETTO` + `HRH`、`ceranflower` = `FLORENCE` + `RAW`、`reversepar` = `REVERE` + `RSPA`。这加强了“连续词窗”的解释，却没有确定窗口边界或城市词典。
- **旅行指南的交叉线索**：`天好 - 旅行指南` 明说“柔枝”是加香用、通常不随薯条食用。这与“载体中多出的字母是标记用残余，不属于城市名”的方向一致，但没有提供城市词典或顺序。
- **全局索引复核**：`work/fast_beam.py` 对 world-cities 的全部连续词窗做了长度、字母多重集和黑白残余模式的索引扫描；M01、M04、M05 在该词表下各自只有一个输出字母，但其他位置仍有 3–52 个命中，20,000 状态 beam 的最佳串为 `enteerinestiontionsterande` 一类非英文噪声。因此“换一个更快的全局穷举”没有产生稳定答案。
- **重复字母的精确审计**：`work/exact_subset_scan.py` 枚举了载体中重复字母的所有位置，而不是像 greedy 扫描那样只取一种余字母分配。它确认 `ceranflower` 可按 `FLORENCE` 留下 `RAW` 或 `AWR`，并且 M01/M04/M05 等强例仍需要跨词窗口；因此单一 greedy 残余、载体边界或重复字母位置都不能视为定解。
- **伪词窗口 + 意大利目标的有界反证**：把载体限制为包含低频词的全局窗口，再用 GeoNames `IT.zip` 的意大利地名作为城市词典，单标记仍有 2–35 个候选；按六组把输出约束为意大利地名时，组 1 只有 `Rina`，组 2 有 38 个目标，组 3 有 3 个，组 4 有 4 个，组 5 有 47 个，组 6 有 5 个，且组 1 也有 3 种载体解释。`Rina` 等是词典碰撞，不是可提交答案。
- **严格按句子分组的有限检验（否定）**：把每组标记严格限制在对应句子、连续窗口至多 5 词，并用 GeoNames Italy 的全部 P 类地名；第 1 句的 M01、第 4 句的 M17、第 6 句的 M23 没有任何载体，六组中只有第 2 组出现完整目标（11 个），其余组均无法完成。因此标记在版面上的六组不能直接等同于载体所在句子。见 `work/csp_local_italy.py`。
- **全局唯一性加强检验（否定）**：把低频伪词全局窗口与 GeoNames Italy 组合，同时要求每组内载体窗口和载体城市都不重复；六组可达的意大利目标数为 1/38/3/4/47/5，组 1 的 `Rina` 仍有 3 种解释，故“双重不重复”也不能唯一化答案。见 `work/csp_global_italy_distinct_city.py`。
- **扩大词典仍无解**：`cities500` 词典的不同载体分配在 M22 后无状态；只看明显异常单词的意大利城市匹配在第 1 步即失败；加入人口先验后各组最佳串仍是无意义字母噪声。更大的词典或排序先验没有提供题目所需的约束。
- **句子输出作为常见城市的有限检验（否定）**：把六组输出的字母集合与 `cities500`（人口至少 500 的 GeoNames 城市）交叉；组 1 仅有 `Este`/`Erre`，但组 2–6 仍分别有 73、216、107、139、187 个目标（最高人口候选也不形成一致序列），所以“每段直接组成一个常见城市”仍不足以确定答案。见 `work/group_targets_cities500.py`。
- **提示 4 后的同词典 CSP（仍多解）**：把载体城市和六段输出都限制为 `world-cities.csv`，并要求每组内载体窗口、载体城市均不重复；组 1 虽唯一落在 `Este`，仍有 2 条解释，组 2–6 分别有 6/13/16/2/10 个目标和 8/114/208/6/115 条解释。城市主题得到支持，但没有产生可提交串。见 `work/csp_global_worldcities_targets.py`。
- **现实城市约束下的组名再筛选（仍多解）**：将六组输出限制为 GeoNames `cities500` 的真实聚居地，并把人口门槛从 500 提高到 500,000；G1 在低门槛时只有 `Este`/`Erre`，但 G2–G6 仍分别有 71/235/104/166/227 个目标（500,000 门槛也留下 G2=`Essen`、G3=`Sanaa`/`Sakai`/`Essen`、G4=`Omsk`/`Oran`、G5=`Lima`/`Aden`、G6=`Aden`/`Teni`，且 G1 反而无目标）。所以“现实城市”与人口先验都不能唯一确定各段答案。见 `work/group_target_thresholds.py`。
- **相邻 WIG 页面的只读复核**：在实时 Launchpad 中打开“天好 - 旅行指南”并点击“其他国家的旅行地点？”，链接只回到同一份 `宣传页 - 旅行指南` 题面；页面没有列出固定城市表、国家顺序或额外提取文字。因此邻页目前只能确认题面来源，不能承担城市词典/读取规则。
- **全局不重复的组名尝试（未形成完整链）**：在 world-cities 候选中同时要求六组输出是城市名、26 个载体窗口及载体城市全局不重复；有界状态在第 5 组归零，说明这个额外约束与当前宽词典/窗口假设不相容，不能据此选答案。见 `work/csp_global_groups_distinct.py`。
- **低频异常词锚定检验（未形成一一对应）**：按 `wordfreq` 把明显伪词作为短窗口锚点，M01、M04、M05 各自几乎被唯一地压到字母 `E`；因此第一组确实可拼成 `ESTE`（例如 `Herentals / Orsk / Hötting / Saint Helier`）。但两处 `E` 都复用 `sheyinterval` 的重叠窗口；若强制每个异常词只用一次，第一组直接无状态。全 26 个标记与异常词也不构成稳定的一对一数目（阈值下有 27 个词），所以 `ESTE` 仍是词典碰撞而非答案。见 `work/odd_anchor_csp.py`、`work/odd_marker_bijection.py`。
- **常见城市人口先验的有界复核（否定）**：在同样的低频锚点窗口下，把 GeoNames 城市限制为人口至少 50,000 或 100,000 时，六组不能同时组成目标城市（第一组在高门槛下即无解）；人口/“现实城市”先验不能补足载体选择。见 `work/popular_group_csp.py`。
- **载体城市与组名分离的检查**：允许载体城市来自 world-cities、只把六组输出限制为意大利地名时，组 1 只有 `Este`，但组 2–6 分别仍有 7、41、15、26、37 个命中；若同时把载体限制为意大利城市，M01 等多处直接无命中。因此“题名是翡冷翠”不能推出全题只用意大利城市。
- **组名自载体检验（否定）**：以同一 `world-cities` 词典测试“每组最终城市也必须是该组某个载体城市”。只有 G1 留下 `Este`，G2–G6 均无自载体目标；这个额外规则既不能解释后五组，也不能把 `Este` 提升为最终答案。见 `work/self_target_scan.py`。
- **最有区分力的下一测**：从 WIG 其它已确认剧情/线索中找到题目采用的固定城市词典或城市属性，再对每个载体按同一多重集规则筛选；在没有这项外部约束前继续换城市数据库只会重复产生多解。

## Extraction

当前没有可提交候选答案。可复核的局部抽取如下（城市名均去空格计数）：

| 载体 | 城市 + 残余字母 | 方框/索引 | 输出 |
| --- | --- | --- | --- |
| `ceranflower` | `FLORENCE` + `RAW` | `■□■ (5/8)` | `E` |
| `instead` | `ASTI` + `NED` | `■□■ (3/4)`（原文还带多余 `4`） | `T` |
| `ckerman` | `CREMA` + `KN` | `■■ (5)`，按 5/5 解读 | `A` |
| `reversepar` | `REVERE` + `RSPA` | `■■■□ (1/6)` | `R` |
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
- 低频单词、同段词窗与候选排序：`work/token_candidates_all.py`、`work/span_by_stanza.py`、`work/rank_candidates.py` 及对应 `_out.txt`。
- 索引化全局有限测试：`work/fast_beam.py`、`work/fast_beam_out.txt`。
- 伪词短窗的不同载体分配实验：`work/assignment_anomalous.py`（固定 1000 状态 beam；未完成 26 项分配）。
- 意大利城市对照实验：`work/span_allitaly.py`、`work/span_allitaly_out.txt`。
- 单词/低频伪词检查：`work/carrier_sets.py`、`work/typo_token_candidates.py`。
- 局部/全局载体窗口核验：`work/span_inventory.py`、`work/group_target_scan.py`、`work/global_weird_italy.py` 及 `work/global_weird_italy_out.txt`。
- 伪词窗口的意大利组名 CSP：`work/group_global_weird_italy.py`、`work/csp_global_italy.py` 及 `work/csp_global_italy_out.txt`；后者记录了每个标记的候选数和六组目标名/解释数。
- 句内分组反证：`work/csp_local_italy.py`；载体窗口/城市双不重复的全局反证：`work/csp_global_italy_distinct_city.py`。
- 其它负面对照：`work/distinct_cities500.py`、`work/odd_token_italy.py`、`work/global_weird_pop.py` 及其输出，分别测试不同载体分配、单异常词和人口排序先验。
- 低频词锚点/城市目标诊断：`work/odd_anchor_csp.py`、`work/odd_marker_bijection.py`、`work/popular_group_csp.py`。
- 句子输出与常见城市表的交叉：`work/group_targets_cities500.py`。
- 现实城市人口门槛对照：`work/group_target_thresholds.py`。
- 城市载体/城市输出同词典 CSP：`work/csp_global_worldcities_targets.py`。
- 重复字母位置与“组名即载体城市”的有界诊断：`work/exact_subset_scan.py`、`work/self_target_scan.py`。
- 六组城市名与全局不重复载体的有界检验：`work/csp_global_groups_distinct.py`。
- 运行方式示例：在本 Node 目录执行 `python work/global_span_worldcities.py`；所有实验输出均位于本 Node 的 `work/`，未修改输入或 Round shared 文件。

## Important failed routes

- 直接把方框当二进制、Morse、化学元素、键盘坐标或普通字符索引：有限枚举未产生稳定英文结果。
- 只对单个异常词做低频词典/英语异序匹配：多个标记无候选，且不能解释分母/黑白图样。
- 只用意大利城市、人口/PPLA、首都或严格文本顺序筛选：仍多解，或无完整单调路径；不能把“翡冷翠”直接当作全题城市范围的充分证据。
- 把 26 个标记强制一一对应到低频伪词短窗：有限 beam 在第 22 项无状态，说明该限制与当前词典不相容。
- 用 world-cities 全部词窗做一次索引化语言模型 beam：得到的最佳串仍是 `enteerinestiontionsterande` 等噪声，且命中数高度不均；不能据此提交。
- “所有载体都是意大利城市”及“低频伪词窗口必然组成意大利组名”：前者在 M01 等位置无命中，后者虽得到 `Rina` 等地名，却存在大量替代目标和解释；两条都不能唯一化答案。
- 严格把六个标记组绑定到六个对应句子：M01、M17、M23 在句内没有载体，且只有第二组能完成目标名；该版面分组假设已被有限检验否定。
- 在全局范围同时要求载体窗口与载体城市不重复：六组目标数仍为 1/38/3/4/47/5，未消除 `Rina` 等碰撞。
- 把各句输出强制当作 `cities500` 城市：第一组虽只剩 `Este`/`Erre`，其余组仍有 73/216/107/139/187 个候选，人口排序没有形成可复核的答案链。
- 把载体和段落答案都强制使用 `world-cities.csv`：`Este` 仍有两条载体解释，其他段落保留 2–16 个目标和最多 208 条解释，不能把 `Este` 当作最终答案。
- 读取在线 puzzle app 的静态页面：只能看到题名、输入框和提示壳，未发现公开答案元数据；未进行提交或 hint 操作。

## Next action

确认 WIG 剧情中是否有一条明确给出国家/城市集合、城市属性或固定旅游网站词典的线索（提示 4 和用户补充只确认“现实城市名”，仍未给出城市集合；提示 2、3、5 的正文尚未提供）。当前最有价值的是提示 5 的正文：它应说明六组城市答案之后的读取步骤。若用户能提供提示 5（或提示 2、3），优先据此确定城市词典、窗口边界与第二层提取；随后再单独解析 `(3/4 4)` 与 `(5)`。在获得该约束或新的题面证据前保持 `working`，不要提交猜测答案。
