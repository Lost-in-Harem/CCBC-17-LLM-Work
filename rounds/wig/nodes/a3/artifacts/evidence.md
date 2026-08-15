# a3 evidence

## Mail and company lookup

| Source | Observed fact | Use |
| --- | --- | --- |
| Mail `第一个任务完成的不错` | Confirm the unique real name; use a delivery-like identity; company orders use landlines; search public company data in 查公公; report by calling Hu Ruihua's mobile. | Defines the intended cross-app chain. |
| 查公公 — 密码菌文化传播有限公司 | Address `星浦市梧桐区鹿荫路1817号青雀创意园7号楼2F`; office phone `021-0018-3141`. | Gives the delivery address and landline. |
| 查公公 — 卡美洛资本管理有限公司 | `021-0011-2101（业务咨询）`; `179-2103-1754（胡*华，长期联系）`. | Explains the busy call-history number and supplies Hu's mobile. |
| a2 accepted result | `徐霓 / 沈梦雯 / 宋锦雪`. | A confirmed three-name universe; a confirmed surname uniquely selects one. |

## Correct Jumpwindow order

The order action returned:

```json
{"result":"changed","data":{"accepted":true,"correct":true},"status":1,"message":null,"location":null}
```

Its relevant payload was:

```json
{
  "store": "jumpwindow/happydear_wutongli",
  "storeName": "快乐小鹿（梧桐里店）",
  "address": "星浦市梧桐区鹿荫路1817号青雀创意园7号楼2F",
  "phone": "02100183141",
  "recipient": "沈梦雯",
  "items": [{"name": "生椰拿铁", "quantity": 1, "price": 22}],
  "total": 22
}
```

The apparently wrong recipient is intentional: the subsequent real call starts from “沈小姐” and has the caller correct it to “徐小姐”. The full bounded test table is in `../work/order-tests.tsv`.

## `call_ccb_coffee` pre-order dream

This is explicitly a dream/hypothetical call, not a company statement.

> Lost-MSth: 您好，我这边是给您送咖啡的。沈小姐给您点了一杯，我现在到创意园这边了，但是实在找不到路，想问一下该怎么走。
>
> 密码菌接线人: 沈小姐？
>
> 密码菌接线人: 可是沈小姐从来不帮别人点咖啡，而且我今天也没有填过这个地址。
>
> 密码菌接线人: 创意园南门没有咖啡店。
>
> 密码菌接线人: 我们这里也没有 A 栋。
>
> （我刚才竟然以为自己已经把单下出去了，原来只是一场梦。）

This ranks 沈梦雯 as a tempting hypothesis but cannot confirm it.

## `call_ccb_right_coffee` real call

The correct order changes the landline HSS to `call_ccb_right_coffee`:

> Lost-MSth: 您好，我这边送咖啡的。沈小姐给您点了一杯，我到创意园附近了，但是路有点绕，想确认一下怎么走。
>
> 密码菌接线人: 沈小姐？
>
> （不对，他迟疑了。）
>
> Lost-MSth: 啊不好意思，我看错单了，不是沈小姐，是徐小姐。
>
> 密码菌接线人: 哦，徐小姐啊。
>
> （她果然姓徐。这样的话，徐霓大概就是她的真名）
>
> 你在五峰大学的校园网输入“徐霓”，果然查询到了她学生时期的照片。

The HSS ends with `@sync read/call_ccb_right_coffee`. Exact extracted source: `../work/call_ccb_right_coffee.hss`.

Surname mapping:

| a2 candidate | Surname matches `徐小姐`? |
| --- | --- |
| 徐霓 | yes |
| 沈梦雯 | no |
| 宋锦雪 | no |

## Mentor confirmation

Calling `17921031754` after the real landline call loads `call_hrh_got_real_name`:

> Lost-MSth: 嗯，我刚刚套出来了。她那边有人提到“徐小姐”，基本可以确认时柒真名确实姓徐。
>
> 胡瑞华: 干得不错啊。
>
> 胡瑞华: 这种信息看着不起眼，实际上很关键。知道真实姓名，后面很多公开痕迹就能对上了。

It ends with `@sync read/call_hrh_got_real_name`. The call history then records:

- `装作是外卖小哥，给密码菌打了电话，确认了时柒的真实名字。`
- `给胡瑞华打了电话，告诉他我已经确认了真实姓名，可以继续调查了。`

This is explicit Hunt-site confirmation of the answer event. Exact extracted source: `../work/call_hrh_got_real_name.hss`.

## Negative number tests

| Number | Rationale | Result |
| --- | --- | --- |
| `02100112101` | Visible in old Hu Ruihua call history | Busy; company page identifies it as business consultation. |
| `48784482` | T9 of `huruihua` | Empty number. |
| `74366364936` | T9 of `SHENMENGWEN` | Empty number. |
| `17921031754` | Hu's long-term contact on Camelot company page | Connected; both mentor HSS events use this mobile. |
