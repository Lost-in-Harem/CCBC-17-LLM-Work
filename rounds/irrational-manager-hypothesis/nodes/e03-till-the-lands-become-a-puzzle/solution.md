---
node_id: e03-till-the-lands-become-a-puzzle
title: 直到大地变成一块拼图
kind: puzzle
round: irrational-manager-hypothesis
parent:
source:
round_feeder: yes
feeders:
status: candidate
answer: 上海国际航运服务中心
confidence: high
summary: 8 小时采集结束时队伍已有 61/64 种拼片。61 片可唯一落入 8×8 网格，仅缺 (5,0)、(4,4)、(6,6) 三格；其中 55 片与上海北外滩同一幅 Google 卫星图形成可靠单应匹配，网格中心残差 0.626 px。复原图、约 31.25154°N 121.49833°E 的中心和官方所述近 800 米岸线、东中西三地块、游艇港池均对应上海国际航运服务中心，故答案候选为“上海国际航运服务中心”。
updated: 2026-08-21
---

# 直到大地变成一块拼图

## Current conclusion

答案候选是 **上海国际航运服务中心**，置信度高。

8 小时采集在 P168 到达硬截止，队伍状态为 180 个领取实例、**61/64 种不同拼片**，无领取错误。虽然仍未领到三片，但现有 61 片已经全部唯一落位；同一幅公开卫星底图还可以补出三个缺口，地点识别不再依赖猜测。

拼图覆盖上海虹口区北外滩黄浦江滨江：画面主体是航运办公建筑群、滨江绿地、游艇港池和岸线。拼图中心约为 **31.25154°N, 121.49833°E**。虹口区政府对“上海国际航运服务中心”的介绍明确写到，该项目位于北外滩黄浦江滨江核心地段，拥有近 800 米岸线，由东、西、中三幅地块组成，并以游艇港池为航运特色；这些特征与复原图逐项吻合。项目西侧相连的上海港国际客运中心只占画面西缘，因此“北外滩”过于宽泛，“上海港国际客运中心”也不是画面主体，正式项目名最能解释整张图。

## Observations

- 官方玩法说明表示答案在拼图里，地图 Cache 只用于加快收集；领取坐标不是答案提取材料。
- 同一坐标稳定返回同一图片，不同远距离坐标会重复同片，数据符合确定性空间哈希近似均匀映射到 64 个桶。
- 每片有效图像核心为 140×140，客户端源图为 1120×1120，故完整图固定为 **8×8，共 64 片**。
- 最终导出 `ccbc17-geo-results-1787278136986.json` 记录 P05–P168 共 164 次本轮结果；连同断点，已完成 P01–P168。页面最终报告 61 种不同图像，未发生错误。
- 复原图中可以直接看见黄浦江、滨江步道、船只、游艇港池、成组航运办公楼和项目北侧街区。

## Extraction

`work/jigsaw_solve.py` 是本假设族的唯一参数化复现脚本。它为每片识别 140×140 逻辑核心和四边拼齿，枚举四种旋转，使用透明边界几何及 RGB 接缝建立精确邻接，再把断开的分量与候选卫星图做 SIFT/单应匹配。

61 片首先形成：

- 一个 **53 片**、无坐标冲突的主分量；
- 一个 **3 片**分量；
- 五个单片分量。

上海北外滩 Google z18 卫星图给出 **55 个可信单应定位**。这些定位的中心落在间距恰为 140 px 的网格上，整体均方根残差只有 **0.626 px**。主分量确定全局坐标系；3 片分量中的两张有图像特征，可唯一确定整个刚性分量的平移和旋转，因此其中没有特征的纯水面片 `ea661231…` 也被唯一带到 `(5,7)`、旋转 270°。五个单片同样由位置和朝向唯一确定。

最终 61 片全部落位，未占用格只剩：

| y\x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | ✓ | ✓ | ✓ | ✓ | ✓ | 缺 | ✓ | ✓ |
| 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4 | ✓ | ✓ | ✓ | ✓ | 缺 | ✓ | ✓ | ✓ |
| 5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 6 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 缺 | ✓ |
| 7 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

把参考瓦片向北平移一格后，同一 140 px 网格可直接裁出完整 1120×1120 底图；三个红框处正好补齐上述缺口。这既复原了完整画面，也独立验证了拼片排列和卫星图来源。

## Candidate audit

### 主候选：上海国际航运服务中心

支持证据：

