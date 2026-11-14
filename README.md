# Superlurk plugins

This repository contains the Superlurk plugin files only. No access to the private application repository is required.

As of 2026-11-15, version 0.3.7 is available as a manual-install release candidate from this public Git repository. The last observed public `main` commit was `165b9a5c346db43a3f347a100c188bec6f457a7e` (tree `a7949d61e67789246cd6e2b962fe69733ca23a0a`).

Install from the public repository:

```sh
codex plugin marketplace add https://github.com/scrapegg-software/superlurk-plugins --ref main --json
codex plugin add superlurk@superlurk-release --json
claude plugin marketplace add https://github.com/scrapegg-software/superlurk-plugins --scope user
claude plugin install superlurk@superlurk-release --scope user
```

For an extracted release directory, use `.` as the marketplace source and omit Codex's `--ref main` option.

The Codex marketplace selects `plugins/codex`, the generated transport compatibility projection of the same Superlurk identity, version, skills and icon. `plugins/openai` is the canonical ChatGPT package and retains its OpenAI OAuth extension; it is not a second Codex install.

Restart Codex, then run `codex mcp login superlurk`. In Claude Code, open `/mcp`, select `plugin:superlurk:superlurk`, and choose Authenticate. Sign in to your own Superlurk account in the browser; OpenAI or Claude account sign-in is separate. Never paste tokens in chat. Use either the plugin connection or a direct MCP connection in a test session, so tools are not duplicated.

Fresh public Git installation and static checks passed with Codex CLI 0.162.1 and Claude Code 2.1.322. Both hosts reported an enabled 0.3.7 plugin; their installed payloads matched the published source, with four skills and one Superlurk MCP declaration each. These checks do not establish authenticated tool behavior, model-mediated skill activation, host UI behavior or complete retained client acceptance.

The last observed official OpenAI and Claude directory records were unsubmitted version 0.3.6 drafts that had not been approved. A newer directory submission or approval is not established. Native mobile/account access, live test budget, reviewer credentials and a complete walkthrough remain separate gates.

Version 0.3.7 keeps saved rows and whole links reachable through free reading pages, restores supported TikTok profile source URLs, reports settled search charges accurately, and bounds group status polling across mixed outcomes, rate limits and page lifecycle changes. The eight tools, OAuth and account charging are unchanged. Existing versioned archives are unchanged.

## License

Superlurk's plugin files are licensed under [MIT](./LICENSE), copyright 2026 Scrapegg Software Private Limited. Vendored validation schemas retain Apache 2.0; see [third-party notices](./THIRD_PARTY_NOTICES.md). The private application repository, hosted service and customer/provider data are outside this plugin-only distribution.
