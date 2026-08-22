---
node_id: e11-four-treasure-bags
title: 套四宝
kind: puzzle
round: irrational-manager-hypothesis
parent:
source:
round_feeder: yes
feeders:
status: accepted
answer: WEIGHT
confidence: high
summary: 用户已确认 WEIGHT 为正确答案。九行按提示 1 跨原词边界连续藏出 GRASS、BOTTLE、GUTTER、POND、BONNET、WONDERLAND、DEVIL、ROOSTER、STARS；再由句子情境得到 SNAKE、GENIE、LOSER、AROWANA、BEE、ALICE、ANGEL、SHE、DESTINY。九只鸽子的中字母依次为 ANSWEIGHT，直接拆作 ANS / WEIGHT。
updated: 2026-08-22
---

# 套四宝

## Current conclusion

**已确认答案：WEIGHT。**

九个中字母按原顺序组成：

    A N S W E I G H T

直接断为 **ANS / WEIGHT**，也就是“答案：WEIGHT”。这里没有末步变位。

## 鸭中的鸡：跨词界连续隐藏

提示 1 的“在多个词中间藏”应按字面理解：忽略空格和标点，连续取括号指定数量的字母，而且所取片段跨过原词边界。

| # | 跨词位置 | 鸡 |
| --- | --- | --- |
| 1 | Mardi GraS, Spies | **GRASS** (5) |
| 2 | the BOT TL Entered | **BOTTLE** (6) |
| 3 | facinG UTTER | **GUTTER** (6) |
| 4 | weaPON During | **POND** (4) |
| 5 | ribBON. NETworking | **BONNET** (6) |
| 6 | WONDER! LANDslide | **WONDERLAND** (10) |
| 7 | ruDE, VILe | **DEVIL** (5) |
| 8 | kangaROOS. TERrific | **ROOSTER** (7) |
| 9 | beST ARSenal | **STARS** (5) |

用户指出的两个例子是纠正机制的决定性证据：GRASS 与 DEVIL 都跨词界原序连续出现，不是字母袋。

## 鸡中的鸽子

句子其余部分给出一种情境，使鸡所代表的事物里面出现另一事物，即 X in the Y。

| # | 鸡 Y | 鸽子 X | 关系 | 长度 | 中字母 |
| --- | --- | --- | --- | ---: | --- |
| 1 | GRASS | **SNAKE** | 从事破坏的间谍可称 snake in the grass。 | 5 | **A** |
| 2 | BOTTLE | **GENIE** | Genie in a bottle 能实现愿望。 | 5 | **N** |
| 3 | GUTTER | **LOSER** | 连最弱对手也输掉、陷入绝望的一方是落到 gutter 的 loser。 | 5 | **S** |
| 4 | POND | **AROWANA** | 《大展鸿图》唱“水池里面银龙鱼”；no silver lining 去掉 silver 修饰，留下 arowana。 | 7 | **W** |
| 5 | BONNET | **BEE** | 对 networking 念念不忘，即 a bee in one's bonnet。 | 3 | **E** |
| 6 | WONDERLAND | **ALICE** | Tim Burton 语境给出 Alice in Wonderland。 | 5 | **I** |
| 7 | DEVIL | **ANGEL** | 田馥甄《魔鬼中的天使》，即 angel in the devil。 | 5 | **G** |
| 8 | ROOSTER | **SHE** | 若被当成公鸡的动物真的会下蛋，male 判断有误，所谓 rooster 其实是 she。 | 3 | **H** |
| 9 | STARS | **DESTINY** | destined 提示 destiny in the stars。 | 7 | **T** |

