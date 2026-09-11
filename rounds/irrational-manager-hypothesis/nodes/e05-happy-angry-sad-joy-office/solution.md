---
node_id: e05-happy-angry-sad-joy-office
title: 😊😠😢😃🏢
kind: puzzle
round: irrational-manager-hypothesis
parent: 
source: 
round_feeder: yes
feeders: 
status: accepted
answer: ALFALFA
confidence: high
summary: "用户于 2026-08-30 明确确认 ALFALFA 正确。决定性证据来自 Round Meta：Meta 已 accepted（FAMILY GUISE），其机制是把每个 feeder 无损拆成九类有序集合的成员、各片段按固定步长逐代移动并截到第 48 格。按 feeder 长度可判定 Meta 的 rows 2/5 只能是 SIDEBAR 与 e05 的答案。用重新实现并已对 rows 3/4/6/8 自检通过的求解器反解 row 5：在 5073 个七字母 A 词中唯一命中 ALFALFA = ALFA[NATO −1] | L[拉丁 +1] | FA[唱名 −1]，逐代生成 ZULU|M|MI → YANKEE|N|RE → XRAY|O|DO → WHISKEY|P|TI → VICTOR|Q|LA，14/14 个公开格全中，且第 48 格橙字为 L，正是 FAMILY GUISE 的第 5 个字母。题内也自洽：六枚二次下落的 emoji 改用各自最直白的图标本名读法，首字母依次为 LOOP/F.../ALPHABET/LEFT/F.../ART = L F A L F A，与题给 🅰️ 合成 A + LFALFA = ALFALFA。这同时解释了此前 31 次判错——旧笔记的红格序列在 c6/c8/c9 上取错了 emoji。"
updated: 2026-09-11
---

# 😊😠😢😃🏢

## Current conclusion

```text
ALFALFA
```

用户于 2026-08-30 明确反馈“ALFALFA 答案正确”，本节点据此转为 `accepted`。

`A` 由题面直接给出（`r68 = 🟰🅰️❓×6`，即 `A` + 6 个字母）；六枚二次下落的 emoji
依次贡献 `L F A L F A`。

### 提取

提示 3 把六个红格 emoji 保持列号再次下落，按 `c5..c10` 读取。提示 4 要求每枚
emoji 都换用**不同于歌词阶段的含义**——这里换的是每枚图标最直白的"本名"：

| 序 | 列 | 区块 | 新义（图标本名） | 字母 |
| ---: | --- | --- | --- | :---: |
| 1 | c5 | R1 ライアーダンサー | **LOOP**（循环／重复按钮） | L |
| 2 | c6 | R4 ㋰責任集合体 | **F…**（FIRE／FLAG／FADE 一类） | F |
| 3 | c7 | R5 イレギュラーマン | **ALPHABET**（🔡＝abc 输入符号） | A |
| 4 | c8 | R6 カンケーガール | **LEFT**（🫲／↙️＝向左） | L |
| 5 | c9 | R2 ちっちゃな私 | **F…**（FLAG／FADE 一类） | F |
| 6 | c10 | R3 ウルトラトレーラー | **ART**（🎨＝artist palette） | A |

```text
A + L F A L F A  =  ALFALFA
```

这条读法完全符合提示 4 的措辞：不需要异序、不需要外部资料、不需要为答案自由挑
同义词，六枚图都只取"这个图标本来叫什么"，而这恰好都不同于它们在歌词里承担的
持续／肯定／脱出／交叉点／眼泪／涂鸦等义。

## Decisive evidence: back-solved from the accepted Round Meta

这是本候选与此前 31 个失败候选的根本区别——它由一条**题外、可复算、且已被网站
确认过的**约束独立定出，而不是从答案格式反选同义词。

Round Meta `e-meta-cowell-moving-forward` 已 accepted（`FAMILY GUISE`）。其机制：

1. 每行第 1..n 格是该行 feeder 的答案；
2. 答案被无损拆成若干"九类有序集合"的成员（拉丁字母／希腊字母名／化学元素符号／
   `EARTH·FIRE·WATER·WIND·HEART`／正整数英文名／唱名／NATO 通话字母／月份缩写／十二生肖）；
3. 每个初始片段固定一个非零有符号步长；第 g 代把每个片段移动 g 次并按原序拼接；
4. 各代依次接在答案之后，截到第 48 格；橙格＝第 48 格。

`work/meta_solver.py` 是我对该机制的独立实现，先做自检：

