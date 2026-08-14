# a3 evidence

## Mail and company lookup

| Source | Observed fact | Use |
| --- | --- | --- |
| Mail `第一个任务完成的不错` | Confirm the unique real name; use a delivery-like identity; company orders use landlines; search public company data in 查公公; report by calling Hu Ruihua's mobile. | Defines the intended cross-app chain. |
| 查公公 — 密码菌文化传播有限公司 | Address `星浦市梧桐区鹿荫路1817号青雀创意园7号楼2F`; office phone `021-0018-3141`. | Gives the target company and landline. |
| 查公公 — 卡美洛资本管理有限公司 | `021-0011-2101（业务咨询）`; `179-2103-1754（胡*华，长期联系）`. | Explains the busy call-history number and supplies Hu's mobile. |
| Call history after mobile call | New row: `给胡瑞华打了电话，他鼓励我继续进行调查。` with `17921031754`. | Confirms that the mobile number connected and story state advanced. |

## `call_ccb_coffee` critical transcript

This is explicitly a dream/hypothetical call, not a real company statement.

> Lost-MSth: 您好，我这边是给您送咖啡的。沈小姐给您点了一杯，我现在到创意园这边了，但是实在找不到路，想问一下该怎么走。
>
> 密码菌接线人: 沈小姐？
>
> 密码菌接线人: 她给我点了什么？
>
> 密码菌接线人: 可是沈小姐从来不帮别人点咖啡，而且我今天也没有填过这个地址。
>
> 密码菌接线人: 你是哪一家店？
>
> Lost-MSth: 呃，南门那家……
>
> 密码菌接线人: 创意园南门没有咖啡店。
>
> 密码菌接线人: 你订单上写的是哪栋？
>
> Lost-MSth: 我看看，好像是 A 栋？
>
> 密码菌接线人: 我们这里也没有 A 栋。
>
> 密码菌接线人: 要不你再回答我一个问题，你到底是没点对咖啡、没找对店，还是根本没下单？
>
> （我猛地睁开眼。）
>
> （还好这不是真的……）
>
> （我刚才竟然以为自己已经把单下出去了，原来只是一场梦。）

The surname cue maps the accepted a2 candidates as follows:

| a2 candidate | Surname matches `沈小姐`? |
| --- | --- |
| 徐霓 | no |
| 沈梦雯 | yes |
| 宋锦雪 | no |

## `call_hrh_get_real_name` critical transcript

This call was real and ended with `@sync read/call_hrh_get_real_name`.

> 胡瑞华: 很正常，线索不是自己蹦出来的，很多时候得靠你想办法把话问出来。
>
> 胡瑞华: 尤其是这种和现实生活沾边的信息，脑子放灵光点。
>
> 胡瑞华: 你可以试着直接接触目标。
>
> 胡瑞华: 比如给人点点东西，借着配送、取餐、签收这种场景套两句，往往比硬问有效。
>
> 胡瑞华: 当然，别太离谱，也别违法。

## Current external-state audit

- The successful mentor call advanced WIG state and is preserved in `call-history.png`.
- Recalling the Password菌 landline after that sync still returned the same dream script, so the real-order prerequisite remains unsatisfied.
- 跳窗 currently has no orders. Searching `青雀创意园` reveals `快乐小鹿（梧桐里店）`, a deliverable coffee/drink shop; no cart or order was created because the user has not yet explicitly authorized placing an order.

## Negative number tests

| Number | Rationale | Result |
| --- | --- | --- |
| `02100112101` | Visible in old Hu Ruihua call history | Busy; company page identifies it as business consultation. |
| `48784482` | T9 of `huruihua` | Empty number. |
| `74366364936` | T9 of `SHENMENGWEN` | Empty number. |
| `17921031754` | Hu's long-term contact on Camelot company page | Connected; new story call and history entry. |
