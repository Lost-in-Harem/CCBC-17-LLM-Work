---
node_id: e07-contingency-contract-battleplan-cryptographia
title: 危机合约「破玄作战」
kind: puzzle
round: irrational-manager-hypothesis
parent: 
source: 
round_feeder: yes
feeders: 
status: accepted
answer: CLIMATIC
confidence: high
summary: "用户已确认 CLIMATIC 为正确最终答案。四个轮换地的完整行串使 288 个主图全部成为英语答案；唯一满分状态 23213 原位读出并由题内框确认 MAIN STORY。全部主答案中恰有主线第 1–8 章的八个标题词，按章节顺序将各配置危机等级作 A1Z26，得到 CLIMATIC。"
updated: 2026-08-22
---

# 危机合约「破玄作战」

## Current conclusion

最终答案为：

```text
CLIMATIC
```

提示 7 的完整规定链已经闭合：

1. 唯一满分状态 `23213` 的危机等级是 `25`。
2. 用正确的四行轮换答案直接读取九格，得到 `MAIN STORY`；题内冷却框明确回复“这是主测试地的答案！”。
3. 枚举全部 288 个主图后，286 个输出是单个常见英语词，另两个是刻意分词的 `EVIL TIME` 与 `MAIN STORY`。
4. 在这 288 个答案中寻找《明日方舟》Main Story 第 1–8 章标题，可各取到一个长词。
5. 按章节 1–8 排序，将这些答案所属配置的危机等级作 A1Z26，得到 `3,12,9,13,1,20,9,3 → CLIMATIC`。

Agent 只在用户授权的指标 `03` 冷却框验证了中间答案，没有操作会消耗次数的 Hunt 最终提交框；用户现已明确确认 Hunt 最终答案 `CLIMATIC` 正确。

## Observations

### 动态页面

- 题页为动态 Vue 组件，共有主测试地和四个轮换测试地。
- 锁定指标说明最终答案长度固定为 8，附加条件的改变可能改变主测试地图。
- 零分 `+1` 指标的主图为 `main-score0-plus1.webp`，恰有编号 1–8；一分 `+2` 指标会出现编号 1–9，因此多出一格噪声。
- 当前零分 `+1` 主图的编号只落在轮换地 1、2 两行；轮换地 3、4 在这个配置中不参与提取。
- 题内提交框初始显示剩余 10 次；指标 `03` 下错误不扣次数，但会进入冷却。Hunt 通用提交框另显示 20 次。`LMUITIAN` 错误后题内次数仍为 10，并触发 10 分钟冷却。
- 页面公开加载的组件 `13a10614326f432ead92e72193a19ed3.vue` 确认主图由五位状态码选择；该状态码只取决于指标 `04`–`13`，不含提交模式 `02/03`。实测从 `02` 切到 `03` 后，主图和四张轮换图地址均不变。
- 提交时组件仍会把完整的 `activeContracts`（包括 `03`）发送给内部判题，用于执行冷却等规则。
- 原作经典危机合约曾以危机等级 **18** 作为常驻挑战阈值，但本题不能据此只选恰好 18 分的状态；`STRENGTH` 的最终拒绝已经证明这只是主题诱饵。提示 7 规定的选态是唯一最高分 `25`，随后要检查全部 288 个主图输出。背景核对来源：<https://arknights.wiki.gg/wiki/Contingency_Contract>。

### 轮换地 1

每句填空都允许多个意思相近的英文表述；整组首字母要形成英语词。两个指标分别把第 4 个字母 `B` 改成 `V`，以及在开头增加 `IM`，所以四种状态组成整齐的词族：

| 变体 | 指标 | 行串 |
| --- | --- | --- |
| 基础 | — | `PROBABLE` |
| 改变 1 个线索 | `06` | `PROVABLE` |
| 线索数 +25% | `07` | `IMPROBABLE` |
| 两项同时开启 | `06+07` | `IMPROVABLE` |

早期把这些宽泛近义词强行消歧成 `PLATINUM / PROVENCE / CLIFFHEART / MATTERHORN / AYERSCARPE`，正是满分中间答案长期读错的根因。最终闭环不是词形猜测：对尚未解出的 8 字母与 10 字母行分别扫描固定的前 300,000 英语词，`PROBABLE` 与 `IMPROBABLE` 都是唯一能让对应 72 张主图全部变成英语答案的行；`PROVABLE / IMPROVABLE` 也各使 71 张成为单词，剩余一张分别是刻意分词的 `EVIL TIME / MAIN STORY`。结果见 `work/stage1-variant0-ranking.tsv`、`work/stage1-variant2-ranking.tsv` 与 `work/meta-answers.tsv`。

### 轮换地 2

八张图都是活动标题的局部。补全标题后，根据画面展示的是标题前部还是后部，取对应关卡代码的第一或第二个字母：

| 图 | 可见部分 | 完整活动 | 关卡代码 | 取字 |
| --- | --- | --- | --- | --- |
| 1 | 黑夜 | 生于黑夜 | DM | M |
| 2 | 一颗酸橙 | 直到大地变成一颗酸橙 | TO | O |
| 3 | 未许 | 未许之地 | UR | U |
| 4 | 长夜 | 长夜临光 | NL | N |
| 5 | 泡影 | 泡影苍霆 | TD | T |
| 6 | 先路 | 吾导先路 | GA | A |
| 7 | 过境 | 风雪过境 | BI | I |
| 8 | 号 | 愚人号 | SN | N |

因此第 2 行为：

```text
MOUNTAIN
```

相邻变体也形成完整英文词：改变 1 张图片时首图由“黑夜”换成“逐火”，得到 **FOUNTAIN**；改变 2 张图片时得到 **MAINTAIN**。

活动代码核对来源：

- https://prts.wiki/w/关卡一览/活动关卡
- https://prts.wiki/w/泰拉年表
- https://prts.wiki/w/RA1-END-1/NBT

### 轮换地 3

