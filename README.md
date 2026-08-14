# Puzzle Hunt for AI

一个供你手动启动多个平级 Agent 任务的轻量模板。

核心模型只有两层：

1. **Round**：区域、章节或主题分组；
2. **Node**：任何能产出答案的单位，包括普通题、复合页面中的小题和 Meta。

Node 之间用显式 `feeders` 组成任意依赖图。依赖可以只覆盖部分题目、跨 Round、指向另一个 Meta，甚至形成环。

每个 Round 还维护一个轻量的 **feeder pool**：普通题和小题默认进入池中。一个或多个 Meta 对池中题目的覆盖关系会自动显示在总表里。

## 目录结构

```text
.
├─ AGENTS.md
├─ HUNT.md
├─ PUZZLE_TASK_PROMPT.md
├─ META_TASK_PROMPT.md
├─ VERIFY_TASK_PROMPT.md
├─ SUMMARY.md
├─ .agents/
│  └─ skills/
│     ├─ work-on-node/
│     └─ inspect-puzzle-visuals/
├─ tools/
│  ├─ README.md
│  ├─ doctor.py
│  ├─ new_puzzle.py
│  ├─ move_node.py
│  ├─ next_nodes.py
│  ├─ build_summary.py
│  └─ inspect_node.py
└─ rounds/
   ├─ _template/
   ├─ pupae/
   │  ├─ ROUND.md
   │  ├─ shared/              # 关系图、复合页面等 Round 共享题面
   │  │  └─ graph-hunt/
   │  └─ nodes/
   │     ├─ 101/
   │     │  ├─ input/
   │     │  ├─ work/
   │     │  ├─ artifacts/
   │     │  └─ solution.md
   │     ├─ 104/
   │     └─ 301/
   └─ final/
      ├─ ROUND.md
      ├─ shared/
      └─ nodes/
         └─ final-meta/
```

每个 Node 对应一个可以手动启动、暂停和恢复的 Agent 任务。

### 有状态 WIG 区域

本仓库的 `rounds/wig/` 是一个例外：它承载连续变化的终端、邮件、通话、搜索和剧情状态，而不是传统的“小题 → Meta”题区。

- `ROUND.md` 记录稳定的 WIG 设定与目录约定；
- `STATE.md` 是跨应用的当前状态、已确认事实、开放问题和待采集清单；
- `shared/` 保存用户采集的原始网页或媒体，Agent 不修改；
- `nodes/` 仍按每个需要答案或判定的剧情事件保存可复核推理。

默认仍按单个 Node 开任务。只有用户明确指定“整个 WIG 区域”时，任务才可以在 `rounds/wig/` 内整理跨 Node 状态；这个例外不扩展到其他 Round。

## 为什么不用固定的 puzzles/metas 树

有些 Hunt 并不是“全部小题喂给一个 Meta”。以 PnKU 蛹区为例：

- `104` 只使用 `101、102、103`；
- `307` 使用 `301～306`；
- `201～204` 互相作为 feeder，形成有环依赖；
- 不同普通题流向不同 Meta；
- 一个复合页面中的小题也可以独立成为 feeder。

因此模板不会根据 Round 自动猜 feeder，也不把 `all` 设为默认。每条依赖都由产生答案的 Node 明确声明。

## 第一次使用

把这个目录作为一个本地项目打开。所有解题任务选择同一个本地项目，不使用 worktree。

先填写一次 `HUNT.md`，记录答案格式、解锁方式、故事背景和其他全场稳定规则。不要把答案或当前进度复制进去。

检查当前机器能够使用哪些可选视觉和多媒体能力：

```text
python tools/doctor.py
```

缺少可选工具不会影响核心 Node、feeder 和总表流程；它只会关闭对应的 OCR、PDF、视频或音频辅助能力。

项目根目录的 `AGENTS.md` 会告诉每个任务：

- 禁止启动 subagent；
- 只处理用户指定的一个 Node；
- 不修改其他 Node；
- 只能读取显式 feeder；
- 不手工编辑总表；
- 每轮结束前保存进度并重建总表。

## 新建普通题

