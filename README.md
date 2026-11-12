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

This artifact is prepared, not publicly published or fully qualified. Native mobile/account access, live test budget, reviewer credentials and walkthrough remain separate gates.
