---
node_id: e04-crazy-icomania
title: 疯狂的猜图
kind: puzzle
round: irrational-manager-hypothesis
parent:
source:
round_feeder: yes
feeders:
status: rejected
answer:
confidence:
summary: MARTINE 已被用户明确判错，酒名枚举路线停止。当前回到两处未闭合的基础机制：图 26 右半矿物的真实识别，以及矿物组的统一排序/提取字段；在这两处独立复原前不再给终答。
updated: 2026-08-22
---

# 疯狂的猜图

## Current conclusion

当前无可提交候选。**`MARTINE` 已被用户明确判错**，因此 `H/Ra/In → vermouth/Angostura/gin → 酒名` 这条终局路线停止；不能再用一个历史配方替代缺失的题内提取。当前调查回到两处未闭合的基础机制：图 26 右半矿物的真实识别，以及矿物组十图的统一排序/提取字段。

用户新提供的官方提示 3 给出了主结构：28 图分为三组，每组对应“三部”中的一部；每图的左半给排序对象，右半给提取对象。按这个结构重新审计后：

- 天体组高置信得到 **`ANGOSTURA`**；
- 赛车场组高置信得到 **`SHOWYOURB`**；
- 矿物组从全局语法几乎必为 **`ASEVDIGITS`**，合成 **`ANGOSTURA / SHOW YOUR BASE V DIGITS`**，但矿物组的排序字段和右侧取字字段尚未独立复原，不能把补句当作证明。

元素层是有意结构：图 10–20 的元素符号精确拼成 **`XENA'S AT BASE V TEAM YES`**；去掉这段操作提示后，以三队五进制数字重组得到操作语 **`GET A LAW`**。Xena 的扮演者是 Lucy **Lawless**；从元素化的 `Lu/C/Y/La/W` 中“取走” `La/W`，留下 **`Lu/C/Y`**，即 `LUCY LESS [LAW]`。

图 26 目前恢复为正式矿物 **Yurmarinite**（Strunz 主类 8）。右侧第一人是权俞利（Yuri），第二人是贾宝玉形象；贾宝玉有马天宇、林青霞等不同扮演者，因此画面可能借角色/演员绕到 `Marin`，但这一 rebus 仍不够直接。另一读法 Ureyite（kosmochlor 旧名，9 类）虽然能用 `Yuri + 玉/stone` 解释，却导向已被判错且违反提示 7 语义的 `VARNISH`。结合现行 IMA 名录、后续精确减法及用户判题，当前以 `8+8=88 Ra` 为较强读法，但保留构词缺口。

三个未消费元素因此为 `Hf/Pu/Ra`。把 `LUCY` 拆成元素 `Lu/C/Y` 并按 `LESS` 逐项相减，精确得到 **`H/Ra/In`**：

`Hf−Lu=H`，`Pu−C=Ra`，`Ra−Y=In`。

这三个元素符号分别补全三个现实配料 vermout**H**、Angostu**RA**、g**IN**。1916 年 D. Schoor 的《Zakboekje voor recepten van American Drinks》在第 13 项 **“Martine. Sweet.”** 中明确列出 `2/3 Italian vermouth`、`1/3 gin`、`Angostura`，酒名恰为七字母 **MARTINE**；另有糖浆、樱桃和柠檬皮作为辅料。它是对提示 7 最直接的新匹配，并且不是已被判错的拼法 `MARTINI`。

## Official hints supplied by the user

### 提示 7：该如何提取？

此前按用户授权解锁，原文为：

> 在现实中，三个中间答案“混在一块”可以变成一个事物，它的长度为（7）。

### 提示 3：图片的具体解读

> 这些图片可分成三组，每组图片中的事物属于同一类，并且这类事物分别对应了“三部”中的一部。每张图片可分为两部分，左边和右边分别体现了一个和主题有关的事物，左边的事物用于排序，右边的事物用于提取。

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

结果为 **`ANGOSTURA`**。这一组的排序、数值和九个字母均已闭合；它单独提交虽已判错，但它在完整句 `ANGOSTURA SHOW YOUR BASE V DIGITS` 中承担指令首词，而非终答。

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

### 矿物组：预期 `ASEVDIGITS`，机制未独立闭合

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
| 26 | Englishite | Yurmarinite（Ureyite 为备选） | 中；后续与现行 IMA 名录支持 Yurmarinite=8，但画面如何完整给出 Marin 尚未闭合 |

赛车场串止于 `...B`，而元素层又独立出现 `AT BASE V`，故矿物组十字母从全局语法应为 **`ASEVDIGITS`**，完整指示为：

**`ANGOSTURA / SHOW YOUR BASE V DIGITS`**

尚未找到一个对十个右侧矿物统一成立、能给出 `A S E V D I G I T S` 的标准属性。已检查矿物名首尾/长度、IMA 符号、Strunz/Dana 编码、晶系、公式元素、发现年份、产地、Fermion Index 等常见字段；没有统一命中。此处必须继续标为“由两条独立语境补全”，而不是已证提取。

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

## 图 26 的重新判定：`Yurmarinite → 88 Ra`

图 26 左半是 Englishite，属 Strunz 主类 8。右半是 Kwon Yuri 与贾宝玉形象。这里存在两个可复现读法：

- **Yurmarinite** 是 IMA 2013-033 正式矿物，名称纪念 Yuri B. Marin，属 8 类；
- **Ureyite** 已并入 kosmochlor，只是旧名/同物异名，属 9 类；`Yuri + 玉/stone` 可近似解释它，但它不在当前 IMA Master List 中。

