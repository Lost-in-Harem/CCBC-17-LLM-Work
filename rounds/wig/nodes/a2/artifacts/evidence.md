# a2 evidence table

## Account and video evidence

| Source | Observed fact | Use |
| --- | --- | --- |
| Y profile `时柒是个小天才` (`@junana_7`) | Self-description identifies the account as 时柒 Junana; the profile is in 星浦市梧桐区. | Confirms the account supplied by the commission. |
| 咱管 `你们的大学生活是什么样的？聊聊我的校园日常` | The three purported friends are placed at 华东传媒大学、五峰大学、枝江师范大学. Distinctive details are 小豆's off-key confession scene, 五峰大学的楠门/南北门外卖错过五次, and the 枝江师范大学“第一儿子/枝二儿” ringtone story. | Produces the three possible schools without assuming which “friend” is the speaker herself. |
| 咱管 `最近新学习了怎么烘焙！第一次烤面包居然没翻车！` | 时柒 says that, in her graduation year, a bakery opened next to her school; its egg tarts were excellent; every weekend she and her friends went there after 围棋社 activity. | Supplies the two filters: a school-adjacent egg-tart bakery and a public Go-club record. |
| 咱管 debut Q&A | She describes herself as `女孩子`. | Reduces the matching 2024 cohort from five names to three. |

The downloaded sources, one-second renders, subtitle crops, inventories, and contact sheets are under `../work/visual/{university,baking,debut}/`. `extract_subtitle_frames.py` is the parameterized cropper used for all three videos.

## Location cross-check

| Possible school | 跳窗 result | Public school result | Verdict |
| --- | --- | --- | --- |
| 华东传媒大学 | `窗下烘焙`, at the south gate, opened in 2022 and specializes in egg tarts. | The current club directory does not list a Go club. | Fails the public Go-club intersection. |
| 五峰大学 | `禾光蛋挞（五峰路店）`, near the university, opened in 2024 and specializes in egg tarts. | A public Go-club page and cohort roster are available. | Unique match to both clues; graduation cohort is 2024. |
| 枝江师范大学 | Searching the university in 跳窗 returns only `快乐小鹿（枝江公园店）`, not a bakery/egg-tart shop. | The Go club has a public 2026 championship record. | Fails the bakery intersection. |

## Candidate extraction

The 五峰大学围棋社 `2024 届` table contains:

| # | Name | Department | Candidate? |
| ---: | --- | --- | --- |
| 1 | 徐霓 | 新闻传播学院 | yes |
| 2 | 沈梦雯 | 外国语学院 | yes |
| 3 | 宋锦雪 | 历史系 | yes |
| 4 | 路轩 | 计算机科学 | no |
| 5 | 何浩然 | 哲学系 | no |

The Q&A gender clue leaves `徐霓 / 沈梦雯 / 宋锦雪`. The mail reply submitted these three names in that order. The follow-up mail, preserved as `../work/visual/live/a2-accepted.png`, says the first task was completed and explicitly confirms that the range was reduced to three candidate names.

## Post-a2 lead

The acceptance mail begins the next stage: determine the unique name. It points to a milk-tea-delivery pretext and public company landline data in 查公公. 查公公 gives 密码菌文化传播有限公司's office number as `021-0018-3141`; the subsequent fixed hypothetical call script refers to an `沈小姐`. This is strong follow-on evidence for 沈梦雯, but it was obtained after the three-name a2 milestone had already been accepted and is not substituted for a2's accepted answer.
