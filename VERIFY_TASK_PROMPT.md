# 候选答案核验提示词

你只负责核验 `rounds/<ROUND_ID>/nodes/<NODE_ID>/` 的当前候选。开始前确认原解题任务已经停止，避免两个任务同时修改同一 Node。

先读取根目录 `AGENTS.md`、`HUNT.md`、本 Round 的 `ROUND.md`，再运行：

```text
python tools/inspect_node.py <ROUND_ID>/<NODE_ID>
```

从原始题面重新核验，不以“证明当前候选正确”为目标：

1. 检查文字、图片、顺序、颜色、版式和附件的转录是否准确；
2. 独立重现机制、重排、索引和最终提取；
3. 检查主要题面元素是否都得到解释；
4. 明确列出未使用信息、含糊步骤和反例；
5. 检查答案长度、格式、题目标题与 flavor 是否吻合；
6. 对视觉或空间步骤，使用 `$inspect-puzzle-visuals` 直接检查持久标注图、网格或坐标表示，不只依赖文字总结。

核验通过时，在 `solution.md` 的 `Candidate audit` 中补充最短的复现路径、未使用信息和核验证据，可以调整 `confidence`，但不要设置 `accepted`。

无法重现或发现矛盾时，把状态改回 `working`，清楚记录最早失败的步骤和最有区分力的下一项测试。网站没有判错时不要使用 `rejected`。

结束前运行 `python tools/build_summary.py`，并向用户报告核验结论、证据、仍有的风险和下一步。