贾宝玉并不能直接等同 `Marin`，这是 Yurmarinite 读法的主要缺口；不过这一角色有马天宇、林青霞等多个著名扮演者，画面很可能要求用演员名继续转义。更重要的是，Ureyite=9 导出的 `H/Ra/Sn + IV → VARNISH` 已被判错且没有三个中间答案；Yurmarinite=8 则同时满足现行矿物名录并精确产出提示 7 所需的三种配料。因此当前恢复：

`Englishite (8) + Yurmarinite (8) = 88 Ra`

四个完整三队列之后的未消费元素据此为 **`Hf / Pu / Ra`**。这不会改变前四列的 `GET A LAW`，却使 `LUCY LESS` 得到完整的 `H/Ra/In`。

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

泛称 **MARTINI** 与配方近邻 **ASTORIA** 均已被用户判错，不能重提。但这次出现了新的、可核验的一手证据：D. Schoor 1916 年调酒书第 13 项的标题是 **“Martine. Sweet.”**，正文逐项列出 `2/3 Ital. Vermouth`、`1/3 Gin`、`Angostura`，另加 gum syrup、cherry 和 lemon peel。`MARTINE` 恰为七字母，并与已判错的 `MARTINI` 是不同历史拼法。因此当前候选为：

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

## Important failed routes

- 上表二十项均是已明确错误的提交；没有新判题证据时不得再次作为答案提出。
- `MARTINE` 已被明确判错。由 `H/Ra/In` 补配料并枚举酒名的路线没有题内唯一性，停止整个酒名家族，不再换拼法或找近邻配方。
- `VARNISH` 已被明确判错。`H/Ra/Sn` 后补 `IV` 再重排的关键两字母没有独立提取，而且三个片段也不是提示 7 所说的三个现实配料名；该字谜枚举家族停止。
- `GET A LAW` 已被判错，不能再作为答案提交；但 `Ge/Ta/La/W` 四列精确成句且能与 Xena/Lucy Lawless 闭合，所以保留为操作语。判题否定的是候选身份，不等于否定所有指令用途。
- `BARISTA` 的 `LESS → Ar/Bi/Ta` 需要把英文 `LESS` 任意转成元素原子序数减法，随后又要从 `XENA'S` 或 `ANGOSTURA[V]` 补一个 S 并重排；判题已否定这条缺乏唯一指示的终局路线。
- `ASTORIA` 已被明确判错，不得重提。它的配方证据没有 `MARTINE` 的 1916 年同名原始条目直接。
- `MARTINI` 作为现代泛称已被明确判错。当前 `MARTINE` 不是无证据替换字母：1916 年同名配方明确逐项列出 vermouth、gin、Angostura；只有这条新证据允许有限恢复该配料族。
- `ARGON / BISMUTH / TANTALUM` 三个元素全名均未通过中间答案验证，不能再次单独提交；它们所属的 `Ar/Bi/Ta → BARISTA` 路线也已整体停止。
- `Backite + Morningstarite → 74 W` 违背图 21 的真实左右空间边界；保留为失败路线。
- 图 26 当前采用 `Yurmarinite → 88 Ra`。`Marin` 的画面构词仍不完整，但它是现行 IMA 正式矿物，且与 `LUCY LESS → H/Ra/In`、提示 7 及 1916 年 MARTINE 配方形成同一条可复现链。Ureyite=9 保留为敏感性对照，其后 VARNISH 已被判错。
- Fermion Index 只在 Colusite、Rutile、Forsterite 等少数位置偶合目标字母；Malachite、Arctite、Loveringite、Perrierite-(Ce) 等立即反例，停止该字段族。
- 矿物公式质子数和 mod-26 在个别行偶合，但不能统一生成十字母后缀，停止该族。
- 在原始五进制位流中盲搜 `GIN/VERMOUTH` 没有命中；这否定的是直接位流读取，不是否定后续由 `LUCY LESS` 明示的元素减法。
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
- Yurmarinite（IMA 2013-033；以 Yuri B. Marin 命名）：https://www.mindat.org/min-43895.html
- Kosmochlor / Ureyite（旧名）的 Nickel–Strunz 编号 `9.DA.25`：https://www.mindat.org/min-2249.html
- Englishite 的 Nickel–Strunz 编号 `8.DH.55`：https://www.mindat.org/min-1386.html
- Westerveldite：https://www.mindat.org/min-4273.html
- Northstarite（Strunz `7.JA.20`）：https://www.mindat.org/min-53865.html
- Caltech 对 Xena/Eris、Dysnomia 与 Lucy Lawless 的说明：https://www.caltech.edu/about/news/dwarf-planet-formerly-known-xena-has-officially-been-named-eris-iau-announces-1187
- Astoria 的经典配方（Old Tom gin、dry vermouth、Angostura orange bitters）：https://www.diffordsguide.com/cocktails/recipe/2260/astoria
- D. Schoor 1916 年《Zakboekje voor recepten van American Drinks》；第 13 项 “Martine. Sweet.” 明列 Italian vermouth、gin、Angostura：https://www.dbnl.org/tekst/scho618zakb01_01/scho618zakb01_01_0003.php
- Martini/Martine 早期名称与 gin、vermouth、Angostura 史料时间线：https://www.thedailybeast.com/the-coming-of-the-martini-an-annotated-timeline/
- Varnish 的传统组成（干性油、树脂、稀释剂/溶剂）：https://en.wikipedia.org/wiki/Varnish
- CAMEO 对 varnish 为树脂溶于干性液体所成涂层的说明：https://cameo.mfa.org/wiki/Varnish

## Next action

重新查看图 17–26 的原始左右半图，并建立矿物名称、分类号及可能提取字段的逐行证据表；优先用矿物组自身的统一规则同时决定排序、`ASEVDIGITS` 是否真实以及图 26 的名称，不再由下游候选反推图 26。若题内证据仍不足且用户允许再开官方提示，信息增益最高的是提示 6（“第三部”怎么做），但本任务不会自行解锁。
