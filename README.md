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

Version 0.3.6 clarifies quote-only warning and balance disclosure and discovery keywords. Public 0.3.5 artifacts remain unchanged; this candidate does not imply directory approval, publication or complete client acceptance.

## Preparation checkpoint: 14 November 2026

This 0.3.6 snapshot is prepared for manual installation and publication review. Preparation is not a production-deployment receipt, official directory approval or public-installation proof. The company OpenAI draft and Claude directory draft remain at 0.3.5; the older personal cloud package is 0.3.2. No vendor form or cloud package is changed by this Git snapshot.

The exact 0.3.6 Codex CLI 0.162.1 package has passed a private install, normal browser reconnect, balance and quote-only disclosure check. Full catalog execution, remaining client/device/lifecycle checks, reviewer access and walkthrough remain separate gates. Source submission notes retain their dated authoring checkpoint; they are not a current budget authorization. Only the separately approved, source-bound live manifest governs paid QA. This artifact preparation performs no live searches, credit allocations, provider calls or paid retries.

Support: [contact](https://superlurk.com/contact), [privacy](https://superlurk.com/privacy), [terms](https://superlurk.com/terms).

### Rollback reference

The prior MIT-licensed 0.3.5 public snapshot is `882e65ec6e202a5e8b9a9e0be01929795c6ade22`. Existing 0.3.5 archives remain unchanged. Use the client's documented named marketplace/plugin update flow and verify the loaded package version and file hashes; do not clear credentials, delete unrelated plugins or add a second direct MCP server. This preparation does not test or claim a persistent downgrade.
