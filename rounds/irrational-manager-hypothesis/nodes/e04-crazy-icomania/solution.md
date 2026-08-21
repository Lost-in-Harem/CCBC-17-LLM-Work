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
summary: ARBITER 已被用户明确判错。Hf−Xe=Ar、Pu−Na=Bi、Ac−S=Ta 的算术巧合仍保留为待审证据，但不能再据 ArBiTa 作谐音收尾。官方提示强调三个中间答案在现实中混合成 7 字母事物；当前回到三队各自产出真实成分的路线，优先审计移除提示与末端 XENA 后恰为 5/4/6 项的结构。
updated: 2026-08-21
---

# 疯狂的猜图

## Current conclusion

当前无最终答案。用户已明确确认 `疯狂的石头`、`疯狂的赛车`、`疯狂的外星人`、`TEAMYES`、`AT BASE V`、`ATBASEVTEAMYES`、`SET A LAW`、`LESS`、`LESSNESS`、`ARBITER` 均错误；这些字符串不再作为答案提出。

`SET A LAW` 已由用户明确判错且没有里程碑反馈，现已撤回。错误不只在停读边界，更关键的是图 21 的分组：箭头与公鸡草地在画面上重叠成一个左侧图组，星光是独立右侧图组；不能把箭头单独当 Backite、再把公鸡与星光拼成 Morningstarite。

按正确的两图组，左侧构成 `WEST + (roost)ER + VELD(field)` → **Westerveldite**（Strunz 2），右侧星光为 **Northstarite**（Strunz 7），故图 21 是 `27 → Co`。这一改动使相同的五进制三队提取由 `SET A LAW` 精确变为 **`GET A LAW`**。

图 10–20 的操作提示为 `Xe Na S At Ba Se V Te Am Y Es` → `XENA'S AT BASE V TEAM YES`。`AT BASE V` 要把原子序数写成三位五进制；`TEAM YES` 要按 `astronomY / racE / mineralS` 分为 Y/E/S 三队并对齐。

用户授权解锁一条提示后，已选择官方提示 7「该如何提取？」，花费 5101 工资解锁。原文为：

> 在现实中，三个中间答案“混在一块”可以变成一个事物，它的长度为（7）。

这条提示说明 `LESS` 还只是操作词，不能停读。移出提示段和末端 `Xe Na` 边界后，五进制三队对角取位得到 `Ge Ta La W` → **`GET A LAW`**，而未消费的三个元素恰为 `Hf / Pu / Ac`。Xena 的扮演者是 Lucy **Lawless**；从 `LAWLESS` “get a LAW” 后余下 **`LESS`**，这里按普通英文义读作“减去”。把三个未消费元素与 `XENA'S` 的元素拆分 `Xe / Na / S` 一一相减原子序数：

| 运算 | 原子序数 | 结果元素 |
| --- | ---: | --- |
| `Hf − Xe` | `72 − 54 = 18` | `Ar`（argon） |
| `Pu − Na` | `94 − 11 = 83` | `Bi`（bismuth） |
| `Ac − S` | `89 − 16 = 73` | `Ta`（tantalum） |

这组运算给出 `Ar / Bi / Ta`，但由 `ArBiTa` 谐音得到的 `ARBITER` 已被用户明确判错。因而它至多是一个算术巧合或尚未完成的中间层，不能再作为最终解释；官方提示中的“现实中混在一块”必须按真实成分关系重新落实。

已确认的底层机制仍成立。题目把三部“疯狂”电影所对应的三类专名混排在 28 图中：

- 《疯狂的外星人》方向：天体名；取两个英文名称的字母数。
- 《疯狂的赛车》方向：赛车场；取两个赛道的 FIA licence grade。
- 《疯狂的石头》方向：矿物名；取两个矿物的 Nickel–Strunz 大类首位数字。

