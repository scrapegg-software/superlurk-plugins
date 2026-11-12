# OpenAI submission status

**Current package 0.3.3 is prepared for Scrapegg Software Private Limited.** It retains the Superlurk product identity and points to the dedicated plugin-only distribution repository. No new portal upload, scan, submission, approval or publication is established by this metadata update.

**Version 0.3.2: private owner-portal upload accepted; not submitted or publicly published.** The
[12 November production report](../../implementation_evidence/integrations/production_main_2026-11-12/README.md)
records the private package update to 0.3.2 and displayed server/skill metadata. This is package-ingestion evidence,
not a directory scan pass, publisher verification, installed ChatGPT acceptance, submission, approval or public
listing. Actual ChatGPT installation/conversation remains unverified in that report.

The widget refresh needs its own pinned build, deployment and real-host readback. Do not relabel the 0.3.2 upload
or earlier screenshots as acceptance of refreshed templates. Follow [release next steps](../RELEASE_NEXT_STEPS.md);
this file does not select or change the next release version.

The public package targets ChatGPT and Codex through the universal plugin directory. It contains
one MCP server, so the five positive and three negative cases belong in
`plugin.json → extensions.com.openai.review.test_cases`. They describe expected behavior, not
completed test results. Run each case from a clean client against the pinned release and retain
redacted evidence. The saved-comment follow-up case needs an owned YouTube comment result with
an eligible reply item; create that prerequisite through the normal quoted customer path as
part of the acceptance run rather than inventing a provider token.

Before submission:

- Reconcile the source package, deployed API/catalog and the artifacts' hashes/versions. Finish
  real install, sign-in, quote/run, saved-result, bulk, follow-up, load-more/refresh, restart,
  access-token refresh, isolation and revocation checks on every supported client surface.
- Validate `https://mcp.superlurk.com/mcp`, its resource metadata and authorization issuer over
  public HTTPS. Confirm actual ChatGPT/Codex callback and CIMD/DCR behavior. Use browser sign-in;
  no credential or bearer token belongs in this package.
- Resolve the documented upstream MCP-schema/OpenAI-extension mismatch in portal scanning and
  retain the finding/decision. Local projected-schema success is not portal acceptance.
- Verify the publisher identity and the existing website, contact, privacy and terms URLs in
  `interface`. Review the AI-integration data categories, purposes, retention, revocation and
  provider disclosures against actual behavior. Complete the required policy attestations.
- Build the Midnight Studio refresh and commit its exact templates. Read deployed content-hashed resource URIs
  and full HTML hashes back, refresh client metadata and start a new conversation. Verify 20 layouts and 25 network
  labels, narrow/light/dark rendering, keyboard access, links, restored state and interrupted actions in real hosts;
  synthetic checks remain separate evidence.
- Check both CSP conventions and configured widget origin. Fetch/connect lists stay empty; only price/results
  may load images from the signed first-party `https://img.superlurk.com` relay. Balance keeps an empty resource
  list. Do not add provider domains or wildcards. For this candidate, validate the intended configured origin
  `MCP_WIDGET_DOMAIN=https://superlurk.com` by reading both `ui.domain` and `openai/widgetDomain` from deployed
  resource metadata and checking the portal requirements. The origin belongs to the single Superlurk universal
  plugin. Earlier proposals for a separate widget subdomain are historical notes, not deployment proof.
- Provide the portal's exact domain-verification challenge at its prescribed URL without
  overwriting another plugin's challenge. Keep domain-verification values out of the package.
- Prepare the fully featured reviewer account and representative sample data with enough
  existing credits. Enter its access information only through the secure portal form. Do not
  add `test_credentials` or `reviewer_instructions` to the ZIP.
  **Blocked:** the current Superlurk UI offers Google and email-code sign-in, with no password
  form. A reviewer email/password alone is not usable through it. Qualify an accepted reviewer
  access method that needs no email/SMS code, magic link or MFA approval before submission;
  this rollout does not introduce that method. See [reviewer-access requirements](https://developers.openai.com/plugins/deploy/submission#complete-review-information).
- Record a reviewer-accessible real walkthrough after acceptance. **No demo recording URL
  exists in this package.** Set `review.demo_recording_url` only when a usable recording exists,
  then rebuild and revalidate the versioned artifact. Do not use a placeholder URL.
- Upload the reviewed ZIP, inspect all imported fields and MCP connection findings, and finish
  required scans. Submit only after those gates pass. After approval, publication is a separate
  owner action. Do not represent review readiness as directory approval.

The full-catalog paid preflight must be regenerated with authored contextual dependencies and current
source/catalog/deployment bindings before approval of credit and provider-dollar ceilings. Historical campaign
totals are not current approval. A second independent QA identity is still needed for isolation checks; a
same-account paid example or fixture coverage is not full-catalog acceptance.

Country targeting and translations are omitted rather than guessed. Confirm any intended
publication targeting in the portal before publishing. `review.commerce` is false: nothing is
sold in the plugin. Existing credits are consumed only after a quote and authorization, and
low balance says “Top up in Superlurk” without a purchase link. Retain the platform's review
decision about this credit model with the submission receipt.

Reference: [OpenAI upload and submission guide](https://developers.openai.com/plugins/deploy/submission).