第 4 行可由《大展鸿图》的歌词“水池里面银龙鱼”复核：[Shazam 歌词页](https://www.shazam.com/es-mx/song/1763742884/%E5%A4%A7%E5%B1%95%E9%B8%BF%E5%9B%BE/music-video)。第 6 行的奥斯卡描述也吻合：学院官方记录显示 Tim Burton 的 Alice in Wonderland 获艺术指导与服装设计两项奖：[83rd Academy Awards](https://www.oscars.org/oscars/ceremonies/2011)。第 7 行歌名可由[田馥甄官方频道](https://www.youtube.com/watch?v=CLApNrkWoPY)核对。

第 3 行句面也会直接让人想到 UPSET；不过提示 2 要找可以处于 gutter 中的对象，因此表中采用实体 LOSER。二者中字母都是 S，完整提取不受影响。第 8 行则由 male / lay eggs 的代词反转与所需中字母 H 锁定 SHE。

## 鸽子中的鹌鹑

九只鸽子的长度为：

    5, 5, 5, 7, 3, 5, 5, 3, 7

全部为奇数，因此各有唯一中字母：

    SNAKE   -> A
    GENIE   -> N
    LOSER   -> S
    AROWANA -> W
    BEE     -> E
    ALICE   -> I
    ANGEL   -> G
    SHE     -> H
    DESTINY -> T

    ANSWEIGHT -> ANS / WEIGHT

所以答案是 **WEIGHT**。

## Accepted audit

- 九只鸡都严格符合括号长度、原序连续且跨至少一个词界。
- 愿望、网络执念、Tim Burton/奥斯卡、田馥甄歌曲、产蛋性别和 destined 等题面信息均得到使用。
- 九只鸽子均为奇数长，中字母原序直接给出 ANSWEIGHT。
- 用户已明确确认 WEIGHT 正确。

机械复核见 [artifacts/bag_relations.tsv](artifacts/bag_relations.tsv) 和 [artifacts/validate_bags.py](artifacts/validate_bags.py)。验证脚本检查九个隐藏词的括号长度与跨词边界条件、鸽子的奇数长度，以及 ANSWEIGHT 到 WEIGHT 的提取。

## Submission history

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-22 | GRUMPY | rejected | 用户明确反馈“答案不正确”。 |
| 2026-08-22 | RUDE DWARF | rejected | 用户明确反馈“RUDE DWARF 不是答案”。 |
| 2026-08-22 | RED DWARF | rejected | 用户明确反馈“RED DWARF 不是答案啊”。 |
| 2026-08-22 | FORWARD | rejected | 用户明确反馈“FORWARD 不是答案”。 |
| 2026-08-22 | FROWARD | rejected | 用户明确反馈“FROWARD 不是答案”，并提供三个官方提示标题。 |
| 2026-08-22 | RAW | rejected | 用户明确反馈“RAW 不是答案”。 |
| 2026-08-22 | OUTSHINE | rejected | 用户明确反馈“OUTSHINE 不是答案”，并解锁提示 3。 |
| 2026-08-22 | TORSIONAL | rejected | 用户明确反馈“TORSIONAL 不是答案”，并解锁提示 1。 |
| 2026-08-22 | CRITERION | rejected | 用户明确反馈“CRITERION 不是答案”，并指出正确机制示例：SNAKE in the GRASS、ANGEL in the DEVIL。 |
| 2026-08-22 | WEIGHT | accepted | 用户明确反馈“WEIGHT 是正确答案”。 |

## Evidence and artifacts

- [artifacts/bag_relations.tsv](artifacts/bag_relations.tsv)：九行跨词鸡、情境鸽和中字母表。
- [artifacts/validate_bags.py](artifacts/validate_bags.py)：复现跨词边界与 ANSWEIGHT -> WEIGHT。
- [work/analyze_layers.py](work/analyze_layers.py)：枚举符合括号长度且跨词界的连续英文候选。
- work/visual/inventory/：此前检查确认题面列表没有额外图片编码；唯一图片为用户头像，与机制无关。

## Important failed routes

- **CRITERION（已明确判错）：** 错把“在多个词中间藏”理解成字母袋，构造出并不连续隐藏的 STAGE、CASTLE 等词；随后自由选择鸽子并把中字母变位。GRASS 与 DEVIL 的跨词连续证据直接推翻该路线。
- **GRUMPY、RUDE DWARF、RED DWARF、FORWARD、FROWARD、RAW、OUTSHINE、TORSIONAL（均已明确判错）：** 都未完成三条提示规定的九行同构链，不得恢复。
- **鸽子强制当鸡中字母子袋：** SNAKE in the GRASS 与 ANGEL in the DEVIL 已证明第二层是情境中的 X in Y，不是字母包含。
- **末步任意变位：** 正确中字母已原序写成 ANSWEIGHT，不需要重排。

## Next action

已完成。WEIGHT 已由用户确认；保留复核表和脚本，不再恢复任何已判错路线。
