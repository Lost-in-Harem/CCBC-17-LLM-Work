---
node_id: e04-crazy-icomania
title: 疯狂的猜图
kind: puzzle
round: irrational-manager-hypothesis
parent:
source:
round_feeder: yes
feeders:
status: candidate
answer: WEATHER
confidence: medium
summary: 旧调酒路线已撤回。题内操作可复现地留下 H/Ra/Sn；把大小写保留为英语词首，唯一明显的同类四字母补全是 HAIL/RAIN/SNOW。三者都是降水/天气类型，按提示 7 “混在一块”得到七字母 WEATHER。应先用中间答案框依次验证 RAIN、SNOW、HAIL，再提交 WEATHER；矿物组右侧十字母的逐项查表法仍是未复原缺口。
updated: 2026-08-22
---

# 疯狂的猜图

## Current conclusion

当前候选为 **`WEATHER`**，但应先验证三个中间答案 **`HAIL / RAIN / SNOW`**。这条补全不再使用任何外部酒谱，也不把一个品牌反推成配料。

官方提示 4 把“第一部”锁定为《疯狂的石头》：左侧识别矿物并按石头相对于鸡蛋所体现的“硬”这一性质，即矿物硬度排序；右侧指向记录石头的《石头记》，画面中的林黛玉、贾宝玉正是校验。图 26 的右半是 `Kwon Yuri + 贾宝玉/玉`，直接给 **Ureyite**（kosmochlor 的旧名，Strunz 主类 9），不是需要画面中不存在的 `Marin` 的 Yurmarinite。因此图 26 为 `Englishite(8)+Ureyite(9)=89 Ac`。

三组第一层共同给出 **`ANGOSTURA / SHOW YOUR BASE V DIGITS`**。图 10–20 再以左右主题对象的数值拼原子序数，元素符号精确拼成 **`XENA'S AT BASE V TEAM YES`**；按 astronomY / racE / mineralS 三队取五进制数字，四个完整三队列得到 **`Ge Ta La W → GET A LAW`**。

移除这四个完整列后，三个余项是 `Hf/Pu/Ac`。`XENA'S` 指向 Xena 的演员 **Lucy Lawless**；`GET A LAW` 从 `LAWLESS` 中取走 `LAW`，留下操作语 **`LUCY LESS`**。把 `LUCY` 元素化为 `Lu/C/Y`，依次作原子序数减法：

| 余项 | 减数 | 原子序数差 | 元素碎片 | 完整中间答案候选 |
| --- | --- | ---: | --- | --- |
| Hf 72 | Lu 71 | 1 | `H` | **HAIL** |
| Pu 94 | C 6 | 88 | `Ra` | **RAIN** |
| Ac 89 | Y 39 | 50 | `Sn` | **SNOW** |

这里保留元素符号的自然大小写，并把它们当作词首：`H... / Ra... / Sn...`。三个同为四字母、同属天气/降水且逐项精确保留词首的补全是 **HAIL / RAIN / SNOW**；相比旧路线给 H、Ra、Sn 任意补不同长度的酒类词，这一补全有统一的长度、语义和方向。官方提示 7 又要求三个中间答案在现实中“混在一块”成为一个七字母事物；三者共同构成 **WEATHER**，长度正好为 7。

尚未闭合的证据缺口是：矿物组右侧如何逐图统一查得 `ASEVDIGITS` 仍未复原。它由完整指令和下层独立出现的 `AT BASE V` 交叉固定，但不能伪装成已经逐项证明。因此当前置信度为 `medium`。为节省提交次数，先验证词首约束最强的 `RAIN → SNOW`，两者若都有中间反馈，再测只固定首字母的 `HAIL`；三个均通过后才提交 `WEATHER`。

## Official hints supplied by the user

### 提示 7：该如何提取？

此前按用户授权解锁，原文为：

> 在现实中，三个中间答案“混在一块”可以变成一个事物，它的长度为（7）。

### 提示 3：图片的具体解读

> 这些图片可分成三组，每组图片中的事物属于同一类，并且这类事物分别对应了“三部”中的一部。每张图片可分为两部分，左边和右边分别体现了一个和主题有关的事物，左边的事物用于排序，右边的事物用于提取。

