---
node_id: final-meta-seeker-sinking-into-the-net
title: 沉向网中的追迹者
kind: meta
round: the-internet-is-dead
parent:
source:
round_feeder: no
feeders: wig/a9
status: accepted
answer: "艺人得道，弃圈†升天†"
confidence: high
summary: "Final Meta 已由网站与用户双重确认完成，答案为精确字符串【艺人得道，弃圈†升天†】，CCBC 17 正式完赛。现实 App 链为闲鱼→算菜→颤音→锤锤→猛隆过江→加拿天→猴子喂食俱乐部；中间验证依次包含 DONQUIXOTE、HERSTORY、ONEPIECE、PARANOIA AGENT。加拿天评价给出静海镇，猴子目录返回 26 张监控；每图四项 CCTV 频道线索替换为十六进制编码并按 Unicode 读取完整明文。省略两个 U+2020 会被判错；完整提交后进入警方及时赶到、时柒获救并毕业的最终结局。"
updated: 2026-09-03
---

# 沉向网中的追迹者

## Current conclusion

Final Meta 已由网站与用户确认完成，精确答案是：

**`艺人得道，弃圈†升天†`**

逗号和两个 `†` 是题目输出的一部分；尤其 `†` 是十六进制 `2020` 对应的 Unicode U+2020。删去这些符号的版本被判错，完整逐字提交后页面直接进入「最终结局」。

完整链条为：

`闲鱼 → 算菜 → 颤音 → 锤锤 → 猛隆过江 → 加拿天 → 静海镇 → 猴子喂食俱乐部 → CCTV/Unicode 明文`

最终剧情明确确认守护成功：警察在“鬼火暗”刚闯入时赶到，徐霓受到惊吓但没有受伤；之后时柒宣布毕业。

## Observations

- 题面风味文本要求“在虚拟的世界下载现实里的 APP，打开拯救时柒的路”。
- 用户明确禁止搜索公开答案或题解；所有工作只使用 WIG、已解锁提示、剧情记录和公开的原始漫画封面素材。
- 首步证据闭合为：徐霓说二手与短视频小号同名；陈子衿泰迪熊图片说物品从“她”手中经二手平台购得；现实 App 为闲鱼，WIG 商店精确映射到算菜。
- 算菜的三项验证依次是全黑格、八圆圈、许多简约线条；完成后链条继续到颤音，再到锤锤。
- 锤锤第三项先前的 `EGYPTIAN` 轮廓假设被验证否定；重新按封面数字位置校准后，正确英文验证为 **ONEPIECE**。网站接受后显示黄紫捷聊天，给出“今天扑棱蛾子漫展 / 给休息酒店点外卖 / 时柒最爱甜食和猪脚饭”。
- 既有剧情已确认时柒最爱甜食是 **红糖糍粑**。谷猫组合检索 `猪脚饭 红糖糍粑` 唯一命中餐馆 **猛隆过江**，由此进入加拿天商户验证。
- 加拿天人物图验证的机制是英国女王伊丽莎白二世柯基犬谱系：两图箭头取绝对世代差，再按题面运算得到 `PARANOIA AGENT`。网站接受后恢复杨国富的评论：“整个静海镇，不，整个有明区最好的猪脚饭”。
- 猴子喂食俱乐部搜索 `静海镇` 唯一命中 `有明区静海镇`，给出 26 张监控画面和前三个明文字符 `最 / 终 / ，`。
- 第三项原图地址为 `https://static.cipherpuzzles.com/static/images/ef57497769c3402ba540e024f2ce15e5.webp`。
- 八个红圈中心（5291×5291 原图坐标）为 `(1570,2200)`, `(2300,2240)`, `(3120,2240)`, `(3850,2260)`, `(1570,2830)`, `(2300,2860)`, `(3120,2860)`, `(3850,2860)`。
- 提示 5 原文：本题对应第三章 Meta【善和设计图】；草图展现与“奇妙冒险”有关的漫画封面，需要关注这些封面上数字的位置。
- a9 邮件点名隐藏应用 **猴子喂食俱乐部**，它能查看道路监控；提示顺序表明猴子位于前三项验证和人物图片验证之后，不能先盲搜地点。

## Working hypotheses

没有剩余工作假设。`EGYPTIAN` 已由网站否定；`ONEPIECE`、`PARANOIA AGENT` 和最终字符串均有正确回执。

## Extraction

猴子谜题的可复核最终提取：

1. 16 个可用 CCTV 频道映射到十六进制：国际0、新闻1、财经2、戏曲3、军事4、体育5、音乐6、少儿7、科教8、奥运9、电影A、社会与法B、电视剧C、纪录D、综艺E、农业农村F。
2. 每张图按自然顺序取四项频道，拼成四位十六进制 Unicode 码位。
3. 26 个码位依次是：`6700 7EC8 FF0C 4F60 627E 5230 4E86 65F6 67D2 3002 7ED3 679C 5C31 662F FF1A 827A 4EBA 5F97 9053 FF0C 5F03 5708 2020 5347 5929 2020`。
4. 解得：`最终，你找到了时柒。结果就是：艺人得道，弃圈†升天†`。

完整逐图表见 `rounds/wig/nodes/a9/artifacts/cctv-decode.md`。

## Candidate audit

答案已由网站接受。三个近似形式提供了必要的负面对照：复原典故 `一人得道鸡犬升天`、删掉符号的 `艺人得道弃圈升天`、以及主题推断 `DOXXING / CYBERSTALKING` 都错误；只有保留逗号和两枚 U+2020 的逐字明文触发最终结局。

