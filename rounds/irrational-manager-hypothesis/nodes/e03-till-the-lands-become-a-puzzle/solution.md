---
node_id: e03-till-the-lands-become-a-puzzle
title: 直到大地变成一块拼图
kind: puzzle
round: irrational-manager-hypothesis
parent:
source:
round_feeder: yes
feeders:
status: accepted
answer: PIRATES
confidence: high
summary: 用户于 2026-08-21 确认 PIRATES 为正确答案。61/64 种实收拼片可唯一排成 8×8 上海北外滩卫星图；读取 7 条横向行界的凸齿方向得到 8 位 ASCII 字符串 P1RaTe$，规范化为 PIRATES。通过后题面新增一张寻宝指令图，含坐标模板 `0??.?????, 1??.?????`、Captain Blackheart/Blackbeard、现代城市对应地点、东南角结构下方 cache 及带笔等信息；原图已保存，推测供后续 Meta 使用。
updated: 2026-08-21
---

# 直到大地变成一块拼图

## Current conclusion

答案 **PIRATES** 已由用户确认正确，状态为 **accepted**。

拼图先复原为 8×8；真正的提取材料不是地点名称，而是相邻两排拼片之间真凸齿属于上片还是下片。七条横向行界各有八个接缝，正好各组成一个 8-bit 字符，读出刻意混用大小写和 leetspeak 的 **`P1RaTe$`**，规范化即 **PIRATES**。题面称它为“藏宝图”，也直接呼应 pirates。

## Observations

- 客户端源图为 1120×1120，每片逻辑核心为 140×140，因此完整拼图固定为 **8×8，共 64 片**。
- 8 小时采集结束时共有 180 个领取实例、**61/64 种不同拼片**；缺少 `(5,0)`、`(4,4)`、`(6,6)` 三格。
- 61 片全部可唯一落位。55 片与同一张上海北外滩 Google 卫星图形成可靠单应匹配，网格中心 RMSE 为 **0.626 px**；地点证据用于确定排列，不是答案。
- 旧拼齿分类只检查核心方框外是否存在透明度像素。核心锚点有最多 5 px 误差，因此凹边旁的薄像素带曾被误判成“凸齿”，制造了不存在的“凸凸相撞”。
- 对 101 条两端拼片都已取得的内部接缝，较浅一侧最大只有 **5 px**，真凸齿一侧最小 **32 px**、最大 52 px，中间存在完全空白的 6–31 px 区间。以 12 px 为保守阈值时，每条接缝都恰好只有一侧是真凸齿。

## Assembly

`work/jigsaw_solve.py` 识别 140×140 核心、枚举四种旋转，并结合透明轮廓、图像接缝与参考卫星图定位。最终 61 片占位如下：

| y\x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | ✓ | ✓ | ✓ | ✓ | ✓ | 缺 | ✓ | ✓ |
| 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4 | ✓ | ✓ | ✓ | ✓ | 缺 | ✓ | ✓ | ✓ |
| 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 6 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 缺 | ✓ |
| 7 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

`work/visual/jigsaw/reference-assisted-layout-annotated.png` 是 61 张实收拼片的稳定复原图，红框标出三处缺格。参考图只补画背景以方便核验；拼片坐标和旋转均由实收片确定。

## Extraction

只看上下相邻两排之间的接缝。对行界 `y=0..6`，从左到右检查八个位置：

- 真凸齿属于下方拼片：记 `1`；
- 真凸齿属于上方拼片：记 `0`。

三张未取得拼片不妨碍判位：101 条双端已知接缝证明每条接缝恰有一个真凸齿；若缺片相邻的已知一侧是 32 px 以上的真凸齿，则缺片侧为凹，反之亦然。由此五个涉及缺片的横向位也都能唯一反推。

| 行界 | 8 位二进制 | 十六进制 | 字符 |
| ---: | --- | ---: | :---: |
| 0 | `01010000` | `50` | `P` |
| 1 | `00110001` | `31` | `1` |
| 2 | `01010010` | `52` | `R` |
| 3 | `01100001` | `61` | `a` |
| 4 | `01010100` | `54` | `T` |
| 5 | `01100101` | `65` | `e` |
| 6 | `00100100` | `24` | `$` |

因此原始提取为：

```text
01010000 00110001 01010010 01100001 01010100 01100101 00100100
P        1        R        a        T        e        $
```

`1 → I`、`$ → S`，忽略大小写后得到 **PIRATES**。这同时解释了题面的藏宝图意象。竖向列界没有产生文本，属于拼图结构而非本次从上到下逐行读取的字符行；这是未使用信息，但不影响横向七行给出的精确、主题一致字符串。