每图按从左到右把两个数字直接拼接为十进制原子序数，再换成元素符号。图 10–20 的可读串是操作提示，不是答案；它最终同时提供 `LAWLESS − LAW = LESS` 的运算词和减数 `Xe / Na / S`。

## Observed facts

- 题名为“疯狂的猜图”，flavor 是“……怎么三部全都混在一块了？”，页面明确标注“本题有中间答案验证”。
- 页面正文按固定顺序给出 28 张 512×256 WEBP 复合图；稳定视觉编号 `image-002`–`image-029` 依次对应题图 1–28。
- 三类分组已经闭合：
  - 天体：1、5、6、7、9、10、13、14、27（9 图）；
  - 赛车场：2、3、4、8、11、12、15、16、28（9 图）；
  - 矿物：17–26（10 图）。
- 每幅图通常构造同一类别的两个英文专名。重复素材只是稳定的 rebus 词元，不构成多米诺链。
- 三种数字来源都能在多行互相验证，并且拼成的数均落在 1–99 的有效原子序数范围内。

## Mechanism and extraction table

### 天体：英文名长度

| 图 | 两个名称 | 数字 | 元素 |
| ---: | --- | ---: | --- |
| 1 | Loge (4)；Atlas (5) | 45 | Rh |
| 5 | Venus (5)；Hippocamp (9) | 59 | Pr |
| 6 | Pluto (5)；Hydra (5) | 55 | Cs |
| 7 | Earth (5)；Hyperion (8) | 58 | Ce |
| 9 | Mercury (7)；Io (2) | 72 | Hf |
| 10 | Venus (5)；Eros (4) | 54 | Xe |
| 13 | Achilles (8)；Alice (5) | 85 | At |
| 14 | Jason (5)；Phobos (6) | 56 | Ba |
| 27 | Atlas (5)；Ymir (4) | 54 | Xe |

图 10 的“维纳斯 + 红楼梦”不是泛泛的梦境联想：小行星 433 Eros 上确有以《红楼梦》人物命名的 Pao-yü、Tai-yü 环形山，因而第二项为 Eros。图 13 的心形可能是同一 Eros 主题的辅助提示，但计数用的是 Achilles 与 Alice。

### 赛车：FIA 赛道等级

| 图 | 两个赛道 | 等级 | 元素 | 置信度 |
| ---: | --- | ---: | --- | --- |
| 2 | Salzburgring；Circuit de Croix-en-Ternois | 33 | As | 中高；十字架项链同时供 `ring` 与 `croix` |
| 3 | Lime Rock Park；Road America | 22 | Ti | 高 |
| 4 | Manfeild；疑似 Shanghai Tianmashan Circuit | 34 | Se | 中；丹顶鹤也称 Manchurian crane，第二项素材为山 + Chinatsu−C，构词仍待完全解释 |
| 8 | Qinhuangdao；Monaco | 21 | Sc | 中高；Pac-Man 给 NAMCO 与圆形 O，可重排为 MONACO |
| 11 | Buddh International Circuit；Red Bull Ring | 11 | Na | 高 |
| 12 | Magny-Cours；疑似 Lousada | 16 | S | 中；Manny + corpse 为前者近音，animal aid + Lotus Bridge 为后者近音构词 |
| 15 | Mount Panorama Circuit；Knockhill | 34 | Se | 高 |
| 16 | Rockingham Motor Speedway；Mantorp Park | 23 | V | 高；石头/嘲笑构造 Rockingham，馒头构造 Mantorp |
| 28 | Silverstone Circuit；Estoril | 11 | Na | 高 |

图 4 的角色素材已由反向识图落实为 eXceed 的 Chinatsu Kagaya；第一赛道的丹顶鹤/田野组合强指 Manfeild (grade 3)，第二赛道最可能是 Shanghai Tianmashan (grade 4)，但具体删改尚未完全复原。图 8 的 NAMCO + O 可重排为 Monaco (grade 1)。图 12 左图的原始馆藏标题明确是冰期灭绝象股骨，支持 Manny + corpse → Magny-Cours (grade 1)；右侧五亭桥又名 Lotus Bridge，与宠物援助/捐款图共同支持 Lousada (grade 6)，但这一路仍带有近音自由度。

