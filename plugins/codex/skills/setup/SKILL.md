---
name: setup
description: Connect and check the Superlurk plugin in ChatGPT or Codex when the person asks to set up Superlurk, sign in, reconnect, or verify its tools. Uses free discovery and balance checks without running a search.
---

# Set up Superlurk

Use the Superlurk MCP connection packaged with this plugin. It connects to
`https://mcp.superlurk.com/mcp` through the client's browser OAuth flow. The host owns authentication;
never ask the person to paste a token, password, cookie, client secret or API key into chat.
The person must sign in to their own Superlurk account in that browser flow. Signing in to
ChatGPT or Codex is separate from signing in to Superlurk; installation alone does not connect an account.

1. Check whether the Superlurk tools are available in this conversation. The eight tools are
   `list_networks`, `find_searches`, `get_price`, `run_search`, `get_run`, `list_results`,
   `open_result` and `get_balance`. Resolve the tool names from the client's available tools;
   namespacing differs between clients, so do not assume a hard-coded prefix.
2. If they are unavailable, explain that the installed plugin or MCP connection must be enabled and
   authenticated in this client's plugin settings. In Codex, `/mcp` can show the connection. In
   ChatGPT, open the installed Superlurk plugin's connection settings. Complete sign-in in the
   browser opened by the client, then start a fresh chat if the tools do not refresh here.
3. If a standalone Superlurk MCP entry already exists, explain the duplication before changing it.
   Keep one active connection path for testing; do not silently remove or overwrite client settings.
4. Once available, call `list_networks` and `get_balance`. Both are free. Summarize the currently
   offered networks and distinguish `source: "native"` from `source: "web"`. Web sources return
   public page titles, links and snippets without native likes, views or follower counts.
5. Report the balance and plan. New plugin connections default to no daily connection cap;
   the actual usable wallet balance still limits spending. Do not recommend a cap during setup.
   If this existing connection returns a numeric `connection.daily_cap_credits`, report that
   actual limit and remaining allowance. When it is `null`, omit cap details from the setup summary.

Every Superlurk plan, including free, can connect. Searches use the same account's wallet,
usable free or paid credits, prices and saved results as the Superlurk website. A plan alone
does not guarantee spendable credits. At zero balance, the person can still connect and use
free discovery, balance and their own saved results; a paid run needs enough usable credits.

Eligible people may claim 10 trial credits, valid for 30 days, through Superlurk's existing
website browser verification, including email verification and CAPTCHA. The trial is a one-time
offer per person, with account, verified email, source IP and browser eligibility checks. It is
not a new allowance for each plugin or connection. Never promise a grant, automatically claim
credits, suggest bypassing eligibility checks or report credits that `get_balance` did not return.
If verification is still needed, explain that the person must finish it on the Superlurk website.

This setup check does not call `run_search` and spends no credits. A successful balance/discovery
check proves only that this connection can authenticate and read those tools; it does not prove
all catalog actions, search execution or rich ChatGPT cards have been tested.

For a 401, an `unauthenticated` error or `_meta["mcp/www_authenticate"]`, reconnect through the
client's own UI. A `search:read` connection cannot run searches; reconnect with `search:run` only
when the person wants that permission. Do not repeatedly retry a revoked connection.

When setup succeeds, explain the next step: ask for a search, see its exact credit price, then
approve that quote. Purchases remain on the website; if needed say “Top up in Superlurk” as plain
text, without a purchase link. Never run a paid search as an automatic setup test.
