---
node_id: b4-keep-solving-and-nobody-explodes
title: 保持解谜就无人爆炸
kind: puzzle
round: shi-qi-love-in-chaos
parent:
source:
round_feeder: yes
feeders:
status: working
answer:
confidence:
summary: "已确认 Miracle Sudoku 唯一解、蓝色数字 {9,6}、紫色数字 4 与七图彩虹顺序；HELP/SOS:HELP 依赖从目标短语反选五个缺失色格数字并挑选图片同义词，属于循环论证，已撤回。当前检验能否从节点自身证据用一条统一规则独立恢复五个缺失色格。"
updated: 2026-08-17
---

# 保持解谜就无人爆炸

## Current conclusion

当前**没有可提交候选答案**。

此前的提取为：

~~~text
MAUSOLUS[4]             = S
BABYLON[6]              = O
LIGHTHOUSE[9]           = S
SPHINX[3]               = H
ZEUS[2]                 = E
COLOSSUS[|9-6| = 3]     = L
TEMPLAR ASSASSIN[4]     = P

display = SOS:HELP  (overfit hypothesis only)
~~~

这不是有效提取。五个未从音频恢复的彩格数字 4、6、9、3、2 是从
`SOS:HELP` 倒推的，而若干图片名称又是在多个同义候选中为这些目标字母
挑选的；输入与输出互相证明，构成循环论证。七大奇迹仍可作为待检验的
主题假设，但 **HELP / SOS:HELP 已撤回，且没有被用户提交或判题拒绝**。

## Observed facts

- 页面故意只提供 137.4 秒录音，没有原数独图或七张小图。
- 输出形状是三个字母、冒号、四个字母。
- 录音给出 r5c3=9、r6c7=8。
- r5c3 和它正下方的 r6c3 都是蓝色；r6c7 右侧的 r6c8 是紫色。
- 彩虹顺序为红、橙、黄、绿、青、蓝、紫；只有蓝色占两个格。
- 七图的口述依次是国王头像、顶层有露台的大楼、港口、蓝色飞行神话生物
  万智牌、O2 场馆内戴眼镜的亚洲选手举杯、巨大的履带陆行舰游戏模型、
  老式游戏中的绿色女性角色与 Warcraft 式技能图标。

完整时间戳转写见
[audio_transcript.md](artifacts/audio_transcript.md)。

## Miracle Sudoku

“创造奇迹”提示标准 Miracle Sudoku 规则：普通数独、反王步、反马步、
正交相邻数字不得连续。加入录音给定 r5c3=9、r6c7=8 后，
[miracle_sudoku.py](artifacts/miracle_sudoku.py) 得到唯一解：

~~~text
6 2 7 | 3 8 4 | 9 5 1
3 8 4 | 9 5 1 | 6 2 7
9 5 1 | 6 2 7 | 3 8 4
------+-------+------
2 7 3 | 8 4 9 | 5 1 6
8 4 9 | 5 1 6 | 2 7 3
5 1 6 | 2 7 3 | 8 4 9
------+-------+------
7 3 8 | 4 9 5 | 1 6 2
4 9 5 | 1 6 2 | 7 3 8
1 6 2 | 7 3 8 | 4 9 5
~~~

直接可核验的彩格数字是：

- 蓝色两格：r5c3=9、r6c3=6，即无序对 {9,6}。
- 紫色格：r6c8=4。

红、橙、黄、绿、青五格的位置在录音叠音中没有可靠恢复。当前主题和完整
短语反推出它们的盘面数字依次应为 4、6、9、3、2；这是候选中最主要的
残余风险，不能写成直接听到的事实。

## Seven Wonders mapping

