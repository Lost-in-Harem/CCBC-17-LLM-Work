# All-crossing reconstruction reproducer

This artifact records the bounded commands and the decisive extraction rows
for the candidate in `solution.md`.  Puzzle input is not modified.

## Commands

From the repository root, using the bundled Python runtime:

```powershell
& 'C:\Users\Lost\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\crossing_trade.py --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json --model rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\gpt2_distil_zh --vendor rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\vendor_lm --output rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\all_crossings_unanchored.md --swap-mode all --anchor-mode none --iterations 50000 --restarts 6 --swap-penalty 0 --report-count 3

& 'C:\Users\Lost\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\crossing_trade.py --layout rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\visual\canonical\layout.json --model rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\gpt2_distil_zh --vendor rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\vendor_lm --output rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\blank_route_audit_all.md --swap-mode all --anchor-mode none --iterations 20000 --restarts 2 --swap-penalty 0 --route-audit-row G1-D03 --route-audit-row G2-D04 --route-audit-row I01
```

The first command converges to the same best state in all six restarts.  The
second forces every compatible route for each underline-bearing source row.

## Decisive rows

| Blank source | Assigned route | Repaired host | Required fill |
| --- | --- | --- | --- |
| `G1-D03: 好□□` | `G1-D03.3 -> G1-A06.4` | `雷锋是 / 每个小 / 朋友的 / 好□□` | 榜样 |
| `G2-D04: 丽□□` | `G2-D06.2`, no crossing | `形容美 / 丽□□ / 之容不 / 悦于目` | 曼丽 |
| `I01: □□不` | `Z05.1 -> G1-A09.1` | `□□不 / 均则于 / 体不同` | 气性 |

The source underline order in the HTML is therefore `榜样 / 曼丽 / 气性`.