### 提示 4：“第一部”怎么做？

用户于 2026-08-22 解锁，原文为：

> 主题拥有一种特殊的性质（鸡蛋和主题拥有相反的这类性质），左侧是用主题进行对于这个性质的排序。右边是一本“记”录主题的书，你会注意到某些图片就和这本书有关。

## 第一层：按提示 3 分组、排序、提取

三组分别是天体、赛车场、矿物，对应《疯狂的外星人》《疯狂的赛车》《疯狂的石头》。每张 512×256 图的稳定编号和左右边界见 `work/visual/transcription.md`。

### 天体组：`ANGOSTURA`

左侧按天体的编号/序号递增；右侧天体的编号以 A1Z26 取字。若同一画面还可读成另一个天体名，那是后面的元素层，不替代这里的主读法。

| 顺序 | 图 | 左侧排序对象 | 左值 | 右侧对象 | 右值 | 字母 |
| ---: | ---: | --- | ---: | --- | ---: | --- |
| 1 | 9 | Mercury | 1 | Io（Jupiter I） | 1 | A |
| 2 | 5 | Venus | 2 | Hippocamp（Neptune XIV） | 14 | N |
| 3 | 7 | Earth | 3 | Hyperion（Saturn VII） | 7 | G |
| 4 | 1 | Vesta | 4 | Atlas（Saturn XV） | 15 | O |
| 5 | 27 | Atlas | 15 | Ymir（Saturn XIX） | 19 | S |
| 6 | 13 | 588 Achilles | 588 | 20 Massalia | 20 | T |
| 7 | 10 | 1388 Aphrodite | 1388 | 21 Lutetia | 21 | U |
| 8 | 6 | 4017 Disneya | 4017 | 18 Hydrae | 18 | R |
| 9 | 14 | 6063 Jason | 6063 | Phobos（Mars I） | 1 | A |

结果为 **`ANGOSTURA`**。这一组的排序、数值和九个字母均已闭合；它单独提交已判错，因此既不是终答，也不是完整中间答案。它只承担完整指令 `ANGOSTURA SHOW YOUR BASE V DIGITS` 的首词；此前把后出的 `Ra` 强行对回该品牌并猜成 BITTERS 的路线已由 VERMOUTH 判错而撤回。

### 赛车场组：`SHOWYOURB`

左侧按赛道单圈长度递增；右侧识别另一条赛道，取其 FIA 国家三字码的中间字母。

| 顺序 | 图 | 左侧赛道（约 km） | 右侧赛道 | 国家码 | 字母 |
| ---: | ---: | --- | --- | --- | --- |
| 1 | 3 | Lime Rock Park（2.462） | Road America | USA | S |
| 2 | 4 | Manfeild（3.030） | Tianmashan | CHN | H |
| 3 | 8 | Qinhuangdao（3.740） | Monaco | MON | O |
| 4 | 16 | Rockingham（约 3.9） | Mantorp Park | SWE | W |
| 5 | 2 | Salzburgring（4.241） | Sepang | MYS | Y |
| 6 | 12 | Magny-Cours（4.411） | Lousada | POR | O |
| 7 | 11 | Buddh（5.125） | Red Bull Ring | AUT | U |
| 8 | 28 | Silverstone（5.891） | Estoril | PRT | R |
| 9 | 15 | Mount Panorama（6.213） | Knockhill | GBR | B |

结果为 **`SHOWYOURB`**。图 2、4、12 的完整 rebus 文字解释仍略弱，但排序结果和国家码中间字母组成的英文串非常稳定。

### 矿物组：硬度排序，输出 `ASEVDIGITS`

目前最稳的左右矿物识别如下：

| 图 | 左侧矿物 | 右侧矿物 | 备注 |
| ---: | --- | --- | --- |
| 17 | Calcite | Eldragónite | 右图直接含 dragon/no/top 词元；旧 Cinnabar 读法不再优先 |
| 18 | Topaz | Malachite | 高 |
| 19 | Parkinsonite | Perrierite-(Ce) | 中 |
| 20 | Jadeite | Forsterite | 高 |
| 21 | Westerveldite | Northstarite | 左右空间分组明确 |
| 22 | Tsumoite | Arctite | 高 |
| 23 | Baumstarkite | Colusite | 高 |
| 24 | Spangolite | Rutile | 高 |
| 25 | Johnsenite-(Ce) | Loveringite | 中高 |
| 26 | Englishite | Ureyite（kosmochlor 旧名） | 高；Yuri + 宝玉/玉，且提示 4 明示《石头记》；旧 Yurmarinite 缺少 Marin 画面证据 |

