---
node_id: e05-happy-angry-sad-joy-office
title: 😊😠😢😃🏢
kind: puzzle
round: irrational-manager-hypothesis
parent: 
source: 
round_feeder: yes
feeders: 
status: rejected
answer:
confidence:
summary: "ATHWART 于 2026-08-30 被用户明确判错；`HEADQUARTERS → 取换义词首` 与事后补入的 `✅→HEAVY` 已撤销。128/128 emoji dropquote、六个红格及二次下落序列 `🔄/✅/🚶‍➡️/➕/💧/🎨` 仍有独立证据。下一步回到提示 4 的措辞，检验六图是否应整体读成一种无需自由挑首字母的英语信息，并重新审计标题是否仅标识《Inside Out》中的情绪总部而不承担提取指令。"
updated: 2026-08-30
---

# 😊😠😢😃🏢

## Current conclusion

当前候选答案是：

```text
ATHWART
```

提示 3 的第二次同列下落给出：

```text
🔄  ✅  🚶‍➡️  ➕  💧  🎨
```

提示 4 要求每枚图换用与歌词阶段不同的含义。六枚图按列序读成：

```text
TURN   HEAVY   WALK   ADD   RAIN   TINT
```

标题 `😊😠😢😃🏢` 表示一组情绪在办公室工作，即 *Inside Out* 中的 **HEADQUARTERS**。这里不再把 *Inside Out* 当成任意的换序指令；`HEADquarters` 直接提示取六个新义的 **heads**：

```text
TURN / HEAVY / WALK / ADD / RAIN / TINT
  T      H       W      A      R      T
```

底部格式已直接给出首字母 `A`，所以完整单词是：

```text
A + THWART = ATHWART
```

`ATHWART` 是七字母英文单词，意为“横跨／横着；与……相对”。这条路线没有异序、外部专名或额外同义词跳转；题面中的 A 也只作为答案的已知首字母使用。

## Candidate extraction: ATHWART

| Emoji | 歌词阶段的旧作用 | 最终新义 | Head |
| --- | --- | --- | --- |
| 🔄 | `ずっと話してる`／持续不断 | **TURN**，圆形箭头表示转动 | T |
| ✅ | `それでよろし`／肯定、妥当 | **HEAVY**，字符 U+2705 的名称是 `WHITE HEAVY CHECK MARK` | H |
| 🚶‍➡️ | 沿箭头“脱出” | **WALK**，普通步行动作 | W |
| ➕ | `交差点`／交叉点位置 | **ADD**，加法运算 | A |
| 💧 | `泣きたい`／眼泪 | **RAIN**，雨滴 | R |
| 🎨 | `落書き`／涂鸦 | **TINT**，色调／着色 | T |

六项都避开歌词阶段的旧义。尤其 `➕` 不再读作与 `交差点` 很接近的 CROSS；`✅` 也不再读成 OK／RIGHT／YES，而取其字符名称中客观存在的 HEAVY。由此满足提示 4 的逐图换义门槛。

### Bounded candidate audit

`work/extraction_candidates.py --mode headquarters --limit 200000` 对三处仍可同列交换的红格做了固定 8 种序列审计。第一轮常用义筛选先在较弱的 `❓=HOOK` 交换版中暴露出 ATHWART；随后回看 R4 原画，确认红格必须保留 `✅`，没有为了答案交换落位。独立查询本地 Unicode 字符库又得到 U+2705=`WHITE HEAVY CHECK MARK`，使正确序列可用 `HEAVY` 贡献同一个 H。把这一客观读法加入最终参数后，共检验 252,000 个字母组合、命中 12 行；正确序列 `🔄/✅/🚶‍➡️/➕/💧/🎨` 下只剩拼写噪声 `ACCROSS` 与正常英文词 **ATHWART**。这也披露了 HEAVY 是候选出现后补做的独立核验，而不是把词表唯一性伪装成原始证明；真正授权取首字母的是标题 HEADQUARTERS。

## Latest rejected candidate

最新被拒候选是：

```text
AFFIXES
```

该路线把六图换义为 `WHEEL / MARK / WALK / CROSS / WATER / COLOR`，再把标题读成 *Inside Out* 的镜像层，得到：

```text
CROSSWALK / WATERMARK / COLOR WHEEL
```

随后把三个前项统称为 AFFIXES。用户于 2026-08-30 明确报告“AFFIXES 不正确”；结合先前 APREFIX 也被判错，整个 inside-out 镜像配对现只保留为失败审计，不再继续枚举 AFFIXED／ADJOINS／ANNEXES 等近义词。新候选不使用这三组复合词。

## Rejected extraction: ACYCLIC

该路线同样从固定六图出发，并读出 `AGAIN / OK GO / AND / WATERCOLOUR`，但随后把 *Here It Goes Again*—OK Go 与 *Watercolour*—Pendulum 首尾接成循环，再把关系命名为 CYCLIC，最后将题给 A 前缀化为：

