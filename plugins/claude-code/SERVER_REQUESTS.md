# Claude Code plugin release dependencies

**16 November 2026:** version 0.3.7 is manually available from public plugin-only main
`c9c36333b430577ec9d6eb372cbe9e4ebfe3a10f`. The existing Claude and OpenAI 0.3.7 directory drafts remain
unsubmitted and unpublished. This working source and the hosted service require evidence separate from that
public snapshot.

Version 0.3.7 reuses the shared eight-tool MCP server and charging path. The source changes keep saved rows
and whole links reachable, restore supported TikTok profile source URLs, report actual settled search charges,
and bound group status polling across mixed terminal outcomes, rate limits and page lifecycle changes.
The r0039 widget rollout has partial actual-host evidence. Complete widget and retained-client qualification,
the later customer-fix source freeze and its final archives and rollout remain open.
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
* Preserve the public plugin-only manual distribution and build a fresh allowlisted artifact for changed source.
  A tester must be able to install it without private application-repository access. Directory submission,
  approval, publication and public-directory installation verification remain separate gates.
* Confirm the configured endpoint, OAuth issuer and web integration guides agree with the release environment.
* Preserve real-client, paid-provider, account/device access and directory-review checks as distinct gates.
  A local fixture pass is evidence only for the tested fixture scenario.