提示 4 的“鸡蛋与石头相反”指向软硬，故左侧按矿物硬度递增；其自然顺序为 `19,23,22,24,17,26,25,21,20,18`。低硬度端的文献常以相邻区间报告（例如 `2–2.5`、`2.5`、`2.5–3`），具体并列次序由右侧明文消歧。右侧《石头记》线索与全局语法给出 **`ASEVDIGITS`**，完整指示为：

**`ANGOSTURA / SHOW YOUR BASE V DIGITS`**

其中 `...BASE V DIGITS` 还被下一层独立出现的 `AT BASE V` 交叉校验。当前仍有一项可披露缺口：提示 4 已确定右侧文本为《石头记》，但十张右图各自如何统一落到十个字母的标准化查表尚未逐项复原；`ASEVDIGITS` 由完整英语句、官方主题提示和下层独立指令三重确定，不把未知的逐图字段伪装成已证事实。

## 第二层：元素提示

同一批画面还能给出另一套三类数值：

- 天体：两个可读英文名的长度；
- 赛车场：两个赛道的 FIA licence grade；
- 矿物：两个矿物的 Nickel–Strunz 大类首位。

把左右两个数字依次拼成十进制原子序数，再换为元素符号。图 10–20 连续得到：

| 图 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 原子序数 | 54 | 11 | 16 | 85 | 56 | 34 | 23 | 52 | 95 | 39 | 99 |
| 元素 | Xe | Na | S | At | Ba | Se | V | Te | Am | Y | Es |

连读为 **`XENA'S / AT BASE V / TEAM YES`**。这解释了为什么用户试过的 `AT BASE V`、`TEAMYES` 和连写都不是答案：它们是操作提示。

## 第三层操作语：`GET A LAW`（不得再作为答案提交）

把图 10–20 作为提示段移出，把末尾图 27–28 的 `Xe/Na` 作为边界标记暂时移出。余项按页面出现次序分成 astronomY、racE、mineralS 三队；每个原子序数写成三位五进制，三队分别取第 1、2、3 位，再把三位重组成一个原子序数：

| 列 | 天体第 1 位 | 赛车第 2 位 | 矿物第 3 位 | 五进制 | 元素 |
| ---: | --- | --- | --- | --- | --- |
| 1 | 45=`140` →1 | 33=`113` →1 | 27=`102` →2 | `112`=32 | Ge |
| 2 | 59=`214` →2 | 22=`042` →4 | 28=`103` →3 | `243`=73 | Ta |
| 3 | 55=`210` →2 | 34=`114` →1 | 22=`042` →2 | `212`=57 | La |
| 4 | 58=`213` →2 | 21=`041` →4 | 74=`244` →4 | `244`=74 | W |

元素符号为 **`Ge Ta La W` → `GET A LAW`**。图 21 的左右边界修正本身仍成立：箭头和公鸡草地重叠成左组 `WEST + (roost)ER + VELD`，星光是独立右组 Northstarite。用户已明确判错 `GET A LAW`，所以它不得再作为答案；但四列同时成为合法元素且精确成句，再与 `XENA'S/Lawless` 闭合，远强于随机命中，应保留为操作语。

## 图 26 的最终判定：`Ureyite → 89 Ac`

图 26 左半是 Englishite，属 Strunz 主类 8。右半是 Kwon Yuri 与贾宝玉形象：

- `Yuri` 直接近音 `Urey`；
- `宝玉/玉` 直接给 stone/mineral 的 `-ite`，并由提示 4 的《石头记》明示；
- 合起来是 **Ureyite**，即 kosmochlor 的旧名，Nickel–Strunz `9.DA.25`。

旧读法 Yurmarinite 虽是现行正式矿物，却需要图中不存在的 `Marin`；它此前完全由错误的 MARTINE 配方反推。提示 4 消除了这一歧义，不能再用下游猜答覆盖直接图像证据。因此：

