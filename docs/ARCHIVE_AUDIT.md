# CCBC 17 赛后归档核查

核查日期：**2026-09-11**。范围：本仓库六个实际题区、65 份节点解答、WIG 状态、漫画素材题图、关键接受记录与目录引用。依据均为现有本地材料；本次没有登录比赛网站、重新提交答案或查询公开题解。

## 结论与统计口径

**按现有记录，比赛已经完成，全部已建档节点均已通过，漫画素材大全已经收集齐。** “全部通过”是验收状态结论，不能等同于“每题都有从头到尾可独立重跑的完整题解”。

| 检查项 | 结果 | 依据 |
| --- | --- | --- |
| 节点状态 | 65/65 为 accepted，其余五种状态均为 0 | 所有节点 `solution.md` 的元数据与 [自动总表](../SUMMARY.md) |
| 节点类型 | puzzle 41、subpuzzle 4、meta 20 | 生成总表所用的实际节点记录 |
| 置信度字段 | high 64、medium 1 | 唯一 medium 是已通过的 [d-meta14](../rounds/summer-of-talents/nodes/d-meta14-surrounded-by-villains-what-now/solution.md)；未自行调整 |
| 常规 B/C/E 区覆盖 | 11/11、10/10、11/11 | 显式 feeder 池的解析结果 |
| D 区 Meta | 15 道门派 Meta + 1 道区域终极 Meta 全部 accepted | [艺人之夏](../rounds/summer-of-talents/ROUND.md) |
| Final Meta 与 a9 | 2026-09-03 均已接受，用户明确确认正式完赛 | [Final Meta 提交记录](../rounds/the-internet-is-dead/nodes/final-meta-seeker-sinking-into-the-net/solution.md#submission-history)、[a9](../rounds/wig/nodes/a9/solution.md) |
| 漫画素材册 | 71/71；编号 001–071 的题图全部存在 | [网站回执摘录](../rounds/wig/nodes/manga-013/artifacts/verification-2026-09-11.txt)、[素材原图目录](../rounds/summer-of-talents/shared/manga/) |

65 是本仓库的节点数量，不是赛事独立题目总量：漫画素材只单独建立了 4 个补档节点，其余 67 道主要记录于共享清单和 Meta 笔记；a9 与 Final Meta 则分别记录同一终局。因此不能将 65 与 71 直接相加。

### 直接支持完赛的记录

- Final Meta 的提交表同时保存网站接受与用户确认，最终字符串为 **`艺人得道，弃圈†升天†`**，两个 `†` 都是 U+2020，不能从档案中删去。[Final Meta 解答](../rounds/the-internet-is-dead/nodes/final-meta-seeker-sinking-into-the-net/solution.md)
- 漫画素材最后四项依次完成：070「中」使 67→68，020「主唱」使 68→69，032「纸牌」使 69→70，013「列车」使 70→71。[WIG 状态](../rounds/wig/STATE.md)
- 013 的回执文件保存了正常提交后的可见页面状态：“已收集 71 张，共 71 张”，且素材关键词为“列车”。[回执摘录](../rounds/wig/nodes/manga-013/artifacts/verification-2026-09-11.txt)

## 本次目录与文档整理

1. 根 [README](../README.md) 改为比赛归档入口；原模板 README 保存在 [WORKFLOW.md](WORKFLOW.md)，保留复用说明与建题命令。
2. 补齐六个 `ROUND.md` 的实际内容说明和阅读导航。节点编号与原始目录位置保留，WIG 状态增加当前归档结论，早期推进记录明确标作历史。
3. 整理 26 份解答中的过期状态说明、下一步、引用或记录格式。所有节点原有的 `status`、`answer`、`confidence`、`feeders` 均保持不变；仅修改过的解答将 `updated` 更新到本次日期。
4. B 区 Meta 明确区分旧反推候选与 b4、b6、b10 后来的最终答案；旧推导仍保存在本题中，不再将旧候选列作小题待办。
5. C 区 Meta 同步 c03=JOHN TYLER 与转换串 CARLOAZEGLIOCIAMPI；现有 [复算脚本](../rounds/toringmoni/nodes/c-meta-henry-who-sees-truth/artifacts/build_slot_map.py) 与 [槽位表](../rounds/toringmoni/nodes/c-meta-henry-who-sees-truth/artifacts/meta-slot-map.tsv) 已写入十个最终 feeder、转换串和实际提取字母。
6. E 区 Meta 同步 e05=ALFALFA 的 row 5：48 格生成流命中 14 个公开格，橙字为 L。保留尚未恢复的其他行，不声称重跑了缺失的历史穷举程序。
7. 修正 d-meta12 原题图片引用中截短的文件名；e05 的 10 个失效临时文件链接改为明确的缺失记录。
8. c06 的三列表格整理为统一四列，将旧正文明确记载的 2026-08-18 用户确认补入表中；原有记录保留。这不是一次新的答案提交。
9. 修复 `.gitignore` 对原始音视频的误忽略，13 个已有媒体文件现在可被 Git 纳入归档。`work/` 中的临时媒体继续忽略。
10. 使用生成工具重建 [SUMMARY.md](../SUMMARY.md)，没有手工编辑总表或改动任何 `input/`、`shared/` 文件内容。

### 音视频归档范围

| 位置 | 已有文件 | 大致体积 |
| --- | ---: | ---: |
| B 区 Meta `input/1.mp3` 至 `11.mp3` | 11 段音频 | 9.1 MiB |
| b4 `input/保持解谜就无人爆炸.mp3` | 1 段音频 | 3.2 MiB |
| WIG `shared/wig-web/` 中小七生活视频 | 1 段视频 | 2.6 MiB |

这些都是原先已经存在的本地证据。本次仅解除忽略规则，没有重新下载、移动、修改或提交媒体文件；在当前 Git 状态中它们显示为待纳入版本管理的文件。

## 尚存的归档缺口

以下是从现有笔记核实的重要缺口，不是未通过题目清单。本次负责核对和整理，没有以已知答案反造缺失的解题步骤。

| 记录 | 尚缺的内容 | 后续补档方向 |
| --- | --- | --- |
| [b1 欢迎来到互联网](../rounds/shi-qi-love-in-chaos/nodes/b1-welcome-to-the-internet/solution.md) | 八公、小白、赤丸三个局部图的完整载体未补齐；正文明确记有用户确认，但提交表未单独列最终答案及其确认日期 | 补齐局部推导；从原任务恢复实际确认记录，不能把本次核查日期当作提交日期 |
| [b3 雪为何色](../rounds/shi-qi-love-in-chaos/nodes/b3-color-of-snow/solution.md) | 元数据为 accepted，提取链已有记录，但提交表只明确记录中间答案确认，没有最终 REST 的独立回执 | 保留原有接受状态，补录原始最终确认记录；本次未新增或推测判定 |
| [B 区 Meta](../rounds/shi-qi-love-in-chaos/nodes/b-meta-pandora-that-is-trapped/solution.md) | 旧提取用 WONDER / PERSPECTIVE / CURRENT，实际对应节点后来接受 PEEP / LIGHTNING / INFLOOD | 重新核对三行音频、含“音”名称及最终 feeder 的配对；PARADOXXING 的用户接受记录本身完整 |
| [c01 把握今朝](../rounds/toringmoni/nodes/c01-carpe-diem/solution.md) | 已由 Meta 与用户确认 PITA，但目标分钟的鸟位置如何在题内唯一导向该词仍未复原 | 补齐题面内最后一步 |
| [c06 情迷翡冷翠](../rounds/toringmoni/nodes/c06-love-in-florence/solution.md) | 六段只完整复原第 5 段，最后六段结果到 JAMES SHOAL 的提取未复原；答案由用户提供 | 补齐其余段落、最终提取及脚本所需外部词表 |
| [c10 周游列国](../rounds/toringmoni/nodes/c10-traveling-around/solution.md) | 四件纪念品的确切英文名未定，部分字母由已确认答案与 Meta 约束锁定 | 补齐逐位求同的完整原始词对 |
| [e04 Crazy Icomania](../rounds/irrational-manager-hypothesis/nodes/e04-crazy-icomania/solution.md) | 第三个正确中间答案及导向 SIDEBAR 的完整机制未留存 | 从已有参考记录恢复缺失阶段 |
| [e05](../rounds/irrational-manager-hypothesis/nodes/e05-happy-angry-sad-joy-office/solution.md) | c6/c8/c9 的确切 emoji 落位未唯一复原；10 个旧临时脚本/结果缺失 | 恢复脚本并补齐 128 格填表；保留正文中的 ALFALFA 生成流 |
| [E 区 Meta](../rounds/irrational-manager-hypothesis/nodes/e-meta-cowell-moving-forward/solution.md) | row 5 已同步；rows 1/2 与 row 11 的目标 E 尚未独立复原 | 继续查证三行的题面支持与生成规则 |
| [d-meta14](../rounds/summer-of-talents/nodes/d-meta14-surrounded-by-villains-what-now/solution.md) | 第一条成语的确切全文与素材编号未定 | 补齐成语与素材对应；提取出的“文笔”已有正确记录 |

[b6](../rounds/shi-qi-love-in-chaos/nodes/b6-magic-square-trading-strategy/solution.md) 的前两条暗语典故说明、[e08](../rounds/irrational-manager-hypothesis/nodes/e08-one-legendary-night/solution.md) 的局部牌面歧义也保留在各自笔记中，均不影响已有接受记录。

### 素材清单与依赖结构

- 艺人之夏的 15 道门派 Meta 仍使用 `feeders: unknown`，因此总表会显示 `unknown Meta scope`。这是结构化依赖尚未建齐，并非 15 道 Meta 仍待解。
- 71 张素材都有原图，但只有最后补档的 4 道拥有独立节点解答。若要形成“每张素材一份完整解答”的题解集，仍需将其余 67 道的现有记录逐题核对并建档。
- `shared/FEEDER_LIST.md`、`HANDOFF.md`、`AGENT_NOTES.md` 包含旧候选、旧统计和旧任务安排，是不可改写的历史材料。当前进度请读 `solution.md`、`SUMMARY.md`、WIG `STATE.md`，不要从旧交接清单推断尚有未解题。

### 本地工作目录与复现

整理前的文件盘点不含 `.git/`：约 9.68 万个本地文件，其中各节点 `work/` 合计约 **12.8 GiB**。Git 当时仅跟踪 872 个路径；两者差异主要来自被忽略的实验、下载、缓存及运行依赖。

现有解答中，至少 43 个节点以行内路径引用了当前仍存在的 `work/` 内容。这些文件不能因为节点已接受就直接认定为无用。此次保留全部本地工作材料；普通 Git 克隆仍不会附带被忽略的文件，因此本仓库尚不能视为完全自包含的复现包。

## 验证结果

| 检查 | 结果 |
| --- | --- |
| `python tools/build_summary.py` | 65 个节点、6 个题区；元数据及显式依赖校验通过，无错误或警告 |
| `python tools/next_nodes.py` | 可开工 0、候选待核验 0、等待或阻塞 0；隐藏已接受节点 65 |
| `python tools/doctor.py` | 必需的仓库结构与运行条件通过；本机 Python 3.12.10，可选 Tesseract 未安装 |
| C 区 Meta 复算 | 30 槽覆盖完整，所有转换串长度和索引通过，输出 BACKUPANDTESTSUMMARIZETHEGISTS |
| E 区 Meta row 5 | 48 格、14 个公开格全部匹配，末格 L |
| 漫画素材题图 | 001–071 编号集合完整 |
| 文档与改动检查 | 本次新增/修改文档的有效本地文件链接已核对；Git 空白检查通过 |
| 历史保护 | 65 个节点的答案、状态、置信度和 feeder 元数据未改变；原有提交表记录保留；原始输入和共享资料未改动 |

这些检查验证了当前统计、文档和已同步的两处复现内容，没有重新运行所有题目的历史脚本。当前没有比赛待办；若继续完善仓库，应按上表选择具体题目补档。
