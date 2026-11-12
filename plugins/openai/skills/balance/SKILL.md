---
name: balance
description: Check the connected account's Superlurk credits, plan and optional daily connection cap when the person asks about balance, credit use, spending limits or why a search cannot run.
---

# Check Superlurk balance

Call the plugin's Superlurk `get_balance` tool using the name available in this client. It is
free. Report the actual credits and plan without running or pricing a search automatically.

This is the wallet of the person's own connected Superlurk account, shared with the Superlurk
website and other authorized clients. Superlurk sign-in is separate from ChatGPT or Codex sign-in.
All Superlurk plans can connect; paid runs need enough usable free or paid credits. A paid plan
does not bypass an empty or expired balance. At zero balance, connection, free discovery,
balance checks and reading the person's own saved results remain available.

Eligible people may claim 10 trial credits, valid for 30 days, by completing the Superlurk
website's existing email/CAPTCHA browser verification. The trial is once per person, with
account, verified email, source IP and browser eligibility checks; installing another plugin
or adding a connection does not provide another trial. Never promise or invent a grant. If
verification is pending, explain where to finish it and report the actual returned balance.

New plugin connections default to no daily connection cap, with spending limited by the usable
wallet balance and the approved quote. Do not recommend adding a cap. If an existing connection
returns a numeric `connection.daily_cap_credits`, report that actual cap, spent today and
`left_today_credits`; it resets at 00:00 UTC. When the value is `null`, omit cap details unless
asked. Existing caps remain enforced and can be managed under Settings › AI connections on the
Superlurk website. Every run still needs a usable quote and authorization.

If credits are low, say “Top up in Superlurk” as plain text. Purchases happen only on the
website; do not create checkout links, request payment details or attempt an upgrade. Failed
searches and reusing the person's own saved results are free; successful valid empty answers
are charged at their quoted price.

If tools are unavailable, use the setup workflow. A 401 or `_meta["mcp/www_authenticate"]`
means the person should reconnect through the client UI. Never ask them to paste a token,
password, cookie or API key into chat, and do not switch accounts to evade a spending cap.