`Englishite (8) + Ureyite (9) = 89 Ac`

四个完整三队列之后的未消费元素为 **`Hf / Pu / Ac`**；这不改变前四列的 `GET A LAW`，但使 `LUCY` 的逐项减法得到正确的 **`H/Ra/Sn`**。

## 已拒绝的终局路线：`VERMOUTH / BITTERS / GIN -> PERFECT`

`XENA'S` 指 Xena 的演员 **Lucy Lawless**。把她的名字按题内两条操作语切成：

`LUCY / LAW / LESS`

`GET A LAW` 是从 `LAWLESS` 取走 `LAW`，留下 **`LUCY LESS`**。将 `LUCY` 元素化为 `Lu/C/Y`，按原子序数逐项从三个未消费元素中相减。原串 `XENA'S = Xe/Na/S` 还明确留有末尾的 `S`，可供第三行的 `less S` 使用：

| 运算 | 差 | 符号 | 后续处理 | 完整中间答案候选 |
| --- | ---: | --- | --- | --- |
| `Hf72−Lu71` | 1 | H | 补在 `VERMOUT` 后 | **VERMOUTH** |
| `Pu94−C6` | 88 | Ra | 补在 `ANGOSTU` 后识别品牌，再取品类 | **BITTERS** |
| `Ac89−Y39` | 50 | Sn | `LESS S` 得 N，补在 `GI` 后 | **GIN** |

这曾被当作提示 7 所要求的三个完整中间答案候选，但 `VERMOUTH` 已被用户明确判定既不是答案也不是中间答案。因此由 H/N 和调酒语境补出 VERMOUTH/GIN、再由 ANGOSTURA 猜 BITTERS 的做法没有题内依据，整条路线撤回。

三种配料在现实中确有对应 Perfect Cocktail / Perfect Martini 的外部配方，但这不能替代题内提取；由于中间答案 VERMOUTH 已被判错，以下旧候选同时撤回：

**`PERFECT`**

不得再提交 `PERFECT`，除非出现全新的题内提取链并重新得到它。

## 已撤回的终局路线：`HARNESS`

`H+Ra+Sn+Es → HARNESS` 虽是精确七字母重排，但把提示 7 的“现实中混在一块”误读为纯字谜，而且 `Es` 不是三个完整中间答案之一。该路线在提交前主动撤回。

## 已撤回的终局路线：`NARWHAL`

`NARWHAL` 未收到提交判题结果，但用户指出其推导没有给出三个完整中间答案，而且 `H+Ra+Sn+LAW−S` 的合并不符合提示 7。故该候选主动撤回：`LAW` 的作用仅是从 `LAWLESS` 中取走自身、留下减法词 `LESS`，不能再次作为终局字母加入；也没有依据把 `LESS` 改读成对字母池执行 `−S`。

## 已拒绝的终局路线：`VARNISH`

`XENA'S` 指向 Xena 的扮演者 Lucy **Lawless**。`GET A LAW` 又恰可读成：从元素化的姓名片段 `Lu / C / Y / La / W` 中取走 `La/W`（LAW），留下 `Lu/C/Y`。把这三个元素按队列与未消费的 `Hf/Pu/Ac` 对齐并按原子序数相减：

| 运算 | 差 | 元素碎片 |
| --- | ---: | --- |
| `Hf − Lu` | `72−71=1` | `H` |
| `Pu − C` | `94−6=88` | `Ra` |
| `Ac − Y` | `89−39=50` | `Sn` |

得到三个碎片 **`H / Ra / Sn`**，合计五个字母。提示 7 指定终物为七字母，所以还差两个；第一层指令又特意说 `BASE V DIGITS`。把五进制数字以罗马数字表示，恰有两个字母的候选是 `II` 与 `IV`。固定 50 万常用英语词表做完全集检查：

- `HRA SN + IV` 可重排成普通实物 **`VARNISH`**；
- 其他满足碎片和两字符五进制罗马数字的词只有 `NASHIRI`、`SHIRVAN` 等专名；
- 因而 **`H + RA + SN + IV → VARNISH`** 是该受限搜索中的唯一普通实物。

