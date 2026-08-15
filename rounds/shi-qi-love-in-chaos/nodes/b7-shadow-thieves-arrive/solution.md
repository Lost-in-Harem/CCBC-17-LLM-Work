---
node_id: b7-shadow-thieves-arrive
title: 盗影团参上！
kind: puzzle
round: shi-qi-love-in-chaos
parent:
source:
round_feeder: yes
feeders:
status: accepted
answer: NADIR
confidence: high
summary: 双色 Nonogram 唯一解先由八条编号灰路提取出网站确认的里程碑 KNUCKLES。提示 1 确认应取其“指关节”义：十个 3×5 小块编码左右手五指的关节屈伸；提示 2 再由共同字“影”指向手影，底图给出 A–J 双手的空间姿态。五组依次形成 SNAIL、CRAB、DOG、RABBIT、DEER，按 (2/5)、(3/4)、(1/3)、(5/6)、(4/4) 提取得 NADIR；用户已确认答案正确。
updated: 2026-08-15
---

# 盗影团参上！

## Current conclusion

最终答案为 **`NADIR`**，用户已确认正确。

第一阶段网站确认的 **`KNUCKLES`** 应按字面理解为“指关节”。提示 1 又明确要求查词义、观察盘面形状并活动身体：每个 A–J 小块都是 3×5，五列对应五根手指，三行对应最多三个指关节；拇指只有两个，所以角上的灰格正好标出缺少的第三格，并同时确定左右手。黑格指示相应关节屈曲，白格保持伸直；五张底图中的立体 A–J 则给出两手的朝向、相对位置和交叠关系。

标题和风味文本共有的关键字是“影”；把“影”与上一层的手指/关节主题合起来就是**手影**。风味文本“自由地跳着指尖上的舞蹈”具体描述了摆动、弯曲手指来表演手影。依照 A–J 关节状态和底图姿态，五对双手依次形成 `SNAIL / CRAB / DOG / RABBIT / DEER`；按括号的“位置/词长”提取即得 `NADIR`。

## Observed facts

- 题面标题为“盗影团参上！”，风味文本为“自由地跳着指尖上的舞蹈，轻盈得像暗影中藏伏的波斯猫”。二者共有“影”和“上”；提示所指的是能与上一阶段的指关节主题组成“手影”的“影”。
- 正文明确说明本题有中间答案验证，并要求完成 Nonogram 后将十个灰色区域按阅读顺序标作 A–J。
- 主图是 10 列 × 15 行的双色 Nonogram。黑色和浅灰色线索是两种不同颜色；异色段可相接，同色段之间必须留白。
- 网格下方五图依次包含立体字片 `A/B`、`C/D`、`E/F`、`G/H`、`I/J`，注记依次为 `(2/5)`、`(3/4)`、`(1/3)`、`(5/6)`、`(4/4)`。
- 用户明确说明这些括号是标准“位置/词长”提取，而不是坐标、方向或另一层二进制。
- 用户解锁的提示 1 原意是：若看不懂第一阶段所得词，应搜索词义、观察 Nonogram 盘面的形状特征并活动身体。词典将 `knuckle` 释为手指弯曲处的关节；这直接确认十个 3×5 块是关节屈伸表，而不是 Sonic/Shadowmatic 主题。
- 用户提供的提示 2 原意是：关注标题与风味文本共有的一字；将它与上一阶段掌握的主题联想，可理解底部五图；风味文本具体描述了正在进行的行为。
- 粗线划出的每个 3×5 块都在拇指列的同一角缺一格：A、C、E、G、I 的灰格在左上，B、D、F、H、J 的灰格在右上。把右侧五块左右翻转到人体自身视角后，十块全都成为“拇指缺少第三关节”的五指表，且每对恰为左手/右手。
- E/F 是最强的极性校验：两手都只有食指一列为黑，正对应手影 DOG 的“两食指向内弯，其余手指伸展”；因此本层采用黑格=弯曲，而非反色解释。

## Nonogram solution

记 `#` 为黑格、`g` 为灰格、`.` 为空白。双色约束恰有一个解：

```text
g####....g
#####.....
#####.....
g########g
##########
#........#
g#......#g
.#......#.
.#......#.
g##......g
#..###..##
...##....#
g........g
#####.....
.........#
```

十个灰格坐标（行、列从 1 起）为：

| Label | Cell | Label | Cell |
| --- | --- | --- | --- |
| A | r1c1 | B | r1c10 |
| C | r4c1 | D | r4c10 |
| E | r7c1 | F | r7c10 |
| G | r10c1 | H | r10c10 |
| I | r13c1 | J | r13c10 |

若忽略浅灰线索，黑白模型在枚举上限 20 内有两个解；按双色规则则唯一，因此灰色线索不是界面上的划除标记。

## Confirmed milestone

八条编号灰线各沿格心通过五格。由红色编号圆点向外读取，以黑格为 1、白格为 0，并按五位二进制 A1Z26 解码：

