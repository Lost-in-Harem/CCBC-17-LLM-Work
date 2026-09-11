# CCBC 17 · LLM 解题与调查归档

本仓库保存 CCBC 17 的个人解题工作：原始题面、WIG 互动调查、逐题解答、提交反馈，以及用于复核的脚本和图表。解题过程中使用了 LLM 辅助，也包含用户提供的答案、纠正与确认；每题的实际过程以 `solution.md` 为准。

**截至 2026-09-11：已完赛，仓库中 65 个节点全部记录为 `accepted`，漫画素材大全已确认 71/71。** Final Meta 与 WIG 最终事件于 2026-09-03 确认完成，最后四张漫画素材随后补齐。

仓库包含完整答案和剧情剧透。已通过表示答案获得确认；部分题目的独立推导、素材对应关系和复现文件仍有归档缺口，详见 [归档核查](docs/ARCHIVE_AUDIT.md)。

## 从哪里开始

- [全场题目与答案总表](SUMMARY.md)：按题区查看状态、答案、摘要和逐题入口，由工具自动生成。
- [完赛与归档核查](docs/ARCHIVE_AUDIT.md)：统计口径、完赛证据、已修复的问题和仍需补齐的记录。
- [WIG 调查状态](rounds/wig/STATE.md)：模拟终端中的人物、邮件、通话、应用线索与最终结局。
- [比赛背景与约定](HUNT.md)、[剧情笔记本](NOTE.md)：理解比赛框架与故事。
- [工作流与模板用法](docs/WORKFLOW.md)、[工具说明](tools/README.md)：复核、续写或复用仓库结构。

## 题区

以下数量是**本仓库独立建档的节点数**，不等于赛事独立题目总数。

| 题区 | 内容 | 节点数 | 记录状态 |
| --- | --- | ---: | --- |
| [卡美洛终端 WIG](rounds/wig/ROUND.md) | 9 个调查事件 + 4 个补档漫画小题 | 13 | 全部 accepted |
| [祸乱时柒的爱情](rounds/shi-qi-love-in-chaos/ROUND.md) | 11 道普通题 + 1 道 Meta | 12 | 全部 accepted |
| [视中监](rounds/toringmoni/ROUND.md) | 10 道普通题 + 1 道 Meta | 11 | 全部 accepted |
| [艺人之夏](rounds/summer-of-talents/ROUND.md) | 15 道门派 Meta + 1 道区域终极 Meta | 16 | 全部 accepted |
| [不理性经纪人假设](rounds/irrational-manager-hypothesis/ROUND.md) | 11 道普通题 + 1 道 Meta | 12 | 全部 accepted |
| [互联网过载](rounds/the-internet-is-dead/ROUND.md) | Final Meta | 1 | accepted |
| **合计** | 41 个 puzzle、4 个 subpuzzle、20 个 meta | **65** | **65 accepted** |

“漫画素材大全”另有 **71 张素材**：全部编号题图保存在艺人之夏的共享材料中，013、020、032、070 的后续独立解答建在 WIG 下。其余素材主要保存在旧清单和 Meta 笔记中，没有逐一建立 67 个独立节点。WIG `a9` 与 Final Meta 也是同一终局的两份事件记录，因此不能简单把节点数与素材数相加作为赛事题量。

## 目录结构

```text
.
├── README.md                      # 仓库入口
├── SUMMARY.md                     # 自动生成的题目与答案总表
├── HUNT.md                        # 全场背景和稳定约定
├── NOTE.md                        # 人工维护的剧情笔记
├── AGENTS.md                      # 解题任务的范围与记录规则
├── PUZZLE_TASK_PROMPT.md           # 普通题任务模板
├── META_TASK_PROMPT.md             # Meta 任务模板
├── VERIFY_TASK_PROMPT.md           # 候选核验模板
├── docs/
│   ├── ARCHIVE_AUDIT.md            # 2026-09-11 归档核查
│   └── WORKFLOW.md                 # 原模板 README 的用法说明
├── tools/                         # 建题、检查、移动节点、生成总表
├── .agents/skills/                 # 解题与视觉检查工作流
└── rounds/
    ├── _template/                 # 新节点模板，不计入进度
    ├── wig/                       # WIG 调查及部分漫画小题
    ├── shi-qi-love-in-chaos/       # 祸乱时柒的爱情
    ├── toringmoni/                 # 视中监
    ├── summer-of-talents/          # 艺人之夏
    ├── irrational-manager-hypothesis/
    └── the-internet-is-dead/       # Final Meta
```

常规题区采用以下结构；WIG 另有一份跨事件的 `STATE.md`：

```text
rounds/<round-id>/
├── ROUND.md                       # 题区说明与阅读入口
├── shared/                        # 多题共用的原始资料，只读
└── nodes/<node-id>/
    ├── input/                     # 本题原始题面，只读
    ├── solution.md                # 唯一的解答、反馈与后续工作记录
    ├── artifacts/                 # 值得长期保存的复核材料
    └── work/                      # 临时提取、下载、OCR 与实验
```

`solution.md` 开头的元数据记录题型、答案、状态和依赖；正文保留结论、推导、失败路线及 `Submission history`。`feeders` 是题目依赖的依据，可跨题区，也可形成环；不要仅凭目录位置推定依赖。

## 查看与复核

阅读 Markdown 不需要额外环境。仓库结构工具使用 **Python 3.10 或以上版本**；从仓库根目录执行：

```sh
# 校验节点元数据和依赖，并重新生成总表
python tools/build_summary.py

# 查看是否还有待处理节点
python tools/next_nodes.py

# 检查一个节点的输入、依赖和记录
python tools/inspect_node.py the-internet-is-dead/final-meta-seeker-sinking-into-the-net

# 检查当前机器的可选图像、OCR、PDF、音视频能力
python tools/doctor.py
```

各题复算脚本的依赖不同，应先阅读该题的解答说明。`doctor.py` 检查的是通用能力；通过结构校验不等于所有历史解题脚本都能在新机器上直接运行。

## 归档约定

- `input/` 与 `shared/` 保留采集时的原貌；其中的旧进度清单是历史快照，最新状态以各题 `solution.md` 和 WIG `STATE.md` 为准。
- 临时实验留在 `work/`，默认不纳入 Git。当前本地工作材料约 12.8 GiB，普通克隆不包含这些被忽略的文件；清理前应先检查解答的复现依赖。
- 原始题面与 `artifacts/` 中的音视频可纳入版本管理。复核必需的少量结果放在 `artifacts/`，不要把整个实验目录当作最终解答。
- `accepted` 表示已有确认，`confidence` 是记录中的置信度，两者不代表相同的事。不得因推导缺口自行撤销正确回执，也不得用推测补造回执。
- 原始提交记录和失败路线保留在原题中。总表只运行生成工具更新。

如需继续补写某题，按 [AGENTS.md](AGENTS.md) 指定目录，并从其 `Next action` 恢复。新建题目、显式依赖和安全移动节点的完整用法见 [工作流说明](docs/WORKFLOW.md)。