## Submission history

以下是锤锤第三项验证的已知网站回执；它们是中间验证码，不是 Final Meta 总答案提交。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-09-01 | EMAIL | rejected | 锤锤第三项明确返回错误。 |
| 2026-09-01 | QQ@QQ | rejected | 非英文单词路线。 |
| 2026-09-01 | HATE | rejected | 早期盲猜。 |
| 2026-09-01 | IDEA | rejected | 早期盲猜。 |
| 2026-09-01 | HEART | rejected | 早期盲猜。 |
| 2026-09-01 | DRAFT | rejected | 早期盲猜。 |
| 2026-09-01 | JOJO | rejected | 主题词但非提取结果。 |
| 2026-09-01 | JUMP | rejected | 出版品牌词但非提取结果。 |
| 2026-09-01 | DEAD | rejected | 早期盲猜。 |
| 2026-09-01 | DATA | rejected | 早期盲猜。 |
| 2026-09-01 | NEXT | rejected | 早期盲猜。 |
| 2026-09-01 | MADE | rejected | 早期盲猜。 |
| 2026-09-01 | MADEINHEAVEN | rejected | JOJO 相关词但不符合八圈提取。 |
| 2026-09-01 | META | rejected | 早期盲猜。 |
| 2026-09-01 | GOATIT | rejected | 早期盲猜。 |
| 2026-09-01 | ASAP | rejected | 早期盲猜。 |
| 2026-09-01 | SAVE | rejected | 早期盲猜。 |
| 2026-09-01 | HELP | rejected | 早期盲猜。 |
| 2026-09-01 | KEEP | rejected | 早期盲猜。 |
| 2026-09-01 | SAFE | rejected | 早期盲猜。 |
| 2026-09-01 | STAND | rejected | JOJO 主题词但不符合八圈提取。 |
| 2026-09-01 | TRACE | rejected | 早期轮廓路线。 |
| 2026-09-03 | EGYPTIAN | rejected | 锤锤第三项中间验证；JOJO 封面识别路线的错误整词闭合。 |
| 2026-09-03 | ONEPIECE | accepted (intermediate) | 锤锤第三项接受，解锁黄紫捷聊天。 |
| 2026-09-03 | PARANOIA AGENT | accepted (intermediate) | 加拿天人物谱系验证接受，恢复杨国富的静海镇评价。 |
| 2026-09-03 | 一人得道鸡犬升天 | rejected | Final Meta；把监控末句复原成典故是错误路线。 |
| 2026-09-03 | 艺人得道弃圈升天 | rejected | Final Meta；省略标点与 U+2020 不被接受。 |
| 2026-09-03 | DOXXING | rejected | Final Meta；主题判断不是提交串。 |
| 2026-09-03 | CYBERSTALKING | rejected | Final Meta；主题判断不是提交串。 |
| 2026-09-03 | 艺人得道，弃圈†升天† | accepted | Final Meta；网站进入「最终结局」。 |
| 2026-09-03 | 艺人得道，弃圈†升天† | accepted (user-confirmed) | 用户明确确认“两题正确，正式完赛”。 |

## Evidence and artifacts

- `input/沉向网中的追迹者.html`：Final Meta 题面。
- `work/visual/hammer-minimal-lines.webp`：锤锤第三验证原图。
- `work/visual/hammer-lines-labelled-overview.png`：八圈编号标注。
- `work/visual/jojo-volume-covers/`：累计卷号 1–140 的封面证据集。
- `work/visual/jojo-cover-align-064-manual-edges-true-allmask.jpg`：第 64 卷坐姿徐伦与草图的精确轮廓叠图。
- `work/project_jojo_number_positions.py`：以印刷卷号锚定红圈、搜索旋转与缩放的参数化脚本。
- `work/render_jojo_word_hypothesis.py`：八字母候选的整组叠图脚本。
- `wig/a9/artifacts/a9-mail-and-account-clues.md`：a9 邮件和猴子应用关系。
- `wig/a9/artifacts/cctv-decode.md`：CCTV 频道编码、26 个 Unicode 字符和完整明文。
- `wig/a9/artifacts/jinghai-cctv-contact.jpg`：26 张静海镇监控联系表。

## Important failed routes

- 不搜索公开答案、公开题解或外部解答资料；这是用户明确禁止的路线。
- 不能把红圈直接视为二进制或 ASCII 位；第 64 卷印刷数字投影到 `1/4` 圈并给出 `P`，支持“卷号×倍率→A1Z26”。
- `COMPUTER` 曾因词形 `___P____` 被提出，但只有第 64 卷能重合，其余七卷不匹配，已否定且未提交。
- 只用显著性/人物自动分割的单向轮廓距离会被很小的错误掩膜欺骗；自动分数必须配合整个人物人工叠图，不再根据局部低分盲提交。
- 猴子喂食俱乐部是后段工具；现有地点词的有限检索均无命中，停止无新信息的盲搜。
- `EGYPTIAN` 曾因部分 JOJO 封面轮廓与字母闭合而误导，但网站否定；正确中间验证是 `ONEPIECE`。
- Final 不能把末句复原成典故，也不能丢弃两个 dagger；判题对完整 Unicode 明文敏感。

## Next action

无后续解题动作。a9 与 Final Meta 均已确认正确，CCBC 17 正式完赛。
