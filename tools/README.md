# Tools

根 `tools/` 只放所有 Node 都需要的 Hunt 结构工具。题型专用的确定性脚本随
repo-local skill 放在 `.agents/skills/<skill>/scripts/`，避免根目录重新变成脚本堆。

## 日常命令

| 命令                                      | 作用                               | 写入位置                |
| ----------------------------------------- | ---------------------------------- | ----------------------- |
| `python tools/new_puzzle.py ...`          | 新建 Round 或 Node                 | 新 Node、必要时新 Round |
| `python tools/move_node.py OLD NEW`       | 安全移动 Node 并更新 feeder 引用   | Node、引用者、总表      |
| `python tools/next_nodes.py`              | 列出任务菜单与启动命令             | 不写文件                |
| `python tools/inspect_node.py ROUND/NODE` | 只读检查输入、feeder、状态与下一步 | 不写文件                |
| `python tools/build_summary.py`           | 校验 Node 并重建全场总表           | `SUMMARY.md`            |
| `python tools/doctor.py`                  | 检查模板结构和可选媒体能力         | 不写文件                |
| `python tools/doctor.py --json`           | 输出同一检查的机器可读结果         | 不写文件                |

运行各命令的 `--help` 查看完整参数。

`next_nodes.py` 为每个可开工 Node 打印可复制的 `$work-on-node` 命令。
`candidate` 单独进入核验区；未解决的显式 feeder 进入等待区；合法循环依赖不会
被错误地判为死锁。使用 `--round ROUND_ID` 只查看一个 Round。

移动或重命名 Node 时先停止正在写入该 Node 及其引用者的任务，然后运行：

```text
python tools/move_node.py unassigned/p001 forest/p001 --dry-run
python tools/move_node.py unassigned/p001 forest/p001
```

第二条命令会再次显示计划，只有输入 `MOVE` 才执行。工具移动整个 Node 目录，
更新 `node_id`、`round` 和结构化 `feeders`，再校验并重建总表；失败时自动回滚。
它不会猜测性改写正文。跨 Round 移动带 `source` 的 Node 时，必须显式使用
`--new-source SOURCE` 或 `--clear-source`。

## Repo-local skills

### `$work-on-node`

位置：`.agents/skills/work-on-node/`

处理或恢复用户明确指定的一个 Node。它按 `solution.md` 中的 `kind` 选择普通题或
Meta 流程，并执行实验止损和结束前保存规则。

### `$inspect-puzzle-visuals`

位置：`.agents/skills/inspect-puzzle-visuals/`

其脚本入口为：

```text
python .agents/skills/inspect-puzzle-visuals/scripts/visual_workbench.py --help
```

子命令：

- `inventory`：展开、去重、稳定编号并生成 contact sheet；
- `crop`：按原图坐标裁切、放大和叠坐标网格；
- `channels`：生成 RGB、CMYK、灰度、Alpha 和指定阈值图；
- `annotate`：从 JSON 画框、线、点、路径与标签；
- `ocr`：保存 OCR 文本、置信度、坐标和标注图；
- `render`：有上限地渲染 PDF 页、视频帧、音频波形和频谱。

这些命令不修改原始题面。输出应放入当前 Node 的 `work/visual/`。

## 工具边界

- 缺少可选依赖时先查看 `doctor.py`，不要让工具自动安装软件。
- 一次性题目脚本留在该 Node 的 `work/`。
- 同一假设族只保留一个参数化脚本和一个结果表。
- 只有在至少两个无关题目中复用的确定性操作，才提升到 skill 的 `scripts/`。
- 题名、专属坐标、专属语料和答案不得进入通用工具。