基础图的九个技能图标与括号索引可逐项匹配：

| 位 | 干员（技能） | 括号索引 | 取字 |
| --- | --- | --- | --- |
| 1 | Surtr（3） | 1/5 | S |
| 2 | Qiubai（2） | 2/6 | I |
| 3 | Blaze the Igniting Spark（3） | 10/5 3 8 5 | G |
| 4 | Angelina the Mellow Wish（2） | 7/8 3 6 4 | N |
| 5 | Vulpisfoglia（3） | 12/12 | A |
| 6 | Mantra（3） | 4/6 | T |
| 7 | Mountain（2） | 3/8 | U |
| 8 | Nearl the Radiant Knight（1） | 9/5 3 7 6 | R |
| 9 | Eyjafjalla（3） | 1/10 | E |

因此基础第 3 行为 **SIGNATURE**。图标通过公开技能图资源像素匹配，首名均与次名有明显距离；详细表见 `artifacts/stage3-identifications.tsv`。

指标 `10` 不更换图标，只删去括号中的显式索引，其合约图标为 shuffle。早期曾把它错解为技能名末字母、`DESIGN…` 猜测行或自由重排 `SIGNATURE` 字母袋，由此得到的 `PRINTED / GREETED / GREETER` 均被网站精确拒绝；这些反例否定的是具体取字规则，不是否定固定改变行本身。

随后对 144 个启用指标 `10` 的主图做了有界词形反推：词库只取 `wordfreq` 前 300,000 个英文词，同时另测 `SIGNATURE` 的全部排列。精确 18 分状态 `01013` 的逐格模板为

```text
X5 R E E T X2 X1
```

把改变后的第三行强行补成 `DESIGN…` 前缀时会得到 `GREETED`；网站在精确配置下明确拒绝，证明这个具体行只是词形过拟合。后续正例先锁定改变行的模式 `DE??CR??Y`。在其 456,976 种补全中，`DEMOCRACY` 是唯一能令 143 张相关主图成为常见英语词、并令最后一张满分图成为短语 `MAIN STORY` 的补全；第二名只能命中 142 张。因此改变行完整为：

```text
DEMOCRACY
```

曾据网站反例提出：第三行仍按基础解保留为 **`SIGNATURE`**，先照常由主图编号读出完整原串，然后对**整条主测试地答案**做变位。对 144 个指标 `10` 状态用同一规则，在前 300,000 个英文词的固定上限内确实会产生下列词形聚类：

| 状态码 | 分数 | 原串 | 变位词 |
| --- | ---: | --- | --- |
| `00010` | 6 | `PLASUAT` | `SPATULA` |
| `00112` | 12 | `LMISING` | `SMILING` |
| `01010` | 9 | `REAOTSR` | `ROASTER` |
| `01110` | 11 | `AERTEIN` | `TRAINEE` |
| `11012` | 13 | `SIRTENAE` | `TRAINEES` |
| `13110` | 14 | `TNAINTRE` | `INTRANET` |
| `13112` | **18** | **`RTTHSNGE`** | **`STRENGTH`** |
| `21213` | 22 | `EMIRGENAE` | `MENAGERIE` |
| `22213` | 22 | `AFLIRTTIS` | `STAIRLIFT` |

完整有界结果还包括 `STIFFER / FERRITE / RIVETERS / MINARETS` 等；专名或极低频异形保留在 `work/stage3-anagram-completions.tsv`。但用户对 `STRENGTH` 的明确最终否定，加上提示 5 的标题“改变提取方式的轮换测试地 3 怎么做？”，说明这些变位词只是词库筛选造成的偶然聚类，不能证明指标 `10` 作用于完整主串。

旧路线曾把配置 `13112` 错填为：

```text
MATTERHORN
FOUNTAIN
SIGNATURE
CARSMING
```

主图编号 1–8 依次取 `R T T H S N G E`，指标 `10` 的 shuffle 再把完整原串 `RTTHSNGE` 变位为：

```text
STRENGTH
```

这个结果虽同时满足危机等级 18 与锁定长度 8，却已被用户明确否定。用正确四行 `IMPROVABLE / FOUNTAIN / DEMOCRACY / CASTLING` 直接读取，同一状态实际主答案是 `STRATEGY`；无需重排。

#### 指标 10 的有效结果

转而把指标 `10` 严格作用在轮换地 3 后，网站先确认了五个位置：第 1、2、5、6、9 格依次为 `D,E,C,R,Y`，给出：

```text
DE??CR??Y
```

其中第 1 格由 `EDITION / EVIDENCE` 锁定，第 2 格由 `EVERYONE` 锁定，第 5 格由 `EVIDENCE / CONTINUED / PROCEDURE` 锁定，第 6 格由 `PRINTER` 锁定，第 9 格由 `EVERYONE / EMERGENCY` 锁定。其余四格由上述全状态唯一性审计补为 `M,O,A,C`，即 `DEMOCRACY`。逐格证据见 `artifacts/stage3-changed-row.tsv`。

只使用已经由网站锁定的五个位置，离线枚举突出八个常见英语词；随后全部在精确指标状态下由题内框确认：

| 状态码 | 分数 | 主答案 |
| --- | ---: | --- |
| `01011` | 11 | `PRINTER` |
| `01213` | 21 | `EDITION` |
| `11011` | 11 | `EVERYONE` |
| `11111` | 13 | `EVIDENCE` |
| `21010` | 10 | `CONTINUED` |
| `21011` | 12 | `DETERMINE` |
| `21110` | 12 | `PROCEDURE` |
| `21213` | 22 | `EMERGENCY` |

这组验证也否定了 `TEMPORARY` 等只共享已知局部字母的替代行：例如它在状态 `01213` 会给 `ETITION`，而网站接受的是 `EDITION`。

尚未从无括号技能图本身复原提示 5 的直接取字细节，但完整行已由五个题内正例字母、全状态唯一性以及满分 `MAIN STORY` 正例三重锁定；这不再影响答案链。