这还得到提示 7 的表面现实校验：传统 varnish 由树脂、干性油和稀释剂/溶剂组合而成，似乎是“三种东西混在一块”形成的七字母事物。

用户已明确判错 `VARNISH`。这与上述两个未闭合点一致：矿物组 `ASEVDIGITS` 由全句反补，而 `IV` 也不是三个中间答案之一。整条“元素差值 + 罗马数字 + 字谜重排”路线停止，不再枚举邻近词。

## 已拒绝的终局：`LUCY LESS → H / Ra / In → MARTINE`

`XENA'S` 指向扮演 Xena 的 Lucy **Lawless**。把 `GET A LAW` 作用于姓氏：

`LAWLESS − LAW = LESS`

把人物全名解释成元素化的逐项减法 `LUCY LESS`：将 `LUCY` 拆成 `Lu / C / Y`，从三个余项中相减：

| 运算 | 原子序数差 | 结果符号 | 配料词尾 |
| --- | ---: | --- | --- |
| `Hf − Lu` | `72−71=1` | H | vermout**H** |
| `Pu − C` | `94−6=88` | Ra | Angostu**RA** |
| `Ra − Y` | `88−39=49` | In | g**IN** |

三个符号作为词尾，结合已经独立得到的 ANGOSTURA 与提示 7 的现实混合关系，补成：

- vermout**H**；
- Angostu**RA**；
- g**IN**。

泛称 **MARTINI** 与配方近邻 **ASTORIA** 均已被用户判错，不能重提。D. Schoor 1916 年调酒书第 13 项虽有 **“Martine. Sweet.”**，正文列出 `2/3 Ital. Vermouth`、`1/3 Gin`、`Angostura`，但这只能构成当时的外部枚举依据，不能弥补题内机制缺口。该旧候选为：

`VERMOUTH + ANGOSTURA + GIN → MARTINE`

用户已明确判错 `MARTINE`。这条路线依赖两个未由题面独立支持的跳步：把图 26 强行读作 Yurmarinite，以及把三个元素碎片补成三种配料后再用外部历史配方选酒名。该酒名枚举路线停止。

## Submission history

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-20 | 疯狂的石头 | 错误答案 | 用户报告三个建议的中间答案均被判错；无其他判题文字。 |
| 2026-08-20 | 疯狂的赛车 | 错误答案 | 用户报告三个建议的中间答案均被判错；无其他判题文字。 |
| 2026-08-20 | 疯狂的外星人 | 错误答案 | 用户报告三个建议的中间答案均被判错；无其他判题文字。 |
| 2026-08-21 | TEAMYES | 错误答案 | 用户明确报告不是答案，并提示中间答案可能不完整。 |
| 2026-08-21 | AT BASE V | 错误答案 | 用户明确报告不是答案，并提示中间答案可能不完整。 |
| 2026-08-21 | ATBASEVTEAMYES | 错误答案 | 用户明确报告不是答案；无其他判题文字。 |
| 2026-08-21 | SET A LAW | 错误答案 | 用户明确报告不是答案，且判题无任何反馈。 |
| 2026-08-21 | LESS | 错误答案 | 用户明确报告不是答案；未提供其他判题文字。 |
| 2026-08-21 | LESSNESS | 错误答案 | 用户明确报告不正确；随后提供官方提示。 |
| 2026-08-21 | ARBITER | 错误答案 | 用户明确报告不是答案；未提供其他判题文字。 |
| 2026-08-21 | ANGOSTURA | 错误答案 | 用户明确报告不是答案；未提供其他判题文字。 |
| 2026-08-21 | ARGON | 错误答案 | 用户报告建议测试的三个元素全名均不对；无其他判题文字。 |
| 2026-08-21 | BISMUTH | 错误答案 | 用户报告建议测试的三个元素全名均不对；无其他判题文字。 |
| 2026-08-21 | TANTALUM | 错误答案 | 用户报告建议测试的三个元素全名均不对；无其他判题文字。 |
| 2026-08-21 | MARTINI | 错误答案 | 用户明确报告不是答案；无其他判题文字。 |
| 2026-08-21 | BARISTA | 错误答案 | 用户明确报告“不对啊”；无其他判题文字。 |
| 2026-08-21 | ASTORIA | 错误答案 | 用户明确报告不是答案；无其他判题文字。 |
| 2026-08-21 | GET A LAW | 错误答案 | 用户明确报告不是答案；无其他判题文字。 |
| 2026-08-22 | VARNISH | 错误答案 | 用户明确报告不是答案，并指出这一候选明显不合理；无其他判题文字。 |
| 2026-08-22 | MARTINE | 错误答案 | 用户明确报告不是答案；无其他判题文字。 |
| 2026-08-22 | VERMOUTH | 错误答案/中间答案 | 用户明确报告“不是答案或者中间答案”；无其他判题文字。 |

