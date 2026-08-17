---
node_id: c02-born-from-the-same-root
title: 本是同根生
kind: puzzle
round: toringmoni
parent: 
source: 
round_feeder: yes
feeders: 
status: accepted
answer: LITHARGE
confidence: high
summary: 已确认里程碑 IN ONE FAMILY 指示每关寻找同一植物科的两种植物；它们相对中央旗帜再次构成旗语，读出 ANS LITHARGE，最终答案 LITHARGE 已获用户确认。
updated: 2026-08-17
---

# 本是同根生

## Current conclusion

最终答案为 **LITHARGE**，已由用户确认正确。

第一层中，每关 12 组程序认可的配对恰有一组在知识层面并不相等。以中央第 13 格的 🚩 为旗语者，向那一对错误牌各画一条射线，十一关得到已由题站确认的里程碑 `IN ONE FAMILY`。

把该短语当作下一步指令：逐关在所有植物中找出同属一个植物科的两种不同植物，再从中央旗帜读取它们的方位。第二轮十一字母为 `ANS LITHARGE`，其中 `ANS` 是 answer 的提示前缀，故最终答案为 **LITHARGE**。

## Observations

- 题面位于 WIG 启动台应用 **植物神经紊乱**；制作名单把程序、玩法、设计均署名为“大陆帅哥”。
- 标题页规则为“消掉相同的牌，留下 🚩。”游戏共 11 关；每关是固定 5×5 牌面、12 对普通牌和正中央第 13 格的一张 🚩，限时 40 秒。
- 每一关的“相同”不是字面相同，而是不同表达下的同一对象或对应关系。例如：
  - 第一关：城市别称与市花，如 `申=白玉兰`、`鹏=簕杜鹃`；
  - 第二关：《植物大战僵尸》植物与阳光费用，如 `樱桃=150`、`蘑菇=0`；
  - 第七关：带生肖的植物与含对应地支部件的词，如 `鸡冠花=酒吧（酉）`、`鼠尾草=好题（子）`；
  - 第九关：花札月份植物与含一至十二数字的植物，如 `松树=一叶兰`、`梅花=二月兰`；
  - 第十一关：把答案汉字拆成部件并成对消去后留下的残片，如 `卜又寸=著名歌手（朴树）`、`巴比=清肺止咳（枇杷）`、空白牌对应 `甜味饮料（可可）`。
- 全部通关页只显示“11 关的『相等』都被你找出来了”，没有额外 `finishNote`。
- 制作名单另给出：
  - “游戏就是一系列毫无意义的点击”；
  - “木骨灰痕，在素笺留下沙沙碎响”；
  - `14.4.1.12`。
- 本地静态 `input/本是同根生.html` 只保存了题站外壳和头像资源，关卡正文来自 WIG 动态组件；因此以只读浏览器 DOM 和关卡响应为准。
- 关键反转是：程序判定的“相等”不保证语义正确；每关恰有一个可核实的错配。例如：
  - `万寿果=黄瓜` 错，万寿果是木瓜别名；
  - `萱草=父爱` 错，萱草是传统母亲花；
  - `古超=印度尼西亚` 错，台风名古超由密克罗尼西亚提供。
- 十一组错配的两个位置相对中央旗帜都严格落在上、下、左、右或四个对角方向，不需要任意取整；这给出旗语机制的独立几何证据。
- 题站答案记录明确把 `IN ONE FAMILY` 标为“里程碑”，判题消息为“你正在正确的道路上。”，因此它是第二层指令而不是最终答案。
- 逐关检查植物科后，每关又恰有一组不同植物同科；这 22 张牌也全部严格位于中央旗帜的八条射线上。再次按同一旗语表读取，得到 `ANSLITHARGE`。

## Extraction

以牌面左上为位置 1，逐行编号到右下位置 25，中央 🚩 为位置 13。方向均从 13 指向错误牌：

| 关 | 程序中的假相等 | 核验/纠正 | 位置 | 方向 | 旗语 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `金=君子兰` | 君子兰对应长春“春城”，不是金城 | 7, 17 | NW + SW | I |
| 2 | `豌豆豌豆=250` | 两个豌豆表示双发射手，费用应为 200 | 17, 19 | SW + SE | N |
| 3 | `椰蛋树=鸡蛋` | 椰蛋树是“椰子宝可梦”，原型不是鸡蛋 | 7, 12 | NW + W | O |
| 4 | `昙花=一再留下你孤独睡` | 该歌词出自罗文《杜鹃》 | 17, 19 | SW + SE | N |
| 5 | `万寿果=黄瓜` | 万寿果是木瓜别名 | 5, 23 | NE + S | E |
| 6 | `五果=葡萄` | 《本草纲目》把葡萄列在果之五蓏类（瓜类），不是五果 | 14, 18 | E + S | F |
| 7 | `狗牙根=芦笋` | 狗对应地支戌，但“芦笋”不含戌部件 | 18, 21 | S + SW | A |
| 8 | `萱草=父爱` | 萱草象征母爱 | 14, 17 | E + SW | M |
| 9 | `丁香=七里香` | 花札七月是萩（胡枝子），不是丁香 | 1, 21 | NW + SW | I |
| 10 | `古超=印度尼西亚` | 古超由密克罗尼西亚提供 | 9, 17 | NE + SW | L |
| 11 | `西反=修理水管` | `西反` 可还原板栗，但修理水管直接指马里奥，并不等于板栗 | 1, 14 | NW + E | Y |

