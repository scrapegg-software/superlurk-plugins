# Claude Code plugin release dependencies

Version 0.3.5 reuses the existing shared MCP server; no additional server or charging path is required.
The current source catalog covers 25 networks; release tests check that count against the registry.
The source and nested marketplaces now agree with plugin.json. Earlier server requests and November 6
fixture observations remain available in Git history; their completion does not qualify a current release.

## Required shared behavior

* HTTP `/mcp`, authenticated eight-tool discovery, readable text and structured outputs.
* OAuth discovery from 401, DCR/CIMD, PKCE S256, hosted callback handling and port-agnostic native loopback
  callbacks, rotating refresh tokens and immediate server-side revocation.
* Owner-scoped quotes/results, safe replay of a quote, server-enforced optional cap and correct charging for
  valid empty results versus failures. An annotation never proves conversational approval.
* `get_price` supports bulk lookup, saved-result load-more/refresh and owner-bound contextual follow-ups;
  plugin instructions preserve those interfaces and keep provider cursors out of assistant-visible input.

## Release gates

* Validate a pinned source artifact and record the installed client version and actual tool-call observations.
* Build an integration-only distributable that a tester can extract and install without private repository access.
  Public host/repository and directory publication are pending owner publication approval and need receipts.
* Confirm the configured endpoint, OAuth issuer and web integration guides agree with the release environment.
* Preserve real-client, paid-provider, account/device access and directory-review checks as distinct gates.
  A local fixture pass is evidence only for the tested fixture scenario.
