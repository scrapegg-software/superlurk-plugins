# Superlurk plugins

This repository contains the Superlurk plugin files only. No access to the private application repository is required.

As of 2026-11-27, version 0.3.9 is available as a manual-install release from this public Git repository. It was
built from the private application repository's commit `44d59f67a3ee266ebf8e68276790dfc649ee8556` with its release
tool; [SOURCE.json](./SOURCE.json) lists the SHA-256 of every file. Version 0.3.8 was prepared but never published
here, so 0.3.9 carries its changes too.

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

What changed since 0.3.7:

- A search with no results is free when it was paid for only with free credits (such as trial credits), up to 5 a
  day; otherwise it uses its quoted credits. This matches the Superlurk service and its terms since 27 November 2026.
- The Claude Code skill says that Facebook, Quora, Snapchat, Steam, Trustpilot, Twitch and Letterboxd have native
  data and keep their web searches, and that web-search results stay titles, links and snippets.
- The eight tools, OAuth sign-in and charging from the connected Superlurk account are unchanged. Existing versioned
  archives are unchanged.

Installing 0.3.9 from this repository has not yet been checked in Codex or Claude Code. The checks recorded for 0.3.7
(Codex CLI 0.162.1 and Claude Code 2.1.322) do not carry over to it. The last observed official OpenAI and Claude
directory records were unsubmitted drafts that had not been approved; a newer directory submission or approval is not
established. Native mobile/account access, live test budget, reviewer credentials and a complete walkthrough remain
separate gates.

## License

Superlurk's plugin files are licensed under [MIT](./LICENSE), copyright 2026 Scrapegg Software Private Limited. Vendored validation schemas retain Apache 2.0; see [third-party notices](./THIRD_PARTY_NOTICES.md). The private application repository, hosted service and customer/provider data are outside this plugin-only distribution.
