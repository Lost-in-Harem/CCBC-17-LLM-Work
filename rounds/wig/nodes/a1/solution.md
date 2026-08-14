---
node_id: a1
title: 入职声明
kind: puzzle
round: wig
parent: 
source: wig-web
round_feeder: no
feeders: 
status: accepted
answer: 祁希艾
confidence: high
summary: 用户已确认答案祁希艾正确；WIG 人物采访以标题和正文两次明确对应密码菌创办人“小七”的真实姓名。
updated: 2026-08-14
---

# 入职声明

## Current conclusion

答案 **祁希艾** 已由用户明确确认。WIG 站内采访直接把“祁希艾”“密码菌创办人”和偶像名“小七”写在同一人物卡中，正文又独立重复这一对应关系。

## Observations

- 邮件《入职声明》明确要求找到“小七”的真实姓名后回复。
- 已查看的站内博客《小七的小本子》称她是“前国民团体偶像、密码菌创始人”，并附有一段 10 秒、背对镜头的偶像舞蹈视频。
- “密码菌 - 官方主页”确认公司的业务覆盖谜题创作、活动运营、媒体运营和虚拟主播，并将搜索者引向更多站内材料。
- 《30岁以下优秀文娱创业青年采访》的人物卡原文为：“祁希艾 / 密码菌创办人，前国民团体美少女偶像‘小七’”。
- 同一采访正文再次写道：“很多人第一次认识祁希艾，是在国民团体的舞台上。那时她叫‘小七’。”
- 视频逐秒帧表明人物始终未露脸；无可读身份文字。音频以有损和无损格式各做一次识曲，均无匹配，因此暂不能用歌曲确认身份。

## Working hypotheses

- 已确认主路线：WIG 站内采访直接给出本名，且标题与正文互相复核。
- 现实互联网同名偶像路线已排除；本题要求调查的是 WIG 世界内的虚构人物，而不是现实中的赖美云或徐诗琪。

## Extraction

1. 邮件给出检索对象：多栖偶像、密码菌创办人“小七”。
2. 搜索“小七”得到个人博客，确认“小七”确是密码菌创始人和前偶像。
3. 搜索密码菌得到官方主页及人物采访。
4. 采访人物卡把“小七”对应到 **祁希艾**；正文再次确认。
5. 因此答案为 **祁希艾**。

## Candidate audit

- 格式：三字中文人名，吻合“真实姓名”的提问。
- 设计：完整解释了邮件要求使用浏览器搜索、博客提供身份关键词、官方主页与采访完成消歧的 WIG 搜索链。
- 独立检查：人物卡标题和正文分别给出同一对应；又在原始 HTML 搜索文本中逐字复核为“祁希艾”，不存在 OCR 字形不确定性。
- 未使用但不矛盾的信息：piggy 的厨艺综艺故事、Cute Cipher Baby Club、时柒 Junana、手机状元榜和应用下载提示明显在铺垫后续 WIG 内容；博客视频仅强化偶像背景，不参与姓名提取。
- 未发现与候选冲突的站内信息。

## Submission history

只记录用户或比赛网站明确反馈过的提交；不要把尚未提交的候选写进来。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-14 | 祁希艾 | accepted | 用户明确反馈“对的”。 |

## Evidence and artifacts

- `artifacts/wig-text-report.md`：五个 WIG HTML 页面的可复核文本与 SHA-256；直接证据位于采访页章节。
- `artifacts/extract_wig_text.py`：从 SingleFile ZIP HTML 的 `<main hidden>` 搜索文本块生成上述报告。复现：`python rounds/wig/nodes/a1/artifacts/extract_wig_text.py rounds/wig/nodes/a1/input rounds/wig/shared/wig-web --output rounds/wig/nodes/a1/work/wig-text-report.md`。
- `work/visual/input-inventory/` 与 `work/visual/source-inventory/`：当前题面和共享 WIG 页面的稳定图像清单。
- `work/visual/video/`：视频元数据、逐秒帧和接触表；复现命令见其中 `render-manifest.json`。
- `work/recognize_audio.py` 与 `work/audio-recognition*.json`：有界识曲实验及空匹配结果。

## Important failed routes

- 不再继续音频识曲路线：压缩 MP3 与无损 WAV 均返回空匹配；视频本身也无面部或文字身份线索。
- 现实互联网曾产生赖美云、徐诗琪等“小七”同名匹配，但它们不能解释密码菌背景；WIG 采访已经明确给出虚构本名祁希艾，因此不再沿现实人物路线搜索。

## Next action

已确认完成；本 Node 无需进一步解题。若 WIG 推进后出现与本题直接相关的新反馈，再追加记录。
