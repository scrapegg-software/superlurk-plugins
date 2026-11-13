# Claude Code plugin requirements and evidence

Checked against official Anthropic documentation on **11 November 2026**. Version 0.3.5 uses one remote
Streamable HTTP MCP server and four skills. Public release qualification uses Claude Code **2.1.289 or later**;
the locally installed 2.1.177 is an older compatibility target, not the strict release validator.

## Official references

* [Manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference): plugin metadata, listing fields,
  standard layout and environment variables. Directory icon/privacy fields are recognized by validators from
  2.1.281; earlier strict validators warn. Keep directory-only metadata in plugin.json.
* [Plugin commands](https://code.claude.com/docs/en/plugins/cli-reference): validation, install, details, upgrade,
  disable and uninstall. Validating a folder containing both manifests includes both from 2.1.289.
* [Marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference): relative sources resolve
  from the marketplace root; plugin.json supplies the installed version.
* [MCP reference](https://code.claude.com/docs/en/mcp): HTTP configuration, OAuth through `/mcp`, scoped tools,
  client permission settings and connection lifecycle.
* [Publishing](https://code.claude.com/docs/en/plugins/publish): controlled marketplace, archive and directory
  distribution are separate options; local validation does not imply directory acceptance.

## Packaging and behavior contract

* Plugin and server name: `superlurk`. The bundled connection is `plugin:superlurk:superlurk` and tools are named
  `mcp__plugin_superlurk_superlurk__<tool>`. Components remain at the plugin root.
* All source manifests agree on version 0.3.5. Increment the version on each released content update.
* `.mcp.json` uses the absolute `https://mcp.superlurk.com/mcp` URL without environment expansion or token
  headers. Authentication uses Superlurk's browser OAuth flow. Fixture tests use a separate direct MCP entry.
* Commands pre-approve only tools that do not spend credits. `run_search` is never in `allowed-tools`.
* Approval covers an exact quote or a clearly enumerated batch with its individual prices and total. A changed
  or expired quote needs renewed approval. Tool prompts depend on client permissions; annotations are hints.
  Server enforcement covers account ownership, quote validity, balance and connection caps, not whether a person
  read a message. Saved page reads and quoted provider continuations are distinct operations.
* Public distribution contains integration files only. The application repository is private, verified on
  11 November 2026, so its GitHub install is a developer workflow. An extracted release archive can be added
  locally without application-repository access. Publication needs its own observed receipt.

## Historical evidence, not current client qualification

The 6 November notes recorded synthetic-stack work at server commits `1ab89cf`, `3a21ee7` and `ae4dd65`:
manifest validation and scratch-profile installation, OAuth discovery/DCR/PKCE, local browser consent,
fixture find/price/run/open/balance, and optional no-cap handling. Some shell commands in those original notes
are absent from the currently installed CLI. Use `/mcp` for reproducible interactive authentication guidance.
Those receipts did not establish a model-mediated Claude Code tool call, paid-provider coverage, public
installation, mobile behavior or production readiness. Existing local helper scripts likewise are HTTP tests,
not a substitute for a real assistant session.

## Release qualification

Record CLI version, source SHA, target URL, installed plugin version and an outcome for each case. Keep failed
and unrun outcomes visible. Never log tokens, authorization codes or raw private client configurations.

1. Strictly validate both marketplaces and the plugin on the supported CLI; run the manifest/skill contract tests.
2. Install from an isolated local marketplace and an extracted distributable without private repository access.
   Confirm four skills, one MCP connection, the canonical server address and restart persistence.
3. Complete actual browser OAuth with the default uncapped connection. Confirm discovery exposes the eight tools.
   Separately verify server enforcement on an existing capped connection managed in AI connection settings.
4. In a model session, exercise natural language and all commands; quote/approve/run/poll/read, bulk partial
   failure, saved paging, quoted load-more/refresh, contextual follow-up, cache reuse, balance and CSV safety.
5. Exercise rejected approval, changed/expired quote, insufficient credits/cap, provider failures, session
   expiry/refresh, server outage, revocation and reconnect without double spending.
6. Upgrade an existing 0.3.2 install to 0.3.5, restart, confirm changed content, disable/uninstall and revoke the connection separately.

Automated/fixture results and actual-client observations must be reported separately. No public or directory
release is implied by these requirements.

## Working-tree checks, 11 November 2026

* Pinned qualification CLI 2.1.318, installed only under `.local/qualification/claude-2.1.318`:
  strict validation passed for the plugin folder, root marketplace and nested marketplace. Its directory
  validator explicitly excludes the remote safety/policy review; this is not directory acceptance.
* Existing CLI 2.1.177: ordinary validation passed with two warnings for icon/privacy directory metadata.
  That older CLI is not the strict release baseline. No global CLI installation or upgrade was performed.
* `tests/test_claude_code_plugin.py` and `tests/test_mcp_networks.py`: 28 passed. These check packaging,
  instruction contracts and registry consistency, not model adherence. Ruff on owned Python files and
  `git diff --check` passed. Re-run on the final pinned release revision.
* Actual-client OAuth, model-mediated calls, provider-paid coverage and public publication were not
  established by these packaging checks. Record those in the overall release evidence separately.