标准旗语把这些无序方向对分别读作：

```text
I N O N E F A M I L Y
```

加空格即 **IN ONE FAMILY**。这与题名“本是同根生”互相确认；中央特殊牌必须是“旗”而不是任意图标，也由此得到完整解释。题站已确认它是里程碑。

### Second extraction: plants in one family

逐关找同科的两种不同植物，并沿用中央 🚩 的旗语读法：

| 关 | 同科植物 | 植物科 | 位置 | 方向 | 旗语 |
| ---: | --- | --- | --- | --- | --- |
| 1 | 茉莉花、丁香 | 木犀科 Oleaceae | 18, 21 | S + SW | A |
| 2 | 西瓜、南瓜 | 葫芦科 Cucurbitaceae | 21, 25 | SW + SE | N |
| 3 | 向日葵、菊苣 | 菊科 Asteraceae | 11, 19 | W + SE | S |
| 4 | 海棠、梅 | 蔷薇科 Rosaceae | 5, 21 | NE + SW | L |
| 5 | 地瓜（红薯）、喇叭花（牵牛花） | 旋花科 Convolvulaceae | 1, 17 | NW + SW | I |
| 6 | 艾草、木香 | 菊科 Asteraceae | 3, 7 | N + NW | T |
| 7 | 龙舌兰、芦笋 | 天门冬科 Asparagaceae | 12, 21 | W + SW | H |
| 8 | 红豆、槐树 | 豆科 Fabaceae | 21, 23 | SW + S | A |
| 9 | 梅花、樱花 | 蔷薇科 Rosaceae | 12, 14 | W + E | R |
| 10 | 海高斯（Higos＝无花果）、榕树 | 桑科 Moraceae | 19, 23 | SE + S | G |
| 11 | `卜又寸`→朴树、`广大`→大麻 | 大麻科 Cannabaceae | 5, 18 | NE + S | E |

十一字母连读：

```text
A N S  L I T H A R G E
```

即 **ANS LITHARGE**，明确给出答案 **LITHARGE**。第 5 关的同义牌 `红薯`（7）与 `牵牛花`（21）也分别落在同样的 NW、SW 射线上，因此选用哪张同义牌不影响字母 `I`。

复现命令：

```text
python rounds/toringmoni/nodes/c02-born-from-the-same-root/artifacts/decode_semaphore.py
```

## Candidate audit

- **双层逐关覆盖：** 第一层每关一个假相等，第二层每关一组同科植物；两层都恰好覆盖 11 关、各给一个字母。
- **几何约束：** 两轮共 44 个端点全部恰在中央八条标准射线上；依次读成 `INONEFAMILY` 与 `ANSLITHARGE`，偶然概率极低。
- **外部验证：** 题站已把第一轮结果标为里程碑；第二轮开头的 `ANS` 又直接标记后八字母为答案。
- **主题闭合：** “family”落实为植物科，题名“本是同根生”得到精确解释；🚩 与无序点击分别解释旗语和双臂无先后。
- **答案自洽：** `LITHARGE` 是 lead monoxide（PbO，氧化铅/铅黄的一种），也轻微呼应制作名单中铅笔“lead”的意象，但该旁证不参与字母提取。
- **重要未用信息：** 制作名单的诗句与 `14.4.1.12` 曾诱导出被否定的 PAPERCLIP 路线；没有把它们强行并入已闭合的双层提取。

## Research checks