### 轮换地 4

每个小块由上下两张《岁的界园志异》关卡图组成。用公开关卡缩略图匹配地图后，分别取两张图出现的层数；层号对作为标准 5×5 Polybius 方阵（合并 I/J）的行列坐标。例如基础首块是 1 层 `Pest Control` 与 3 层 `Return to Your Roots`，坐标 `13` 取 `C`。

四种状态依次得到：

| 变体 | 层号对 | 原始串 |
| --- | --- | --- |
| 基础 | `13 11 43 24 33 22` | `CASING` |
| 指标 `11` | `13 15 11 43 24 33 22` | `CEASING` |
| 指标 `12` | `13 11 43 44 31 24 33 22` | `CASTLING` |
| 指标 `13` | `13 11 42 15 43 43 24 33 22` | `CARESSING` |

四串都是正常英语词。早期误把 Polybius 方阵按不一致的字母表换算，才得到 `CARING / CEARING / CARSMING / CAQERRING`；尤其把 `43` 错读成 `R`，导致满分答案第 5 字母读错。逐图关卡名、楼层与坐标见 `artifacts/stage4-identifications.tsv`；匹配脚本为 `work/match_stage4_maps.py`。楼层表核对来源：<https://tomimi.dev/zh/sui>。

## Main-test enumeration

公开组件给出 288 张主图（3 种提取格数 × 4 种轮换地 1 × 3 种轮换地 2 × 2 种轮换地 3 × 4 种轮换地 4）。对每张图识别编号格，再从相应四行按编号顺序取字。十八个结果已在指标 `03` 下由网站直接确认；其中关键正例如下：

| 状态码 | 附加指标 | 分数 | 主测试地答案 | 网站判定 |
| --- | --- | ---: | --- | --- |
| `01000` | `06` | 3 | `OPTIONS` | 正确 |
| `01003` | `06+13` | 12 | `REPORTS` | 正确 |
| `01100` | `06+08` | 5 | `SERVICE` | 正确 |
| `01101` | `06+08+11` | 7 | `VERSION` | 正确 |
| `11101` | `04+06+08+11` | 7 | `PREVIOUS` | 正确 |
| `21001` | `05+06+11` | 6 | `RINGTONES` | 正确 |
| `21103` | `05+06+08+13` | 15 | `FURNITURE` | 正确 |
| `21201` | `05+06+09+11` | 9 | `COUNTRIES` | 正确 |
| `01011` | `06+10+11` | 11 | `PRINTER` | 正确 |
| `01213` | `06+09+10+13` | 21 | `EDITION` | 正确 |
| `11011` | `04+06+10+11` | 11 | `EVERYONE` | 正确 |
| `11111` | `04+06+08+10+11` | 13 | `EVIDENCE` | 正确 |
| `21010` | `05+06+10` | 10 | `CONTINUED` | 正确 |
| `21011` | `05+06+10+11` | 12 | `DETERMINE` | 正确 |
| `21110` | `05+06+08+10` | 12 | `PROCEDURE` | 正确 |
| `21213` | `05+06+09+10+13` | 22 | `EMERGENCY` | 正确 |
| `23001` | `05+06+07+11` | 9 | `GUARANTEE` | 正确 |
| `23213` | `05+06+07+09+10+13` | 25 | `MAIN STORY` | 正确 |
| `11100` | `04+06+08` | 5 | `SERVICER` | 错误（对照） |
| `01011` | `06+10+11` | 11 | `PRINTED` | 错误 |
| `01013` | `06+10+13` | 18 | `GREETED` | 错误 |
| `01013` | `06+10+13` | 18 | `GREETER` | 错误 |
| `13112` | `04+06+07+08+10+12` | 18 | `STRENGTH` | 题内框拒绝，用户又明确否定为 Hunt 最终答案 |

状态码五位依次表示提取格变体、轮换地 1、轮换地 2、轮换地 3、轮换地 4。完整提交表见 `artifacts/main-valid-states.tsv`。用最终八条轮换行重新生成 `work/meta-answers.tsv` 后，288 个状态中 286 个是 `wordfreq` 词库内的普通英语词，另两个正好是 `EVIL TIME` 与 `MAIN STORY`；不存在随机补词或变位步骤。这一全覆盖也是各轮换行最强的交叉验证。

## Summit extraction and final extraction

提示 7 指定唯一满分状态 `23213`。该状态四行是：

```text
IMPROVABLE
MAINTAIN
DEMOCRACY
CARESSING
```

九个编号格按原位、原编号读取：

| 编号 | 来源 | 字母 |
| ---: | --- | --- |
| 1 | 轮换地 1，第 2 格 | M |
| 2 | 轮换地 1，第 7 格 | A |
| 3 | 轮换地 1，第 1 格 | I |
| 4 | 轮换地 2，第 4 格 | N |
| 5 | 轮换地 4，第 5 格 | S |
| 6 | 轮换地 2，第 5 格 | T |
| 7 | 轮换地 1，第 5 格 | O |
| 8 | 轮换地 1，第 4 格 | R |
| 9 | 轮换地 3，第 9 格 | Y |

因此中间答案是 `MAIN STORY`，已由题内框确认。它指示在全部 288 个主答案中寻找《明日方舟》主线章节标题。长度 7–9 的标题词恰好覆盖第 1–8 章各一个：

| 章 | 英文标题 | 主答案 | 状态 | 危机等级 | A1Z26 |
| ---: | --- | --- | --- | ---: | --- |
| 1 | Evil Time Part 2 | `EVIL TIME` | `11000` | 3 | C |
| 2 | Separated Hearts | `SEPARATED` | `22011` | 12 | L |
| 3 | Stinging Shock | `STINGING` | `13200` | 9 | I |
| 4 | Burning Run | `BURNING` | `03202` | 13 | M |
| 5 | Necessary Solutions | `SOLUTIONS` | `20000` | 1 | A |
| 6 | Partial Necrosis | `NECROSIS` | `11113` | 20 | T |
| 7 | The Birth of Tragedy | `TRAGEDY` | `00210` | 9 | I |
| 8 | Roaring Flare | `ROARING` | `00200` | 3 | C |

