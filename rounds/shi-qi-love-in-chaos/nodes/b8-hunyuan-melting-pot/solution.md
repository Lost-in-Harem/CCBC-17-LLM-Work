---
node_id: b8-hunyuan-melting-pot
title: 混元大熔炉
kind: puzzle
round: shi-qi-love-in-chaos
parent:
source:
round_feeder: yes
feeders:
status: accepted
answer: PENTAGON
confidence: high
summary: "用户已确认 PENTAGON 正确。按提示 3 的 10×14 盘面手工填完全部横纵答案；18 个异字交点均由同一字形骨架上的五行部件替换构成。编号格依次给出“生短克长”，指示相生记摩斯短点、相克记长划；逐行解得 PENTAGON。"
updated: 2026-08-16
---

# 混元大熔炉

## Current conclusion

答案 **PENTAGON** 已由用户确认正确。

提示 3 给出的盘面可用全部线索唯一手填。所有普通交点取相同汉字；18 个异字交点则把字中的金、木、水、火、土部件互换，同时保留另一部分字形。四个编号格依次是：

1. `r6c12=生`
2. `r9c7=短`
3. `r2c3=克`
4. `r1c4=长`

因此提取指令为 **生短克长**：五行关系为“相生”时记摩斯短点 `.`，为“相克”时记长划 `-`。

## Fill

完整词位及起点见 `artifacts/fill.tsv`。其中较关键、曾经不确定的答案为：

- A1=`棒冰`，符合整组答案的拼音排序。
- A18=`六丁神火`，对应烤过孙悟空之物。
- A19=`钼铅`。
- D3=`冰锥`。
- D11=`柯烂棋`，即仙人所下的棋。
- D12=`六阶堂`：二阶堂红丸、二阶堂美树、二阶堂希罗三个“二阶堂”相加。

右半盘的交叉链也可人工复核：

- A22 `一岁一枯荣`、A14 `红光满面`、A1 `棒冰` 依次与 D21 `荧光棒` 的 `荧/光/棒` 相交。
- A7 `床头柜` 与 D7 `楚庄王` 在 `床/庄` 相交；A11 `蜂王浆` 再与 D7 在 `王` 相交。
- D8 `蜂房水涡` 依次穿过 A11 的 `蜂`、A8 的 `水`、A12 的 `埚`。
- D9 `泔水桶` 穿过 A12 的 `坩` 和 A6 `潮涌核心` 的 `涌`。
- A23 `银河系` 依次与 D16 `生根`、D11 `柯烂棋`、D14 `平面直角坐标系` 相交为 `银/根`、`河/柯`、`系`。

提示 3 原图的正确盘面有 106 个白格；早期转录曾把 `r8c13`（D11 的“烂”）误记为黑格，现已在 `work/representation/hint3_mask.txt` 中校正。横向总长 78、纵向总长 76，所以完整填表恰有 `78+76-106=48` 个交点。

## Five-element crossings and extraction

逐行保留异字交点，按“生短克长”转成摩斯码。完整逐格表见 `artifacts/morse_extraction.tsv`。

| Row | 异字交点 | 五行关系 | Morse | Letter |
| --- | --- | --- | --- | --- |
| 1 | 泉/柏，坂/板，坡/波，荣/荧 | 生、克、克、生 | `.--.` | P |
| 2 | 沓/杳 | 生 | `.` | E |
| 3 | 钼/相，汀/钉 | 克、生 | `-.` | N |
| 4 | 床/庄 | 克 | `-` | T |
| 5 | 火/木，吐/杏 | 生、克 | `.-` | A |
| 7 | 棠/堂，银/根，河/柯 | 克、克、生 | `--.` | G |
| 8 | 坩/泔，埚/涡，钳/柑 | 克、克、克 | `---` | O |
| 10 | 集/锥，涌/桶 | 克、生 | `-.` | N |

没有异字交点的第 6、9 行不产生摩斯字母。按行读得：

`P E N T A G O N`

这同时使用了风味文本的“行”（五行）、提示 1 的部分字形交叉规则、四个编号格和完整盘面，没有剩余矛盾。

## Submission history

| Date | Candidate | Result | Note |
| --- | --- | --- | --- |
| 2026-08-15 | 心灵手巧 | rejected | 用户明确报告“心灵手巧 不是答案”。 |
| 2026-08-16 | PENTAGON | accepted | 用户明确确认“PENTAGON 是正确答案”。 |

## Important failed routes

- **心灵手巧 / XLSQ**：已被比赛结果明确拒绝，不得复用。
- **二阶堂**：三个人名并非只取共同姓；加号要求把三个“二阶”相加，答案是“六阶堂”。
- **老君丹炉 / 八卦丹炉、罗宾、冰棱**：分别被完整填表中的“六丁神火”“钼铅”“冰锥”取代。
- **金木水火 / 缺土**：四个编号格实际为“生短克长”，不是五行部件枚举。
- **早期 SAT 无解**：根因之一是把 `r8c13` 误录为黑格；不能据此修改明确的线索答案。

## Evidence and reproducibility

- `work/visual/user_partial_fill_latest.png`：用户最新手填图的持久副本。
- `work/representation/hint3_mask.txt`：校正后的 10×14 黑白格。
- `work/representation/user_partial_grid.txt`：带坐标的手填转录。
- `artifacts/fill.tsv`：全部 44 个词位、答案和起点。
- `artifacts/morse_extraction.tsv`：18 个异字交点、五行关系、点划及逐行解码。
- `work/visual/manual_complete_geometry.txt`：完整词位覆盖和 48 个交点的程序复核；程序未用于改写线索答案。

## Next action

已完成；答案与完整提取均已记录。
