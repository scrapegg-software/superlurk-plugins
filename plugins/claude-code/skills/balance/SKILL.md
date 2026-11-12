---
description: Show your Superlurk credits, plan and, if one is set, this connection's daily spending cap
disable-model-invocation: true
allowed-tools: mcp__plugin_superlurk_superlurk__get_balance
---

Call the Superlurk `get_balance` tool and report, in two or three lines:

* credits available and the plan,
* only if this connection has a daily spending cap set (`connection.daily_cap_credits` is a number): the cap
  and `left_today_credits`. When `daily_cap_credits` is `null` there is no cap; do not mention one.

These are the credits of the person's own connected Superlurk account, shared with the website and
other authorized clients. Superlurk sign-in is separate from Claude sign-in. Every Superlurk plan can
connect; paid runs need enough usable free or paid credits. A plan alone does not guarantee spendable
credits. At zero balance, connection, free discovery, balance and owned saved results remain available.

Eligible people may claim 10 trial credits, valid for 30 days, through Superlurk's existing website
email/CAPTCHA browser verification. The trial is once per person, with account, verified email, source
IP and browser eligibility checks; it is not per plugin or connection. Never promise or invent a grant.
If verification is pending, tell the person to finish it on the Superlurk website and report the actual
returned balance.

If credits are low, say "Top up in Superlurk" as plain text, with no purchase link; nothing is sold inside
Claude Code. New plugin connections default to no daily connection cap; spending still requires usable wallet
credits and an approved quote. Do not recommend adding a cap. If an existing cap is returned and the person
asks about it, direct them to Settings › AI connections on the Superlurk website. If the tool is not available, tell the
person to sign in to their own Superlurk account with `/mcp` (choose the Superlurk server). Never ask for a
token, password, cookie or API key in the chat.