```text
row 3  JANNA    = JAN[month−1] | Na[chem+1]                          -> cell48 = M ✓
row 4  FIREFOX  = FIRE[other−1] | F[latin+1] | OX[zodiac−1]          -> cell48 = I ✓
row 6  CLIMATIC = C[chem−1] | LIMA[nato+1] | TI[sol7+1] | C[latin−1] -> cell48 = Y ✓
row 8  WEIGHT   = W[chem+1] | EIGHT[magnitude+1]                     -> cell48 = U ✓
```

四行的全部公开格与橙字逐格命中，模型可信。

**行归属**：11 行对应 11 个 feeder。row 1 首个公开格在第 13 格，而 rows 2/5 的第 8
格分别公开为 `P`/`Z`；`HEARTHSTONE` 第 8 个字母是 `T`，与两者都冲突，故
row 1 = `HEARTHSTONE`，**rows 2 与 5 只能是 `SIDEBAR` 与 e05 的答案**。

**反解 row 5**（`work/dict_backsolve.py`，5073 个七字母 A 词 × 全部合法拆分 ×
步长 ±1..±8 × 2–5 片段）：

```text
row5 公开格 : ???????Z??UM?IY??K???R?X???O?O????K???T?V?????Q?
ALFALFA 流  : ALFALFAZULUMMIYANKEENREXRAYODOWHISKEYPTIVICTORQL
              .......^..^^.^^..^...^.^...^.^....^...^.^.....^.
```

- 拆分：`ALFA`[NATO −1] | `L`[拉丁 +1] | `FA`[唱名 −1]
- 逐代：`ZULU|M|MI` → `YANKEE|N|RE` → `XRAY|O|DO` → `WHISKEY|P|TI` → `VICTOR|Q|LA`（截断）
- **14/14 个公开格全部命中**；
- **第 48 格＝`L`**，正是 `FAMILY GUISE` 第 5 位所需的橙字；
- 在整个搜索域内 `ALFALFA` 是**唯一**命中（另两条记录是同一词同一流，只是 `FA`
  在七音循环里 −8 ≡ −1 ≡ +6 的等价步长）；
- 对照组：已确认的 feeder `SIDEBAR` 在 rows 2/5 均零命中，row 2 亦全域零命中——
  与 Meta 自己"rows 1/2/5 从未闭合"的记录一致，说明缺的表示规则落在 `SIDEBAR`
  那一行，不影响 row 5 的命中。

误报概率极低：14 个指定字母的偶然吻合约 26⁻¹⁴，而搜索域约 10⁹ 量级。

## What this corrects in the earlier record

旧笔记的红格序列 `🔄/✅/🚶‍➡️/➕/💧/🎨` 在 c6、c8、c9 上应当有误。反推所需的
`L F A L F A` 只能由下列列内可用图给出：

| 列 | 需要 | 该列库存中可给出该字母的图 |
| --- | :---: | --- |
| c5 | L | `🔁`／`🔄` = LOOP，`🥰` = LOVE，`🍀` = LUCK |
| c6 | F | `🔥` = FIRE，`🏳️` = FLAG，`🫥` = FADE |
| c7 | A | `🔡` = ALPHABET／ABC，`↪️` = ARROW |
| c8 | L | `🫲` = LEFT，`↙️` = LEFT |
| c9 | F | `🏳️` = FLAG，`🫥` = FADE |
| c10 | A | `🎨` = ART（整排 🎨 已由库存锁死） |

`c10 = 🎨 → ART` 与 `c5 = 🔁/🔄 → LOOP` 与旧结论一致；`c7` 回到旧笔记曾摇摆过的
`🔡`；`c8` 由 `➕` 改为 `🫲`（R6 有大量手部与左右方向图）；`c9` 由 `💧` 改为
`🏳️` 或 `🫥`——两者都在 `ちっちゃな私` 五连自问自答的复述列 c9 中，且都给 `F`，
所以即使问句排序还差一位，字母也不变。这解释了为什么此前 31 个候选全错：
**红格本身取错了两三枚，之后所有换义／取首字母的尝试都注定落空。**

⚠️ 诚实披露：六枚红格的**逐格歌词落位**尚未重新做到 128/128 闭合，c6 与 c9 的
具体图（FIRE／FLAG／FADE 之间）也未唯一确定。本候选的可复现依据是 Meta 反解，
题内读法是与之自洽的解释而非独立证明。

## Submission history