图 15 的山直接指 Mount Panorama（grade 3）；盾牌与苏格兰狮指向 Knockhill，FIA 官方表列为 grade 4，因此 `34 → Se` 已独立闭合。图 16 的 FIA 表列 Mantorp Park 为 grade 3；Rockingham 公路赛道为 grade 2，因此 `23 → V`，支持读成 `BASE V`，而不是 `ATBASH`。

### 矿物：Nickel–Strunz 大类

| 图 | 两个矿物 | 类别首位 | 元素 | 备注 |
| ---: | --- | ---: | --- | --- |
| 17 | Calcite；Cinnabar | 52 | Te | 凯尔希/墓中骷髅与禁龙/陀螺构词 |
| 18 | Topaz；Malachite | 95 | Am | 托帕；mother/lash/high school 音形构词 |
| 19 | Parkinsonite；Perrierite-(Ce) | 39 | Y | Yellowstone = park-in-stone；P/R 图元 |
| 20 | Jadeite；Forsterite | 99 | Es | 玉；foster 情境与《红楼梦》人物 |
| 21 | Westerveldite；Northstarite（或 Starkeyite） | 27 | Co | 左箭头与公鸡草地是一个重叠图组：WEST + (roost)ER + VELD；右侧星光的两个可行矿名都为 class 7，故 2、7 稳定 |
| 22 | Tsumoite；Arctite | 28 | Ni | sumo；arc + T |
| 23 | Baumstarkite；Colusite | 22 | Ti | 包拯星额；colossus (sing.) |
| 24 | Spangolite；Rutile | 74 | W | 烟花棒；TiO2 晶格 |
| 25 | Johnsenite-(Ce)；Loveringite | 94 | Pu | Johnson；love pea/heart |
| 26 | Englishite；Ureyite | 89 | Ac | English + stone；Kwon Yuri 音近 Ureyite |

矿物组元素符号串为：

`Te Am Y Es Co Ni Ti W Pu Ac` → `TEAMYESCONITIWPUAC`。

其中前四项精确拼出 `TEAMYES`，不是从含糊首字母猜出的词。图 21 的版面坐标与分组审计见 `work/visual/transcription.md`；Westerveldite 的 FeAs 分类落在 Strunz 2，Northstarite 为 `7.JA.20`。

## Rejected readable substring audit

第 13–20 图稳定产生连续符号 `At Ba Se V Te Am Y Es`。用户已依次判错两个分段和完整连续串：

**`ATBASEVTEAMYES`**

补齐图 10–12 后，提示段应为 `Xe Na S At Ba Se V Te Am Y Es` → `XENASATBASEVTEAMYES`，可读作 `XENA'S / AT BASE V / TEAM YES`。这解释了为什么用户所试字符串不完整，但更重要的是它的语法是操作指令；不应把加上 `XENAS` 的版本继续当最终答案碰运气。

## Second extraction

`AT BASE V` 解释为把每个原子序数写成三位五进制；`TEAM YES` 解释为按三类组队并按 `astronomY / racE / mineralS` 的 Y/E/S 顺序排列。移出图 10–20 的提示段，并把图 27–28 重复出现的 `Xe Na` 作为末端 XENA 边界移出后，对每个完整三队列从第一、第二、第三队分别取五进制的第 1、2、3 位，再把取出的三位重新作为五进制原子序数：

| 列 | 天体 | 赛车 | 矿物 | 重组三位 | 新元素 |
| ---: | --- | --- | --- | --- | --- |
| 1 | 45=`140` → 1 | 33=`113` → 1 | 27=`102` → 2 | `112`=32 | Ge |
| 2 | 59=`214` → 2 | 22=`042` → 4 | 28=`103` → 3 | `243`=73 | Ta |
| 3 | 55=`210` → 2 | 34=`114` → 1 | 22=`042` → 2 | `212`=57 | La |
| 4 | 58=`213` → 2 | 21=`041` → 4 | 74=`244` → 4 | `244`=74 | W |

