# OpenAI submission status

**14 November 2026, 09:02:52 UTC manual-distribution checkpoint:** version 0.3.6 is available from the public
plugin-only repository at commit `9d54b0cb0c23d8f1ea77e61bfeb4383e44c1cc5c` as a manual-install release candidate.
The official OpenAI and Claude directory drafts remain 0.3.5, not submitted, approved or published. Public Git
availability does not establish complete retained-client acceptance. Historical checkpoints below keep their
original versions and dates.

**Portal checkpoint, 14 November 2026, 07:23:42 UTC: the company 0.3.5 draft is uploaded, not submitted or published.** The verified company
owner publishes as **Scrapegg Software Private Limited**. Four skills passed package checks. Version 0.3.5
adds MIT licensing, preserves the upstream validation schemas' Apache 2.0 notice and uses the public
[plugin-only repository](https://github.com/scrapegg-software/superlurk-plugins) at reviewed commit
`882e65ec6e202a5e8b9a9e0be01929795c6ade22`. The application repository stays private. Package checks and
business verification do not establish a completed client journey or review acceptance.

A private 12 November production report records the earlier personal 0.3.2 upload. That historical
checkpoint does not describe the current company draft or certify refreshed widgets. Private application
release coordination and evidence are intentionally absent from this public plugin-only distribution.
See this distribution's root README and SOURCE.json for the prepared snapshot and its status; neither
substitutes for production, client or submission receipts.

## Resolve the OpenAI review gates

OpenAI Support case **19960253** has a human response, with no subsequent determination observed in the latest
approved browser check. It is not a formal rejection or preapproval. Support already has the three questions
and said they need not be resent:

- **Operation exposure:** current [tool guidance](https://developers.openai.com/plugins/plugin-guidelines#tool-independence-and-exposure)
  requires individually exposed model-callable operations and disallows discovery/selection plus a generic
  executor enabling operations not individually exposed for review. Superlurk's catalog → generic quote inputs
  → executor structure needs a review-team determination or an explicitly selected adapter design. Eight named
  tools, owner-bound quotes and spending controls do not establish an exception. Preserve the shared eight-tool
  backend/accounting contract for other clients; a fixed-capability OpenAI adapter is not implemented or approved.
- **Reviewer access:** the portal offers email-code sign-in, while the
  [written submission requirements](https://developers.openai.com/plugins/deploy/submission#complete-review-information)
  require a dedicated sample-data account that works without email/SMS codes, magic links or MFA approvals.
  Support has not confirmed that option as an exception or confirmed first-time account initialization. Ordinary
  customer OAuth continues to reuse the website's Google/email-code login. No password feature, special bypass,
  personal customer credentials or session tokens are authorized. The optional profile tool is not a prerequisite
  for this login; do not add a ninth tool merely for authentication.
- **Existing-wallet eligibility:** current [commerce guidance](https://developers.openai.com/plugins/plugin-guidelines#commerce-and-monetization)
  permits existing subscription entitlements but prohibits digital credit/service sales and indirect upsells.
  Existing prepaid-wallet deductions have no confirmed exception. Review the shared errors, OpenAI skills,
  test-case copy and price widget that say “Top up in Superlurk”; plain text without checkout links is not an
  established exemption. Do not change billing or declare this model accepted without the required decision.

## Qualify the submitted release

The shared ChatGPT/Codex identity contains one MCP server and four skills. The five positive and three negative
cases in `plugin.json → extensions.com.openai.review.test_cases` describe expected behavior, not completed tests.
Run each case from a clean actual client against the final pinned release and retain sanitized evidence. The
saved-comment follow-up case needs an owned YouTube comment result with an eligible Replies item; prepare it
through the ordinary quoted path within the exact approved allowance rather than inventing provider context.

Before submission:

- Reconcile the source, schema, catalog, capability state, deployed API/worker/scheduler and artifact versions and
  hashes. The initial `400ea6a7` API clock rollout and `r0036` catalog alignment passed, including authenticated
  exhaustive discovery and a strict 16-sample/900-second watch. The later 0.3.6 source has separate production,
  migration 0061 and bounded health-watch readbacks; complete client and catalog-execution acceptance remain
  pending. Those private operational receipts are outside this plugin-only distribution. Preserve historical
  receipts at their original source and time.
- Complete real install, sign-in, quote/decline/approve/run/poll, saved-result reuse, bulk, follow-up,
  continuation/refresh, export, restart, token refresh, isolation, revocation and package lifecycle checks for every
  retained client surface. Public Codex 0.3.5 installation and bounded CLI balance/results reads are supporting
  evidence, not full desktop/IDE/ChatGPT acceptance. Native-device gaps remain blockers under the retained scope.
- Validate `https://mcp.superlurk.com/mcp`, its eight tool definitions, resource metadata, authorization issuer,
  callback and CIMD/DCR behavior over public HTTPS. Reconnect through browser login where required. No credential
  or bearer token belongs in the package. New connections have no daily-cap selector/default cap; legacy capped
  grants retain their existing limits.
- Re-run the actual portal MCP scan against the final deployment and inspect each tool's live/held findings,
  including the upstream MCP-schema/OpenAI-extension mismatch. Earlier scans and local projected-schema checks
  do not establish current portal acceptance.
- Check the verified publisher's website, contact, privacy and terms URLs in `interface`. Review actual data
  categories, purposes, retention, deletion/revocation, provider authorization and disclosures before attestation.
- Verify the exact built and shipped Midnight Studio template hashes and content-hashed resource URIs, refresh
  host metadata and start a new conversation. Exercise 20 layouts and 25 network labels, safe images/links,
  spacing/columns/buttons, narrow/light/dark, keyboard/accessibility, table/fullscreen, restored state,
  quote expiry, repeated clicks and interrupted/partial-bulk/error cases in actual hosts. Test MCP Apps and the
  OpenAI bridge separately, retaining complete text/structured fallback. Synthetic renders remain separate evidence.
- Check both CSP conventions and the OpenAI widget origin. Fetch/connect lists stay empty; price/results may load
  images only through the signed first-party `https://img.superlurk.com` relay. Balance keeps an empty resource
  list. Do not add provider domains or wildcards. Read back `MCP_WIDGET_DOMAIN=https://superlurk.com` through
  `openai/widgetDomain`. The shared server does not inject host-specific standard `ui.domain`. Confirm nested
  standard UI metadata and both CSP conventions. Earlier separate-widget-subdomain proposals are historical.
- Preserve the existing domain-verification challenge. If a new one is required, use the exact prescribed origin
  and value without overwriting another plugin's challenge. Keep challenge values outside the package.
- Qualify reviewer access once its supported route is confirmed. The dedicated reviewer Auth identity is prepared;
  ordinary first sign-in/product initialization, a populated sample-only account, usable access and allowance
  remain unqualified. Enter accepted access information only in the secure portal review fields, never in the ZIP
  or chat. Do not share a real customer account or fabricate an ordinary first login.
- Record the real ChatGPT test cases and functionality with an accessible video walkthrough. **No demo recording URL is established.** Set `review.demo_recording_url` only when it exists, then rebuild/revalidate
  the versioned artifact. Personal 0.3.2, Copilot screenshots and synthetic renders do not establish this journey.
- Inspect all imported 0.3.5 fields, package checks and final MCP findings. Complete accurate review details,
  five actual positives, three negatives, screenshots and release notes. Submit only after retained claims pass
  or the owner explicitly changes scope. Review new binding agreements with the owner at the time of acceptance.
  Approval, publication and public-directory installation verification are later distinct stages.

## Budget and final declarations

The distinct second QA identity has been supplied; account-isolation evidence must remain tied to the tested
release. A separate source-bound **743-operation QA packet has been approved**, with allocation and paid
execution awaiting qualified runtime, account, provider and guard prerequisites. The two-operation reviewer
allowance is a separate bounded approval. This public package contains no private test manifest, credentials,
credit-allocation authority or execution token. The private operator ledger holds the exact approved operations,
ceilings and settlement evidence; this document neither expands those permissions nor creates account credits.
Only the operations and attempts explicitly covered by the current approval may run. Additional retries,
refreshes, continuations, replacements or top-ups require covered authorization. Historical totals, authored
reservations and fixture success are not execution approval or full-catalog acceptance.

Country targeting and translations are omitted rather than guessed; confirm them in the portal before publication.
`review.commerce: false` is the developer's declaration that no purchase flow exists, not a platform decision that
wallet debits or indirect credit-purchase prompts comply. Retain the actual determination with the submission receipt.

Reference: [OpenAI upload and submission guide](https://developers.openai.com/plugins/deploy/submission).
