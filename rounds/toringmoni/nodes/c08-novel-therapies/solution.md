---
node_id: c08-novel-therapies
title: 新式疗法
kind: puzzle
round: toringmoni
parent:
source:
round_feeder: yes
feeders:
status: accepted
answer: KAGAMINE RIN
confidence: high
summary: 十五条英文线索的答案都是 Cure 名；每条线索的词数等于 Cure 后缀长度，以其中暗示变身者本名的词位索引后得到 MIRROR SOUND BELL，逐词转成「鏡・音・鈴」即 KAGAMINE RIN（鏡音リン），已由用户确认正确。
updated: 2026-08-17
---

# 新式疗法

## Current conclusion

答案 **KAGAMINE RIN**（鏡音リン）已由用户确认正确。

题名“新式疗法”与群聊中的“医院最新疗法”都在双关新的 **Cures**：十五条英文描述各自定义一个可接在 `Cure` 后的《光之美少女》变身名。题面给出的 `(6 5 4) → (8 3)` 中，前者是中间提取 `MIRROR SOUND BELL` 的枚举，后者是最终名字 `KAGAMINE RIN` 的枚举。

用户指出广告末尾的“顶花带刺！ / 11.10.5.4”很可能是 Round Meta 信息；它不参与本 Node 的提取。

## Observations

- 题目页正文只有“疗程里为啥会用到这些？”以及一个文件夹图标；实际题面在下载的群聊 `放课后补番同好会.html` 中。
- 纸片骑士发出十五条英文描述，随后给出 `（6 5 4）→（8 3）`。
- 每条描述的英文词数恰好等于其 Cure 后缀的字母数（`KYUNKYUN` 忽略连字符）。
- 每条描述还包含一个词，能提示该 Cure 普通身份姓名中的汉字、假名或读音；这个词在描述中的位置就是索引。
- 视觉清单共八张图：一张手机壁纸、六张群聊头像和一张题目页头像；未发现承载额外题目信息的图片。

## Extraction

按空格计数题面单词，并以“身份提示词”的词位索引对应 Cure 后缀：

| # | Cure 后缀（长度） | 普通身份 | 身份提示词（词位） | 取字 |
| ---: | --- | --- | --- | :---: |
| 1 | MILKY (5) | 羽衣ララ | **Plumage** → 羽衣 (1) | M |
| 2 | MINT (4) | 秋元こまち | **yuan** → 元 (2) | I |
| 3 | RHYTHM (6) | 南野奏 | **Play** → 奏 (1) | R |
| 4 | BUTTERFLY (9) | 聖あげは | **saint** → 聖 (6) | R |
| 5 | HONEY (5) | 大森ゆうこ | **forest** → 森 (2) | O |
| 6 | WONDERFUL (9) | 犬飼こむぎ | **wheat** → こむぎ (6) | R |
| 7 | SCARLET (7) | 紅城トワ | **Eternally** → Towa (1) | S |
| 8 | IDOL (4) | 咲良うた | **good** → 良 (3) | O |
| 9 | KYUNKYUN (8) | 紫雨こころ | **heart** → こころ (7) | U |
| 10 | ANSWER (6) | 明智あんな | **sensible** → 明智 (2) | N |
| 11 | MERMAID (7) | 海藤みなみ | **sea** → 海 (7) | D |
| 12 | BLOSSOM (7) | 花咲つぼみ | **Bud** → つぼみ (1) | B |
| 13 | PINE (4) | 山吹祈里 | **mountains** → 山 (4) | E |
| 14 | GELATO (6) | 立神あおい | **standing** → 立 (3) | L |
| 15 | FINALE (6) | 菓彩あまね | **colorful** → 彩 (5) | L |

顺次读出：

```text
MIRROR / SOUND / BELL
  (6)     (5)    (4)
```

其中几个容易误判的描述：

- 第 1 条是 **MILKY**：milky stork 因乳白色羽毛得名；`Plumage` 同时提示羽衣ララ。
- 第 6 条不是 March。Banjo Paterson 的 *Song of the Wheat* 原句为 `The wonderful march of Wheat`，所以是 **WONDERFUL**。
- 第 12 条不是 Bloom；`Bud = つぼみ` 精确指向 Cure Blossom 的普通身份花咲つぼみ。
- 第 15 条不是 Dream；Flowey 的彩色灵魂战斗曲名是 **Finale**，而 `colorful` 提示菓彩あまね的“彩”。

最后将三个英文词逐个还原为日文名字元素：