```text
python tools/new_puzzle.py p001 -r forest -t "林中来信" --round-title "Enchanted Forest"
```

得到：

```text
rounds/forest/nodes/p001/
```

同一 Round 后续题目不必重复 `--round-title`：

```text
python tools/new_puzzle.py p002 -r forest -t "蘑菇环"
```

如果暂时不知道所属 Round，可以先放进：

```text
python tools/new_puzzle.py p001 -r unassigned -t "未知区域题目"
```

## 安全移动或重命名 Node

先停止正在写入该 Node 及其引用者的任务，再预览移动计划：

```text
python tools/move_node.py unassigned/p001 forest/p001 --dry-run
```

确认后执行：

```text
python tools/move_node.py unassigned/p001 forest/p001
```

工具会再次展示计划，只有输入 `MOVE` 才会移动整个目录、更新 Node 的
`node_id` 与 `round`、改写所有结构化显式 feeder 引用并重建总表。移动失败或
校验失败时会自动回滚。它不会改写正文中的普通文字，只会列出可能仍含旧路径的
`solution.md` 供人工复核。

跨 Round 移动会保留本 Node 原有裸 feeder 的语义，把它们改为明确的跨 Round
引用。若 Node 声明了共享 `source`，必须先在目标 Round 准备对应目录并传入
`--new-source SOURCE`，或明确使用 `--clear-source`。`round_feeder: yes` 的
Node 跨 Round 后会改变两个 Round 的 feeder pool，工具只警告这些影响，不猜测
应如何修改各 Meta 的 pool 声明。

## 新建 Meta 并指定部分 feeder

```text
python tools/new_puzzle.py 104 -r pupae -k meta -t "腰带" -f 101 102 103
```

生成的 frontmatter：

```yaml
node_id: 104
kind: meta
round: pupae
feeders: 101, 102, 103
```

无斜杠的 ID 总是在当前 Round 内解析。

## 一个 Meta 使用整个 Round

普通题与小题默认带有：

```yaml
round_feeder: yes
```

如果一个 Meta 使用整个区域的所有 feeder：

```text
python tools/new_puzzle.py forest-meta -r forest -k meta ^
  -t "Forest Meta" -f all-round-feeders
```

`all-round-feeders` 只选择同 Round 中 `round_feeder: yes` 的 Node，不会误把其他 Meta、辅助节点或共享页面算进去。它也可以和其他精确 feeder 或外部 Round 的 feeder pool 组合使用。

## 多道 Meta 合计覆盖全部小题

让每道 Meta 声明自己的实际子集：

```text
python tools/new_puzzle.py meta-a -r forest -k meta -f p001 p003 p005
python tools/new_puzzle.py meta-b -r forest -k meta -f p002 p004 p006
```

总表会计算：

```text
Feeder coverage: 6/6
```

如果漏了一题，会显示：

```text
unassigned: p006
```

如果一题同时喂给多道 Meta，会显示：

```text
shared: p003 -> meta-a, meta-b
```

重叠是合法的，只会展示，不会判错。

如果某个普通题、小题只是内部中间步骤，不应属于 Round 的 Meta feeder 池，创建时使用：

```text
python tools/new_puzzle.py helper-a -r forest --round-feeder no
```

Meta 自身默认 `round_feeder: no`；如果某道 Meta 也要进入同 Round 后续 Meta 的 feeder pool，可以显式传入 `--round-feeder yes`。

## 有环依赖

有环是允许的。蛹区 `201～204` 可以分别创建为：

```text
python tools/new_puzzle.py 201 -r pupae -k meta -f 202 203 204
python tools/new_puzzle.py 202 -r pupae -k meta -f 201 203 204
python tools/new_puzzle.py 203 -r pupae -k meta -f 201 202 204
python tools/new_puzzle.py 204 -r pupae -k meta -f 201 202 203
```

先创建的 Node 会暂时提示 feeder 尚不存在；全部创建后提示自动消失。生成器不会把环当成错误。

## 页面内小题

如果一个页面包含多道能分别产出答案的小题，就让每个小题成为独立 Node：

