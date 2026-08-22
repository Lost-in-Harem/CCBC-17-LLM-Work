---
node_id: e09-typing-lessons
title: 精删打字通
kind: puzzle
round: irrational-manager-hypothesis
parent: 
source: 
round_feeder: yes
feeders: 
status: accepted
answer: SEAHORSE
confidence: high
summary: 用户已确认 SEAHORSE 为正确答案；四关分别使用 QWERTY、Dvorak、Colemak、Workman 布局输入 Plover 速录和弦，隐藏句和服务器返回的原始键块给出 SE-AH-OR-SE。
updated: 2026-08-22
---

# 精删打字通

## Current conclusion

用户已确认正确答案是 **SEAHORSE**。

题面模拟的是 Plover/英文 stenotype 速录：一次同时按下的一组键是一个无序和弦（stroke），而不是逐字输入。四关使用同一套 Plover 词典，但把速录键盘依次映射到 QWERTY、Dvorak、Colemak、Workman 四种键盘布局。四关均已在网页中完成，用户随后明确确认最终答案正确。

## Observations

### 题面与交互事实

- 首页文案称这是“世界上最快的打字机器”，四关要求在限时内录入英文句子。
- 页面组件的键盘处理会收集同时按下的键，在按空格/回车或超时后把整组键作为一个 stroke 发送给 `/c17sp/typing`。
- 第一关中 QWERTY 的 `C+U` 被服务器识别为 Plover `AF`，输出 `after`。这确认了标准 Plover 的 QWERTY 模拟键位。
- 同一个 `AF` 在后续关卡分别需要 `J+G`、`C+L`、`M+F`，与 Dvorak、Colemak、Workman 在相同物理键位上的字符完全吻合。
- 四关风味文字也分别提示布局：
  - 第一关：“最简单，最直白，最不绕弯”——默认 QWERTY；
  - 第二关：“聆听十九世纪来自东欧的乐声”——捷克作曲家 Dvořák；
  - 第三关：“在广阔的天地下码字”——Colemak；
  - 第四关：“咱们是最有力量的群体”——Workman/工人群体。

### 四句隐藏信息

每关成功后完整显示的共同开头是：

> after typing this sentence correctly you can see the information you need during extraction …

其后的关卡专属信息为：

1. `to look at or consider a person or thing carefully in order to discover something about them` → **examine**。
2. `the abbreviated title referring to the older of two people in the same family who have the same name` → **Sr.**。
3. `the company that maintains the world's largest global crowd funding platform dedicated to creativity projects` → **Kickstarter**。
4. `a line from the song played during credits in the final episode of stranger things we blank heroes` → David Bowie 的 *Heroes* 中 **we can be heroes**，所以空格是 **can be**。Netflix 的官方说明确认该曲用于大结局片尾：https://www.netflix.com/tudum/articles/stranger-things-finale-end-credits

## Working hypotheses

- **已确认：速录和弦 + 四种键盘布局。** 四个布局都由同一 Plover stroke `AF` 的不同原始键映射直接验证，且四关均已完成。
- **已确认：隐藏信息要再次作为速录词条输入。** 在对应关卡训练模式中输入 `examine`、`Sr.`、`Kickstarter`、`can be` 的短写，服务器分别返回预期文本和原始按键。
- **最终块内次序：** stenotype 和弦本质上是无序键集合，因此同一 stroke 内的原始键没有语义先后；把四块按关卡顺序排列，并在块内选择构成自然答案的顺序，唯一显著结果是 `SE-AH-OR-SE`。

## Extraction

服务器在训练模式中直接返回了以下 `inputUnit`、`rawKeys` 和输出；这比外部 Plover 词典更权威：

| Level | Layout | 隐藏答案 | Plover stroke | 服务器 `rawKeys` | 答案块 |
| --- | --- | --- | --- | --- | --- |
| 1 | QWERTY | `examine` | `KP` | `SE` | `SE` |
| 2 | Dvorak | `Sr.` | `S-R` | `AH` | `AH` |
| 3 | Colemak | `Kickstarter` | `K-S` | `RO`（和弦无序） | `OR` |
| 4 | Workman | `can be` | `K` / `-B` | `S` / `E` | `SE` |

按关卡顺序得到：

```text
SE + AH + OR + SE = SEAHORSE
```

因此答案为 **SEAHORSE**。

## Answer audit

- **答案格式：** 8 个英文字母，符合全场允许英文答案的规则。
- **机制覆盖：** 使用了速录、四种布局、四条风味提示、四句隐藏信息和服务器返回的原始键；题目主要设计均得到解释。
- **独立检查：** 四个隐藏答案都在相应关卡训练模式中得到服务器确认；首页最终显示四关均“已完成”。
- **剩余歧义：** 第三关同一和弦的事件记录是 `RO`，而和弦没有按键先后；为形成自然答案需取为 `OR`。这是块内顺序歧义，不影响字母集合。四块唯一明显的英文答案是 `SEAHORSE`。
- **未使用信息：** 各关倒计时长度和确认速度滑杆只服务于交互难度，没有参与最终提取。

## Submission history

只记录用户或比赛网站明确反馈过的提交；不要把尚未提交的候选写进来。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-22 | SEAHORSE | correct | 用户明确确认答案正确。 |

## Evidence and artifacts

- 最终提取表：[`artifacts/extraction.tsv`](artifacts/extraction.tsv)。
- Plover 反查与 QWERTY 和弦转换脚本：[`artifacts/steno_lookup.py`](artifacts/steno_lookup.py)。
- 脚本示例（外部词典只用于候选 stroke 搜索；最终以网页服务器响应为准）：

  ```text
  python rounds/irrational-manager-hypothesis/nodes/e09-typing-lessons/artifacts/steno_lookup.py rounds/irrational-manager-hypothesis/nodes/e09-typing-lessons/work/plover-main-master.json examine Sr. Kickstarter can be
  ```

- Plover 主词典来源：https://raw.githubusercontent.com/openstenoproject/plover/master/plover/assets/main.json
- 动态题目组件的只读副本：[`work/visual/typing-lessons.vue`](work/visual/typing-lessons.vue)，来源：https://static.cipherpuzzles.com/static/images/76c2baa7765b4878b0748bdca83b29d2.vue
- SingleFile 输入的稳定资产清单：[`work/visual/inventory/manifest.json`](work/visual/inventory/manifest.json)。复现命令：

  ```text
  python .agents/skills/inspect-puzzle-visuals/scripts/visual_workbench.py inventory rounds/irrational-manager-hypothesis/nodes/e09-typing-lessons/input/精删打字通.html --output rounds/irrational-manager-hypothesis/nodes/e09-typing-lessons/work/visual/inventory
  ```

## Important failed routes

- 把普通单词的各字母依次按下、最后统一确认，会被视为一个大和弦；最初把 `AFTER` 当成五个普通字母输入因此失败。正确做法是每个 Plover stroke 单独确认。
- 第二至第四关不是 QWERTY。用 QWERTY 原始键会得到键名本身；分别切换为 Dvorak、Colemak、Workman 映射后才可通过。
- 当前 Plover `main.json` 含有一些服务器词典没有的较新/较短 brief（例如 `information` 的 `TP-FGS`）。挑战中必须以训练模式服务器实际接受的 stroke 为准；完成挑战时使用了服务器接受的替代 outline。
- `can` 单独只给 Workman 原始键 `S`；第四条线索的空格必须补完整短语 **can be**，第二个 stroke `-B` 才给出结尾 `E`。

## Next action

无需进一步解题；保留现有复现材料，等待本题作为 feeder 使用。