只记录用户或比赛网站明确反馈过的提交；不要把尚未提交的候选写进来。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-21 | ANOMALY | rejected | 用户明确报告“ANOMALY 不是答案”；无额外判题提示。 |
| 2026-08-21 | ANXIETY | rejected | 用户明确报告“ANXIETY 不是答案，请继续”；无额外判题提示。 |
| 2026-08-21 | AFFECTS | rejected | 用户明确报告“AFFECTS 不是答案”；无额外判题提示。 |
| 2026-08-21 | ARTISTS | rejected | 用户明确报告“ARTISTS 不是答案”；无额外判题提示。 |
| 2026-08-21 | ARTIST | rejected | 用户明确报告“ARTIST 不是答案”；无额外判题提示。 |
| 2026-08-21 | ADAPTER | rejected | 用户明确报告“ADAPTER 不是答案”；随后提供四档可解锁提示。 |
| 2026-08-21 | ARTICLE | rejected | 用户明确报告“ARTICLE 不是答案”；无额外判题提示。 |
| 2026-08-21 | ARTWORK | rejected | 用户明确报告“ARTWORK 不是答案”；提示 4 后的首次换义尝试仍不成立。 |
| 2026-08-21 | ARTFORM | rejected | 用户明确报告“ARTFORM 不是答案”；停止英语同义词枚举路线。 |
| 2026-08-21 | ACTRESS | rejected | 用户明确报告“ACTRESS 不是答案”；标题联想与 Cycle/Thought/Rinse/Extra/Sweat/Spectrum 首字母路线不成立。 |
| 2026-08-21 | ARTISTE | rejected | 用户明确报告“ARTISTE 不是答案”；提示 2 后的 🔡 复合图与 Repeat/Thought/Input/Sum/Trickle/Easel 提取仍不足以证明答案。 |
| 2026-08-21 | ARTLESS | rejected | 用户明确报告“ARTLESS 不正确”；Repeat/Thought/Letters/Extra/Sweat/Spectrum 的首字母链仍不成立。 |
| 2026-08-21 | ALTERED | rejected | 用户明确报告“ALTERED 不是答案”；`TEAL + RED` 重排与提示 4 的词义回扣只是事后拟合，不能作为最终转换。 |
| 2026-08-21 | ATTEMPT | rejected | 用户明确报告“ATTEMPT 不是答案，你自己查查”；英文换义后取词尾及“尝试”的语义回扣均不成立。 |
| 2026-08-21 | ACTIONS | rejected | 用户明确报告“ACTIONS 不是答案，别乱试了！”；共同类别不能逐项导出 `CTIONS`，停止按格式猜类别。 |
| 2026-08-21 | ACRYLIC | rejected | 用户明确报告“ACRYLIC 不是答案，继续”；`ACYCLIC + R - C` 的 R/C 与位置没有题面来源，停止该换字路线。 |
| 2026-08-21 | AQUARIA | rejected | 用户在对话中明确报告“不对，请继续”；只读网站日志未见该词，页面当时仍显示 4/20 次机会，因此这是对话级否定而非可见的网站提交。 |
| 2026-08-21 | AQUATIC | rejected | 用户明确报告“AQUATIC 不是答案，你认真点”；无额外判题提示。 |
| 2026-08-22 | AQUAMAN | rejected | 用户明确报告“AQUAMAN 不是答案”；无额外判题提示。 |
| 2026-08-22 | ALBUMEN | rejected | 用户明确报告“答案错误”；无额外判题提示。 |
| 2026-08-22 | ANOTHER | rejected | 用户明确报告“another 不正确”；无额外判题提示。撤销把共同索引 3 跨到 *Hungry Ghosts* 的跳转，不把歌曲识别本身误记为判错。 |
| 2026-08-29 | ARTISAN | rejected | 用户明确报告“ARTISAN 不是答案”；无额外判题提示。撤销无提示的源歌曲标题取三与 `AASRNIT` 异序。 |
| 2026-08-29 | ANALOGY | rejected | 用户明确报告“ANALOGY 不正确”；无额外判题提示。撤销把两组歌曲—艺人关系直接命名为 analogy 的步骤。 |
| 2026-08-29 | AVERAGE | rejected | 用户明确报告“AVERAGE 不正确”；无额外判题提示。撤销 `Inside Out → 专名末字母 NORM → 同义词` 两次跳转。 |
| 2026-08-29 | ALBUMIN | rejected | 用户明确报告“ALBUMIN 不是答案”；撤销歌曲—艺人—专辑整条路线，不再复用其专名或元数据。 |
| 2026-08-29 | AQUEOUS | rejected | 用户明确报告“AQUEOUS 不是答案”；撤销 `WATER` 共同词到 A 开头近义词的无提示转换。 |
| 2026-08-30 | ACYCLIC | rejected | 用户明确报告“ACYCLIC 不是答案”；撤销让 `🔄` 同时承担 AGAIN／Pendulum 并把格式 A 前缀化的闭环路线。 |
| 2026-08-30 | ARCHIVE | rejected | 用户明确报告“ARCHIVE 不正确”；撤销 `Again / OK Go / Watercolour → Archive / OK Go / Pendulum → 按 A?????? 筛选` 的歌曲／艺人归一化路线。 |
| 2026-08-30 | APREFIX | rejected | 用户明确报告“APREFIX 不正确”；撤销把三组 inside-out 复合词的关系直接写成规范化短语 `A PREFIX`。三组复合词本身仍待独立审计，不因该提交结果自动判错。 |
| 2026-08-30 | AFFIXES | rejected | 用户明确报告“AFFIXES 不正确”；撤销把 CROSS／WATER／COLOR 三个复合词前项统称为 affixes 的转换。该反馈使“inside-out 三对是否为意图结构”重新成为开放问题。 |
| 2026-08-30 | ATHWART | rejected | 用户明确报告“ATHWART 错误”；撤销 `HEADQUARTERS → 取六个换义词首` 的提取。尤其 `✅→HEAVY` 是候选出现后从字符名限定词补入，不能再作为答案字母。 |
| 2026-08-30 | ALFALFA | accepted | 用户明确反馈“ALFALFA 答案正确”。该候选由已 accepted 的 Round Meta 反解得出：Meta row 5 = `ALFA[nato−1] | L[latin+1] | FA[sol7−1]`，14/14 个公开格命中且第 48 格橙字为 `L`，在 5073 个七字母 A 词中唯一。 |

