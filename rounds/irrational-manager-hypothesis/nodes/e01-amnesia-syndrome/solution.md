---
node_id: e01-amnesia-syndrome
title: 失忆症候群
kind: puzzle
round: irrational-manager-hypothesis
parent:
source:
round_feeder: yes
feeders:
status: rejected
answer:
confidence:
summary: `GET A HANDLE ON` 已被用户明确否定，连同此前 `COMMENT UPON` 等路线均不得恢复。虽然现有金字塔可闭合到题面 `ANSWER`，最终 cryptic 连续失败说明至少一个上游答案或分词仍可能由错误假设形成自洽闭环；当前从倒数第三行和倒数第二行反向重新审计，不再围绕旧顶层字符串猜同义词。
updated: 2026-08-22
---

# 失忆症候群

## Current conclusion

**当前没有候选答案。** `GET A HANDLE ON` 已被用户明确否定。

这不是把 `WITH/HIGH/GATE` 各自压成冷僻缩写的大字母袋，而是两条同结构习语之间的变换：

```text
OBSERVE  = GET A GANDER AT
                 GANDER = (DANGER)*       [WARNING]

HANG     = DANGLE
HIGH/GATE: DANGLE - G + H = DANHLE
                         -> HANDLE
UPON     = ON, replacing the final AT

TACKLE   = GET A HANDLE ON
```

也就是说，共同骨架 `GET A _ _` 保留；`WARNING=DANGER` 的重排 `GANDER` 换成 `HANG=DANGLE` 经 `G[ate]→H[igh]` 后的重排 `HANDLE`，末尾 `AT` 换成 `ON`。两端分别是现成的 “observe” 与 “tackle” 习语，中间每个顶层词都参与变换。

## Reconstructed pyramid

题图是 `5 → 4 → 3 → 2 → 1` 的相邻合并金字塔。底部印着的 `ANSWER` 是校验值，不是提交答案。

| 层级 | 从左至右 |
| --- | --- |
| 顶层 | `OBSERVE`, `UPON`, `HANG WITH`, `HIGH GATE WARNING`, `TACKLE` |
| 第二层 | `VENUS`, `SUNDAY`, `GEARING`, `RUGBY` |
| 倒数第三行 | `JADE`, `MEMBER`, `PIPKIN` |
| 倒数第二行 | `TRANCE`, `SWEDEN` |
| 题面给定底层 | `ANSWER` |

## Top row reconstruction

### P1: `OBSERVE + UPON → VENUS`

按提示 6，把答案中的含洞字母对齐题图圆洞：

- `OBSERVE` 只有 `O,B` 对应上排两洞，编号位置给 `#1=V, #2=E, #5=S`；
- `UPON` 的 `P,O` 对应下排两洞，编号位置给 `#3=N, #4=U`。

按 `1..5` 读取为 `VENUS`。洞位、词长和编号共同锁定这两个输入，不是从下层答案反猜同义词。

### P2: `UPON + HANG WITH → SUNDAY`

两个输入拆成等长两半：`UP | ON` 与 `HANG | WITH`。青色半圆的方向把 `UP/HANG` 固定为左半，把 `ON/WITH` 固定为右半。四条短语及打印索引为：

```text
相似: UP — TO — THE — SAME — STUFF  -> SAME[1], STUFF[3] = S,U
风险: ON — THIN — ICE                -> ICE[1] +5          = N
胆怯: WITH — COLD — FEET             -> COLD[4]            = D
拖延: HANG — IN — THE — AIR          -> THE[2] -7, AIR[3]+7 = A,Y
```

所以输出严格为 `SUNDAY`。此前写成 `UP ON THE SAME SOUND`、`WITH HOLD BACK` 是误读，已从持久化表中删除。

### P3: `HANG WITH + HIGH GATE WARNING → GEARING`

按提示 6，在两个输入之间逐份配对删除相同字母。`HANGWITH` 的八个字母全部从另一串中各删一份：

```text
HIGHGATEWARNING - HANGWITH
= A,E,G,G,I,N,R
anagram -> GEARING
```

### P4: `HIGH GATE WARNING + TACKLE → RUGBY`

交换左答案内的 `GATE` 与右答案 `TACKLE`，左侧得到：

```text
HIGH TACKLE WARNING
```

