---
node_id: e06-pinduoduo
title: 拼多多
kind: puzzle
round: irrational-manager-hypothesis
parent: 
source: 
round_feeder: yes
feeders: 
status: accepted
answer: FIREFOX
confidence: high
summary: 同一组 64 块拼片存在 FOX 与 FIRE 两个经网页 100% 校验、并获提交里程碑确认的目标图；两词组合为 FIREFOX，用户已确认这是正确答案。
updated: 2026-08-21
---

# 拼多多

## Current conclusion

- 第一幅完整图经网页自带拼图后端校验为 `100%`、反馈 `(3)`；用户提交 **FOX** 后获里程碑确认。
- 利用网页完成率反推出第二幅完整图，同样校验为 `100%`、反馈 `(4)`；用户提交 **FIRE** 后获里程碑确认。
- FOX 与 FIRE 的四个整体旋转已全部纳入排除集；另取 32 个随机完整合法布局，其网页分数每次都恰好等于最近的 FOX/FIRE 旋转布局，没有第三目标的信号。
- 两个里程碑词按唯一自然的英语复合词组成 **FIRE + FOX = FIREFOX**；用户已明确确认这是正确答案，状态为 `accepted`。

## Observed facts

- 本地题面 `input/拼多多.html` 是 SingleFile 快照；静态图片清单只含一个 80×80 头像，64 块拼片由动态组件载入。
- 在线题面显示“本题有中间答案验证”，交互说明为左键拖动、右键旋转，共 64 块。
- 组件源文件为 <https://static.cipherpuzzles.com/static/images/0ba96657f09d4b84ac89354193c15c76.vue>，其中嵌入 64 张透明背景的 256×256 PNG。
- 组件末尾另有一段 257 字符的连接编码；运行逻辑明确说明其余 256 字符按排序后文件名依次给出每块的 `U/R/D/L` 四边码。
- 在不旋转拼片时，每个方向的非平边码唯一，得到一幅固定布局；该图实际是 **FOX**，不是最初误认的“小熊猫”。
- 允许旋转后，64 块恰好分成 16 个循环接口组，每组 4 块且分别对应四个相位；因此存在大量接口合法但图像不连贯的排列。
- FOX 布局的网页返回为 `completionRate: 100, feedback: "(3)"`；FIRE 布局返回为 `completionRate: 100, feedback: "(4)"`。
- 用户明确报告 FOX 与 FIRE 两次提交均为里程碑。

## Interpretation

- 标题“拼多多”指向同一组拼片的多个完整图，而非只找任意一个接口解。
- 两个图名本身就是最终提取材料；英语中自然且顺序唯一的组合是 `FIREFOX`，同时解释为什么 FOX、FIRE 各自只给里程碑而不结束题目。
- 32 次已知目标排除采样不是数学上的目标数完备证明；两个里程碑组成著名单词的提取现已由正确答案确认。

## Extraction