主线标题核对来源：<https://arknights.wiki.gg/wiki/Main_Theme>。

按章节顺序读取危机等级并作 A1Z26：

```text
3 12 9 13 1 20 9 3
C  L I M  A T  I C
```

得到最终答案 **CLIMATIC**。这正好满足锁定指标给出的八字母长度，并已由用户确认正确。

## Rejected candidate audit

- `LMUITIAN` 的格式、配置与逐格复算均一致，但网站的明确判题优先级更高，故候选已作废。
- `PLATINUM / PROVENCE / CLIFFHEART / MATTERHORN / AYERSCARPE` 是由宽泛近义词事后贴合干员名的错路；正确词族是 `PROBABLE / PROVABLE / IMPROBABLE / IMPROVABLE`，并由 288 个主答案全覆盖锁定。
- `SERVICER` 是规范英语名词且离线词频不低，但网站在精确配置 `11100` 下明确拒绝它。这一对照说明有效集合由题目白名单决定，不能只凭“看起来像英语词”收录。
- `LAVENDER` 由错误行 `PROVENCE`、`SIGNATURE` 的语义联想得到，但用户明确否定；正确的对应行是 `PROVABLE`。
- `STRENGTH` 由把指标 `10` 解释为“完整主串 shuffle”，再叠加危机等级 18 与长度 8 得到；用户明确否定它是最终答案。提示 5 还直接把变化归到轮换测试地 3 的提取方式，因此该作用对象判断错误。
- `DIABOLUS` 由把 `TRITONUS` 当作“三全音”语义线索，再取传统拉丁别称 *diabolus in musica* 的核心词得到；用户明确否定。它没有执行 `CENTER ON` 的可复现机制，也依赖外部同义替换，因此整条三全音别称路线作废。
- `JOHANNES` 由把 `TRITONUS` 字形改造成 `TRITHEMIUS` 后，按八字母锁直接取密码学家的名得到；用户明确否定。该路线离开了提示 1 的《明日方舟》主题，且后续规范 Trithemius cipher 测试没有信号。

## Submission history

