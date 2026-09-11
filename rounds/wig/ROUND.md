---
round_id: wig
title: 卡美洛终端 WIG
---

# 卡美洛终端 WIG

这是 CCBC 17 外层的连续互动调查区，不是传统的小题与 Meta 组合。玩家作为数字调查师加入卡美洛资本，通过模拟平板中的邮件、电话、通话记录、浏览器和可安装应用推进委托。

## 区域入口

- WIG 终端：<https://heptadec.cipherpuzzles.com/launchpad>
- Hunt 主界面：<https://heptadec.cipherpuzzles.com/main>

## 文件约定

- `STATE.md`：跨应用的当前剧情状态、已确认事实、开放问题和采集请求。
- `shared/wig-web/`：用户保存的原始网页与媒体；作为证据只读。
- `nodes/<id>/input/`：某个答案事件独有的邮件或题面；只读。
- `nodes/<id>/solution.md`：该答案事件的推理、候选、提交历史和状态。
- `nodes/<id>/work/`：临时提取、帧、OCR 和实验结果。
- `nodes/<id>/artifacts/`：复核结论所需的少量长期材料。

用户明确指定“整个 WIG 区域”时，可以维护本目录内的跨页面状态；否则仍应只处理指定的一个 Node。

## 赛后阅读入口

当前完成状态见 [STATE.md](STATE.md)，全仓库说明见 [README](../../README.md)。本区的 13 个节点包含 a1–a9 九个事件与四道后续补档漫画小题；漫画全部 71 张原题图仍位于艺人之夏的共享材料中，不能用本区节点数量代表素材总数。