| # / 色 | 录音描述 | 用于索引的名称 | 对应古代奇迹 | 证据 |
| --- | --- | --- | --- | --- |
| 1 / 红 | 国王头像 | MAUSOLUS | Mausoleum at Halicarnassus | 多张公开雕像头像直接标为 Mausolus |
| 2 / 橙 | 楼顶层叠露台 | BABYLON | Hanging Gardens of Babylon | 重建图正是层叠建筑与屋顶花园 |
| 3 / 黄 | 港口 | LIGHTHOUSE | Lighthouse of Alexandria | 公开重建图同时表现港湾与灯塔 |
| 4 / 绿 | 蓝色万智牌、飞行神话生物 | SPHINX | Great Pyramid of Giza | 多张蓝色 Flying 牌的生物类别为 Sphinx，联系吉萨 |
| 5 / 青 | O2、戴眼镜的亚洲选手举杯 | ZEUS | Statue of Zeus at Olympia | Riot 官方照片说明明确写 Zeus of T1 lifts the trophy，且标签含 O2 |
| 6 / 蓝 | 巨大、有履带的游戏陆行舰模型 | COLOSSUS | Colossus of Rhodes | 公开 3D 模型名为 Vehicle_Common_Colossus [Planetside 2]，画面为四履带重型载具 |
| 7 / 紫 | 老式游戏的绿色女性角色、技能图标 | TEMPLAR ASSASSIN | Temple of Artemis at Ephesus | 老 Dota 的 Lanaya 使用 Warcraft III 模型，名称开头直接给出 TEMPL- |

