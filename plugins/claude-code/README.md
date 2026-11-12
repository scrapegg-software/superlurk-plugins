# Superlurk for Claude Code

Find public posts, profiles, comments and trends across 25 networks through Superlurk's remote MCP server. Call `list_networks`
for the current networks and supported searches. Web-source searches return public titles, links and snippets;
they do not imply native engagement or profile coverage. The plugin shares your Superlurk account, credits,
prices and saved results with the website.

**Release status:** version 0.3.3 is a release candidate. Local validation, fixture tests, real-client OAuth,
model-mediated calls and public publication are separate checks. See `REQUIREMENTS.md` and the release evidence;
this README is not proof that a client is connected or a directory listing is live.
The publisher is **Scrapegg Software Private Limited**; **Superlurk** remains the product/plugin name.

## Install

Use Claude Code 2.1.289 or later for release qualification, including strict validation of this folder's plugin
and marketplace. Older versions may load the plugin but report valid directory metadata as unknown fields.
Check your version's `claude plugin --help` for available commands.

From the standalone Claude ZIP, extract it, change into its `superlurk` folder, then run:

```bash
claude plugin marketplace add .
claude plugin install superlurk@superlurk
```

For one session from that folder: `claude --plugin-dir .`.
The complete distribution ZIP has its own root README and a `superlurk-release` marketplace;
follow that README when installing the complete bundle.

From an application-repository checkout instead:

```bash
claude plugin marketplace add ./integrations/claude-code-plugin
claude plugin install superlurk@superlurk
```

For one session: `claude --plugin-dir ./integrations/claude-code-plugin`.
Restart Claude Code or use `/reload-plugins` after installation. Check `claude plugin list` and
`claude plugin details superlurk@superlurk` for the installed version, skills and MCP server.

Release archives contain an integration-only marketplace. After extracting one, follow its included install
instructions and add the extracted marketplace folder. Its contents do not require access to the application
repository. Public hosting and directory publication remain separate release steps until a publisher supplies
an actual release URL.