只记录用户或比赛网站明确反馈过的提交；不要把尚未提交的候选写进来。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-21 | FTRETIFN | Rejected | 用户明确指出它既不是题内提交框答案，也不是最终答案；用户的实际提交模式为指标 `03`。未提供网站判题原文。 |
| 2026-08-21 | LMUITIAN | Rejected | 题内提交框原文：`答案不正确。已进入 10 分钟冷却。` 指标为 `01+03+04`；错误不扣次数，剩余次数仍为 10。 |
| 2026-08-21 | UPLTTINN | Rejected | 题内提交框原文：`答案不正确。已进入 10 分钟冷却。` 指标为 `01+03+04`；按主图第 1 行左向、第 2 行右向填词后提取。剩余次数仍为 10。 |
| 2026-08-21 | PREVIOUS | Accepted (main test site) | 指标为 `01+03+04+06+08+11`，分数 7。题内提交框原文：`这是主测试地的答案！` 剩余次数仍为 10；这不是 Hunt 外层最终答案。 |
| 2026-08-21 | SERVICE | Accepted (main test site) | 指标为 `01+03+06+08`，分数 5。题内提交框原文：`这是主测试地的答案！` 剩余次数仍为 10。 |
| 2026-08-21 | OPTIONS | Accepted (main test site) | 指标为 `01+03+06`，分数 3。题内提交框原文：`这是主测试地的答案！` 剩余次数仍为 10。 |
| 2026-08-21 | VERSION | Accepted (main test site) | 指标为 `01+03+06+08+11`，分数 7。题内提交框原文：`这是主测试地的答案！` 剩余次数仍为 10。 |
| 2026-08-21 | REPORTS | Accepted (main test site) | 指标为 `01+03+06+13`，分数 12。题内提交框原文：`这是主测试地的答案！` 剩余次数仍为 10。 |
| 2026-08-21 | COUNTRIES | Accepted (main test site) | 指标为 `01+03+05+06+09+11`，分数 9。题内提交框原文：`这是主测试地的答案！` 剩余次数仍为 10。 |
| 2026-08-21 | FURNITURE | Accepted (main test site) | 指标为 `01+03+05+06+08+13`，分数 15。题内提交框原文：`这是主测试地的答案！` 剩余次数仍为 10。 |
| 2026-08-21 | RINGTONES | Accepted (main test site) | 指标为 `01+03+05+06+11`，分数 6。题内提交框原文：`这是主测试地的答案！` 剩余次数仍为 10。 |
| 2026-08-21 | SERVICER | Rejected | 指标为 `01+03+04+06+08`，分数 5。题内提交框原文：`答案不正确。已进入 10 分钟冷却。` 错误不扣次数，剩余次数仍为 10；此后停止自主提交。 |
| 2026-08-21 | LAVENDER | Rejected | 用户明确指出它不是答案；未提供网站判题原文。该候选来自把有效状态交集解释为 `PROVENCE'S SIGNATURE`，此语义路线作废。 |
| 2026-08-21 | TRITONUS | Rejected (main test site, state `00000`) | 指标为 `01+03`，分数 0。题内提交框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10。此结果只否定它是该配置的主测试地答案，不构成 Hunt 最终答案判定。 |
| 2026-08-21 | VENATION | Rejected (main test site, state `11013`) | 指标为 `01+03+04+06+10+13`，分数 18。题内提交框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10。否定了“轮换地 3 无索引时可任选干员名字母补词”的解释。 |
| 2026-08-21 | PRINTED | Rejected (main test site, state `01011`) | 指标为 `01+03+06+10+11`，分数 11。题内提交框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10。它由九个技能英文名末字母规则产生；此规则因此作废。 |
| 2026-08-21 | GREETED | Rejected (main test site, state `01013`) | 指标为 `01+03+06+10+13`，分数 18。题内提交框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10。它来自把改变后的第三行强行补成固定 `DESIGN…` 前缀；该固定行模型因此作废。 |
| 2026-08-21 | GREETER | Rejected (main test site, state `01013`) | 指标为 `01+03+06+10+13`，分数 18。题内提交框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10。它是 `SIGNATURE` 无放回字母袋模型下唯一的精确 18 分补全；该自由重排模型因此作废。 |
| 2026-08-21 | STRENGTH | Rejected (main test site only, state `13112`) | 指标为 `01+03+04+06+07+08+10+12`，分数 18。题内框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10。该框只判定主测试地子答案；随后用户另行明确否定其 Hunt 最终候选身份。 |
| 2026-08-21 | STRENGTH | Rejected (Hunt final) | 用户明确反馈“不是正确答案”。这独立否定了此前保留的 Hunt 最终候选；完整主串 shuffle 与危机等级 18 的外层路线作废。 |
| 2026-08-21 | TRITONUS | Rejected (Hunt final) | 用户明确反馈“TRITONUS 不是答案”。这独立否定最终候选；不能再把 `CENTER ON` 直接理解为“答案就是 TRITONUS”。 |
| 2026-08-21 | PRINTER | Accepted (main test site) | 指标为 `01+03+06+10+11`，分数 11。题内提交框原文：`这是主测试地的答案！` 剩余次数仍为 10；它把改变后轮换地 3 的第 6 格锁定为 `R`。 |
| 2026-08-21 | EVERYONE | Accepted (main test site) | 指标为 `01+03+04+06+10+11`，分数 11。题内提交框原文：`这是主测试地的答案！` 剩余次数仍为 10；它独立锁定改变行第 2、9 格为 `E,Y`，但不触及四个未知格。 |
| 2026-08-21 | EDITION | Rejected (main test site, wrong state `01013`) | 原计划验证状态 `01213`，但指标切换动画未点亮 `09`，实际指标为 `01+03+06+10+13`、分数 18。题内框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10。此反馈只否定 `01013 → EDITION`，不能否定预期的 `01213 → EDITION`。 |
| 2026-08-21 | EDITION | Accepted (main test site) | 精确指标为 `01+03+06+09+10+13`（状态 `01213`），分数 21。题内框原文：`这是主测试地的答案！` 剩余次数仍为 10；锁定改变后轮换地 3 第 1 格为 `D`。 |
| 2026-08-21 | EVIDENCE | Accepted (main test site) | 精确指标为 `01+03+04+06+08+10+11`（状态 `11111`），分数 13。题内框原文：`这是主测试地的答案！` 剩余次数仍为 10；同时确认改变行第 1、5 格为 `D,C`。 |
| 2026-08-21 | CONTINUED | Accepted (main test site) | 精确指标为 `01+03+05+06+10`（状态 `21010`），分数 10。题内框原文：`这是主测试地的答案！` 剩余次数仍为 10。 |
| 2026-08-21 | DETERMINE | Accepted (main test site) | 精确指标为 `01+03+05+06+10+11`（状态 `21011`），分数 12。题内框原文：`这是主测试地的答案！` 剩余次数仍为 10。 |
| 2026-08-21 | PROCEDURE | Accepted (main test site) | 精确指标为 `01+03+05+06+08+10`（状态 `21110`），分数 12。题内框原文：`这是主测试地的答案！` 剩余次数仍为 10。 |
| 2026-08-21 | EMERGENCY | Accepted (main test site) | 精确指标为 `01+03+05+06+09+10+13`（状态 `21213`），分数 22。题内框原文：`这是主测试地的答案！` 剩余次数仍为 10。 |
| 2026-08-21 | DIABOLUS | Rejected (Hunt final) | 用户明确反馈“DIABOLUS 不是答案”。这否定了把 `TRITONUS` 当作三全音线索并转为 *diabolus in musica* 的语义路线；不再猜其他三全音别称。 |
| 2026-08-21 | JOHANNES | Rejected (Hunt final) | 用户明确反馈“JOHANNES 不是答案”。按八字母锁直接取 Trithemius 名字的路线作废；随后 416 个规范密码变体也无信号，整条密码学家路线停止。 |
| 2026-08-21 | EBENHOLZ | Rejected (Hunt final) | 用户明确反馈“EBENHOLZ 不是答案”。英文台词中 `tritone` 唯一命中 Ebenholz 仍可作为定位证据，但不能直接提交其英文代号。 |
| 2026-08-21 | BLACKKEY | Rejected (Hunt final) | 用户明确反馈“别乱搞了，不对”。把正式中文代号“黑键”直译为八字母答案的延伸没有题面操作支持，整条角色名/翻译路线停止。 |
| 2026-08-21 | PREVIOUS | Rejected (Hunt final) | 浏览器答案记录显示 16:46:29 在 Hunt 标准框提交并判错；这不影响它在精确配置下作为题内主测试地答案被接受。 |
| 2026-08-21 | PROVENCE SIGNATURE | Rejected (Hunt final) | 浏览器答案记录显示 17:38:29 在 Hunt 标准框提交并判错；固定状态交集不能直接作为答案。 |
| 2026-08-21 | CENTER ON TRITONUS | Rejected (Hunt final) | 浏览器答案记录显示 20:21:07 在 Hunt 标准框提交并判错。新机制把它作为需执行的中间指令：取 `TRITONUS` 中央两字母 `TO`，而非再次提交整句。 |
| 2026-08-21 | ANGELINA | Rejected (Hunt final) | 用户明确反馈“不正确”，并解锁提示 7：应检查最高分状态的主测试地答案，再在所有可能的主测试地答案中寻找该中间答案所提示的内容。`CENTER ON TRITONUS → TO → 活动 → Angelina` 路线因此作废。 |
| 2026-08-21 | TRY ANTHEM | Rejected (main test site, state `23213`) | 精确指标为 `01+03+05+06+07+09+10+13`、危机等级 25。题内框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10；这排除满分字母袋 `AHMNRTETY` 的两词解析。 |
| 2026-08-22 | TRY THE MAN | Rejected (main test site, state `23213`) | 精确指标为 `01+03+05+06+07+09+10+13`、危机等级 25。题内框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10；这排除三词解析，也撤销由它推到 `MERCHANT` 的路线。 |
| 2026-08-22 | MATH ENTRY | Rejected (main test site, state `23213`) | 精确指标为 `01+03+05+06+07+09+10+13`、危机等级 25。题内框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10。它不是满分主测试地答案，也不能在没有确认中间答案的前提下继续解释成 `ELEMENT`。 |
| 2026-08-22 | SCIENTIA | Rejected (reasoning route, user) | 未向网站提交。用户明确指出该结果是在强行拼凑，且 `AHMNRTETY` 不是中间答案；`MATH ENTRY → ELEMENT → 元素符号 - CC → SCIENTIA` 整条路线撤销。 |
| 2026-08-22 | TENTH ARMY | Rejected (main test site, state `23213`) | 精确指标为 `01+03+05+06+07+09+10+13`、危机等级 25。题内框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10；它使用了错误的轮换行。 |
| 2026-08-22 | GUARANTEE | Accepted (main test site, state `23001`) | 精确指标为 `01+03+05+06+07+11`、危机等级 9。题内框原文：`这是主测试地的答案！` 剩余次数仍为 10；它锁定轮换地 1 组合变体第 4、7、10 格为 `R,A,E`，但不足以在 `AYERSCARPE` 与 `IMPROVABLE` 间消歧。 |
| 2026-08-22 | STRAY YARN | Rejected (main test site, state `23213`) | 精确指标为 `01+03+05+06+07+09+10+13`、危机等级 25。题内框原文：`答案不正确。已进入 10 分钟冷却。` 剩余次数仍为 10；它是错误行串 `YAANRTSRY` 的自由变位。 |
| 2026-08-22 | MAIN STORY | Accepted (main test site, state `23213`) | 精确指标为 `01+03+05+06+07+09+10+13`、危机等级 25。题内框原文：`这是主测试地的答案！` 剩余次数仍为 10；这是提示 7 要求的登顶中间答案。 |
| 2026-08-22 | CLIMATIC | Accepted (Hunt final, user) | 用户明确反馈“CLIMATIC 答案正确”。 |