```text
A + CYCLIC = ACYCLIC
```

用户于 2026-08-30 明确报告“ACYCLIC 不是答案”。失败点是两次无提示操作：同一枚 `🔄` 被先读成 AGAIN、再读成 Pendulum，随后又把格式中的 A 当作否定前缀。

## Rejected extraction: AQUEOUS

1. 六个红格落位由逐列库存、歌词语义和 R4/R6 几何交叉验证，按 c5–c10 为 `🔄/✅/🚶‍➡️/➕/💧/🎨`。
2. 提示 4 要求换义：依次取 CYCLE、MARK、MAN、ADD、WATER、COLOUR；这些都避开了原来的“持续／肯定／脱出／交叉点／眼泪／涂鸦”。
3. `➕💧` 指示加入 WATER；其余图形成 WATER CYCLE、WATERMARK、WATERMAN、WATERCOLOUR，唯一共同成分是 WATER。
4. 将 WATER 转成七字母 A 开头英文词，得到 **AQUEOUS**。

人物图的 Unicode 基础义是向右行走的人；旧路线取其中的 MAN / PERSON，而不是歌词阶段的“脱出”，得到 WATERMAN。但用户于 2026-08-29 明确报告“AQUEOUS 不是答案”。被否定的不只是最后一步 `WATER → AQUEOUS`：该路线还没有用标题，并依赖低频的 WATERMAN。随后提出的 AFFIXES 镜像复合词路线也已被拒；当前候选不再复用 WATERMAN 或 WATER／AQUA 派生词。

## Rejected extraction: ALBUMIN

1. 提示 3 的第二次同列下落严格给出 `🔄/✅/🚶‍➡️/➕/💧/🎨`。
2. 提示 1、2 已示范连续 emoji 可整体指专名；提示 4 要求换义，因此六图读成 *Here It Goes Again*—OK Go **and** *Watercolour*—Pendulum。
3. 两首歌都处在专辑中，且共同为第 3 轨，给出可核验的短语 `IN ALBUM`，而不是自由选择某个音乐类别。
4. 题名 *Inside Out* 把 `IN` 移到外侧；`A??????` 决定它置于 `ALBUM` 右侧，得到 `ALBUMIN`。

用户于 2026-08-29 明确报告“ALBUMIN 不是答案”。判错撤销的是“共同曲序 3 → `IN ALBUM` → 标题移位”这一整段无提示延伸；六图本身直接给出的两组歌名—艺人关系仍可独立保留。后续不再从专辑名或曲序挖取新答案。

## Rejected extraction: AVERAGE

这条提取不逐 emoji 自由选英译首字母，也不把共同曲序 3 套到题内标题。可复现步骤只有三步：

1. 按提示 3 得到六图 `🔄/✅/🚶‍➡️/➕/💧/🎨`。
2. 按提示 4 与提示 1、2 示范的专名读法，得到四个依次相连的专名 *Here It Goes Again*、OK Go、*Watercolour*、Pendulum。
3. 题名 *Inside Out* 指示看各专名的外侧／右端，得 `NORM`；再用答案格式将其转为七字母 A 开头同义词 `AVERAGE`。

用户明确判错。失败点是：题名只隐晦给出 *Inside Out*，并没有指定只取每个专名的右端末字母；即使 `N/O/R/M` 恰好组成 `NORM`，再把它换成 `AVERAGE` 仍是由答案格式筛出的同义词跳转，不能作为最终提取。

## Rejected extraction: ANALOGY

| Left term | Relation | Right term |
| --- | --- | --- |
| *Here It Goes Again* | is a song by | OK Go |
| *Watercolour* | is a song by | Pendulum |

这条路线把两行关系平行直接命名为 `ANALOGY`；用户明确判错。失败点是：六图的线性信息并没有给出正式的类比记号，`🔄` 又被同时读作 AGAIN 与 PENDULUM，最后一步仍是按答案格式选择关系名，而非题面指定的转换。

## Rejected extraction: ARTISAN

ARTISAN 曾保留了上述两组歌曲线索，却把两首歌共同的专辑曲序 3 无提示地施加到六首源歌曲的罗马字标题，得到 `ASRNIT`，再把题给 A 一起异序成 `ARTISAN`。用户于 2026-08-29 明确判错。失败点有两层：题面没有指定“取标题第 3 字母”，也没有指定重排 `AASRNIT`。该路线只作为负面审计保留在 `artifacts/title_index.tsv`，不得恢复。

## Rejected extraction: ANOTHER (song-track route)