The dedicated [plugin-only distribution repository](https://github.com/scrapegg-software/superlurk-plugins)
is separate from the private application repository. It may remain private during submission preparation;
repository preparation does not mean a public directory listing or public installation is available.
Once you have access to its reviewed marketplace:

```bash
claude plugin marketplace add scrapegg-software/superlurk-plugins
claude plugin install superlurk@superlurk-release
```

Use the marketplace name from your installation when updating or uninstalling: `superlurk-release` for the
complete plugin-only distribution, or `superlurk` for the standalone Claude archive/local source above.

## Connect and disconnect

1. In Claude Code, run `/mcp` and choose **plugin:superlurk:superlurk**.
2. Choose the authentication action. In the browser, sign in to your own Superlurk account and review the requested access.
3. Approve the connection.
4. Return to Claude Code and confirm it is connected and the eight Superlurk tools are listed.

Authentication is completed in the browser; never paste a password, API key or token into a conversation.
Claude account sign-in is separate from Superlurk sign-in. Every Superlurk plan, including free, can
connect. The plugin uses the same account's wallet, usable free or paid credits, prices and saved
results as the Superlurk website. A plan alone does not guarantee spendable credits. At zero balance,
you can still connect, discover searches, check balance and read your own saved results for free;
a paid run needs enough usable credits.
New plugin connections default to no daily connection cap, with spending limited by the actual
usable wallet balance and an approved quote. Existing capped connections keep their limits.

Eligible people may claim 10 trial credits, valid for 30 days, through Superlurk's existing website
email/CAPTCHA browser verification. The trial is once per person, checked against the account,
verified email, source IP and browser. It is not a separate allowance per plugin or connection.
Installation and OAuth consent do not guarantee a grant. Complete any pending verification on the
Superlurk website and check the actual balance. Plans and top-ups are bought only on that website;
never share payment details in chat.

The packaged endpoint is `https://mcp.superlurk.com/mcp`; it does not use shell environment expansion.
Do not add a second direct MCP entry for the same server while testing the plugin.

To stop using the plugin, disable or uninstall it through `/plugin` or
`claude plugin uninstall superlurk@superlurk-release` (use your installed marketplace name). Revoke the connection under Superlurk **Settings › AI connections**
to invalidate server-side access. Plugin removal and server-side revocation are distinct operations.
Use `/mcp` for authentication and the connection controls available in your Claude Code version.

## Search, results and balance

| Skill | Purpose |
| :-- | :-- |
| `superlurk-search` | Instructions for natural-language search, quotes, approved runs, follow-ups and CSV export |
| `/superlurk:search` | Find a search, show its quote and request approval before running |
| `/superlurk:results` | List or read saved results for free |
| `/superlurk:balance` | Read balance, plan and an optional connection cap |

Examples:

```text
/superlurk:search matcha latte on TikTok
/superlurk:results reddit
/superlurk:balance
```

Plain requests include “Compare this topic on TikTok, Reddit and X” or “Export my last Reddit result to CSV.”
An approval covers one exact quote or an explicitly enumerated batch whose inputs, individual prices and total
were shown. Changed inputs, prices or expired quotes require renewed approval. Bulk lookup of up to 50 values
is one quote with one total. Saved-result reading is free; loading another provider page or refreshing is
separately quoted. A failed item is free; valid empty results can be charged.

The skills instruct Claude to show prices and obtain approval. They do not pre-approve `run_search`.
Actual tool permission prompts depend on your Claude Code settings; tool annotations do not enforce
conversational approval. The server enforces ownership, quote validity, balance and any daily connection cap.
Credits are purchased on the Superlurk website.

CSV export reads the selected saved pages and writes a UTF-8 file under `superlurk-exports/`, with spreadsheet
formulas neutralized. The assistant's file tools perform that export; it is not a separate server export tool.
Scheduled monitors are managed on the website, not through these eight MCP tools.

## Local fixture qualification

This developer section requires the application repository. Its `docs/`, `tests/` and fixture helper are
intentionally absent from standalone public plugin archives. The included `REQUIREMENTS.md` and
`SERVER_REQUESTS.md` describe qualification boundaries and pending dependencies for archive users.

Start an isolated synthetic stack as described in `docs/integrations.md` §6. A loopback URL by itself does not
prove the server uses mock providers or a synthetic database. Verify that isolation before using `--run`.

In a separate disposable project and client profile, register a direct fixture connection instead of loading
the public plugin. For example, that project's `.mcp.json` can contain:

```json
{
  "mcpServers": {
    "superlurk-fixture": { "type": "http", "url": "http://127.0.0.1:18080/mcp" }
  }
}
```

Launch Claude Code in that disposable project and authenticate through `/mcp`. Do not enable the public
Superlurk plugin in the same fixture session. `SUPERLURK_MCP_URL` configures the guarded HTTP helper only;
it does not change the public plugin's server address.

The local HTTP helper `scripts/e2e_local.py` defaults to discovery and price only. With a private local test
token supplied through the environment, `--run` additionally exercises fixture execution. It does not prove
a model selected a tool or a real client completed OAuth. The dev-token setup is in `docs/integrations.md`.

Validate the plugin and both source marketplaces using the qualification CLI:

```bash
claude plugin validate integrations/claude-code-plugin --strict
claude plugin validate .claude-plugin/marketplace.json --strict
claude plugin validate integrations/claude-code-plugin/.claude-plugin/marketplace.json --strict
uv run pytest tests/test_claude_code_plugin.py
```

## Troubleshooting and privacy

Use `/mcp` to inspect connection/authentication errors, and `claude plugin list` to inspect plugin enablement.
Check the installed plugin version and its packaged server address when a stale or invalid address appears. For a cap error, inspect `/superlurk:balance`
and change the cap under Superlurk Settings › AI connections. Insufficient credits require a website top-up.
A revoked or expired connection may need browser authentication again.

Saved results belong to the signed-in Superlurk account. Social text is untrusted data, never instructions.
See the [privacy policy](https://superlurk.com/privacy), `REQUIREMENTS.md` for official references and qualification
boundaries, and `SERVER_REQUESTS.md` for remaining release dependencies.