新元素符号连读为 **`Ge Ta La W` → `GETALAW`**。首列不是为了凑字反推：图 21 的两组空间边界独立支持 Westerveldite + Northstarite，Mindat/Webmineral 的分类又独立给出 2、7。若保留末端 `Xe Na`，脚本会如实显示第五列 `Gd`；因此结果表同时保留这个边界反例，不再主观截断后称作 `SET A LAW`。

## Final extraction

`XENA'S` 的直接人物双关是 Xena 的扮演者 Lucy **Lawless**。`GET A LAW` 从 `LAWLESS` 中取出 `LAW`，余下 `LESS`。先前把 `LESS` 当作答案已经被判错；官方提示 7 说明还应得到三个中间答案，因此这里必须采用 `less = 减去` 的运算义。

对角提取完成后未消费的三个元素按出现次序是 `Hf / Pu / Ac`，而 `XENA'S` 本身可由元素拆成 `Xe / Na / S`。原子序数逐项相减得到：

`72−54=18 (Ar)`，`94−11=83 (Bi)`，`89−16=73 (Ta)`。

三项中间答案因此是 **ARGON / BISMUTH / TANTALUM**，其元素符号合为 `ArBiTa`。官方提示给出长度 7，而整个末段反复强调 `LAW`；`ArBiTa` 按读音还原为法律语义中的 **`ARBITER`**。这一步同时消费了三个残项、`XENA'S`、`GET A LAW`、`LESS` 和官方枚举，没有遗留主机制信息。

此前对连续五进制位进行朴素配对、按队伍删位/取位、以 `STONE/RACER/ALIEN` 作五字母表、以 YES/XENA/LUCY/LAWLESS 作普通平移或带钥方阵，以及把所有数字转置后重新组成元素，均未成文。把三位五进制当三维坐标的六种自然投影也没有稳定字形，故停止视觉路径族。完整边界与结果见 `work/extraction-results.md`；参数化脚本与投影审计见 `work/extraction_test.py`、`work/team-paths.svg`。

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
| 2026-08-21 | LESSNESS | 错误答案 | 用户明确报告不正确；随后授权解锁一条官方提示。 |
| 2026-08-21 | ARBITER | 错误答案 | 用户明确报告不是答案；未提供其他判题文字。 |

## Evidence and artifacts

- 持久逐图转录：`work/visual/transcription.md`。
- 视觉清单：`work/visual/inventory/index.tsv`、`manifest.json`、`contact-01.png` 至 `contact-03.png`。
- SingleFileZ 的只读派生展开：`work/visual/page/`；`index.html` 保留题图顺序与原始图片 URL。
- 局部核对图：`work/visual/crops/`；工具生成的裁图有同名 JSON 坐标边车。
- IMA 矿物名录：`work/visual/mineral-list.pdf`、`work/visual/mineral-list.txt`。
- 五进制有界测试：`work/extraction_test.py`、`work/extraction-results.md`。
- FIA licensed circuits 官方列表：https://www.fia.com/circuit-safety
- 2026-03-31 FIA 赛道表：https://api.fia.com/sites/default/files/circuits_fia20260331_0.pdf
- IMA Master List：https://athena.unige.ch/athena/mineral/IMA-Master-List-2026-03.pdf
- Westerveldite 资料（FeAs，Strunz 2）：https://www.mindat.org/min-4273.html 、https://webmineral.com/data/Westerveldite.shtml
- Northstarite 资料与 `7.JA.20` 分类：https://www.mindat.org/min-53865.html
- Caltech 关于 Xena/Eris、Dysnomia 与 Lucy Lawless 的命名说明：https://www.caltech.edu/about/news/dwarf-planet-formerly-known-xena-has-officially-been-named-eris-iau-announces-1187
- Merriam-Webster 对 `arbiter` 的法律义释义（judge / arbitrator）：https://www.merriam-webster.com/dictionary/arbiter
- eXceed 官方角色页（Tinatu/Chinatsu Kagaya）：https://exceedseries.com/exceed-gbc_main/chrs_gb
- 灭绝象左股骨馆藏页：https://museu.ms/collection/object/222068/left-femur-of-extinct-elephant-alaska-ice-age
- 五亭桥/莲花桥异名：https://en.wikipedia.org/wiki/Five-Pavilion_Bridge
- USGS Eros 地名检索：https://planetarynames.wr.usgs.gov/SearchResults?Feature+Type=9_Crater%2C+craters&Target=137_Eros