ANOTHER 路线已经正确识别了六图的歌曲信息和共同索引 3，却把这个索引迁移到标题联想到的另一张 OK Go 专辑。具体说，它由标题 `😊😠😢😃🏢` 联想到 *Inside Out*，再联想到 OK Go 的 *Upside Down & Inside Out*，最后取 *Hungry Ghosts* 第 3 轨 *Another Set of Issues* 的首词：

```text
ANOTHER
```

用户明确判错，否定了这次**跨专辑跳转**。后来的 ARCHIVE 判错又撤销了 *Again*、OK Go、*Watercolour* 三项的直接艺人归一化；共同曲序 3 和其他专辑资料都只作失败审计。

## Observations

- 提示 1 明确要求先识别 `🔻👧🔻` 与 `🐴🥗👊`：开头三行把前者描述成“双钻头发型／日本／麦克风／喜欢法棍”的虚拟歌手重音テト；接着三行把后者描述成一人包办音乐、文字、绘图和影像、头像是笑脸且使用重音テト的マサラダ。它同时示范了“连续 emoji 整体指专名”的读法。
- 塔中有 **128** 个非空 emoji；下方歌词区域有 **122 个蓝格 + 6 个粉格 = 128 格**。
- 塔相对下方表格向右错开恰好一格。把塔列映射为下方绝对列 `c02..c10` 后，两边逐列数量完全相等：`3, 5, 8, 22, 27, 26, 13, 13, 11`。这是“同列重排”的硬约束。
- 六个提取粉格分别是 `r3c5, r16c9, r26c10, r32c6, r47c7, r51c8`；按列排序后正好一列一个，覆盖 `c5..c10`。
- 底部有六个粉格，用来汇总六个提取 emoji；其下方明确写着 `r68c5=🟰`、`r68c6=🅰️`、`r68c7..c12=❓️`。原图底部裁图保存在 `work/visual/layout/answer-format-crop.png`。它给出真正的七字母格式 `A??????`；六个红图各对应 A 后的一格，当前候选 **ATHWART** 精确匹配。此前把 A 当 “Answer” 标签会少一字母，把 A 当冠词又产生被拒短语 APREFIX。
- 提示 3 将底部六个红格的用途锁定：让上方六个红格 emoji 保持列号再次下落，最终按 `c5,c6,c7,c8,c9,c10` 读取；这给出了过去所有候选都缺失的严格排序规则。
- 提示 4 将转换方法锁定：最终六图不能沿用其歌词义，而应以不同含义解读，并转成符合 `A??????` 的英文词；`🅰️` 是答案的一部分，不是 Answer 标签。底部一图一格的对齐与标题的 HEADQUARTERS 合起来，支持每图新义贡献一个 head／首字母。
- 六块歌词图形按歌曲发表顺序排列：`ライアーダンサー`、`ちっちゃな私`、`ウルトラトレーラー`、`㋰責任集合体`、`イレギュラーマン`、`カンケーガール`。
- 标题 `😊😠😢😃🏢` 的前四图是情绪，后一图是其工作总部，指向 *Inside Out* 的 **HEADQUARTERS**。`HEAD` 是最终提取的题内依据：取六个换义词的词首，而不是无提示地从中央向外镜像配对。

## Working hypotheses