连接码的字母表为：

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_
```

首字符为 `c`，在字母表中的索引是 28。对后续字符 `x`，边码为：

```text
edge_code = alphabet.index(x) - 28
```

每块依次读取 `U/R/D/L`。平边为 0；左右相邻要求 `right(A) + left(B) = 0`，上下相邻要求 `bottom(A) + top(B) = 0`。从唯一的 `top=0,left=0` 角块开始遍历，得到稳定编号网格：

```text
36 54 05 64 48 49 11 04
34 42 52 24 14 10 61 63
44 27 29 57 18 38 07 40
51 28 37 08 32 15 20 56
46 59 09 35 25 58 60 06
45 43 03 41 19 53 13 22
17 12 55 23 50 16 31 01
62 02 47 21 39 33 30 26
```

64 块恰好各使用一次，四周均为平边。渲染后再用网页自身的拼图后端校验该完整布局，得到 100% 与反馈 `(3)`。

### 旋转组与第二幅图

把拼片的四边码记为循环四元组 `c=(U,R,D,L)`，定义：

```text
canonical(c) = min(rotation_0(c), rotation_90(c), rotation_180(c), rotation_270(c))
```

按 `canonical(c)` 分组后恰有 16 组，每组 4 块。每个组占固定边码网格中的 4 个位置；在组内任选一个四元排列，并把每块旋到目标位置的相位，接口仍全部吻合。因此完整合法布局空间至少含 `24^16` 个元素，普通顺序枚举只会反复得到 FOX 附近的局部变体。

网页返回的完成率可作为隐藏目标的逐片匹配信号：

- FOX 精确布局为 100%；只交换两个兼容角块后为 96%，符合 62/64 个状态匹配后向下取整。
- 一个随机合法布局为 34%，说明服务器在多个隐藏目标中取最近者。
- 在 16 个随机布局中找到一例：服务器判定 24 个状态吻合，但它与 FOX 任一整体旋转最多只吻合 17 个；多出的 7 个状态证明命中了另一个目标的吸引域。

对每个四片组使用以下 5 个排列探针，其“吻合数相对第一探针的差向量”能唯一标识全部 24 个未知排列：

```text
0123  0132  0213  0231  0312
```

这直接解出 15 组；第 13 组因最近目标在探测时切换而不稳定，固定其余 60 块后枚举该组 24 种排列，在第 17 种 `[2,3,0,1]` 达到 100%，反馈 `(4)`。渲染图经用户辨认为 **FIRE**，提交后获里程碑。

### 最终组合

将第二里程碑放在第一里程碑之前，得到唯一常见复合词：

```text
FIRE + FOX = FIREFOX
```

## Accepted answer audit

- **可复现性**：两幅图都有精确的 64 块行列、旋转表和网页 100% 校验结果；FIRE 的 16 组排列及完成率探针过程已保存。
- **答案格式**：题面未明示最终长度；`FIREFOX` 为 7 个英文字母，且由两个已确认里程碑无损组合。
- **主设计解释**：接口的 16×4 循环复用产生“同片多拼”，两个清晰目标给出词块，标题与最终复合词均得到解释。
- **未用信息或矛盾**：厚涂画面的细节不参与字母提取；大量接口合法的杂乱图只是组合自由度。未发现与 `FIREFOX` 冲突的明确反馈。第三目标采样是负证据而非穷尽证明。

## Submission history

只记录用户或比赛网站明确反馈过的提交；不要把尚未提交的候选写进来。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-21 | FOX | milestone | 用户确认网站判定为里程碑；`(3)` 表示三个字母，并指出同一组拼片还能拼出其他图案。 |
| 2026-08-21 | FIRE | milestone | 用户确认第二个 100% 布局对应 `FIRE`，提交后网站判定为里程碑；布局反馈为 `(4)`。 |
| 2026-08-21 | FIREFOX | accepted | 用户明确确认 `FIREFOX` 是正确答案。 |

## Evidence and artifacts

- `artifacts/assembled.png`、`artifacts/layout.tsv`、`artifacts/validation.json`：FOX 的完成图、布局和网页 100%/`(3)` 校验。
- `artifacts/assembled_grid.png`、`artifacts/assembled_thumb.png`：FOX 的稳定编号网格与低频辨认图。
- `artifacts/rotation_groups.tsv`：16 个循环接口组及每块相位。
- `artifacts/fire_assembled.png`、`artifacts/fire_orientation_sheet.png`：FIRE 的精确布局图与四向总览。
- `artifacts/fire_layout.tsv`、`artifacts/fire_group_permutations.tsv`、`artifacts/fire_permutations.json`：FIRE 的逐片布局和 16 组排列。
- `artifacts/fire_validation.json`：FIRE 的网页 100%/`(4)` 校验。
- `artifacts/oracle_reconstruction.json`：完成率标定、5 探针码本、组排列和最后一组的有限枚举结果。
- `artifacts/known_target_sampling.json`：排除 FOX/FIRE 八个旋转目标后的 32 次第三目标采样摘要。
- `artifacts/solve_jigsaw.py`：提取、解码、分组、枚举和渲染脚本。复现命令：

```text
python artifacts/solve_jigsaw.py --source work/visual/puzzle-source.vue --output-dir work/visual --mode solve
python artifacts/solve_jigsaw.py --source work/visual/puzzle-source.vue --output-dir work/visual --mode render-permutation --permutation-file artifacts/fire_permutations.json
```

## Important failed routes

- 仅扫描本地 SingleFile 的普通图片资源只能得到头像，无法得到动态生成的拼片；需要读取在线组件源文件。
- 单靠透明轮廓拟合会产生多个近似形状配对；组件内置的有符号边码给出了严格且唯一的邻接，应优先使用。
- 最初把 FOX 厚涂图误认成“小熊猫”；用户明确提交 FOX 获里程碑后已纠正，不再沿用该候选。
- “固定朝向下唯一”不等于题目唯一：允许旋转后出现 16 个四片循环组。
- 通用 Z3 整数/数组模型在 60 秒内超时且未出解；专用行优先回溯很快找到解，但前 32 个只是在 FOX 周围做局部等价交换。
- 让 16 组统一偏移一个相位只会得到 FOX 的整体旋转，并非新图。
- 排除 FOX/FIRE 四向后抽取 32 个合法布局，没有一次出现第三目标分数增益；停止继续无界采样。

## Next action

答案 **FIREFOX** 已确认，节点完成；当前没有待办。
