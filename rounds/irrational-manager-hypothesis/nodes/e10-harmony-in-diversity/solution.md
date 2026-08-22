---
node_id: e10-harmony-in-diversity
title: 和而不同
kind: puzzle
round: irrational-manager-hypothesis
parent: 
source: 
round_feeder: yes
feeders: 
status: accepted
answer: HEARTHSTONE
confidence: high
summary: 用户已确认 HEARTHSTONE 为正确答案。与官方比赛规则逐行对齐后，从定义项的替换读音得到隐藏指令；将唯一异常的十八个八点盲文字符排成 12×12 点阵并改按六点盲文切分，读出 FIND THE ANSWER HEARTHSTONE。
updated: 2026-08-22
---

# 和而不同

## Current conclusion

答案 **HEARTHSTONE** 已由用户确认正确。

题面正文是官方《CCBC 17 比赛规则及参赛者行为规范》的八点盲文变体。逐行比对先给出一条隐藏指令，再从唯一不能按正文码表解读的引号内容中构造正方点阵；改用六点盲文切分后，直接得到 `FIND THE ANSWER HEARTHSTONE`。

## Observations

- 题面有 425 行纯盲文；官方比赛规则去掉页面自身的两个标题后也恰有 425 个非空文本块，章节、条号和每一段逐行对应。
- 普通汉字或标点各占两个八点盲文字符；有序列表另有固定前缀，英文则由定界符包围并使用普通英文盲文。题面中的英文可稳定读出 `CCBC 17 Puzzle Hunt`、`AI`、`Source Map`、`Benchmark`、`IP` 等，与官方原文位置吻合。
- 同音字共用码元，例如“第”和“的”（读 `di4`）一致，说明正文主体编码的是带声调读音，不是汉字字形。
- 官方规则正文来源为 <https://ccbc17.cipherpuzzles.com/info/rules>；本次取得的文本副本保存在 `work/official-rules.txt`。
- 标题“和而不同”同时贴合两层设计：同音汉字可共用编码，而最后又把八点盲文点阵改按六点盲文读取。

## Working hypotheses

- 已完成的主路线是“题面为官方规则的改写版”：425 对 425 的逐行一致性和大量英文原样锚点排除了巧合。
- 结尾重切点阵的方向已经由完整英文句子唯一验证；其余七种旋转或镜像均不产生可读六点盲文。
- 用户已明确确认答案正确，当前没有待验证的关键机制。

## Extraction

第一章第三条的八个定义词在题面中被替换。利用正文其他出现位置建立“两个八点盲文字符 → 拼音”码表，依次得到：

| 官方引号内容 | 题面读音还原 |
| --- | --- |
| 主办方 | 下文中 |
| 比赛网站 | 引号内部 |
| 参赛者 | 存在一 |
| 队伍 | 文本 |
| 比赛内容 | 无法解读 |
| 公开信息 | 将其找出 |
| 自动化操作 | 重排为正方 |
| 严重处理措施 | 即可进行提取 |

隐藏指令为：“下文中引号内部存在一文本无法解读，将其找出，重排为正方，即可进行提取。”

后文共有五段引号内容。四段使用正文已经多次出现的码元；官方原文“只确认思路是否正确”对应的九个双码元全部只出现一次，无法由正文独立解码，正是指令所指：

```text
4B4A DD99 9E53 CCC4 8E07 DDE8 2754 7462 7323
```

将十八个八点盲文字符每行六个排列：

```text
⡋⡊⣝⢙⢞⡓
⣌⣄⢎⠇⣝⣨
⠧⡔⡴⡢⡳⠣
```

这样形成 12×12 点阵。将点阵改按 2×3 的标准六点盲文切成 4×6，读为：

```text
FINDTH
EANSWE
RHEART
HSTONE
```

行优先连读为 `FIND THE ANSWER HEARTHSTONE`，故提取答案 **HEARTHSTONE**。

## Candidate audit

- 答案格式：点阵直接给出英文答案，符合全场允许英文答案的约定。
- 设计解释：官方规则作为长篇 crib、定义项隐藏指令、唯一异常引号、八点转六点盲文和标题均得到统一解释。
- 未使用信息：两次“修正了部分文本”的更新时间只起到提示正文存在改动的作用，不参与索引；未发现其他矛盾。
- 独立检查：重新按 Unicode 盲文标准点位渲染九个双码元，再按六点盲文分格；24 个格逐字得到 `FINDTHEANSWERHEARTHSTONE`。脚本语法检查通过，八种整体朝向中只有原方向可读。

## Submission history

只记录用户或比赛网站明确反馈过的提交；不要把尚未提交的候选写进来。

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-22 | HEARTHSTONE | accepted | 用户明确确认答案正确。 |

## Evidence and artifacts

- 可人工复核的最终提取：[artifacts/extraction.md](artifacts/extraction.md)
- 12×12 点阵图：[artifacts/quote-grid.png](artifacts/quote-grid.png)
- 官方正文对齐与异常枚举：`work/compare_official.py`、`work/official-exceptions.tsv`、`work/quoted-spans.tsv`
- 点阵渲染及八种朝向检查：`work/render_quote_grid.py`、`work/quote-grid-variants.tsv`
- 官方规则：<https://ccbc17.cipherpuzzles.com/info/rules>

## Important failed routes

- 直接套用现行汉语双拼盲文只能部分解码；题面使用了替换后的八点码元，不能据此完整还原全文。
- 已有的字节编码页、GF(2) 仿射变换、逐盲文格仿射变换、常见 S-box、字形哈希、拼音哈希和 C.B.A. 八点盲文方案均未与可靠锚点相符。官方正文逐行对齐后，不应继续扩展这类公式搜索。
- 曾按语义猜测若干条款词组来加码表锚点，产生了真实冲突；这些猜测已撤销。只有官方原文与结构性编号锚点可作为可靠 crib。

## Next action

无需继续解题；保留 **HEARTHSTONE** 及上述可复现提取，供后续 Meta 使用。