## Important failed routes

- 上表二十项均是已明确错误的提交；没有新判题证据时不得再次作为答案提出。
- `MARTINE` 已被明确判错。旧路线用错误的 Yurmarinite/88 直接得到 `In`，再靠历史配方枚举酒名；不得恢复。当前路线由提示 4 独立固定 Ureyite/89，保留 `Sn` 作为 **SNOW** 的词首，不再任意执行 `LESS S`。
- `NARWHAL` 没有提交判题，但已由用户指出机制错误并撤回：只给 `H/Ra/Sn` 没有给三个完整中间答案，且 `+LAW−S` 不是提示 7 允许的合并。不得再提。
- `HARNESS` 没有提交判题；它把 `H/Ra/Sn` 与额外的 `Es` 做纯字母重排，既没有给出三项现实中间答案，也误读了“现实中混在一块”，已撤回。
- `VARNISH` 已被明确判错。它在 `H/Ra/Sn` 后凭空补 `IV`；当前把三个元素符号按原大小写统一补成同为四字母的天气词，不再从词表猜补字母。
- `GET A LAW` 已被判错，不能再作为答案提交；但 `Ge/Ta/La/W` 四列精确成句且能与 Xena/Lucy Lawless 闭合，所以保留为操作语。判题否定的是候选身份，不等于否定所有指令用途。
- `BARISTA` 的 `LESS → Ar/Bi/Ta` 需要把英文 `LESS` 任意转成元素原子序数减法，随后又要从 `XENA'S` 或 `ANGOSTURA[V]` 补一个 S 并重排；判题已否定这条缺乏唯一指示的终局路线。
- `ASTORIA` 已被明确判错，不得重提。它的配方证据没有 `MARTINE` 的 1916 年同名原始条目直接。
- `ANGOSTURA` 已明确判错，不得再次作为中间答案提交；当前只保留它在完整操作句中的字面作用，不再据此猜 BITTERS。
- `VERMOUTH` 已明确判定既不是答案也不是中间答案；因此 `VERMOUTH/BITTERS/GIN -> PERFECT` 整条路线撤回，`BITTERS`、`GIN`、`PERFECT` 不得顺次试错。
- `MARTINI` 与 1916 年拼法 `MARTINE` 均已明确判错，不得重提；酒名枚举路线已经停止。
- `ARGON / BISMUTH / TANTALUM` 三个元素全名均未通过中间答案验证，不能再次单独提交；它们所属的 `Ar/Bi/Ta → BARISTA` 路线也已整体停止。
- `Backite + Morningstarite → 74 W` 违背图 21 的真实左右空间边界；保留为失败路线。
- 图 26 的 Yurmarinite=`88 Ra` 是由 MARTINE 反推的失败读法：画面从未给出 `Marin`。官方提示 4 的《石头记》与右图 `Yuri + 宝玉/玉` 直接支持 Ureyite=`89 Ac`；VARNISH 被判错只否定任意补 `IV`，不否定 Ureyite 本身。
- Fermion Index 只在 Colusite、Rutile、Forsterite 等少数位置偶合目标字母；Malachite、Arctite、Loveringite、Perrierite-(Ce) 等立即反例，停止该字段族。
- 矿物公式质子数和 mod-26 在个别行偶合，但不能统一生成十字母后缀，停止该族。
- 在原始五进制位流中盲搜 `GIN/VERMOUTH` 没有命中；这与后续判题共同否定了调酒补词，但不否定由 `LUCY LESS` 明示的元素减法本身。
- `ANGOSTURA/BITTERS` 作为五进制 key 的三种有界算术实验均无稳定明文，停止该假设族。
- 把 `ARGON/BISMUTH/TANTALUM` 当作真实化学配方并猜 `CRYSTAL/CERAMIC/COATING` 需要任意添加反应物、气氛或泛化产物名，缺乏唯一性，不列候选。
- `PINKGIN` 缺少 vermouth；`DRY MARTINI`、`GIN AND IT`、`Turf Club` 又不符合七字母枚举。它们只是配方近邻，不列候选。
- 对“TEAM YES 直接选位”的后续三项有界实验均失败：5 种矿物排序的排序位流、6 种队伍映射的 5×5 路径字形，以及 `6×3×3` 个“选位后三位重组元素”组合均无稳定英文。
- 移除图 10–20 与末端 `Xe/Na` 后，针对剩余 5/4/6 图又依次测试了三种自然读法：用队伍位索引左右专名、删去队伍位后把余下两位读 A–Y、用队伍位索引元素英文名。每项均遍历已记录的自然排序和 6 种队伍映射，没有任何配置同时给出三个词；这是该残余直接取词家族的第三次有界失败，现停止扩张。
- `GET A LAW` 判错后曾改为只移除图 10–20、保留末端 `Xe/Na`，形成 6/5/6 三组；同样对专名索引、删位读字、元素全名索引做三项有界审计，仍无配置同时产出三个词。这个边界修正家族也已停止。