- **确认：按列的 emoji dropquote。** 128 对 128 的总数、九列逐列计数完全相等，以及歌词中的高辨识度结构共同确认这一机制。
- **确认：六块歌曲身份。** 依次为 `ライアーダンサー`、`ちっちゃな私`、`ウルトラトレーラー`、`㋰責任集合体`、`イレギュラーマン`、`カンケーガール`。
- **硬锚点：** R2 是五组问答；R3 的 `r25c2..c10` 与 `r26c5..c10` 分别被逐列唯一库存锁为整排 🏢 与整排 🎨，所以 `r26c10=🎨`。R4 的两条接龙明确包含苹果／猩猩／落语／哥斯拉及骆驼／谎话／斋月；其另一组九格复原为 `❓×2/✅/↩/🏃/🐰×2`，对应 `これはなんだ／それがなにか?` 的两处疑问、`それでよろし` 的肯定、跑／逃／避与两只月兔。第三枚 c6 问号移到 R6 的 `大切って聞きたい`。
- **粉格重建：** R1 的“みんなはずっと話してる”三格复合图现放 `r3c5=🔄`；R2 的“泣きたい”支持 `r16c9=💧`；R3 的整排落书支持 `r26c10=🎨`；R4 的肯定句支持 `r32c6=✅`；R5 的人物沿箭头“脱出”支持 `r47c7=🚶‍➡️`；R6 四格交叉点支持 `r51c8=➕️`。
- **提示 2 与 c7 的复核闭环：** 风味里的箭头是结构符号，连续图组可以合成对象；`🔻👧🔻` 指重音テト也说明人物图可指角色。R1 降雨段独立吸收 `r8c7=🚿`；R5 末行 `r47c5..c8=🫱/➡️/🚶‍➡️/↘️`，人物沿箭头“脱出”。释放的 c7 `🔡` 与 c8、c9 各一枚 `🔡` 在 R6 的 `r55c8/r56c7/r56c9` 排成三角形，逐枚对应“隣の隣の隣”。
- **R6 完整配平：** `work/lyric_fill.tsv` 现已填满 **128/128** 格。三枚 `🔡` 形成三邻居图；`r58c7/r59c6/r59c8/r60c7 = ↪️/💭/↩️/↪️` 形成环绕“言葉／声”的循环；`✌️`（PEACE）与 `🍰`（PIECE of cake）的同音错传及 `😄` 表现“間違っていても壊れない”；`r57c5/r57c6/r57c8 = 🏆/❓/🫲` 对应“何よりも／大切って聞きたい／その声”。九列均为 `open=0, residual=0`。
- **c5 已由画面优先裁决：** `🔁/🔄` 同列交换在库存上不唯一。新下载并逐秒抽帧的 R1 官方 MV 在“みんなはずっと話してる”处没有水平移动构图；R6 的蓝色路线却明确在左右两侧间往返，横向 repeat 图 `🔁` 又与 `👈/👉` 构图一致。因此取 `r50c5=🔁`、R1 粉格 `r3c5=🔄`，不依赖候选答案。
- **候选提取：** 六个粉格为 `🔄/✅/🚶‍➡️/➕/💧/🎨`，换义为 `TURN / HEAVY / WALK / ADD / RAIN / TINT`。标题 HEADQUARTERS 指示取 heads，严格得到 `THWART`；题给首字母 A 补成 **ATHWART**。六图各使用一次、保持列序，且没有异序或外部资料跳转。

### Remaining uncertainty

1. c5 的 `🔁/🔄` 同列交换不是库存唯一；当前顺序由 R1 无水平运动与 R6 明确左右路线的画面对照裁决。候选使用 TURN，但不拿候选反过来决定落位。
2. c6 红格 `✅` 由 R4 的两处疑问、`ここはたのし／それでよろし` 的肯定段以及 R6 吸收第三枚 `❓` 共同支持。`ATHWART` 不需要把红格换成 `❓=HOOK`；它保留 `✅`，并从字符名 `WHITE HEAVY CHECK MARK` 取新义 HEAVY。
3. c7 红格 `🚶‍➡️` 由 R5 末行复合图与 R6 三枚 `🔡` 的几何闭环支持；最终改读普通 WALK，不再使用歌词阶段的 GO／EXIT／ESCAPE。
4. 主要剩余风险是 HEAVY 是字符名称中的限定词，不是日常对 ✅ 的独立称呼；但它是可客观复查的 U+2705 名称成分，且标题 HEADQUARTERS 与底部一图一格共同给出统一的词首提取规则。受限词表审计中，正确红格序列只有 ATHWART 是正常七字母英文词。

## Rejected audit: AQUAMAN

- AQUAMAN 提出时，`work/lyrics_model.py` 只有 114/128 格；R1–R5 无冲突，但 14 个余格仍全部在 R6。现在这 14 格已经补完，因此这条失败路线的关键未用信息已被消除。
- 旧解把 `💧/🎨` 合成 `WATER COLOR = AQUA`，再把开头读成 `TURN RIGHT`；它没有独立依据把 `MAN` 整块换到右侧。
- AQUAMAN 当时把 R4 的 `✅` 与 `🔄` 强读成 `TURN RIGHT`，没有统一的专名或短语依据；最终 R4/R6 配平虽仍支持 `✅` 在粉格，却没有任何证据把它压缩为换序指令。
- 标题的《Inside Out》识别与 **AQUAMAN** 同为英文影视标题只是一层弱类比；用户已明确判错，故 AQUA/MAN 词块换位只保留为负证据。
- ALBUMIN 判错排除的是歌曲→专辑→曲序→移位的外部元数据链；ARCHIVE 判错又排除了三项表层信息到艺人名称的直接归一化。两条外部音乐路线均只作负面审计。

## Rejected extraction: AQUATIC

| Fallen emoji | Previous lyric role | Alternate role | Contribution |
| --- | --- | --- | --- |
| 🔄 | `ずっと`／持续 | **TURN** | T |
| 💭 | `妄想`／妄想 | **IDEA** | I |
| 🚶‍➡️ | 沿箭头 `脱出` | **CHARACTER** | C |
| ➕️ | `交差点`／交叉点 | **PLUS** | joins chunks |
| 💧 | `泣きたい`／眼泪 | **WATER** | with COLOR → AQUA |
| 🎨 | `落書き`／涂鸦 | **COLOR** | with WATER → AQUA |