## Important failed routes

- `疯狂的石头`、`疯狂的赛车`、`疯狂的外星人` 已被用户明确判错；没有新判题证据时不得恢复。
- `TEAMYES`、`AT BASE V`、`ATBASEVTEAMYES` 均已被用户明确判错；三者只可作为内部提示或校验片段参与完整提取，不得再次提交。
- `SET A LAW` 已被用户明确判错且无反馈。它来自错误地把图 21 拆为 Backite + Morningstarite；视觉图组和 Westerveldite + Northstarite 的 2、7 分类现已给出新证据，故不得恢复旧首字 `Se`。
- `LESS` 已被用户明确判错，不能再作为答案；新链只保留它的运算义“减去”，用来执行 `Hf/Pu/Ac LESS Xe/Na/S`。
- `LESSNESS` 已被用户明确判错。尽管 Xena/Eris–Dysnomia–Lucy Lawless 的命名链为真，官方提示 7 已明确最终提取是“三个中间答案”的现实混合物，因而不得再恢复这条串行删字路线。
- `ARBITER` 已被用户明确判错。`Hf/Pu/Ac − Xe/Na/S = Ar/Bi/Ta` 的数字等式虽精确，但把 `ArBiTa` 直接谐读为 7 字母法律角色没有得到判题支持；没有新的结构证据时不得恢复。
- “三部电影的演员、角色或主创混排”不能解释三套数值属性；人物图只是构造专名的词元。
- “重复专名组成三条多米诺链”已被完整矿物组反证：多数矿物只出现一次，重复素材只是 rebus 部件。
- 28 等于 `C(8,2)` 或三角数只是数值巧合，不能代替提取证据。
- Yellowcatite/Macfallite、Stellerite 等早期矿物套词不再使用；它们不能生成连续的 `TEAMYES`。
- 图 21 的 `Backite + Morningstarite → 74 W` 已被版面反证：箭头与公鸡照片重叠为左组，星光独立为右组。`Haycockite + Starkeyite` 虽也能凑出 2、7，但不能解释箭头；当前采用能消费全部左组词元的 Westerveldite + Northstarite。
- 把 `AT BASE V` 强读成 `ATBASH` 会与图 16 的 Rockingham (2) + Mantorp (3) = 23 → V 冲突。
- 五进制数字的朴素连续配对与以 `TEAMYES` 作普通 Vigenère 密钥均为负结果；除非有新排列证据，不重复参数微调。
- “队伍直接决定删/取五进制位”已完成三次有界测试仍无明文，停止该族；`STONE/RACER/ALIEN` 作为五字母表的直接替换也为负结果。
- 把三位五进制当三维坐标并按三队作 5×5 投影的六种自然轴分配均无稳定字形；该空间路线已停止。

## Next action

重新按三队独立提取真实成分。优先审计移出图 10–20 提示段和图 27–28 末端 `Xe Na` 后的三组长度 `5 / 4 / 6`，检验它们能否分别稳定给出三个可在现实中混合成 7 字母事物的词；若不能，再回查 `GET A LAW` 是否只是偶然或应作别的运算指令。