## Evidence and sources

- 持久逐图转录：`work/visual/transcription.md`
- 第一层和五进制审计：`work/extraction-results.md`
- 参数化有界测试：`work/extraction_test.py`
- FIA licensed circuits：https://www.fia.com/circuit-safety
- IMA Master List：https://athena.unige.ch/athena/mineral/IMA-Master-List-2026-03.pdf
- Yurmarinite（失败对照；名称确实来自 Yuri B. Marin，但图中无 Marin）：https://www.mindat.org/min-43895.html
- Kosmochlor / Ureyite（旧名）的 Nickel–Strunz 编号 `9.DA.25`：https://www.mindat.org/min-2249.html
- Englishite 的 Nickel–Strunz 编号 `8.DH.55`：https://www.mindat.org/min-1386.html
- Westerveldite：https://www.mindat.org/min-4273.html
- Northstarite（Strunz `7.JA.20`）：https://www.mindat.org/min-53865.html
- Caltech 对 Xena/Eris、Dysnomia 与 Lucy Lawless 的说明：https://www.caltech.edu/about/news/dwarf-planet-formerly-known-xena-has-officially-been-named-eris-iau-announces-1187
- Met Office 对 rain、snow、hail 均为 precipitation/weather types 的说明：https://weather.metoffice.gov.uk/learn-about/met-office-for-schools/other-content/other-resources/what-is-precipitation
- Astoria 的经典配方（Old Tom gin、dry vermouth、Angostura orange bitters）：https://www.diffordsguide.com/cocktails/recipe/2260/astoria
- D. Schoor 1916 年《Zakboekje voor recepten van American Drinks》；第 13 项 “Martine. Sweet.” 明列 Italian vermouth、gin、Angostura：https://www.dbnl.org/tekst/scho618zakb01_01/scho618zakb01_01_0003.php
- Perfect Martini / Perfect Cocktail 的 gin、dry/sweet vermouth 与 Angostura 配方：https://www.diffordsguide.com/cocktails/recipe/1509/perfect-martini
- Martini/Martine 早期名称与 gin、vermouth、Angostura 史料时间线：https://www.thedailybeast.com/the-coming-of-the-martini-an-annotated-timeline/
- Varnish 的传统组成（干性油、树脂、稀释剂/溶剂）：https://en.wikipedia.org/wiki/Varnish
- CAMEO 对 varnish 为树脂溶于干性液体所成涂层的说明：https://cameo.mfa.org/wiki/Varnish

## Next action

请用户先在中间答案框依次验证 **RAIN、SNOW、HAIL**。前两项分别保留完整词首 `Ra/Sn`，约束强于只保留 `H` 的第三项。若三者均获得中间反馈，再提交七字母 **WEATHER**；若任一项无反馈，就保留 `H/Ra/Sn` 算术层、撤回语义补全，并优先解锁提示 5 或提示 6 来核对第二/第三组的精确取法，而不是继续枚举配料或七字母词。
