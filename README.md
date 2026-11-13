# Superlurk plugin release candidate

This directory contains plugin files only. No application-repository access is required.

Install from this extracted directory:

```sh
codex plugin marketplace add . --json
codex plugin add superlurk@superlurk-release --json
claude plugin marketplace add .
claude plugin install superlurk@superlurk-release
```

The Codex marketplace selects plugins/codex, the generated transport compatibility projection of the same Superlurk identity, version, skills and icon. plugins/openai is the canonical ChatGPT package and retains its OpenAI OAuth extension; it is not a second Codex install.

Restart Codex, then run `codex mcp login superlurk`. In Claude Code, open `/mcp`, select `plugin:superlurk:superlurk`, and choose Authenticate. Sign in to your own Superlurk account in the browser; OpenAI or Claude account sign-in is separate. Never paste tokens in chat. Use either the plugin connection or a direct MCP connection in a test session, so tools are not duplicated.

This artifact is prepared; directory publication and complete client qualification are not established. Native mobile/account access, live test budget, reviewer credentials and walkthrough remain separate gates.

## License

Superlurk's plugin files are licensed under [MIT](./LICENSE), copyright 2026 Scrapegg Software Private Limited. Vendored validation schemas retain Apache 2.0; see [third-party notices](./THIRD_PARTY_NOTICES.md). The private application repository, hosted service and customer/provider data are outside this plugin-only distribution.

Version 0.3.5 adds licensing metadata and notices. Previously prepared 0.3.4 archives remain unchanged; this distribution does not imply directory approval or complete client acceptance.