```text
python tools/new_puzzle.py 301 -r pupae -k subpuzzle ^
  -t "图寻-文" --parent graph-hunt --source graph-hunt
```

对应：

```yaml
kind: subpuzzle
parent: graph-hunt
source: graph-hunt
```

- `parent` 表示它属于哪个复合题或页面；
- `source` 表示它还可以读取 `rounds/pupae/shared/graph-hunt/`；
- 小题自己的临时结果仍放在 `rounds/pupae/nodes/301/work/`。

这样共享题面只下载一次，但 `301～306` 可以分别由不同 Agent 处理，Meta 也能精确引用其中任意一个。

## 跨 Round 与 Final Meta

Final Meta 就是独立 `final` Round 中的普通 Meta Node。部分跨 Round feeder 使用 `round/node`：

```text
python tools/new_puzzle.py final-meta -r final -k meta -t "Final Meta" ^
  -f forest/m01 city/m01 museum/m01
```

如果它使用一个或多个外部 Round 的整个默认 feeder pool：

```text
python tools/new_puzzle.py final-meta -r final -k meta -t "Final Meta" ^
  -f forest/all-round-feeders city/all-round-feeders pupae/104
```

引用规则：

| 写法                      | 含义                               |
| ------------------------- | ---------------------------------- |
| `101`                     | 当前 Round 中的 Node `101`         |
| `pupae/101`               | `pupae` Round 中的 Node `101`      |
| `pupae/104`               | `pupae` Round 中的 Meta Node `104` |
| `all-round-feeders`       | 当前 Round 的默认 feeder pool      |
| `pupae/all-round-feeders` | `pupae` Round 的默认 feeder pool   |
| `unknown`                 | feeder 关系尚未确定                |

`feeders` 不区分“使用答案”还是“使用题面”。列入或由 pool 展开的 Node 都允许 Meta 读取其 `input/`、`solution.md`、声明的共享 `source` 和必要的 `artifacts/`，但不能修改。

Meta 未知 feeder 时不要猜：

```text
python tools/new_puzzle.py m01 -r strange-round -k meta -t "Unknown Meta"
```

它会得到 `feeders: unknown`。待关系图或题面确认后，再改成精确列表。

## 检查一个 Node

解题任务启动时会先运行：

```text
python tools/inspect_node.py forest/p001
```

这个只读工具会：

- 列出本题输入和共享题面；
- 在环境支持时显示图片尺寸、PDF 页数和 WAV 时长；
- 提示 HTML 引用但尚未下载的本地资源；
- 展开同 Round 或跨 Round feeder pool；
- 汇总 feeder 的状态、答案、置信度、摘要和材料位置；
- 显示当前 `Next action` 和与本题有关的校验警告。

它只向终端输出，不创建第二份状态文件，也不把 OCR 当成题面事实。输入超过 80 个文件时默认只展示前 80 个；确实需要完整清单时加 `--all-files`。

## 手动启动任务

Codex 会发现仓库中的 repo-local skills。普通题、小题、Meta 和恢复任务都可以使用同一个入口：

```text
$work-on-node rounds/<ROUND_ID>/nodes/<NODE_ID>
```

它读取 `solution.md` 的 `kind`，自动采用普通题或 Meta 流程，并从已有 `Next action` 恢复。

如果使用的 Agent 环境不支持 repo-local skills，则使用兼容入口：

1. 在 Codex 中新建普通任务，选择这个本地项目。
2. 复制 `PUZZLE_TASK_PROMPT.md`。
3. 替换 `<ROUND_ID>` 和 `<NODE_ID>`。

Meta 使用 `META_TASK_PROMPT.md`。它只读取自身 `feeders` 直接指向或 feeder pool 展开的 Node；若为 `unknown`，先从自身题面和 Round 共享关系图确认依赖。

不同 Node 可以同时运行，因为它们修改不同目录。不要让两个任务同时修改同一 Node。

视觉、空间、网页归档、PDF、视频或音频题会按需使用 `$inspect-puzzle-visuals`。它的确定性脚本只把派生材料写到当前 Node 的 `work/visual/`；命令清单见 `tools/README.md`。

如果不确定接下来该手动启动哪一题，运行：