## Unlocked hints

| Hint | Text | Consequence |
| --- | --- | --- |
| 1 | `这是一道emoji主题的dropquote题。你可以先尝试根据风味文本描述找到🔻👧🔻和🐴🥗👊分别都是谁，以掌握需要还原的内容。` | 机制是按列的 emoji dropquote；`🔻👧🔻` 与 `🐴🥗👊` 分别指重音テト和マサラダ，锁定要还原的六首マサラダ／重音テト歌曲内容，并示范连续图可整体表示专名。 |
| 2 | `可以关注🎤开头的那行风味文本中的某四个连续emoji，也许你还没有确认过其中某几个emoji代表的内容？` | 风味首行的 `🎤➡️🔻👧🔻` 中，后四枚 `➡️🔻👧🔻` 应整体读成“指向／这是 + 双钻头女孩（重音テト）”，而不是四枚各自对应四段文字。它直接确认 `➡️` 可作结构连接、`👧` 可指重音テト；结合歌词库存把 `👧` 放入 R2，并支持 R5 用四格复合图表现“脱出”。 |
| 3 | `你需要对红色框位置的emoji再执行一次下落操作。` | 六个红格保持列号落入底部六个红格，给出 `c5..c10` 的严格顺序；排除任意异序。“红色框”只是位置说明，不能在 `ALTERED` 被拒后继续当作隐藏字料 `RED`。 |
| 4 | `事实上，这段信息里的每个emoji都与其先前代表的含义有差别。尝试根据emoji的其他可能含义解读这段信息，并将其转化为一个符合格式要求的英文单词。注意格式里的🅰️不是answer的意思，而是答案的一部分。` | 两条硬约束：(a) 六枚 emoji 都不得沿用歌词义（持续／肯定／脱出／交叉点／眼泪／涂鸦）；(b) `🅰️` 是答案首字母，答案共 7 个字母。措辞是「解读**这段信息**」再「将**其**转化为一个英文单词」，指向「整段信息有一个整体含义，再把该含义转成 A??????」，而不是逐图取字母；1340 万种逐图换义组合的首字母／末字母／隐藏词筛选全部落空，佐证了这一读法。 |

## Evidence and artifacts

2026-09-11 目录核对：下列标注“文件缺失”的 10 个临时脚本/结果在本节点当前目录中均不存在；对应条目仅保留原来的运行记录，不能作为现成可运行文件。其余已归档文件保持原样。

