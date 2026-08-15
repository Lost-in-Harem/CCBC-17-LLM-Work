# Rejected depth-fit audit

This artifact preserves the exact construction that produced the rejected
candidate **中山大学**. It is **not a verified fill** and must not be used as a
source of solved entries.

## Rejected entry profile

| Grid | Across, in statement order | Down, in statement order |
| --- | --- | --- |
| 1 | 终末地；小便所；一击必中；十项全能；山本五十六；女扮男装；岁寒三友；豪放女；上百万 | 始终如一；女中豪杰；中山装；十六岁；无所不能；友谊万岁 |
| 2 | 罪大恶极；白马王子；义和团；摩擦力；五角大楼；心理学家 | 大地震；超广角；极简主义；摩天大楼；和地面摩擦；白衣军团；力不从心；王老五；中小学 |
| 3 | 天文学；台师大；地质学家；堆积如山；长方体体积；有缘相会；物是人非；意中人；下半时 | 惊天动地；有何意义；家长会；堆积物；四大名山；非常时期 |

The profile was chosen because it satisfies every planar crossing and makes
the five common layer coordinates read as follows:

| Coordinate | Grid 1 | Grid 2 | Grid 3 | Former depth word |
| --- | --- | --- | --- | --- |
| (4, 4) | 地 | 震 | 学 | 地震学 |
| (4, 10) | 小 | 五 | 台 | 小五台 |
| (7, 7) | 五 | 面 | 体 | 五面体 |
| (10, 4) | 女 | 超 | 人 | 女超人 |
| (10, 10) | 上 | 中 | 下 | 上中下 |

This consistency is insufficient. Recombining the visible blocks recovers the
unmistakable phrase `扶清灭洋`, which requires an **义和团** clue/answer in the
third-grid material; the profile instead forced `意中人` to satisfy a chosen
depth word. The same block pool also restores the three-title sequence
`《童年》/《悲惨世界》/《巴黎圣母院》`, which this profile never explains.
Therefore the profile, all five depth readings, and the frequency extraction
below are invalid as a solution. The title sequence may clue `书名号` or a
four-character category such as `世界名著`; its slot is not yet confirmed.

## Rejected extraction trace

Counting each Across/Down string in the rejected profile once gives the top
multiset `大×6，地×5，中×5，山×4，学×4`. Reordering those letters as
**中山大学** was not constrained by the puzzle, and the user explicitly
reported that candidate as wrong on 2026-08-15.

## Reproduction of the failed construction

From the repository root:

```powershell
& 'C:\Users\Lost\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -X utf8 rounds\shi-qi-love-in-chaos\nodes\b6-magic-square-trading-strategy\work\cube_audit.py --g1-profile depth-fit --g2-profile depth-fit --g3-profile solved --direct-only --show-layers --show-frequency
```