第 1 项的公开头像：
[Mausolus](https://en.wikipedia.org/wiki/Mausolus)。

第 2 项的代表性重建：
[Hanging Gardens of Babylon 3D model](https://free3d.com/3d-model/hanging-gardens-of-babylon-8021.html)。

第 3 项的港湾重建：
[Harbour and Lighthouse of Alexandria](https://www.worldhistory.org/image/12903/harbour--lighthouse-of-alexandria/)。

第 4 项不要求辨认唯一牌名。诸如
[Consecrated Sphinx](https://scryfall.com/card/2x2/427/consecrated-sphinx)
都同时满足蓝色牌、Creature - Sphinx、Flying；应取图所代表的通类
SPHINX，而不是旧路线后验挑选的 Serum Raker。

第 5 项现在有直接的官方文字证据。LoL Esports / Riot 的 Flickr 至少有
三张符合口述的照片：

- [54112631903](https://www.flickr.com/photos/lolesports/54112631903/)：
  “Zeus of T1 lifts the trophy ... World Championship 2024 Finals”。
- [54112631638](https://www.flickr.com/photos/lolesports/54112631638/)：
  同样明确标为 Zeus 举杯。
- [54111387222](https://www.flickr.com/photos/lolesports/54111387222/)：
  Zeus 把奖杯举过头顶。

这些照片的标签包含 indigoattheo2 / o2，人物戴眼镜且身形较瘦，完整覆盖
录音描述。旧路线认成 Faker 是同一场馆、同一队伍造成的近邻误认。

第 6 项的定向搜索命中
[Vehicle_Common_Colossus [Planetside 2]](https://sketchfab.com/3d-models/vehicle-common-colossus-planetside-2-d3be18a68b5b4db48684aeff51f9fc7e)。
其公开缩略图是独立游戏模型视图，主体巨大且有四条履带，比 Cocoon、
Big Shiee 等纯外形候选多出名称 COLOSSUS 的主题约束。

第 7 项可与
[Templar Assassin (DotA)](https://dota.fandom.com/wiki/Templar_Assassin_(DotA))
核对。旧版 Lanaya 是女性 Warcraft III 模型，公开截图呈绿色环境和
绿黑色服装；老 Dota 指南通常并列四个技能图标。音频仍不足以证明某一张
具体截图，但 Templar Assassin 同时解释画面、Temple 关键词和第四字母 P。

代表性搜索结果及第 5、6 项的多个近邻候选保存在
[seven-wonders-search-contact-sheet.png](artifacts/visual/seven-wonders-search-contact-sheet.png)。
它们是公开对照图，不是从题页恢复的原图。接触表可由以下命令重建：

~~~powershell
python .agents\skills\inspect-puzzle-visuals\scripts\visual_workbench.py inventory rounds\shi-qi-love-in-chaos\nodes\b4-keep-solving-and-nobody-explodes\work\visual\wonders_candidates --output rounds\shi-qi-love-in-chaos\nodes\b4-keep-solving-and-nobody-explodes\work\visual\wonders_inventory
~~~

## Extraction

统一规则是将名称转大写、去掉空格和标点，只数 A-Z，并用彩格数字作
1-based 索引。

| 色 | 名称 | 数字或运算 | 字母 |
| --- | --- | ---: | --- |
| 红 | MAUSOLUS | 4 | S |
| 橙 | BABYLON | 6 | O |
| 黄 | LIGHTHOUSE | 9 | S |
| 绿 | SPHINX | 3 | H |
| 青 | ZEUS | 2 | E |
| 蓝 | COLOSSUS | abs(9-6)=3 | L |
| 紫 | TEMPLAR ASSASSIN | 4 | P |

蓝色的两个格没有先后次序，因此采用绝对差：

~~~text
|9 - 6| = |6 - 9| = 3
~~~

这是交换两个输入后结果不变的最简单小整数提取。最大公因数
gcd(9,6) 也恰好为 3，因此在这两个常见交换不变运算之间，提取字母 L
不变；加法 15 和乘法 54 则无法索引八字母的 COLOSSUS。

运行 [test_indexing.py](artifacts/test_indexing.py) 可复现完整结果：

~~~powershell
python rounds\shi-qi-love-in-chaos\nodes\b4-keep-solving-and-nobody-explodes\artifacts\test_indexing.py
~~~

期望最后两行：

~~~text
display	SOS:HELP
answer	HELP
~~~

## Submission history

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-14 | 397:1964 | rejected | 用户明确报告“答案错误”。 |
| 2026-08-15 | WIRES | rejected | 用户明确报告“WIRES 不是答案，请不要乱猜”。 |
| 2026-08-15 | COPPER | rejected | 用户明确报告“copper 不是答案”。 |
| 2026-08-15 | 396:3964 | rejected | 用户明确报告“396:3964 答案不正确”。 |
| 2026-08-15 | 396:3464 | rejected | 用户明确报告该纯数字串不是答案，并提出数字应用于英文单词索引。 |
| 2026-08-15 | DEF:USER | rejected | 用户明确报告“DEF:USER 不是答案”。 |
| 2026-08-15 | WAR:HEAD | rejected | 用户明确报告“WAR:HEAD 也不是答案”。 |
| 2026-08-15 | CRUELTY | rejected | 用户明确报告“CRUELTY 不是答案”。 |
| 2026-08-15 | HEAD | rejected | 用户明确报告“HEAD 不是答案”。 |
| 2026-08-17 | MENU | rejected | 用户明确报告“menu 不是答案”。 |

## Important failed routes

- MENU 已明确拒绝。CHARLES / SKY GARDEN / SANTOS / SERUM RAKER / FAKER /
  COCOON / MEDUSA 没有共同类别，且用 min(9,6)=6 是为了让 COCOON 可索引；
  不得恢复。
- HEAD、CRUELTY、WAR:HEAD、DEF:USER、WIRES、COPPER 以及三组纯数字均有
  明确拒绝记录，不再换近义词恢复。
- Faker 是同场比赛的强干扰项，但 Riot 的多个相符照片明确把举杯者标作
  Zeus；这项已有主题外的独立证据。
- Cocoon、Big Shiee、Morden's Battleship 和 Medusa 都只解释外形，没有
  七大奇迹的一一对应关系，降为图像近邻而非当前名称。
- 三次有界 ASR、声道差分和语音增强均未恢复额外坐标或专名，这一实验族
  已停止。

## Residual risk

1. 红、橙、黄、绿、青五个彩格的确切位置没有从录音可靠恢复；数字
   4、6、9、3、2由主题名称与完整短语闭合。这是唯一较大的证据缺口。
2. Sphinx 是吉萨金字塔的邻接象征，Templar Assassin 是 Temple 的词形提示；
   两者不是奇迹的完整正式名称。
3. SOS:HELP 是完整提取；当前按冒号后的四字母提交 HELP。若判题器要求完整
   七字母串，则格式变体会是 SOSHELP，但在没有反馈前不额外提交。

## Evidence and artifacts

- [audio_transcript.md](artifacts/audio_transcript.md)：完整音频时间戳与事实、
  解释分层。
- [miracle_sudoku.py](artifacts/miracle_sudoku.py)：数独唯一解。
- [test_indexing.py](artifacts/test_indexing.py)：七项名称、索引和 SOS:HELP。
- [extraction.md](artifacts/extraction.md)：精简提取审计。
- [seven-wonders-search-contact-sheet.png](artifacts/visual/seven-wonders-search-contact-sheet.png)：
  代表性公开搜索对照。

## Next action

检查本 Node 的历史版本、原始 HTML 与既有搜索对照，寻找一种对红、橙、黄、
绿、青五项都相同且不依赖目标输出的来源编号或坐标规则。判别标准是：规则必须
在选定任何答案词之前唯一给出五个彩格位置或数字；若做不到，则继续保持
`working`，不把七大奇迹同义词链提升为候选答案。
