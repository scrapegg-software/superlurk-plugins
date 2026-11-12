# Superlurk for ChatGPT and Codex

Version **0.3.3** bundles four workflows and the existing remote OAuth MCP connection in one
portable Agent Plugins package. It uses the same account, catalog, balance and saved results as
the Superlurk website. The public directory review and live acceptance checks are pending.
The publisher is **Scrapegg Software Private Limited**; the product name remains **Superlurk**.

## Plugin-only distribution

The dedicated distribution repository is [scrapegg-software/superlurk-plugins](https://github.com/scrapegg-software/superlurk-plugins).
It is prepared separately from the private application repository. A repository URL is not evidence of public
availability or directory approval; the repository can remain private during submission preparation.
Once you can access its reviewed marketplace, install the shared identity in Codex with:

```bash
codex plugin marketplace add scrapegg-software/superlurk-plugins --json
codex plugin add superlurk@superlurk-release --json
codex mcp login superlurk
```

The distribution's `plugins/openai` folder is the canonical ChatGPT package, and `plugins/codex` is its generated
Codex transport projection. Install one intended Superlurk connection. ChatGPT uses the OpenAI directory package
and its own connection flow; adding the Codex marketplace does not install it in ChatGPT.

## Package and developer checkout

| Component | Purpose |
| :-- | :-- |
| `plugin.json` | Portable identity, OpenAI listing, onboarding and five positive/three negative review cases. |
| `mcp.json` | Streamable HTTP connection to `https://mcp.superlurk.com/mcp`. |
| `skills/setup` | Browser sign-in and free discovery/balance checks. |
| `skills/search` | Discovery, exact prices, approval, bulk and contextual follow-ups. |
| `skills/results` | Free history and saved pages; separately quoted load-more and refresh. |
| `skills/balance` | Credits, plan and optional connection cap. |
| `assets/icon.png` | Existing Superlurk Dome mark, copied from the repository's existing square Claude plugin icon. |
| `validation` | Offline checks and unchanged, hash-receipted upstream schemas. |

OAuth prefers CIMD and leaves the runtime's DCR fallback available. Discovery supplies endpoints
and scopes; no client ID, credential, token, header, environment secret, lifecycle hook or
registered application ID is embedded. The server exposes eight tools, independently of the
number of social networks. Its ChatGPT price/results/balance UI resources are hosted by that
server from `integrations/chatgpt-app`; the package does not duplicate the templates.

The repository marketplace is `.agents/plugins/marketplace.json`, named `superlurk-local`,
with `source.path: ./integrations/codex-compat-plugin` relative to the **repository root**.
That generated Codex projection has this canonical package's identity, version, skills and icon;
only its MCP transport declaration differs for older Codex compatibility. The canonical package
in this folder retains ChatGPT's documented OAuth extension. There is one authoring package and
public Superlurk identity, with separate client artifacts.

For a developer application-repository checkout only, install the local Codex artifact from that repository root:

```bash
codex plugin marketplace add . --json
codex plugin add superlurk@superlurk-local --json
codex mcp login superlurk
```

Complete browser authentication in your own Superlurk account. Restart the desktop app after a
local package refresh and start a fresh chat. Release ZIPs have their own `superlurk-release`
marketplace and installation README. The Codex-only ZIP includes that marketplace wrapper;
the OpenAI ZIP contains the canonical package for ChatGPT packaging and review. Installation,
authentication and actual workflows still require separate observations in each client.

Use the packaged setup workflow after installation. If a standalone Superlurk MCP connection
already exists, select one connection path for testing and avoid duplicate registration. Never
paste secrets into chat. A successful free setup check proves discovery and balance access;
quote/run, rich UI, token refresh, restart persistence and revocation need their own evidence.

Sign in to your own Superlurk account through the client's browser flow. Your ChatGPT or Codex
account sign-in is separate. Every Superlurk plan, including free, can connect, and all authorized
clients use your existing Superlurk wallet, usable free or paid credits, prices and saved results.
A plan does not replace the usable credits needed for a paid run. At zero balance you can still
connect, discover searches, check balance and read your own saved results for free.

Eligible people may claim 10 trial credits, valid for 30 days, after completing Superlurk's existing
website email/CAPTCHA browser verification. This is a one-time trial per person, checked against
the account, verified email, source IP and browser, rather than an allowance per plugin or connection.
Installing or connecting the plugin does not guarantee a grant. Complete any pending verification
on the Superlurk website and check the returned balance. Plans and top-ups are purchased only on
the website; never paste credentials or payment details into chat.

### Older Codex compatibility projection

Codex CLI 0.162.1 rejects the documented OpenAI OAuth extension in a portable
`mcp.json` server entry. Keep this canonical package unchanged for ChatGPT. Generate
its Codex transport projection into a fresh ignored directory with:

```bash
python integrations/openai-plugin/validation/codex_projection.py .local/plugin-release/codex-projection
```

The generated bundle retains the same plugin name, version, manifest, skills and
icon. Only `mcp.json` changes to the standard Streamable HTTP URL declaration.
The same backend still requires browser OAuth, discovered by the host; the projection
contains no token or alternate backend. It does not complete login or prove runtime
acceptance. Register its generated directory in an isolated local marketplace to test
the bundled server, then use `codex mcp login superlurk` when authentication is authorized.
Do not create a second direct MCP entry as a substitute for the plugin test.

This is a generated compatibility artifact from one authoring package and identity,
not a separately maintained public plugin. Its runtime, OAuth and paid workflow
evidence remain separate from the canonical package's validation.
The checked-in `integrations/codex-compat-plugin` contains the same seven generated runtime
members. Release packaging verifies every member against the canonical source and rejects stale
skills, identities or transport settings. Regenerate it after any canonical content or version change.

## Validate locally

From the repository root, with its locked Python dependencies available:

```bash
PYTHONPATH=services/python python integrations/openai-plugin/validation/validate.py
PYTHONPATH=services/python python -m pytest tests/test_openai_plugin.py -q
```

The validator uses the unchanged upstream Agent Plugins 1.0.0 schemas captured in
`validation/upstream/provenance.json`. **Known external mismatch:** the published MCP schema
currently rejects the OpenAI server `extensions` object that OpenAI's packaging guide
requires for OAuth configuration. We validate the portable MCP projection against that schema
and the OAuth object separately against OpenAI's documented fields. The report explicitly does
not claim full upstream MCP schema acceptance or portal acceptance. Do not remove OAuth or
silently alter the upstream schema to hide this mismatch.

Schema validation, skill checks, fixture execution, real client tests, live provider tests,
portal scanning, review and publication are distinct statuses. See [SUBMISSION.md](./SUBMISSION.md)
for the remaining public-release gates.

## Charging and limitations

`run_search` is the sole spending tool and requires an exact quote and authorization. Successful
valid empty answers are charged; provider/input failures and reusing your own saved results are
free. New plugin connections default to no daily connection cap; the usable wallet balance still
limits spending. Existing connection caps remain enforced. Purchases stay on the website. The MCP
tools cannot publish social posts, buy credits, create monitors, or invoke server exports.

Native data and web-discovered pages are labeled separately; web sources do not supply native
likes, views or follower counts. Available networks, searches and prices come from discovery,
not a number hard-coded into the skills.

Official references checked for this package on 12 November 2026:
[packaging](https://developers.openai.com/plugins/build/plugins),
[authentication](https://developers.openai.com/plugins/build/auth), and
[submission field reference](https://developers.openai.com/plugins/deploy/submission).