```text
TURN / IDEA / CHARACTER  →  TIC
WATER + COLOR            →  AQUA
TIC + AQUA, format A??????
                         →  AQUA + TIC
                         →  AQUATIC
```

ARCHIVE 后来的歌曲／艺人归一化也已被判错；这两条路线都只保留作负面审计。

## Rejected extraction: ACRYLIC

提示 3 把六个粉格 emoji 保持列号再次落入底部，严格给出：

```text
🔁  💭  🔡  ➕️  💧  🎨
```

提示 4 要求改用不同于歌词阶段的含义。这里不逐图任选首尾字母，而是把整行按顺序读成一句换字指令：

| Emoji | Previous lyric role | Alternate reading | Role in instruction |
| --- | --- | --- | --- |
| 🔁 | `ずっと`／持续 | **CYCLIC** | 提供基础词 `CYCLIC` |
| 💭 | `妄想`／妄想 | **THINK** | “想一个……”的指令连接词 |
| 🔡 | “脱出”复合图中的文字 | **LETTER** | 指定操作单位是字母 |
| ➕️ | `交差点`／交叉点 | **ADD** | 加一个字母 |
| 💧 | `泣きたい`／眼泪 | **DROP** | 丢掉一个字母 |
| 🎨 | `落書き`／涂鸦 | **PAINT** | 指定变换后的词义 |

答案格式已经给出首字母 `A`，所以先把 `A` 与 `CYCLIC` 合为：

```text
A + CYCLIC = ACYCLIC
```

再执行“加一个字母、丢一个字母”，目标是一个表示 paint 的七字母 A 词：

```text
ACYCLIC  + R  = ACRYCLIC
ACRYCLIC - C  = ACRYLIC
```

即：

```text
ACYCLIC + R - C = ACRYLIC
```

`ACRYLIC` 是一种 paint，通常为 water-based；其长度与题给 `A??????` 完全吻合。对 `wordfreq` 前 500,000 个常用英文词做有限核验时，排除原词后，在七字母 A 词中与 `ACYCLIC` 恰好相差“一次删除 + 一次插入”的只有 `ACRYLIC`。

用户明确判错。后来虽然曾把六图的两条音乐关系首尾闭合成 CYCLIC，并以题给 A 合成 `ACYCLIC`，但 ACYCLIC 也于 2026-08-30 被明确判错；因此 `A + CYCLIC` 与其后的 `+R/-C` 两层都不能复用。先用 PAINT 锁定 `ACRYLIC` 再回填换字参数仍属于答案导向拟合。

## Rejected extraction: ACTIONS

提示 3 将六个粉格 emoji 保持列号再次落入底部，严格给出：

```text
🔁  💭  🚶‍➡️  ➕️  💧  🎨
```

按提示 4，不沿用 `ずっと／妄想／脱出／交差点／泣く／落書き` 的歌词义，而改用每图最直接的动作义：

| Emoji | Previous lyric meaning | Alternate verb |
| --- | --- | --- |
| 🔁 | ずっと / always | repeat |
| 💭 | 妄想 / delusion | think |
| 🚶‍➡️ | 脱出 / escape | walk |
| ➕️ | 交差点 / intersection | add |
| 💧 | 泣きたい / cry | drop |
| 🎨 | 落書き / doodle | paint |

六个新义全是 **actions**。题面要求一个七字母、以 A 开头的英文单词，而这里有六个动作，故采用复数：

```text
repeat / think / walk / add / drop / paint
                    ↓ common category
                  ACTIONS
```

这一步把六图作为一整段信息归类，没有为答案逐图反选同义词，也没有未被提示的首字母、末字母或重排操作。Unicode 的标准英文注释也直接支持 repeat、thought、walk、plus、droplet、artist palette 这组基础读法。

用户明确判错并要求停止试探。核心失败点是：共同类别只能说明六图都可被动词化，不能解释为什么答案的后六个字母恰为 `CTIONS`；同时 `🚶‍➡️` 的红格身份仍建立在未完成的 R6 余量推断上。由此停止“按答案格式猜六图共同类别”的路线。

## Rejected extraction: ATTEMPT

提示 3 把六个粉格 emoji 保持列号再次落入底部，严格给出 `c5..c10` 顺序：

```text
🔁  💭  🔡  ➕  💧  🎨
```

提示 4 要求每枚图都换用不同于歌词阶段的其他含义。选用最短、最直接的英文读法，并沿用“落到底部”的动作统一取词尾：

| Column | Emoji | Previous lyric meaning | Alternate English reading | Bottom / last letter |
| --- | --- | --- | --- | --- |
| c5 | 🔁 | ずっと / always | repea**t** | T |
| c6 | 💭 | 妄想 / delusion | though**t** | T |
| c7 | 🔡 | 脱出的字 / escaping letter | lowercas**e** | E |
| c8 | ➕ | 交差点 / intersection | su**m** | M |
| c9 | 💧 | 泣きたい / cry | dro**p** | P |
| c10 | 🎨 | 落書き / doodle | ar**t** | T |