| Path | Cells from numbered circle | Bits | Decimal | Letter |
| --- | --- | --- | ---: | --- |
| 1 | r15c4 → r14c4 → r13c4 → r12c4 → r11c4 | 01011 | 11 | K |
| 2 | r6c2 → r7c2 → r8c2 → r9c2 → r9c3 | 01110 | 14 | N |
| 3 | r3c5 → r3c6 → r4c6 → r3c7 → r4c7 | 10101 | 21 | U |
| 4 | r10c6 → r10c5 → r10c4 → r10c3 → r10c2 | 00011 | 3 | C |
| 5 | r15c5 → r14c5 → r13c5 → r12c5 → r11c5 | 01011 | 11 | K |
| 6 | r8c8 → r8c9 → r7c9 → r7c8 → r7c7 | 01100 | 12 | L |
| 7 | r6c6 → r6c5 → r5c5 → r6c4 → r5c4 | 00101 | 5 | E |
| 8 | r12c10 → r12c9 → r11c8 → r11c9 → r11c10 | 10011 | 19 | S |

按编号排列得到 **`KNUCKLES`**。用户确认它是里程碑，网站反馈为“你正在正确的道路上”。“道路”直接回指这八条灰路。

## Hand-shadow interpretation and extraction

Nonogram 的粗线把整个 10×15 网格分成十个 5 列 ×3 行小块，按阅读顺序正好是 A–J。将右手块左右翻转到人体自身视角后，每块都按拇指、食指、中指、无名指、小指排列；三行记录从指尖侧到掌侧的关节层。灰格是拇指缺少的第三关节位，黑格表示屈曲，白格表示伸直。底图的立体字母只负责说明两只手的朝向、前后和交叠关系，不是待提取的字形。

| Pair | Blocks | Diagnostic pose | Shadow name | Extraction |
| --- | --- | --- | --- | --- |
| A/B | r1–3,c1–5 / r1–3,c6–10 | A 的全部有效关节屈曲成拳，B 完全伸直；两手近乎平行，一拳作壳、另一手作身体和触角 | `SNAIL` | `SNAIL[2] = N` |
| C/D | r4–6,c1–5 / r4–6,c6–10 | 两手状态相同，指端卷曲成爪；图中 C、D 的顶端分别朝外、腕侧相接，形成螃蟹的对称双爪 | `CRAB` | `CRAB[3] = A` |
| E/F | r7–9,c1–5 / r7–9,c6–10 | 两手都只把食指向内卷，其他手指伸展；按图重叠后形成犬的耳、吻部和开合下颌 | `DOG` | `DOG[1] = D` |
| G/H | r10–12,c1–5 / r10–12,c6–10 | 左手收无名指和小指、食指向拇指弯；右手卷食指和拇指并展开其余手指，按图将右手手背搭在左手上 | `RABBIT` | `RABBIT[5] = I` |
| I/J | r13–15,c1–5 / r13–15,c6–10 | 一手五指在中段微屈并分开作鹿角，另一手手指叠合、拇指屈曲作三角形鹿头 | `DEER` | `DEER[4] = R` |

因此最终串为：

```text
N A D I R
```

这严格使用了括号中给出的词长 `5,4,3,6,4` 和位置 `2,3,1,5,4`。公开手影教程对 `SNAIL` 的“一拳作壳”、`DOG` 的“两食指内卷”、`RABBIT` 的左右手逐指姿势、`DEER` 的鹿头/鹿角分工，以及 `CRAB` 的两手腕侧相接、向外展开均有独立说明。`NADIR` 本义是“最低点/正下方”，也与题面最底部的五张图形成自然复核。

## Answer audit

- `NADIR` 是五字母英文单词，符合五次单字母提取的输出格式；词义“最低点/正下方”还呼应了最底部五图的位置。
- 机制使用了 Nonogram 的黑格、全部十个灰格/标签、五张底图、五组括号、里程碑 `KNUCKLES`、两条提示、标题/风味文本中的“影”以及“指尖上的舞蹈”，没有遗留整层题面信息。
- 五个名称的长度全部与分母精确吻合；其中 E/F→`DOG` 和 G/H→`RABBIT` 可由逐指动作说明直接校准，A/B→`SNAIL`、C/D→`CRAB`、I/J→`DEER` 又同时吻合关节状态与底图朝向。用户随后明确确认 `NADIR` 正确，因此状态记为 `accepted`。

## Submission history

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-15 | SPADE | rejected | 用户明确反馈“SPADE 不是答案或者里程碑”。 |
| 2026-08-15 | KNUCKLES | milestone | 网站确认是里程碑；附加信息：“你正在正确的道路上。” |
| 2026-08-15 | ROUGE | rejected | 用户明确反馈“ROUGE 不是答案”。 |
| 2026-08-15 | FINAL | rejected | 用户明确反馈“FINAL 不是答案”，并确认 `(2/5)` 是从五字母单词提取第 2 位。 |
| 2026-08-15 | OMBRE | rejected | 用户明确反馈“答案不是 OMBRE”，并指出 A–J 明显对应上方题解所得十个小块；该候选未使用核心数据。 |
| 2026-08-15 | ORDER | rejected | 用户明确反馈“ORDER 不是答案”；MOOSE/BIRD/DOG/BADGER/DEER 的手影命名链至少有一项错误。 |
| 2026-08-15 | NADIR | accepted | 用户明确反馈“NADIR 正确”。 |