## Evidence and artifacts

- `artifacts/main-score0-plus1.webp`：候选配置的主提取图。
- `artifacts/stage1-base.webp`：轮换地 1 基础八句。
- `artifacts/stage2-base.webp`：轮换地 2 基础八图。
- `artifacts/extraction.tsv`：逐格提取表。
- `artifacts/stage1-variants.tsv`：轮换地 1 的四词族 `PROBABLE / PROVABLE / IMPROBABLE / IMPROVABLE`。
- `artifacts/stage3-identifications.tsv`：轮换地 3 基础九图的技能图标、索引与逐字提取表。
- `artifacts/stage4-identifications.tsv`：轮换地 4 四个变体的逐图关卡名、楼层对、Polybius 坐标与字母。
- `artifacts/main-valid-states.tsv`：十八个网站确认状态及拒绝对照的状态码、指标、分数和答案。
- `artifacts/stage3-changed-row.tsv`：指标 `10` 下完整改变行 `DEMOCRACY` 的逐格证据。
- `artifacts/summit-search.tsv`：唯一满分 `23213` 的九格 `MAIN STORY`、来源格与题内正例支持审计。
- `artifacts/final-extraction.tsv`：主线第 1–8 章标题词、对应状态危机等级和 `CLIMATIC` 提取表。
- `artifacts/final-chain.tsv`：已拒绝的 `TRITONUS → TO → Angelina → ANGELINA` 旧路线，仅保留作反例审计。
- `artifacts/final-rebus.tsv`：把中间词 `TRITONUS` 错按音乐语义延伸到 Arknights 台词、黑键与 `BLACKKEY` 的已拒绝链，用于防止重试。
- `artifacts/tritonus-dialogue.tsv`：英文游戏台词表中完整单词 `tritone` 的唯一命中，以及按角色 ID、语音 ID 对齐的中文干员名与同条中文台词。
- `artifacts/stage3-shuffle-completions.tsv`：把 `SIGNATURE` 视作无放回字母袋时，144 个指标 `10` 状态中仅有的五个英文补全。
- `artifacts/stage3-anagram-evidence.tsv`：指标 `10` 下“完整主串变位”在多状态得到的正常英语词；标出唯一精确 18 分目标。
- `artifacts/risk18-strength-extraction.tsv`：状态 `13112` 的八个编号格、所取行列、原串 `RTTHSNGE` 与变位 `STRENGTH`。
- `work/visual/inventory/`：对输入 SingleFile HTML 建立的 23 个稳定图像编号、清单和接触表。
- `work/visual/stage1-text.png`、`stage2-words.png`：从稳定编号图像按固定坐标放大的直接渲染。
- `work/puzzle-component.vue`：在线页面公开加载的动态组件副本，只用于核对状态映射与提交边界。
- `work/analyze_meta.py`、`work/meta_images/`：有界下载并解析全部 288 张主图；单图限制 512 KiB，总缓存约 20 MB。
- `work/analyze_summit_instruction.py`：复算唯一满分、九格 `MAIN STORY` 和满分各来源格的题内正例支持；已撤销元素路线只保留作失败审计。
- `work/visual/summit/coordinates.tsv`、`annotations.json`、`annotated.png`：满分主图九个编号格的稳定坐标、来源行列和直接标注。
- `work/infer_stage1_rows.py`、`work/stage1-variant0-ranking.tsv`、`work/stage1-variant2-ranking.tsv`：在固定前 300,000 英语词内分别排名 35,883 个八字母行和 20,241 个十字母行；`PROBABLE / IMPROBABLE` 唯一命中各自全部 72 个状态。
- `work/infer_stage3_row.py`、`work/stage3-row-ranking.tsv`：扩展 `DE??CR??Y` 的全部 456,976 种补全；`DEMOCRACY` 唯一命中 143 个单词加 `MAIN STORY`，第二名只有 142 个单词。
- `work/stage3-shuffle-completions.tsv`：同一脚本对 `SIGNATURE` 子多重集补词模型的完整输出；只保留每状态最高 20 个命中，实际总共只有五行。
- `work/solve_stage3_anagram.py`、`work/stage3-anagram-completions.tsv`：保持第三行 `SIGNATURE`，对 144 个指标 `10` 状态的完整主串做有界变位词枚举；词库上限 300,000，最低词频 1.0。
- `work/match_stage4_maps.py`、`work/stage4_ref/`：用 42 张公开关卡图匹配轮换地 4 的上下半图。
- `work/find_outer_patterns.py`、`work/outer-pattern-results.tsv`：已删除为目标词量身挑选顺序的循环论证；现枚举每组 3,840 个可见状态轴规则（去重为基础 48、改变 44 个顺序），并合并文字中心、风险对齐和主图中心等规范对照，共 204 行。状态轴对 `TRITONUS / CENTERON` 及其反序均零命中。
- `work/verify_final_chain.py`：检查两组字母多重集、`TRITONUS` 的中央 `TO`、TO 活动干员与轮换地 3 图片干员的唯一交集，以及最终八字母锁。
- `work/visual/stage3-changed.webp`：指标 `10` 下轮换地 3 的直接下载图；九个技能图不变，括号索引全部消失。
- `work/inspect_stage3_skills.py`：固定检查九个技能的英文名、序数、SP 数据和六组材料字段；这些简单属性均不能给出改变行。
- `work/find_token_keywords.py`、`work/token-keyword-matches.tsv`：在六个公开信物模块及两份英文角色语料（总计 19,318,373 字节）中有界搜索十六个主答案；得到 1,636 个宽泛命中、`RINGTONES` 零命中，故不能形成唯一角色映射。
- `work/identify_tritonus_operator.py`：对 12,662,518 字节英文台词表做完整单词精确检索，再在 12,995,903 字节中文台词表和 20,925,532 字节中文角色表中按稳定 ID 对齐；唯一链为 `Ebenholz / 黑键` 的同一条中英文语音。
- `work/test_trithemius_cipher.py`、`work/trithemius-cipher-results.tsv`：Trithemius 渐进移位、中央起点和两两 tabula recta 的 416 个有限变体；英语词频全部为 0。
- `work/analyze_valid_state_graph.py`、`work/valid-state-graph-paths.tsv`：检查十六个有效配置能否沿单组变化或单指标切换形成 `CENTERONTRITONUS` 路径；两种邻接均无路径。
- `work/visual/accepted-paths/contact.png`、`coordinates.tsv`：16 个题内正例的编号路径接触表与统一坐标，作为主图中心检验的持久空间表示。
- 复现输入图清单：

  ```text
  python .agents/skills/inspect-puzzle-visuals/scripts/visual_workbench.py inventory "rounds/irrational-manager-hypothesis/nodes/e07-contingency-contract-battleplan-cryptographia/input/危机合约「破玄作战」.html" --output "rounds/irrational-manager-hypothesis/nodes/e07-contingency-contract-battleplan-cryptographia/work/visual/inventory"
  ```