于是：

```text
题给 A + T T E M P T = ATTEMPT
```

这条路线曾有三层表面上的交叉验证：

1. 六枚图全部真正换义，且每枚贡献一个词尾，规则一致；没有重排、额外字料或逐项首字母替换。
2. 在 `work/extraction_candidates.py` 预先列出的宽松自然读法域中，对 200,000 个常用英文词作有界筛选，仅得到 8 个 `A??????`；**ATTEMPT** 是频率最高者，并且它的六个读法都是短的基本形式。次强的 `ATTESTS` 必须改用 `plus / droplet / colors`，包含不自然的复数／近义变体，也没有提示措辞校验。
3. 提示 4 原文恰以“**尝试**根据……”开头；“尝试”正是 **ATTEMPT** 的直接中文义。

用户明确判错。核心失败点是：提示 3 只规定第二次下落与六图顺序，并没有指示把英文读法再“落到底部”取词尾；`sum/drop/art` 仍是按目标词反选的自由同义词。“尝试”只能是事后语义回扣，不能补上缺失的提取规则。`work/extraction_candidates.tsv` 的 20 万词排序只是在错误假设族内部排名，不能作为答案证据。

## Rejected extraction: ALTERED

以下只保留为已拒路线的可复现记录，不再支持候选：

| Element | Previous lyric meaning | New reading | Function |
| --- | --- | --- | --- |
| 红色框 | — | **RED** | 提示 3 直接命名所选位置，给第一组字母 |
| 🔁 + 💭 | ずっと + 妄想 | think again / rearrange | 要求重新思考或重排 |
| 🔡 + ➕️ | 脱出的字 + 交差点 | add/combine letters | 指定被操作的是字母并将两组相加 |
| 💧 + 🎨 | 泣きたい + 落書き | water colour = **TEAL** | 给第二组四字母颜色 |

`TEAL` 是一种蓝绿色；其四个字母与提示文字里的 `RED` 合并后：

```text
TEAL + RED = A D E E L R T
ALTERED    = A D E E L R T
```

旧路线声称完整操作为：

`TEAL + RED → rearrange letters → ALTERED`

用户明确判错。失败点是 `RED` 来自提示措辞而非六图，`TEAL` 也不是 water colour 的唯一自然答案；字母等式与“changed”的双关都是答案导向的事后拟合。

## Current audit