## Post-solve hidden information

### Observed facts

用户确认答案后，题面出现“本题隐藏的内容”，其下先写“咦这里怎么还有一张纸……？”，随后显示一张替代文字为 `Treasure Hunt Instructions` 的纸张图片。

- 图片顶部坐标模板为 **`0??.?????, 1??.?????`**：两项均为小数点前 3 位、小数点后 5 位，第一项以 `0` 开头，第二项以 `1` 开头。
- 指令第 1 条要求利用拼图中其余线索，确定 Captain Blackheart 的不义之财所在位置。
- 第 2 条说，若坐标正确，抵达的不是海船，而是现代城市中与 Blackbeard 多年前所在位置相同的地方；原图把 `City` 首字母大写，并提及海风、贪婪及其后果。
- 第 3 条说抵达后会立刻知道地点正确。
- 第 4 条说 cache 固定在**东南角（`SE corner`）某个结构的下方**；该结构被描述成 Blackbeard 可能曾坐着休息、抽烟斗之处。
- 第 5 条要求带一支笔。
- 原始图片尺寸为 1448×1086，SHA-256 为 `487257C5AE5295E54A849919E4CC76EB1A6EC62F3B3E7A213929684CD1680872`；来源为 <https://static.cipherpuzzles.com/static/images/e2f3cddeea5c401eaa7a6f3546810c25.webp>。

### Interpretation for later Meta work

这是一份通过本题后才出现的跨题/实地寻宝线索，而不是对 **PIRATES** 的再次提取。坐标模板和“利用拼图中其余线索”很可能要求把本题已定位的上海北外滩图像继续细化为经纬度；Captain Blackheart 与 Blackbeard 名称不一致、`City` 的异常大写、`SE corner`、结构下方和“带笔”均应在后续 Meta 中保持原样核查。当前 Node 只保存证据，不自行前往地点或操作 cache。

## Submission history

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-21 | 上海国际航运服务中心 | rejected | 用户明确指出该候选不对，并给出已解锁提示：“注意拼图碎片之间的拼接，并转成二进制，然后转成字符。”地点只负责确定拼片排列。 |
| 2026-08-21 | PIRATES | accepted | 用户明确确认答案正确；通过后题面新增寻宝指令图片，疑似供 Meta 使用。 |

## Evidence and artifacts

- 官方题面：<https://heptadec.cipherpuzzles.com/puzzle/till-the-lands-become-a-puzzle>
- `work/ccbc17-geo-results-1787278136986.json`：8 小时采集最终导出。
- `work/visual/pieces/`：61 个唯一原始 PNG。
- `work/visual/jigsaw/reference-grid-placements.tsv`：61 片的最终 8×8 坐标和旋转。
- `work/visual/jigsaw/reference-assisted-layout-annotated.png`：复原拼图及三处缺格。
- `work/visual/jigsaw/binary-lobe-depths.tsv`：112 条接缝两侧伸出深度及真凸齿判位。
- `work/visual/jigsaw/binary-final-extraction.tsv`：七条横向行界的最终位串、字节和字符。
- `work/visual/jigsaw/binary-final-extraction.png`：最终位表可视化。
- `work/binary_probe.py`：轮廓深度校正和二进制提取脚本。
- `artifacts/reference-assisted-layout-annotated.png`：候选所用复原拼图。
- `artifacts/binary-lobe-depths.tsv`、`binary-final-extraction.tsv`、`binary-final-extraction.png`：候选所用轮廓证据与提取表。
- `artifacts/treasure-hunt-instructions.webp`：通过 **PIRATES** 后新增的隐藏寻宝指令原图；由上列静态资源直接保存，供后续 Meta 原样核查。

## Important failed routes

- **地点不是答案。** 上海北外滩/上海国际航运服务中心的像素级定位可靠，但用户明确否定了地点候选；地点只用于排列拼片。
- **“凸凸相撞”是假象。** 旧分类器把 3–5 px 锚点误差当成凸齿，基于该表进行的接缝重叠、路径、Unicode 和单块属性读取全部是乱码。真实轮廓呈 0–5 px 与 32–52 px 两群，修正后每条接缝恰有一个真凸齿。
- **不需要遍历复杂路径。** 正确结构就是从上到下七条横向行界，每条八位；标准 ASCII 直接给出 `P1RaTe$`。

## Next action

本 Node 已完成。后续若分配相关 Meta，应读取 `artifacts/treasure-hunt-instructions.webp`，结合上海北外滩的拼图定位和坐标模板继续分析；本 Node 内不进行实地 cache 操作。