## Evidence and artifacts

- 原始题面与不可变资源：`input/盗影团参上！.html`。
- 解出的正文与资源清单：`work/visual/page/`、`work/visual/inventory/manifest.json`。
- 双色 Nonogram 求解器：`work/solve_nonogram.py`。
- 唯一解示意与原图叠加：`work/visual/nonogram-solution.png`、`work/visual/nonogram-overlay.png`。
- 灰路几何与里程碑提取：`work/analyze_gray_regions.py`、`work/decode_gray_paths.py`。
- 五图颜色层、纯剪影和去滚转视图：`work/visual/letter-layers/`。
- 十块的左右手规范化表示：`work/render_hand_codes.py`、`artifacts/hand-code-map.png`、`artifacts/hand-code-map.tsv`。
- 手影参考图与页面截取保存在 `work/visual/hand-shadow-reference/`，最终识别表为 `artifacts/hand-shadow-extraction.tsv`。[MadeForMums 的手影教程](https://www.madeformums.com/school-and-family/hand-shadow-puppets/) 同页列出并解释 `SNAIL / CRAB / DOG / RABBIT / DEER` 五种姿势；其中更细的逐指说明可由 [ParentCircle](https://www.parentcircle.com/how-to-make-animal-hand-shadows/article) 交叉核对。[Cambridge Dictionary](https://dictionary.cambridge.org/dictionary/english/knuckle) 将 `knuckle` 释为手指弯曲处的关节，[Merriam-Webster](https://www.merriam-webster.com/dictionary/nadir) 将 `nadir` 释为“最低点”或天球上与天顶相反的正下方点。

复现主要结果：

```text
python rounds/shi-qi-love-in-chaos/nodes/b7-shadow-thieves-arrive/work/solve_nonogram.py --mode colour --max-solutions 20
python rounds/shi-qi-love-in-chaos/nodes/b7-shadow-thieves-arrive/work/decode_gray_paths.py
python rounds/shi-qi-love-in-chaos/nodes/b7-shadow-thieves-arrive/work/render_hand_codes.py --output rounds/shi-qi-love-in-chaos/nodes/b7-shadow-thieves-arrive/artifacts/hand-code-map.png --table rounds/shi-qi-love-in-chaos/nodes/b7-shadow-thieves-arrive/artifacts/hand-code-map.tsv
```

## Important failed routes

- `SPADE` 只联系到题目角色背景，没有使用完整谜面机制；用户确认它既非答案也非里程碑。
- 把括号当成“第几条路/路内第几格”得到 `10101₂=U`，再解释为 **Up**，违反了用户确认的标准词语取位；这条路线已撤回。
- `ROUGE` 和 `FINAL` 都来自把五张图误建模成具有隐藏第三投影字母的三向字母块。实际去滚转图显示它们只是十个独立的 A–J 立体字片；两候选也都已被用户拒绝。
- `OMBRE` 来自把五张彩图自身的轮廓主观命名成 `TONGS/DOME/BUS/PLIERS/PIPE`；用户明确拒绝，并指出 A–J 对应十个 Nonogram 小块。该路线没有使用核心数据，相关候选产物已撤下。
- 把 `KNUCKLES` 仅当成 Sonic 角色、再由“影”联想到 `SHADOW` 和 Shadowmatic，是一次主题过拟合；它解释不了 3×5 块中拇指少一关节的稳定结构。字面的指关节 + “影”直接给出手影，且能使用全部 A–J 数据。
- `ORDER` 来自把五组手影主观认成 `MOOSE/BIRD/DOG/BADGER/DEER`。用户已明确拒绝；尤其 A/B 与 G/H 只靠参考图外观倒推，未由关节角和底图三维姿态独立生成轮廓，因此这组名称和 `ORDER` 均不得复用。
- 除去八条路径后的 110 格恰等于 22×5，但在 D4 朝向、每对交换、灰格自由取值和全局反色下做完整有界 CSP 搜索仍为零解；不存在简单的“剩余位串直接分成 22 个 A1Z26 字母”读法。
- 把十个 3×5 小块作不受底图姿态约束的平面拼接、蛇形扫描、路径覆盖或布尔重叠，均无法在同一全局规则下生成长度为 5、4、3、6、4 的五个自然词；这些实验不能排除按五张图所示空间姿态投影。
- 数字、特殊符号和第三字形的体素/精确 STL 筛选没有产生同时满足五张图、词长与统一机制的结果。提示 2 和纯剪影识别已经给出更简单且可复现的解释，不再扩大该模型族。

## Next action

本 Node 已完成；保留 **`NADIR`** 及上述提取链，等待其作为 `round_feeder` 被相应 Meta 使用。