1. **像素级定位。** 55/61 片与同一北外滩卫星图形成可靠单应，网格残差 0.626 px，不是一般性的城市外观相似。
2. **地理中心。** 复原图中心约 31.25154°N, 121.49833°E，位于北外滩滨江航运建筑群内。
3. **项目构成。** [虹口区政府项目介绍](https://www.shhk.gov.cn/zjhk/001003/001003001/20170417/9f1b4199-e29b-4bd2-9df5-031cfcd302a4.html)所述“近八百米沿江岸线、东中西三幅地块、办公商业和游艇港池”全部出现在拼图中；政府页面的项目照片也能看到同一游艇港池和办公楼群。
4. **范围排歧。** [项目开工资料](https://kab.sww.sh.gov.cn/xwzx/001001/20090323/EF9E930F-620B-4E03-A509-97E3A6168D0C.html)给出东起秦皇岛路、西至公平路的 780 米岸线，并说明它与西侧上海港国际客运中心相连。复原图主体正是这一项目，而“北外滩”是包含它和客运中心在内的更大区域。

尚未由用户或比赛网站确认，因此状态保持 `candidate`。三张未领取拼片不影响结论：它们已经由像素一致的参考底图补出，且不包含另一个地点或额外文字。画面也没有支持二次字母提取的特殊标记；题面的“碎得很有规律”由 8×8 标准拼图机制充分解释。

## Submission history

只记录用户或比赛网站明确反馈过的提交；当前未提交任何候选。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |

## Evidence and artifacts

- 官方题面：<https://heptadec.cipherpuzzles.com/puzzle/till-the-lands-become-a-puzzle>
- 寻迹应用：<https://caching.cipherpuzzles.com/>（需由官方入口建立队伍会话）
- `work/ccbc17-geo-results-1787278136986.json`：8 小时采集最终导出；P01–P168 已完成，队伍 61/64 种。
- `work/visual/pieces/`：61 个唯一原始 PNG。
- `work/visual/pieces-inventory/`：61 片稳定清单和六张联系表。
- `work/jigsaw_solve.py`：参数化拼齿、接缝、刚性分量和参考图定位脚本。
- `work/visual/jigsaw/assembly.tsv`：53、3、1、1、1、1、1 片分量的原始坐标/旋转。
- `work/visual/jigsaw/reference-matches.tsv`：每片 SIFT/单应证据。
- `work/visual/jigsaw/reference-grid-placements.tsv`：61 片最终 8×8 坐标、旋转和定位来源。
- `work/visual/jigsaw/reference-grid-summary.txt`：55 个参考定位、0.626 px RMSE 和三处缺格摘要。
- `work/visual/jigsaw/reference-assisted-layout.png`：61 片复原总图。
- `work/visual/jigsaw/reference-assisted-layout-annotated.png`：标出三处未领取格的复原图。
- `work/visual/jigsaw/reference-source-grid.jpg`：从匹配卫星瓦片裁出的完整 1120×1120 底图。
- `work/visual/jigsaw/reference-source-grid-annotated.jpg`：8×8 网格及三处原缺口标注。
- `work/visual/reference-official-shanghai-international-shipping-service-center.jpg`、`reference-official-shanghai-international-shipping-service-center-marina.jpg`：虹口区政府页面的项目效果图和实景照片。
- `artifacts/jigsaw_solve.py`：候选使用的脚本快照。
- `artifacts/reference-grid-placements.tsv`、`reference-grid-summary.txt`：最终 61 片布局和定位指标的持久证据。
- `artifacts/reference-assisted-layout-annotated.png`：61 张实收拼片与三处缺口。
- `artifacts/reference-source-grid-annotated.jpg`：同源卫星图补齐后的完整 8×8 画面。

## Important failed routes

- **6×6 推断错误。** `FALLBACK_PIECE_SIZE=188` 只是显示备用尺寸；140 px 核心配合 1120 px 源图明确给出 8×8。
- **固定位置挂机无效。** 同一位置只会增加实例数，不增加唯一拼片。
- **简单地理分区不成立。** 极远坐标会重复同片；最有效采集方式是大量新坐标。
- **新开 360 的 Playwright 路径不可用。** `360ChromeX.exe` 在远程调试管道下退出；登录名额已满时应复用既有标签内的 Snippet。
- **早期地点类比均被像素证据否定。** 摩纳哥 / Mareterra、香港尖沙咀与会展中心、澳门渔人码头、悉尼 Darling Harbour 都没有可靠单应；不能因“滨水、高楼、工地”这些泛特征提交。
- **“北外滩”过宽。** 它是区域名；项目的岸线、三地块和游艇港池特征共同指向更具体的上海国际航运服务中心。
- 原始 SingleFile 题面只保存外壳和头像，没有寻迹拼片或完整源图，不能单凭 `input/*.html` 恢复拼图。

## Next action

由用户向比赛网站提交 **上海国际航运服务中心**，并把明确的接受或拒绝结果告知本任务；收到结果后追加 `Submission history` 并按反馈更新状态。若网站要求更短地名，优先尝试同一项目的简称，而不是改投更宽泛的“北外滩”。
