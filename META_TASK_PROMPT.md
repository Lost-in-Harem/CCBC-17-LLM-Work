# Meta 任务启动提示词

你只负责 `rounds/<ROUND_ID>/nodes/<NODE_ID>/` 这个 Meta Node。

先读取根目录 `AGENTS.md`、`HUNT.md`、本 Round 的 `ROUND.md`、本 Meta 的 `solution.md` 和 `input/`，再运行：

```text
python tools/inspect_node.py <ROUND_ID>/<NODE_ID>
```

如果 frontmatter 声明了 `source`，再读取本 Round 对应的 `shared/<source>/`。

从本 Meta 的 `feeders` 字段确定其他可读 Node：

- `101, 102`：当前 Round 中的这些 Node；
- `pupae/104, forest/m01`：指定 Round 中的这些 Node；
- `all-round-feeders`：当前 Round 中所有 `round_feeder: yes` 的 Node；
- `pupae/all-round-feeders`：指定 Round 中所有 `round_feeder: yes` 的 Node；
- `unknown`：依赖尚未确认；先从本 Meta 题面和关系图确定依赖，不要扫描全 Round 答案。

每个展开后的 feeder 都允许读取其题面和答案，包括 `input/`、`solution.md`、它声明的共享 `source`，以及必要的 `artifacts/`。依赖可能是普通题、小题或另一个 Meta，也可能形成环。把 feeder 的 `candidate` 与 `accepted` 明确区分，不要把低置信候选当成确定事实。

请尝试解决 Meta：

- 只能读取 `feeders` 直接列出或 feeder pool 展开的 Node，不能修改它们；
- 对 feeder 的 backsolve 或修正只写进本 Meta 的 `solution.md`；
- 机制不明时保留少量竞争假设；如果 feeder、顺序或提取与当前路线矛盾，回退而不是增加补丁解释；
- 空间、叠图、路径或多媒体步骤使用 `$inspect-puzzle-visuals`，维护可复核的持久表示，不能只依靠文字总结；
- 同一假设族只保留一个参数化脚本和一个结果表；连续三次有界实验没有产生新证据时，记录并停止该路线；
- 可以在本 Node `work/` 中创建脚本和临时结果；
- 把最终需要复核的少量文件整理到 `artifacts/`；
- 如果用户报告了提交结果，先把日期、候选、明确结果和反馈追加到 `Submission history`，再按 `AGENTS.md` 更新状态；
- 不启动 subagent；
- 不手工编辑 `SUMMARY.md`；
- 不提交答案、请求提示或操作比赛网站。

在结束本轮工作前：

1. 更新本 Meta 唯一的 `solution.md`；
2. 列出实际使用的 feeder、各自状态，以及仍缺哪些输出；
3. 如果反推出 feeder 约束，写清目标 Node、约束和推导依据；
4. 更新 frontmatter 中的状态、摘要和日期；
5. 运行 `python tools/build_summary.py`；
6. 简短报告当前结论、候选答案、依赖和下一步。
