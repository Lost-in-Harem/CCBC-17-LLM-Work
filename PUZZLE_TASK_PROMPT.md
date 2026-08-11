# 普通题 / 小题任务启动提示词

你只负责 `rounds/<ROUND_ID>/nodes/<NODE_ID>/` 这一个 Node。

先读取根目录 `AGENTS.md`、`HUNT.md`、本 Round 的 `ROUND.md` 和本 Node 的 `solution.md`，再运行：

```text
python tools/inspect_node.py <ROUND_ID>/<NODE_ID>
```

随后读取：

- 本 Node `input/` 中的全部题面和附件；
- 如果 frontmatter 声明了 `source`，读取本 Round `shared/<source>/`；
- 如果 frontmatter 声明了 `feeders`，按 `AGENTS.md` 展开后读取这些 Node 的题面、答案和必要产物。

如果已有进度，先理解现有结论、失败路线和 `Next action`，从那里继续，不要无故从头重复。

请认真尝试解出这个 Node：

- 观察文字、顺序、布局、图片、颜色、格式和附件；
- 机制不明时保留少量竞争假设，优先做能区分它们的便宜测试；证据矛盾时回退；
- 空间、路径、叠图、旋转、网格或多媒体题使用 `$inspect-puzzle-visuals`，维护带坐标或稳定编号的持久表示，不能只依靠 OCR 或文字记忆；
- 同一假设族只保留一个参数化脚本和一个结果表；连续三次有界实验都没有增加事实、改变候选排序或更新机制时，记录负面证据并换路线；
- 可以联网查询；
- 可以在本 Node `work/` 中创建 OCR、裁图、脚本和临时结果；
- 把最终需要复核的少量文件整理到 `artifacts/`；
- 只修改本 Node，不修改其他 Node 或共享题面；
- 如果用户报告了提交结果，先把日期、候选、明确结果和反馈追加到 `Submission history`，再按 `AGENTS.md` 更新状态；
- 不启动 subagent；
- 不手工编辑 `SUMMARY.md`；
- 不提交答案、请求提示或操作比赛网站。

在结束本轮工作前：

1. 更新本 Node 唯一的 `solution.md`；
2. 即使没有解出，也保存已确认事实、重要失败路线和一个具体的 `Next action`；
3. 更新 frontmatter 中的状态、摘要和日期；
4. 运行 `python tools/build_summary.py`；
5. 简短报告当前状态、候选答案、置信度、关键证据和下一步。