- 长春与君子兰：[人民网关于长春市花君子兰](https://jl.people.com.cn/n2/2025/0706/c349771-41282600.html)。
- 双发射手费用：[PvZ Wiki 的 Repeater 条目](https://plantsvszombies.wiki.gg/wiki/Repeater_%28PvZ%29)。
- 椰蛋树分类：[宝可梦官方网站图鉴](https://tw.portal-pokemon.com/play/pokedex/0103)。
- 第四关歌词：[《杜鹃》歌词页](https://www.mulanci.org/lyric/sl239716/)。
- 万寿果别名：[农业部食农教育平台的木瓜条目](https://fae.moa.gov.tw/map/food_item.php?id=51&type=AS01)。
- 《本草纲目》葡萄分类：[维基文库《果之五》](https://zh.wikisource.org/zh-hans/%E6%9C%AC%E8%8D%89%E7%B6%B1%E7%9B%AE/%E6%9E%9C%E4%B9%8B%E4%BA%94)。
- 萱草与母爱：[南阳市纪委监委“萱草寄母恩”](https://www.kflz.gov.cn/sitesources/nysjwjw/page_pc/xcjd/wh/article494e6d6211e54f96a91eba5e08ffcc0b.html)。
- 古超来源：[香港天文台台风命名表](https://www.weather.gov.hk/sc/informtc/sound/tcname2026e.html)。
- 旗语读法：[Australian National Botanic Gardens 的 Semaphore 说明](https://www.anbg.gov.au/flags/semaphore.html)。
- 植物科核验采用 Kew Plants of the World Online；较关键的边界包括：[天门冬科同时收录 Agave 与 Asparagus](https://powo.science.kew.org/taxon/urn%3Alsid%3Aipni.org%3Anames%3A30275682-2/general-information)、[Cannabis sativa 属大麻科](https://powo.science.kew.org/taxon/urn%3Alsid%3Aipni.org%3Anames%3A306087-2)以及[朴树 Celtis sinensis 属大麻科](https://powo.science.kew.org/taxon/urn%3Alsid%3Aipni.org%3Anames%3A851171-1)。
- 第 10 关词源：[日本气象厅的官方台风名表](https://www.jma.go.jp/jma/jma-eng/jma-center/rsmc-hp-pub-eg/tyname.html)注明 Higos 是查莫罗语 “fig”；无花果与榕树同为桑科榕属。
- 答案释义：[PubChem 的 Lead monoxide 条目](https://pubchem.ncbi.nlm.nih.gov/compound/14827)把 Litharge 列为 PbO 的名称。

## Submission history

只记录用户或比赛网站明确反馈过的提交；不要把尚未提交的候选写进来。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-17 | PAPERCLIP | rejected | 用户明确反馈“PAPERCLIP 不是答案”，并指出答案应从 11 道小题提取。 |
| 2026-08-17 | IN ONE FAMILY | milestone | 用户明确反馈“IN ONE FAMILY 是里程碑”；题站答案记录的完整消息为“你正在正确的道路上。” |
| 2026-08-17 | LITHARGE | accepted | 用户明确反馈“LITHARGE 是正确答案”。 |

## Evidence and artifacts

- `artifacts/level-pairs.tsv`：11 关全部 132 对牌的持久转录和主题概括。
- `artifacts/semaphore-extraction.tsv`：十一组错配、坐标、方位和逐字结果。
- `artifacts/family-extraction.tsv`：第二层十一组同科植物、还原名、坐标、方位和逐字结果。
- `artifacts/decode_semaphore.py`：由坐标校验八方位、查旗语表，并分别断言 `INONEFAMILY`、`ANSLITHARGE` 的统一复现脚本。
- `artifacts/semaphore-extraction.png`：只保留十一组错误牌射线的可视化证据。
- `artifacts/family-extraction.png`：十一组同科植物射线的第二层可视化证据。
- `artifacts/cancel_letters.py`：被否定的 PAPERCLIP 路线复现脚本，仅保留为失败记录。
- `work/visual/inventory/`：静态 HTML 的资源清单；确认只有一个头像位图，正文不在静态抓取中。
- `work/visual/pair_layout.py` 与 `pair_layout*.png`：把全部配对相连的否定实验。
- `work/visual/binary_grids.py` 与 `binary_grids.png`：把两类牌标成黑白的否定实验。
- `work/cross_level.py`：跨关重名植物的排查脚本；帮助发现关卡语义错误，但不参与最终提取。

## Important failed routes

- **PENCIL LEAD + `14.4.1.12` → PAPERCLIP。** 原路线把诗句解释成 `PENCIL LEAD`，把数字按 A1Z26 读成 `NDAL`；字母两两消去后余 `CILP`，重排为 `CLIP`，再与“素笺”联成 `PAPERCLIP`。虽能局部自洽，却完全没有从 11 关逐关提取，且用户已明确判定 **PAPERCLIP 不是答案**；无新证据不得复用。
- **把每关 12 对牌在 5×5 上直线相连。** 已做三项有界实验：十一关总览、穿过中心旗帜的线、交点数/曼哈顿距离等统计。各序列都不形成可读文字，且制作名单明确称点击“毫无意义”；停止该假设族。
- **把两类牌做成 5×5 二值字形。** 十一关的主题对象/说明两色矩阵及其反色在统一朝向下均不成字；停止该假设。真正要画的只有每关那一组假相等。
- **把正中央旗帜位置当 A1Z26。** 十一关的 🚩 都固定在第 13 格，只会重复得到 `M`，不能区分关卡。
- **跨关精确重名植物串联。** 找到莲花、梅花、卷心菜等自然重名，但第 6、11 关不进入一致链，也没有覆盖全部关卡的稳定排序；不作为提取。

## Next action

无；答案 **LITHARGE** 已确认，节点完成。