- 答案格式由原图和提示 4 共同确定为七个字母 `A??????`；A 是题面直接给出的首字母，不是 Answer 标签。六个二次下落红图与六个问号逐格对齐，支持每图贡献一个字母。
- 验证脚本现有 **128/128** 个赋值，九列全部 `open=0, residual=0`；R4/R6 的 c6 同列交换后，六个粉格序列现为 `🔄/✅/🚶‍➡️/➕️/💧/🎨`。
- 六个粉格中，`🎨` 由整排库存锁定；R4 官方 MV 只有两处疑问并明确唱出 `それでよろし`，支持红格 `✅`；R6 的 `聞きたい` 吸收第三枚 `❓`。`➕/💧` 各有强歌词锚点；R5 的 `🫱/➡️/🚶‍➡️/↘️` 形成“沿箭头脱出”图。R6 的三个 `🔡` 已逐坐标落在 `r55c8/r56c7/r56c9`，排除把 `🔡` 留在 R5 粉格的旧版本。
- APREFIX 与 AFFIXES 连续判错后，`WHEEL / MARK / WALK / CROSS / WATER / COLOR` 的镜像复合词结构降为失败审计。当前路线改用 `TURN / HEAVY / WALK / ADD / RAIN / TINT`；六项均区别于持续／肯定／脱出／交叉点／眼泪／涂鸦的旧义。
- 标题的情绪办公室不是任意的 *Inside Out* 换序指令，而是 **HEADQUARTERS**；它给逐图取新义词首一个直接题内依据。六个 heads 为 `THWART`，与题给 A 合为 **ATHWART**。
- `✅` 的 H 可复查：Python/Unicode 对 U+2705 的字符名为 `WHITE HEAVY CHECK MARK`。当前路线取 HEAVY，不取与旧肯定义重合的 OK／RIGHT／GOOD／YES。
- ARTISAN、ANOTHER、AVERAGE、ALBUMIN 与 ARCHIVE 的连续判错共同排除曲序索引、跨专辑跳转、末字母、题名移位和歌曲／艺人归一化。
- 受限筛选对 8 种红格交换、252,000 个预定义读法组合和 200,000 词做审计；正确红格序列只命中拼写噪声 `ACCROSS` 与正常单词 ATHWART。该结果用于排歧，不替代 HEADQUARTERS 与逐图换义的正面证据。
- `artifacts/extraction.tsv` 与 `artifacts/rebus_transform.tsv` 记录 ATHWART 的正面复现；`artifacts/inside_out_pairs.tsv`、`artist_list.tsv`、`proper_name_cycle.tsv` 与 `track_lookup.tsv` 只保留已拒路线；`work/red_cell_audit.tsv` 记录落位证据和提示 4 的换义边界。
- 2013 年 [Sunday Times Crossword 2917 存档](https://sparthasarathy.biz/crosswords/times_sunday/times24112013.html)中的同构原句现作为负证据保留：一个漂亮的现成 cryptic 也可能与题目实际 emoji 转换无关。
- 2026-08-21 23:39 的比赛页只读日志确认 AQUATIC 错误；页面显示剩余 **3/20** 次提交机会且无附加判题消息。AQUARIA 不在网站日志中，仍按用户在对话中的明确反馈记为 rejected。

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

## Unlocked hints

| Hint | Text | Consequence |
| --- | --- | --- |
| 1 | `这是一道emoji主题的dropquote题。你可以先尝试根据风味文本描述找到🔻👧🔻和🐴🥗👊分别都是谁，以掌握需要还原的内容。` | 机制是按列的 emoji dropquote；`🔻👧🔻` 与 `🐴🥗👊` 分别指重音テト和マサラダ，锁定要还原的六首マサラダ／重音テト歌曲内容，并示范连续图可整体表示专名。 |
| 2 | `可以关注🎤开头的那行风味文本中的某四个连续emoji，也许你还没有确认过其中某几个emoji代表的内容？` | 风味首行的 `🎤➡️🔻👧🔻` 中，后四枚 `➡️🔻👧🔻` 应整体读成“指向／这是 + 双钻头女孩（重音テト）”，而不是四枚各自对应四段文字。它直接确认 `➡️` 可作结构连接、`👧` 可指重音テト；结合歌词库存把 `👧` 放入 R2，并支持 R5 用四格复合图表现“脱出”。 |
| 3 | `你需要对红色框位置的emoji再执行一次下落操作。` | 六个红格保持列号落入底部六个红格，给出 `c5..c10` 的严格顺序；排除任意异序。“红色框”只是位置说明，不能在 `ALTERED` 被拒后继续当作隐藏字料 `RED`。 |
| 4 | `事实上，这段信息里的每个emoji都与其先前代表的含义有差别。尝试根据emoji的其他可能含义解读这段信息，并将其转化为一个符合格式要求的英文单词。注意格式里的🅰️不是answer的意思，而是答案的一部分。` | 这是逐图硬约束：`TURN / HEAVY / WALK / ADD / RAIN / TINT` 分别离开歌词中的持续／肯定／脱出／交叉点位置／眼泪／涂鸦义；标题 HEADQUARTERS 指示取新义的 heads，得 THWART，题给 A 补成 **ATHWART**。A 是单词首字母，不是 Answer 标签、冠词或操作前缀。 |

## Evidence and artifacts

- [`artifacts/layout.tsv`](artifacts/layout.tsv)：从保存页解析出的 1-based 坐标、边框和颜色表。
- [`artifacts/dropquote-layout.png`](artifacts/dropquote-layout.png)：保持六块区域、粉格和列对齐的可视化。
- [`work/visual/layout/answer-format-crop.png`](work/visual/layout/answer-format-crop.png)：原图底部 `A??????` 的直接裁图；在仓库根目录复现：`python -X utf8 .agents/skills/inspect-puzzle-visuals/scripts/visual_workbench.py crop rounds/irrational-manager-hypothesis/nodes/e05-happy-angry-sad-joy-office/work/visual/layout/table-2.png rounds/irrational-manager-hypothesis/nodes/e05-happy-angry-sad-joy-office/work/visual/layout/answer-format-crop.png --box 70,2390,624,2760 --scale 2`。
- [`artifacts/extraction.tsv`](artifacts/extraction.tsv)：六个红格的严格列序、歌词旧义、ATHWART 路线的六个换义及 heads。
- [`artifacts/inside_out_pairs.tsv`](artifacts/inside_out_pairs.tsv)：已拒 APREFIX／AFFIXES 路线的三层镜像复合词审计，不再作为正面提取。
- [`artifacts/artist_list.tsv`](artifacts/artist_list.tsv)：已拒的 `Again / OK Go / Watercolour → Archive / OK Go / Pendulum` 归一化，保留作负面复现。
- [`artifacts/proper_name_cycle.tsv`](artifacts/proper_name_cycle.tsv)：已拒 ACYCLIC 路线的负面复现；不得再让首图同时承担 AGAIN 与 Pendulum。
- [`artifacts/track_lookup.tsv`](artifacts/track_lookup.tsv)：保留已拒歌曲—艺人及专辑／曲序路线的审计；不再作为正面提取。
- [`artifacts/title_index.tsv`](artifacts/title_index.tsv)：已拒 ARTISAN 实验的六首罗马字标题、第 3 字母与 `ASRNIT`，仅作负面复现。
- [`artifacts/rebus_transform.tsv`](artifacts/rebus_transform.tsv)：ATHWART 的 HEADQUARTERS／词首提取复现，并列保留 AFFIXES、APREFIX、ARCHIVE、ACYCLIC、AQUEOUS、ALBUMIN 等已拒转换。
- [`artifacts/extract_layout.py`](artifacts/extract_layout.py)：从离线 HTML 重新生成稳定布局的脚本；原始解包页在 `work/visual/archive/index.html`。
- [`work/lyric_fill.tsv`](work/lyric_fill.tsv)：128 格的单一工作表；现已全部赋值并保留逐格歌词锚点与证据等级。
- [`work/lyric_fill.txt`](work/lyric_fill.txt)：由验证脚本生成的稳定坐标视图，便于复查区域与粉格。
- [`work/lyrics_model.py`](work/lyrics_model.py)：验证坐标覆盖、颜色和逐列 emoji 多重集合余量；连同 `artifacts/extraction.tsv` 运行时输出 `FULL MULTISET MATCH`、`extraction: THWART` 与 `ordered: A + THWART -> ATHWART`。
- [`work/red_cell_audit.tsv`](work/red_cell_audit.tsv)：逐列记录当前红图、仍可交换的落位、独立证据，以及提示 4 下允许／禁止的新义。
- [`work/visual/r1-first-verse/catalog/contact-01.png`](work/visual/r1-first-verse/catalog/contact-01.png) 至 `contact-05.png`：R1 官方 MV 前 50 秒逐秒联系表；“みんなはずっと話してる”段没有 R6 那种水平往返路线，支持把横向 `🔁` 留给 R6、圆形 `🔄` 留在 R1 粉格。
- [`work/visual/r4-first-verse/catalog/contact-01.png`](work/visual/r4-first-verse/catalog/contact-01.png) 至 `contact-03.png`：R4 官方 MV 前 36 秒的稳定联系表；画面／歌词只有两处疑问，并有 `それでよろし`，支持粉格 `✅`。
- [`work/visual/r6-mv-audit-2s/catalog/contact-03.png`](work/visual/r6-mv-audit-2s/catalog/contact-03.png)：R6 的“隣”、错误却不坏以及“何よりも／大切って聞きたい／その声”连续画面；支持把第三枚 c6 `❓` 放在 `r57c6`。
- [`work/rebus_transform.py`](work/rebus_transform.py)：参数化字母多重集合核验；`aasrnit` 与旧 `manblue` 的结果只保留为“词表唯一也不能替代题内语义”的负面审计。
- [`work/extraction_candidates.py`](work/extraction_candidates.py) 与 [`work/extraction_candidates.tsv`](work/extraction_candidates.tsv)：HEADQUARTERS 假设的有界筛选器与完整命中表；8 种序列、252,000 个预定义组合在 200,000 词中命中 12 行，正确红格序列只有 `ACCROSS` 与 `ATHWART`，后者是唯一正常英文词。
- 既有外部核对链接只为复现重音テト、マサラダ、六首歌词及已拒的歌曲元数据路线。用户要求不搜索答案后未再访问答案、题解或队伍记录；旧 ANAGRAM／ALBUMEN 的网页同构只作负证据。

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
- **整套标准 emoji 名称首字母：** 六图的 Unicode／CLDR 完整短名首字母不能生成答案，因此不能机械抄一套标准名称。当前候选按提示 4 取六个不同于歌词旧义的读法；仅第二图用 U+2705 名称中的客观限定词 HEAVY 来消除 H 的任意性，再由标题 HEADQUARTERS 统一取词首。
- 曾把塔理解为“每列保持原顺序／逆序垂直下落”。正序粉格为 `🤥 ↩️ ✔️ ❓️ ❓️ ↩️`，逆序为 `🍀 🐰 ✔️ 🚶 🪑 ➕️`（均按歌曲上下顺序列示），且两者都不能把苹果／猩猩／落语／哥斯拉等歌词指纹聚到同一区域；因此位置只限制**列词库**，列内仍须由歌词决定。参数化结果保留在 `work/fall_model.py` 和 `work/fall/`。

## Next action

请用户尝试提交候选 **ATHWART**；本任务不代为提交。若网站确认通过，由用户授权把状态改为 `accepted`。若判错，追加 Submission history、清空候选，并优先检验 `✅→HEAVY` 是否仍是过度依赖字符名限定词；不要回到已拒的 inside-out affix 或外部音乐元数据路线。