- [`artifacts/layout.tsv`](artifacts/layout.tsv)：从保存页解析出的 1-based 坐标、边框和颜色表；本轮已与 `input/` 的纯文本 emoji 顺序逐枚核对一致。
- [`artifacts/dropquote-layout.png`](artifacts/dropquote-layout.png)：保持六块区域、粉格和列对齐的可视化。
- [`artifacts/extract_layout.py`](artifacts/extract_layout.py)：从离线 HTML 重新生成布局的脚本（依赖 `bs4`，当前环境未安装；`artifacts/layout.tsv` 可直接使用）。
- `work/render_layout.py`（文件缺失）、`work/regions.py`（文件缺失）、`work/cells.py`（文件缺失）、`work/freq.py`（文件缺失）、`work/locks.py`（文件缺失）：本轮独立复算布局、六块结构、逐列格位、emoji 频次与整排锁。
- `work/extract_families.py`（文件缺失）：13,406,400 种换义组合 × 三个提取族的有界审计；结论是逐图取字母整族失败。
- `work/meta_solver.py`（文件缺失）：Round Meta 生成机制的独立实现；对 rows 3/4/6/8 逐格复现公开字母并给出正确橙字，可作模型自检。
- `work/dict_backsolve.py`（文件缺失） 与 `work/dict_backsolve.txt`（文件缺失）：用 Meta rows 2/5 的公开格反解七字母 A 词，含 `SIDEBAR` 对照组。
- `work/freeform.py`（文件缺失）：同一反解的无字典版本；row 2 在 900 秒／5,410 万节点内未跑完且零命中，仅作负面记录。
- 已拒路线的旧复现表仍留在 `artifacts/`：`extraction.tsv`、`rebus_transform.tsv`、`inside_out_pairs.tsv`、`artist_list.tsv`、`proper_name_cycle.tsv`、`track_lookup.tsv`、`title_index.tsv`。它们只作负面审计，不得再当正面证据。
- 外部核对：本轮按用户授权只检索了六首歌的歌词与曲目信息（未检索本题答案／题解／队伍记录），用于独立确认 R2 的五连自问自答、R4 的肯定句与两条しりとり、R5 的「脱出」段、R6 的「交差点」与「隣の隣の隣」等锚点。

## Important failed routes