这是橄榄球领域的争议性规则名，所以本格答案是 `RUGBY`（[World Rugby](https://www.world.rugby/news/338390/u20-championship-2018-disciplinary?lang=en)）。

## Hint 5: third-from-bottom row

### P5: `VENUS + SUNDAY → JADE`

箭头必须连续走；后一箭头不是重新从原答案起步：

```text
VENUS  +3 -> JUPITER[1] = J
JUPITER+2 -> URANUS[3]  = A

SUNDAY    +3 -> WEDNESDAY[3] = D
WEDNESDAY +6 -> TUESDAY[3]   = E
```

得到 `JADE`。此前表格把第二步仍写作从 `VENUS/SUNDAY` 出发，机制说明确实有误，虽未改变四个提取字母。

### P6: `SUNDAY + GEARING → MEMBER`

提示说的是可拆为元素符号的**前半部分**，不是整词：

```text
SUNDAY  -> S | U | Nd ... AY
GEARING -> Ge | Ar | In ... G
```

沿周期表箭头移动：

```text
S -> Se -> Ca -> Mg  => M
U -> Am -> Eu        => E
Nd -> Tm -> Md       => M
Ge -> C -> B         => B
Ar -> Kr -> Ca -> Be => E
In -> Rb -> Fr       => R
```

得到 `MEMBER`。六条路线见 `artifacts/periodic-routes.tsv`。

### P7: `GEARING + RUGBY → PIPKIN`

保持原顺序写成 `GEARINGRUGBY`，从左至右标为 `A..L`，再作 A1Z26：

```text
label: A B C D E F G H I J K L
value: G E A R I N G R U G B Y
       7 5 1 18 9 14 7 18 21 7 2 25

E+J    = 16 -> P
D/K    =  9 -> I
I-B    = 16 -> P
H-A    = 11 -> K
2√L-C  =  9 -> I
4G-F   = 14 -> N
```

得到 `PIPKIN`。

## Hint 4: penultimate row

### P8: `JADE + MEMBER → TRANCE`

```text
JADE   -> 玉; 加囗 -> 国 -> NATION
MEMBER -> 员; 加囗 -> 圆 -> CIRCLE
```

按图中编号：

```text
NATION[3], CIRCLE[3], NATION[2], NATION[6], CIRCLE[1], CIRCLE[6]
     T          R          A          N          C          E
```

得到 `TRANCE`。

### P9: `MEMBER + PIPKIN → SWEDEN`

两词结构同为 `ABACBD`，故建立：

```text
M <-> P
E <-> I
B <-> K
R <-> N
```

下方可连的拼音端点恰为：

```text
灭 MIE <-> 配 PEI
笔 BI  <-> 渴 KE
热 RE  <-> 逆 NI
```

画三条线，按从上到下读取线上字母（交点只计一次）为 `S,W,E,D,E,N`，即 `SWEDEN`。路线见 `artifacts/panel-09-hint4-routes.png/.tsv`。

### P10 checksum

底图路线读取：

```text
TRANCE[3], SWEDEN[6], SWEDEN[1], SWEDEN[2], TRANCE[6], TRANCE[2]
     A          N          S          W          E          R
```

精确回到题面已印出的 `ANSWER`，因此下层重建是闭合校验，不是最终提交。

## Final cryptic audit

五个顶层答案依次组成：

```text
OBSERVE UPON HANG WITH HIGH GATE WARNING TACKLE
```

### Two idiomatic endpoints

首尾不是两个互不相干的短定义，而是同一骨架的起点和终点：

```text
OBSERVE = GET A GANDER AT
TACKLE  = GET A HANDLE ON
```

`gander at` 的 “look/observe” 义可由 [Cambridge](https://dictionary.cambridge.org/us/dictionary/english/gander) 核对；[`get a handle on`](https://dictionary.cambridge.org/us/dictionary/english/to-get-a-handle-on-something) 则是 “understand or be able to deal with”，与 `tackle` 直接对应。两式的枚举同为 `(3,1,6,2)`，共同部分为 `GET A`。

### Exact middle transformation

| Clue material | Normalization | Exact role |
| --- | --- | --- |
| `WARNING` | `DANGER` | `DANGER* = GANDER`，给起点习语的核心词 |
| `HANG` | `DANGLE` | 作为目标核心词的新 fodder |
| `WITH HIGH GATE` | `H` for `G` | `DANGLE-G+H = DANHLE` |
| implied rearrangement | `DANHLE*` | 得到 `HANDLE` |
| `UPON` | `ON` | 把起点末尾的 `AT` 换成目标末尾的 `ON` |

完整链为：

```text
GET A GANDER AT                     (OBSERVE)
      ^^^^^^  ^^
      DANGER* AT

WARNING=DANGER  ->  HANG=DANGLE
                         -G[ate] +H[igh]
                         -> HANDLE*
AT                ->  ON                  (UPON)

GET A HANDLE ON                      (TACKLE)
```

这比 `COMMENT UPON` 的 `MOUNT + C + P + OMEN` 路线少了三层任选缩写，并解释了为何 clue 同时刻意选用高度相似的 `WARNING/HANG`、`GATE/HIGH` 和首尾习语。

## Submission history

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-20 | CARNIVAL | rejected | 用户明确反馈“答案不是 CARNIVAL”。 |
| 2026-08-20 | CARNAL | rejected | 用户明确反馈“CARNAL 不是答案”。 |
| 2026-08-20 | CARNAVAL | rejected | 用户明确反馈“CARNAVAL 不是答案”。 |
| 2026-08-20 | LACUNAR | rejected | 用户明确反馈“LACUNAR 不正确”。 |
| 2026-08-21 | ANSWER | rejected | 用户纠正：这是题面已给出的最底层校验量。 |
| 2026-08-21 | five top words individually/together | rejected | 用户说明顶层五块本身不是提交答案；提示 3 说明它们组成 cryptic clue。 |
| 2026-08-21 | CUTTING | rejected | 用户明确否定。 |
| 2026-08-21 | STINGS | rejected | 用户明确否定。 |
| 2026-08-21 | STINGING | rejected | 用户明确否定。 |
| 2026-08-21 | CUTTING IN | rejected | 用户明确否定。 |
| 2026-08-21 | BITING | rejected | 用户明确反馈“BITING 不是答案”。 |
| 2026-08-21 | RANCID | rejected | 用户明确反馈“RANCID 不是答案”。 |
| 2026-08-21 | STEAMY | rejected | 用户明确反馈“steamy 不是答案”；来自错误顶层重建。 |
| 2026-08-21 | COMMENTON | rejected | 用户明确反馈“COMMENTON 不是答案”。 |
| 2026-08-21 | WATCH | rejected | 用户明确反馈“WATCH 不是答案”。 |
| 2026-08-21 | NEGOTIATE | rejected | 用户明确反馈“这根本不对”。 |
| 2026-08-21 | GEAR | rejected | 用户明确指出不符合 cryptic clue。 |
| 2026-08-21 | GET ON WITH | rejected | 用户明确反馈“不对”。 |
| 2026-08-21 | NOTICE | rejected | 用户明确反馈“不正确”。 |
| 2026-08-22 | TAKE OUT | rejected | 用户明确反馈“take out 不是答案”。 |
| 2026-08-22 | COMMENT UPON | rejected | 用户明确判断该解析不可能是 intended answer；未声称已向网站提交。 |
| 2026-08-22 | GET A HANDLE ON | rejected | 用户明确反馈“不对”；是否为网站提交结果未另行说明。 |

## Important failed routes

- `DISTRESSING / RAZOR / NEMATOCYSTIC / SIDE / OFF` 是整组错误顶层重建；由它导出的 `CUTTING / STINGS / STINGING / CUTTING IN / BITING / RANCID / STEAMY` 均不可恢复。
- `BEARING` 无法完成提示 5 的周期表路线；正确词为 `GEARING`，其 `Ge|Ar|In` 恰给 `B,E,R`。
- `ANSWER` 只是底部 checksum。
- `COMMENT ON / COMMENT UPON / WATCH / NEGOTIATE / GEAR / GET ON WITH / NOTICE` 都依赖无 indicator 的删字、任选冷僻缩写或间接重排，且已被用户明确否定。`COMMENT UPON` 虽有精确字母袋，但需要 `HANG=MOUNT, WITH=C, GATE=PORT→P, WARNING=OMEN` 四层转换，未解释题面刻意形成的两条同构习语。
- `OUTTAKE / TAKE OUT` 的缺词矩阵没有受到题面指示；`TAKE OUT` 已被明确否定，不得恢复。
- 单答 `GANDER` 或 `HANDLE` 都只解释 clue 的一半，不能提交；它们是完整习语变换中的两个核心词。
- `GET A GANDER AT` 是 `OBSERVE` 给出的起始习语，不是当前目标；经过 `WARNING→HANG`、`G[ate]→H[igh]` 和 `AT→ON` 后，目标才是 `GET A HANDLE ON`。
- `GET A HANDLE ON` 的双习语变换虽能逐字母闭合，但用户已明确否定；不得因字母等式再次恢复。

## Evidence and artifacts

- `artifacts/extraction.tsv`：整座金字塔逐格复算。
- `artifacts/panel-02-word-chains.tsv`：修正后的四条英文短语与提取。
- `artifacts/top-row-reconstruction.tsv`：P1–P4 的输入与输出。
- `artifacts/periodic-routes.tsv`：P6 六条周期表路线。
- `artifacts/panel-08-hint4-extraction.tsv`、`artifacts/panel-09-hint4-routes.png/.tsv`、`artifacts/panel-10-answer-route.png/.tsv`：倒数两行与底部校验。
- `artifacts/final-cryptic.tsv`：最终 clue 的逐项字母等式。
- `work/puzzle-preview.png`：原题完整布局的可视化缩放图，用于核对各格邻接关系。

## Hypothesis audit

| Hypothesis | Exact evidence | Remaining caveat | Rank |
| --- | --- | --- | --- |
| `GET A HANDLE ON` | `OBSERVE=GET A GANDER AT`; `WARNING=DANGER→GANDER`; `HANG=DANGLE`, `-G[ate]+H[igh]→HANDLE`; `UPON=ON` | explicitly rejected by user | rejected |
| `GET A GANDER AT` | exact starting idiom and `DANGER* = GANDER` | it is the source phrase indicated by `OBSERVE`, before the clue's stated transformations | intermediate only |
| `COMMENT UPON` | exact but highly indirect anagram bag | explicitly rejected by user; ignores the paired `GANDER/HANDLE` construction | rejected |

The last observed website state showed only 3 of 20 attempts remaining and no enumeration; the remaining count after the latest rejection is not confirmed.

## Next action

从倒数第三行起反向审计每个输出是否由图面唯一决定，重点检查 `MEMBER / PIPKIN / TRANCE / SWEDEN` 是否只是被底部 `ANSWER` 反推出来的自洽词；在找到新的唯一顶层字符串前不再给提交候选。