## Important failed routes

- **`FTRETIFN` 已被用户否定。** 错误来自把十句变体的错误干员名 `CLIFFHEART` 机械截成八句的 `IFFHEART`；正确行是 `PROBABLE / IMPROBABLE` 词族。
- **`LMUITIAN` 已被网站否定。** 它使用了错误的轮换地 1 行；正确八行令包括零分配置在内的 288 个状态全部产生合法主答案。
- **`UPLTTINN` 已被网站否定。** 它把主图交替楔形解释为第 1 行右至左、第 2 行左至右的填词方向；该直接方向修正仍不成立，因此不继续盲试其余翻转组合。
- **`SERVICER` 已被网站否定。** 它来自错误行 `PROVENCE`；状态 `11100` 用正确行 `PROVABLE` 读作 `SERVICES`。
- **`LAVENDER` 已被用户否定。** 它来自错误行 `PROVENCE` 与 `SIGNATURE` 的语义联想；正确行是 `PROVABLE`，最终机制也不使用状态交集。
- **`TRITONUS / CENTER ON` 外层已整体作废。** 十六个网站确认答案按危机等级循环取字只能制造字母袋 `TRINUOTS / NNEECTOR`，3,840 种可见状态轴顺序均零命中；其后 `TO → Angelina` 的终点又被用户明确否定。提示 7 规定的新路线直接从满分状态遍查 288 个输出，因此不得恢复这条循环取字路线。
- **“居中排词/主图空间中心”路线没有信号。** 当前 204 行有限对照覆盖主答案文字中心、风险取字点对齐、规范状态/风险/答案序、可见状态轴序和四种空间排序；没有产生唯一八字母串。这只否定把十六张主图做几何居中的路线，不否定对中间词 `TRITONUS` 直接取中央两字母的简单指令。
- **`VENATION → TRAGODIA` 路线被关键对照削弱。** 在 18 分状态 `11013`，把轮换地 3 的三个无索引图标分别从 `VULPISFOGLIA / SURTR / MOUNTAIN` 中任选 `V/T/O`，能把模板补成唯一常见词 `VENATION`；该词又精确出现在 Tragodia 的信物描述中。但题内框在这一精确状态明确拒绝 `VENATION`，所以“无索引即任选名字母”的规则不成立，`TRAGODIA` 不能据此作为候选。
- **`PRINTED` 已被网站否定。** 九个技能英文名的末字母模板为 `TWN?ADEEO`；状态 `01011` 不使用未知的第 4 位，仍会稳定给出 `PRINTED`。精确配置下的拒绝说明这个完整英语词只是偶然命中，不能据此把指标 `10` 解释为“取技能名末字母”。
- **`GREETED` 已被网站否定。** 把改变行强行补成 `DESIGN…` 前缀会拼出该词；正确改变行已由全状态唯一性锁定为 `DEMOCRACY`。
- **`GREETER` 已被网站否定。** 它是把基础 `SIGNATURE` 当作可任意重排字母袋时唯一的精确 18 分英文补全，使用 `G,E,R`；精确配置仍被拒绝，故不能把 shuffle 理解为逐配置自由选取这些字母。`WELCOMER` 等由 `GREETER (8)` 推出的外层同义词也随之失去前提，不构成候选。
- **`STRENGTH` 已被用户否定为 Hunt 最终答案。** “先读完整主串，再整体变位”的模型虽然能制造一批英语词，但提示 5 明确说变化的是轮换测试地 3 的提取方式；精确 18 分也不是充分的选态依据。没有新证据不得恢复这一候选。
- **`DIABOLUS` 已被用户否定为 Hunt 最终答案。** 它来自把 `TRITONUS` 语义替换为 *diabolus in musica*，却没有由题面规定这个替换，也没有实际执行 `CENTER ON`；不再猜或提交其他三全音别称。
- **`JOHANNES` 已被用户否定为 Hunt 最终答案。** `TRIT[ON]US → TRIT[HEMI]US` 是离开《明日方舟》主题的字形联想，“八字母锁直接选择其八字母名字”也没有题面操作支持。后续 416 个规范 Trithemius / tabula recta 变体全部无词频信号，因此整条密码学家路线停止，不得恢复。
- **`EBENHOLZ` 已被用户否定为 Hunt 最终答案。** 英文台词表中 `tritone` 的唯一命中证明该干员是强定位点，但八字母锁与其英文代号同长不足以规定“直接提交代号”；后续必须从题面操作或角色字段继续提取，不得恢复。
- **`BLACKKEY` 已被用户否定为 Hunt 最终答案。** 它把中文代号“黑键”逐字翻译成八字母，并用音乐/密码双关作事后确认；题面没有规定翻译这一步。该拒绝也终止从 Ebenholz/黑键的别名、真名、译名或台词位置继续派生答案。
- **`ANGELINA` 已被用户否定为 Hunt 最终答案。** 它来自把两组已确认词的循环取字字母袋解释为 `CENTER ON TRITONUS`，再把中央 `TO` 解释成活动代码并取与轮换地 3 的唯一干员交集。提示 7 给出的规定路线是“满分主答案 → 遍查所有可能主答案”，而这条链既没有使用满分状态，也没有遍查全部输出；整条活动/干员交叉路线停止。
- **`TRY ANTHEM` 已被满分状态题内框否定。** 它与 `TRY THE MAN` 使用相同九字母袋，且两词切分一度更简洁；但状态 `23213` 的明确拒绝优先。不能再从 `ANTHEM` 延伸到歌曲、国家或 `COUNTRIES`。
- **`TRY THE MAN` 已被满分状态题内框否定。** 由它把状态 `13113` 的字母袋 `RHCATMEN` 变位成八字母 `MERCHANT` 的路线随之前提一起作废；即使 `MERCHANT` 是常见词和《明日方舟》职分，也不能在没有新证据时提交或恢复。
- **`TENTH ARMY` 与 `STRAY YARN` 已被满分状态题内框否定。** 两者都来自错误行 `MATTERHORN / AYERSCARPE` 与错误 Polybius 字母的自由变位；正确九格无需变位，原位即为 `MAIN STORY`。
- **`MATH ENTRY → ELEMENT → SCIENTIA` 整条路线已撤销。** `MATH ENTRY` 已被满分状态题内框拒绝，用户又明确指出 `AHMNRTETY` 不是中间答案。由此联想到 matrix element、筛六个元素、收元素符号、删除无指令的 `CC` 再变位为 `SCIENTIA`，属于跳过提示 7 第一步后的事后拼接；它也不能锁定轮换地 3 第 8 格为 `U`。
- **Trithemius 数值解码无信号。** 四个已有八字母串在现代/历史字母表、正反方向、渐进/中央起点及两两 tabula recta 下共 416 个有限变体，没有一个获得正英语词频；不再增加任意起点、关键词或复合密码。
- **有效状态不构成目标短语路径。** 把十六个配置视为顶点，以“一个状态码分组改变”或“单指标开关”连边，均不存在拼出 `CENTERONTRITONUS` 或其反序的 Hamilton 路径；因此不能用配置邻接为两组变位指定统一顺序。
- **技能固定属性枚举没有直接复原改变行。** 九个技能英文名首尾字母、按技能序数取干员名/技能名、SP 常数及六个固定材料槽没有稳定规则；但 `DEMOCRACY` 已由题内锁定字母和全状态唯一性确定，不再需要继续扩展字段。
- **主答案到干员语料的关键词映射不唯一。** 十六个主答案在公开信物、语音和档案语料中产生 1,636 个命中，且 `RINGTONES` 完全缺失；频繁词有数百处命中，无法规定唯一干员或提取顺序，因此停止该路线。
- **不要假设所有指标组合共享同一个八字母答案。** 对 96 个 `+1` 主图状态做了有界一致性检查；仅用已确认的 `MOUNTAIN` 锚定时，同一个最终位置在不同状态同时得到 `M` 与 `I`，直接否定跨状态不变量。页面组件也把 `activeContracts` 传给内部判题。实验脚本与缓存保留在 `work/analyze_meta.py`、`work/meta_images/`。

## Next action

已完成；`CLIMATIC` 已由用户确认正确，无需进一步操作。