```text
MIRROR  -> 鏡 -> kagami
SOUND   -> 音 -> ne
BELL    -> 鈴 -> rin（角色名写作 リン）

鏡音リン -> KAGAMINE RIN
```

`KAGAMINE` 为 8 个字母，`RIN` 为 3 个字母，严格符合 `(8 3)`。

## Candidate audit

- **答案格式：** `KAGAMINE RIN` 严格符合 `(8 3)`。
- **完整提取：** 十五项全部同时满足“线索答案是 Cure 后缀”“线索词数等于后缀长度”“身份提示词提供索引”，无须使用广告数字。
- **末步确认：** Crypton/Sonicwire 官方产品页采用拼写 `KAGAMINE RIN`；Crypton 的许可文本也列出中文形式“鏡音鈴”，直接对应 `MIRROR SOUND BELL`。
- **重要未用信息：** “顶花带刺！ / 11.10.5.4”依用户提示视为 Round Meta 馈送；群聊吐槽、时间戳、头像和壁纸是 WIG 场景包装。
- **确认结果：** 用户于 2026-08-17 明确确认 `KAGAMINE RIN` 正确，状态据此改为 `accepted`。

## Submission history

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-17 | CUCUMBER BEE | rejected | 用户明确表示不是答案，并指出 `11.10.5.4` 可能是 Meta 相关信息。 |
| 2026-08-17 | KAGAMINE RIN | accepted | 用户明确确认答案正确。 |

## Evidence and artifacts

- `artifacts/cure_grid.tsv`：十五条线索的词数、Cure、普通身份、身份提示词、索引和提取字母。
- `work/extract_html.py`：从 SingleFile 的 `<main>` 文字回退层提取稳定 UTF-8 文本。
- `work/chat_dom.json` 与 `work/puzzle_dom.json`：上述脚本生成的题面转录。
- `work/visual/inventory/index.tsv`、`manifest.json`、`contact-01.png`：HTML 内嵌图片的稳定编号与接触表。
- 复现文字提取：

  ```powershell
  python rounds/toringmoni/nodes/c08-novel-therapies/work/extract_html.py rounds/toringmoni/nodes/c08-novel-therapies/input/放课后补番同好会.html rounds/toringmoni/nodes/c08-novel-therapies/work/chat_dom.json
  ```

- 外部核对：
  - Cure Milky / 羽衣ララ：https://www.toei-anim.co.jp/tv/startwinkle_precure/info/
  - Cure Wonderful / 犬飼こむぎ：https://www.toei-anim.co.jp/tv/wonderful_precure/character/?character=1
  - Cure Finale / 菓彩あまね：https://www.toei-anim.co.jp/tv/delicious-party_precure/character/chara4.php
  - Cure Answer / 明智あんな：https://www.toei-anim.co.jp/tv/precure/character/?character=3
  - Cure Mermaid / 海藤みなみ：https://www.toei-anim.co.jp/tv/princess_precure/character/curemermaid.php/1000
  - Cure Honey / 大森ゆうこ：https://www.toei-anim.co.jp/tv/happinesscharge_precure/character/precure_curehoney.php
  - Cure Butterfly / 聖あげは：https://www.toei-anim.co.jp/tv/hirogaru-sky_precure/character/chara3.php?char=item_05
  - Banjo Paterson 原诗：https://www.readbookonline.org/readOnLine/13955/
  - Kagamine Rin/Len 官方英文产品页：https://sonicwire.com/product/virtualsinger/special/rinlennt?lang=en
  - Crypton 许可文本（含“鏡音鈴”）：https://ec.crypton.co.jp/download/pdf/eula_virtualsingertry.pdf

## Important failed routes

- **CUCUMBER BEE（已拒绝）：** 旧路线误把第 1、15 条答成 White、Dream，再将广告数字 `11,10,5,4` 用作普通身份索引，拼出 `MAYA` 后联想到 Bee；用户明确否定答案。该路线还无法解释十五条描述的精确词数，因此没有新证据不得恢复。
- 第 6 条把关键词 `march` 直接猜作 Cure March 会丢失原诗中的 **wonderful**；原诗完整措辞排除此解。
- 第 12 条表面可答 Bloom，但 `Bud = Tsubomi` 与 Cure Blossom 的普通身份形成双重对应，且只有 BLOSSOM 的 7 字母长度与线索 7 词吻合。
- 直接从 SingleFile 源码读取会混入压缩归档和 emoji 扩展数据；应使用 `work/extract_html.py` 的 `<main>` 回退层转录。

## Next action

本 Node 已完成，无待办；`11.10.5.4` 与“顶花带刺”继续保留为 Round Meta 馈送信息。