```text
python tools/next_nodes.py
```

它只读取现有状态，分组显示可开工、候选待核验、等待 feeder 或已经阻塞的 Node，并给出可复制的 `$work-on-node` 命令。它不会启动 Agent、创建锁或修改任务。

## 暂停与恢复

在原任务或新任务中说：

```text
$work-on-node rounds/<ROUND_ID>/nodes/<NODE_ID>
```

`solution.md` 是恢复点，不依赖旧聊天记录。

## 核验候选答案

对 Meta、低置信候选或提交代价较高的答案，可以先停止原任务，再手动启动一个新任务并使用 `VERIFY_TASK_PROMPT.md`。

核验任务会从原始题面重现机制和提取，专门检查转录错误、未使用信息与反例。它可以调整候选和置信度，但仍然只有你可以确认 `accepted`。

## Node 记录

```yaml
---
node_id: 104
title: 腰带
kind: meta
round: pupae
parent:
source:
round_feeder: no
feeders: 101, 102, 103
status: candidate
answer: I
confidence: high
summary: 将三张参宿小题图直接拼合并提取得到 I
updated: 2026-07-30
---
```

`kind` 允许：

- `puzzle`：普通题；
- `subpuzzle`：复合页面中独立产出答案的小题；
- `meta`：依赖其他 Node 输出的题。

`round_feeder` 允许：

- `yes`：属于本 Round 的默认 feeder pool；
- `no`：不属于该池，但仍可被其他 Node 用 ID 显式引用。

状态允许：

| 状态        | 含义                       |
| ----------- | -------------------------- |
| `pending`   | 已建目录，尚未开始         |
| `working`   | 正在探索，并有明确下一步   |
| `candidate` | 有可解释、可复核的答案候选 |
| `blocked`   | 暂时没有可靠下一步         |
| `accepted`  | 你或比赛网站确认正确       |
| `rejected`  | 最近候选被判错，需要新证据 |

只有你可以授权把状态改成 `accepted`。

进入 `candidate` 时还要填写 `solution.md` 中的 `Candidate audit`，记录答案格式、未使用信息、矛盾和已经完成的核验。

用户或比赛网站明确反馈提交结果时，把日期、实际提交的候选、结果和必要备注追加到 `Submission history`。它只记录真实反馈，不记录尚未提交的猜测；之后即使继续尝试其他候选，也保留原有记录。

## 全场总表

每个任务结束一轮工作前运行：

```text
python tools/build_summary.py
```

生成器会：

- 按 Round 分节；
- 显示 Node 类型、parent 和 feeder；
- 显示各 Round 的 feeder pool 覆盖率、遗漏与重叠；
- 校验目录、Round、状态和引用格式；
- 展开并校验同 Round 或跨 Round 的 feeder pool；
- 提示尚未创建的 feeder 或 shared source；
- 允许合法的循环依赖；
- 使用文件锁和原子替换避免并发写坏总表。

Agent 不直接编辑 `SUMMARY.md`。

## 文件取舍

- `rounds/<round>/shared/`：关系图或多 Node 共用的题面；
- `input/`：该 Node 独有的原始题面，Agent 只读；
- `work/`：OCR、裁图、搜索结果和试验脚本，默认不进入 Git；
- `artifacts/`：支撑最终结论、值得长期保留的少量文件；
- `solution.md`：恢复任务所需的结论、证据、失败路线和下一步；
- `ROUND.md`：Round 名称和简短说明；
- `HUNT.md`：全场稳定规则与背景，不保存答案和进度。
- `.agents/skills/`：按需加载的通用工作流和少量确定性脚本，不保存题目专属常量。

## 最简日常操作

1. 开 Hunt 时填写一次 `HUNT.md`；
2. 在正确 Round 新建一个 Node；
3. 下载独有题面到 `input/`，共享题面放 Round 的 `shared/`；
4. 运行 `python tools/next_nodes.py` 并选择一个可开工 Node；
5. 手动开一个 Agent 任务并调用菜单给出的 `$work-on-node`；
6. 查看按 Round 分组的 `SUMMARY.md`；
7. 把提交反馈告诉对应任务。