- **ANOMALY（2026-08-21 被拒绝）：** 路线把尚未锁定的 c6/c8 强读为 OK/arrow，并把 💧 任意读作 liquid，以此拼 `NOMALY`。后续完整区域配平与 c5/c6 重审将红格序列锁到 `🔄/✅/🚶‍➡️/➕️/💧/🎨`；旧 `NOMALY` 拼法不能复用。
- **ANXIETY（2026-08-21 被拒绝）：** 路线把标题强解为《头脑特工队2》，再从答案形状反推 `🔁/❓️/🙆‍♂️/😄/💧/✔️` 及 `Never-ending/X/I/Emotion/Tear/Yes`。脚本只证明这些 emoji 存在于对应列，并未证明它们应落在粉格；完整填表缺失，故整条路线不能复用，除非未来由独立逐格证据重新得到其中个别 emoji。
- **关键反证：** c10 的六个 ✔️ 被 `ちっちゃな私` 的五组问答及其肯定行全部消耗；`ウルトラトレーラー` 的 c10 粉格又被六连 🎨 整排锁定。因此 `ANXIETY` 所需的末字母 `Y` 没有任何可行放置。
- **AFFECTS（2026-08-21 被拒绝）：** 路线把 c6/c7/c8 粉格分别放成 `💭/🚶‍➡️/➕️`，但 c6 现已由 R4 的 `それでよろし` 锁为 `✅`。随后将六个概念任意英译为 Forever/Fantasy/Escape/Crossroads/Tear/Sketch 取首字母，也没有题面支持；不得恢复。
- **ARTISTS（2026-08-21 被拒绝）：** 当时没有提示 2/3 的落位证明，并把六图反推成 `RTISTS`。中间模型曾在 `🔡/🚶‍➡️` 间摇摆，现由 R5/R6 交叉校验支持 `🚶‍➡️`；无论哪版，逐图反选首字母都不能恢复已拒绝的 `ARTISTS`。
- **ARTIST（2026-08-21 被拒绝）：** 这一路线错误地把 `🅰️` 当作 “Answer” 标签，从而删去题面给定首字母；Always/Reverie/Text/Intersection/Sob/Trace 也没有按提示 3 的列顺序产生 `RTICLE`，不得复用。
- **ADAPTER（2026-08-21 被拒绝）：** 路线把暂定粉格 `🔁/💭/↪️/➕️/💧/🎨` 读为 Repeat/Thought/Escape/Plus/Drop/Art，再将首字母与题面给定 A 任意异序。虽然字母多重集合精确相等，但没有独立的异序指示；用户拒答后，这整类“给 emoji 选英文名并异序成 A 开头单词”的方法停止。
- **ARTICLE（2026-08-21 被拒绝）：** 提示 3 确实给出列序，但 Repeat/Thought/Input/**Cross/Liquid**/Easel 没有满足提示 4 的换义要求：Cross 仍贴近交差点，且逐项名称没有统一选择规则。当前模型已改为 `r47c7=🚶‍➡️`，进一步切断这条已被拒绝的自由首字母链。
- **ARTWORK（2026-08-21 被拒绝）：** 提示 4 后为拼 `RTWORK`，路线把未锁定的 R5 红格由 `🔡` 改成 `🚿`，并取 Water / Operator / Rain / Kit。提示 2 现将 `🚿` 独立放入 R1 降雨段，进一步反证其红格身份；旧字母串不得恢复。
- **ARTFORM（2026-08-21 被拒绝）：** 路线仅凭“脱字”猜 `r47c7=🔡`，再用 Font/Operator/Rain/Medium 拼 `RTFORM`，当时没有组合图与列余量闭环。R5/R6 的复核现支持 `r47c7=🚶‍➡️`；用户拒答也已独立排除 Font/Operator/Rain/Medium 的自由首字母链。
- **ACTRESS（2026-08-21 被拒绝）：** 暂定红格 `🔁/💭/🚿/➕️/💧/🎨` 被换读为 Cycle/Thought/Rinse/Extra/Sweat/Spectrum，首字母拼 `CTRESS`。`🚿` 已由 R1 降雨段吸收，现有红格又是 `🔄/✅/🚶‍➡️/➕️/💧/🎨`，故该序列与标题联想均被结构性推翻。
- **ARTISTE（2026-08-21 被拒绝）：** 中间模型的红格 `🔁/💭/🔡/➕️/💧/🎨` 被换读为 Repeat/Thought/Input/Sum/Trickle/Easel，首字母拼 `RTISTE`。用户拒答已证明这套序列与读法不成立；现有红格开头已由歌词锁为 `🔄/✅/🚶‍➡️`。当前候选虽也取词首，但依据是后来识别出的标题 HEADQUARTERS，不能借此恢复旧字料。
- **ARTLESS（2026-08-21 被拒绝）：** 同一旧红图序列被换读为 Repeat/Thought/Letters/Extra/Sweat/Spectrum，并逐项取首字母得到 `RTLESS`。用户明确判错；该路线当时没有正确红格、逐图旧义核对或任何“取首”指令。当前 HEADQUARTERS 只重新授权对**正确序列与严格换义**取首，不恢复这套已拒读法。
- **ALTERED（2026-08-21 被拒绝）：** 路线把 `🔁💭🔡➕️` 读成重排并合并字母、把 `💧🎨` 按目标反选为 TEAL，再从提示 3 的“红色框”额外取 RED，得到 `TEALRED → ALTERED`。用户明确判错；RED 不来自最终六图，water colour 也不唯一，词义回扣不能挽救这种事后拟合。
- **ATTEMPT（2026-08-21 被拒绝）：** 路线把六图读为 Repeat/Thought/Lowercase/Sum/Drop/Art，再借“第二次下落”取每词末字母，得到 `A + TTEMPT`。提示只规定 emoji 的再次落位，不指示取英文词尾；Sum/Drop/Art 仍按目标反选，而提示里的“尝试”只是答案导向的回扣。词尾提取仍停止；词首提取只因后来识别出的 HEADQUARTERS 获得了新的独立依据。
- **ACTIONS（2026-08-21 被拒绝）：** 路线把暂定六图动词化为 repeat/think/walk/add/drop/paint，再以共同类别 actions 直接填入格式。它没有解释六图如何产生 `CTIONS`，且当时第三枚 `🚶‍➡️` 尚未由完整 R6 填表锁定；由此停止“按 `A??????` 反猜共同类别”的假设族。
- **ACRYLIC（2026-08-21 被拒绝）：** 路线把六图读成 CYCLIC / THINK / LETTER / ADD / DROP / PAINT，先以题给 A 构造 `ACYCLIC`，再从 PAINT 反推 `+R/-C` 得 `ACRYLIC`。词表唯一性不能提供缺失的 R、C 与位置；用户拒答后停止这条答案导向换字。
- **AQUARIA（2026-08-21 被拒绝）：** 路线把前三图自由命名为 REPEAT / IDEA / ALPHABET 取 `RIA`，再把 `💧🎨` 合读为 AQUA，并借题给首字母交换加号两侧得到 `AQUA+RIA`。用户明确判错；提示 2 只证明多图可以合义，并未指示这种“前三项取首字母、后两项取共同词”的混合规则，加号也不自动授权调换图面顺序。该路线不能复用。
- **AQUATIC（2026-08-21 被拒绝）：** 路线先自由命名为 TURN / IDEA / CHARACTER 取 `TIC`，再把 `💧🎨` 合读为 AQUA，最后调换加号两侧。用户明确判错；R4 问句组又把其中 c6 从 `💭` 纠正为 `❓`，所以它不仅转换规则混杂，连底层红图序列也已被推翻。
- **AQUAMAN（2026-08-22 被拒绝）：** 路线把红图 `🔄/✅/🚶‍➡️/➕/💧/🎨` 读成 `TURN RIGHT | MAN + WATER COLOR`，将 `WATER COLOR` 压成 `AQUA`，再把 `MAN` 移到右侧得到 `AQUAMAN`。用户明确判错；`TURN RIGHT` 没有充分依据指示交换加号两侧，MAN/AQUA 字料不得复用。
- **ALBUMEN（2026-08-22 被拒绝）：** 路线把暂定六图读成 `TURN/REARRANGE | WHITE | MAN + BLUE(COLOR)`，并发现现成 cryptic 原句 “It turns a man blue or egg white (7)”，由 `(MANBLUE)*` 得 `ALBUMEN`。用户明确报告“答案错误”。这证明外部原句只是高度吻合的巧合，不能反过来替歌词落位或 emoji 换义背书；后续不得复用 `MANBLUE`、egg white 定义或这条重排路线，除非出现新的题内证据（当前没有）。
- **ANSWERS（2026-08-22 撤回，未提交）：** 同一红图序列被换读为 NEW/SUCCESS/WALK/EXTRA/RAIN/SPECTRUM 得 `NSWERS`。用户指出不像正确答案；更关键的是 SUCCESS/WALK/EXTRA 等读法没有共同选择原则，`ANSWERS` 只回扣提示里的 “answer”。不把撤回候选写入提交历史。
- **ANOTHER（2026-08-22 被拒绝）：** 旧路线把六图自由换读为 NEW/OPTION/TRAVEL/HOSPITAL/EYEDROP/RAINBOW，再取首字母 `NOTHER`；这一套完全作废。后来的歌曲路线识别出 *Here It Goes Again*—OK Go 与 *Watercolour*—Pendulum，并得到共同曲序 3，但错误地把 3 迁移到 *Hungry Ghosts* 第 3 曲 *Another Set of Issues*。共同曲序和跨专辑跳转都不得复用。
- **ARTISAN（2026-08-29 被拒绝）：** 路线继续把共同曲序 3 施加到六首题内源歌曲的罗马字标题，按二次下落列序取出 `ASRNIT`，再将题给 A 一起异序成 `ARTISAN`。用户明确判错；题面既没有标题取三指令，也没有异序指令，曲序、`ASRNIT` 和异序都不得复用。
- **AVERAGE（2026-08-29 被拒绝）：** 路线把四个专名的右端字母取成 `N/O/R/M`，再按答案格式把 `NORM` 换成同义词 `AVERAGE`。用户明确判错；*Inside Out* 没有指定“只取右端”，`NORM → AVERAGE` 又是第二次无提示跳转。专名首尾字母路线不得复用。
- **ANALOGY（2026-08-29 被拒绝）：** 路线把六图读成 *Here It Goes Again* : OK Go 与 *Watercolour* : Pendulum，再把平行关系本身命名为 `ANALOGY`。用户明确判错；线性六图没有类比符号。后来改读三项列表的 ARCHIVE 路线也已判错，两种关系语法都不得复用。
- **ALBUMIN（2026-08-29 被拒绝）：** 路线从 *Here It Goes Again*—OK Go 与 *Watercolour*—Pendulum 继续查询两首歌均为专辑第 3 轨，再概括为 `IN ALBUM` 并借题名 *Inside Out* 移成 `ALBUM IN`。用户明确判错；共同曲序、容器短语和词序操作都缺少题内指令。后来的直接艺人归一化也随 ARCHIVE 判错而撤销。
- **AQUEOUS（2026-08-29 被拒绝）：** 路线把六图读成 `CYCLE / MARK / MAN + WATER / COLOUR`，形成 WATER CYCLE、WATERMARK、WATERMAN、WATERCOLOUR，再按格式把共同词 WATER 换成 AQUEOUS。用户明确判错；四个复合词虽整齐，`WATER → AQUEOUS` 没有题面指令。不得继续枚举 WATER／AQUA 的 A 开头派生词。
- **ACYCLIC（2026-08-30 被拒绝）：** 路线把六图读成 *Here It Goes Again*—OK Go 与 *Watercolour*—Pendulum，再让首尾共用 `🔄`，把整段命名为 CYCLIC，并将格式 A 前缀化成 ACYCLIC。用户明确判错；同一图的双重角色和 `A + CYCLIC` 都没有题面指令。随后只读 `🔄 = AGAIN` 一次的 ARCHIVE 路线也已判错。
- **ARCHIVE（2026-08-30 被拒绝）：** 路线把六图分成 `AGAIN / OK GO / AND / WATERCOLOUR`，再把混合的歌曲名／艺人名统一成 `Archive / OK Go / Pendulum`，由答案格式筛出 Archive。用户明确判错；*Again* 同名不唯一，且题面没有“统一为艺人并筛选”的指令。停止沿这三项继续枚举外部歌曲归属或 A 开头艺人。
- **APREFIX（2026-08-30 被拒绝）：** 路线把六图换义成 `WHEEL / MARK / WALK / CROSS / WATER / COLOR`，再按标题 *Inside Out* 从中央向外配成 CROSSWALK、WATERMARK、COLOR WHEEL，最后把三组前置关系命名为 `PREFIX`，与题给 A 合成短语 `A PREFIX`。用户明确报告“APREFIX 不正确”。失败点已锁定在最后转换：提示 4 要求的是符合格式的**英文单词**，不能把一个冠词短语去空格冒充单词。三组复合词是否正确仍须另行审计，不能把 APREFIX 的判错误写成它们也被网站否定。
- **AFFIXES（2026-08-30 被拒绝）：** 路线保留同样的 inside-out 三组复合词，再把 CROSS／WATER／COLOR 三个前项作为三个 affixes，借复数得到七字母 A 单词。用户明确报告“AFFIXES 不正确”。这不仅排除 `PREFIX → AFFIXES` 的术语替换，也暴露出三项本来是复合词自由成分、并非严格 affix；不得继续枚举 AFFIXED／ADJOINS／ANNEXES 等近义词。由于 APREFIX 和 AFFIXES 已连续否定同一中间结构的两种直接命名，inside-out 三对必须降级为待证而非保留为默认真相。
- **ATHWART（2026-08-30 被拒绝）：** 路线把标题读作情绪们的 HEADQUARTERS，取 `TURN / HEAVY / WALK / ADD / RAIN / TINT` 的词首得到 THWART，再补题给 A。用户明确报告“ATHWART 错误”。失败点不只是词本身：`✅→HEAVY` 是 ATHWART 在 `❓=HOOK` 弱交换版出现后才从 `WHITE HEAVY CHECK MARK` 中补入的限定词，属于事后修补；判错后不得继续换一组六个同义词做 HEAD／首字母筛选。
- **ANAGRAM（2026-08-22 撤回，未提交）：** 路线把为候选而交换后的 `🔄/❓/🚶‍➡️/➕/💧/🎨` 读成 REARRANGE / WORD PUZZLE / `A MAN + RAG`。用户指出牵强；独立复核也发现 R4 只有两处疑问，红格应为 `✅`，而 `💧🎨→RAG` 无直接依据。该词未作为网站提交，不加入 Submission history。
- **整套标准 emoji 名称首字母（判断已修正）：** 早期结论是“Unicode／CLDR 短名首字母不能生成答案”。正确答案 ALFALFA 说明相反：**恰恰就是每枚图标最直白的本名的首字母**（LOOP／F…／ALPHABET／LEFT／F…／ART）。当时之所以否掉这条，是因为红格序列在 c6/c8/c9 上取错了图，用错误的六枚图当然拼不出词。教训：在底层落位未闭合前，不要用“某提取族拼不出词”去否定提取族本身。
- 曾把塔理解为“每列保持原顺序／逆序垂直下落”。正序粉格为 `🤥 ↩️ ✔️ ❓️ ❓️ ↩️`，逆序为 `🍀 🐰 ✔️ 🚶 🪑 ➕️`（均按歌曲上下顺序列示），且两者都不能把苹果／猩猩／落语／哥斯拉等歌词指纹聚到同一区域；因此位置只限制**列词库**，列内仍须由歌词决定。参数化结果保留在 `work/fall_model.py` 和 `work/fall/`。

## Next action

答案 ALFALFA 已确认，无比赛提交待办；row 5 的已知生成链已同步到 Round Meta。若完善复现，先恢复缺失的求解脚本，再核对 c6/c8/c9 的歌词落位与具体 emoji，补齐 128 格填表。
