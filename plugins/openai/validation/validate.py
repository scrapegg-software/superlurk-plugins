"""Offline package checks against pinned upstream schemas and the documented OpenAI fields.

The upstream MCP schema does not yet allow OpenAI's documented server extensions.
Validate the portable projection and OpenAI OAuth object separately, and report that
limitation explicitly. Never silently patch the vendored upstream schema.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import struct
from pathlib import Path
from urllib.parse import urlsplit

import jsonschema

BASE = Path(__file__).resolve().parent
SCHEMA_NOTE = (
    "Upstream MCP 1.0.0 rejects the server extensions object documented by OpenAI. "
    "The unchanged upstream schema validates the portable projection; the OpenAI OAuth "
    "extension is checked separately against the documented contract. Full upstream "
    "MCP schema acceptance and portal acceptance are not claimed."
)


class PackageInvalid(ValueError):
    """A package is incomplete, unsafe to distribute or outside the supported contract."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise PackageInvalid(message)


def _json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    _require(isinstance(data, dict), f"{path.name} must be an object")
    return data


def _packaged_path(root: Path, value: str) -> Path:
    _require(isinstance(value, str) and value.startswith("./"), "paths need a ./ prefix")
    _require(".." not in Path(value).parts and "\\" not in value, "unsafe package path")
    path = (root / value).resolve()
    _require(path.is_relative_to(root.resolve()) and path.is_file(), "missing or escaped file")
    return path


def _https(value: str) -> bool:
    if not isinstance(value, str):
        return False
    p = urlsplit(value)
    return bool(
        p.scheme == "https"
        and p.hostname
        and p.username is None
        and p.password is None
        and not any(c.isspace() or ord(c) < 32 for c in value)
    )


def _validate_schemas(plugin: dict, mcp: dict) -> None:
    provenance = _json(BASE / "upstream" / "provenance.json")
    for receipt in provenance["schemas"]:
        path = BASE / "upstream" / receipt["file"]
        _require(
            hashlib.sha256(path.read_bytes()).hexdigest() == receipt["sha256"],
            "vendored schema hash differs from its retrieval receipt",
        )
    jsonschema.Draft202012Validator(_json(BASE / "upstream" / "plugin.schema.json")).validate(
        plugin
    )
    portable = copy.deepcopy(mcp)
    for server in portable.get("mcpServers", {}).values():
        server.pop("extensions", None)
    jsonschema.Draft202012Validator(_json(BASE / "upstream" / "mcp.schema.json")).validate(portable)


def validate_package(root: Path) -> dict:
    root = root.resolve()
    plugin = _json(root / "plugin.json")
    mcp = _json(root / "mcp.json")
    _validate_schemas(plugin, mcp)
    _require(plugin["name"] == "superlurk", "unexpected plugin identity")
    _require(bool(re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", ""))), "invalid version")
    _require(bool(plugin.get("description", "").strip()), "missing description")
    _require(set(mcp["mcpServers"]) == {"superlurk"}, "exactly one Superlurk server is required")
    server = mcp["mcpServers"]["superlurk"]
    _require(set(server) == {"type", "url", "extensions"}, "unexpected server settings")
    _require(server["type"] == "streamable-http", "Superlurk requires streamable HTTP")
    _require(server["url"] == "https://mcp.superlurk.com/mcp", "unexpected public MCP endpoint")
    _require(
        server["extensions"]
        == {"com.openai": {"auth": {"type": "oauth", "client": {"mode": "cimd"}}}},
        "OAuth must prefer CIMD without credentials or endpoint overrides",
    )
    _require(set(plugin.get("extensions", {})) == {"com.openai"}, "unexpected extension")
    oa = plugin["extensions"]["com.openai"]
    _require(
        set(oa) == {"interface", "onboardingSkill", "review", "publication"},
        "unexpected OpenAI fields (hooks and registered apps are not packaged)",
    )
    interface = oa["interface"]
    limits = {
        "displayName": 30,
        "shortDescription": 30,
        "longDescription": 4000,
        "developerName": 80,
    }
    for field, maximum in limits.items():
        value = interface.get(field)
        _require(isinstance(value, str) and 0 < len(value) <= maximum, f"invalid {field}")
    _require(interface.get("category") == "Productivity", "unexpected category")
    for field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        value = interface.get(field)
        _require(_https(value) and len(value) <= 1024, f"invalid {field}")
    capabilities = interface.get("capabilities")
    _require(
        isinstance(capabilities, list)
        and len(capabilities) <= 20
        and all(isinstance(v, str) and 0 < len(v) <= 120 for v in capabilities),
        "invalid capabilities",
    )
    prompts = interface.get("defaultPrompt", [])
    prompts = [prompts] if isinstance(prompts, str) else prompts
    _require(
        isinstance(prompts, list)
        and len(prompts) <= 3
        and len(prompts) == len(set(prompts))
        and all(isinstance(v, str) and 0 < len(v) <= 128 and "@" not in v for v in prompts),
        "invalid default prompts",
    )
    for field in ("composerIcon", "logo"):
        path = _packaged_path(root, interface.get(field))
        raw = path.read_bytes()
        _require(
            raw.startswith(b"\x89PNG\r\n\x1a\n") and len(raw) <= 5 * 1024 * 1024, "invalid PNG"
        )
        width, height = struct.unpack(">II", raw[16:24])
        _require(48 <= width == height <= 4096, "icon must be square and 48-4096 pixels")
    onboarding = _packaged_path(root, oa["onboardingSkill"])
    _require(onboarding == root / "skills" / "setup" / "SKILL.md", "unexpected onboarding skill")
    for name in ("setup", "search", "results", "balance"):
        text = (root / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
        _require(
            text.startswith(f"---\nname: {name}\ndescription: "), f"invalid {name} frontmatter"
        )
        _require("allowed-tools:" not in text, "skills must not pre-approve spending tools")
    review = oa["review"]
    _require(
        {"test_cases", "commerce", "commerce_description"} <= set(review)
        and set(review) <= {"test_cases", "commerce", "commerce_description", "demo_recording_url"},
        "unexpected review fields",
    )
    if "demo_recording_url" in review:
        demo = review["demo_recording_url"]
        _require(
            _https(demo)
            and urlsplit(demo).hostname not in {"example.com", "example.org", "example.net"},
            "demo must be an actual HTTPS recording URL, not a placeholder",
        )
    _require(review["commerce"] is False, "commerce must remain disabled")
    _require(bool(review["commerce_description"]), "missing commerce explanation")
    cases = review["test_cases"]
    _require(set(cases) == {"positive", "negative"}, "unexpected test case groups")
    for kind, count in (("positive", 5), ("negative", 3)):
        _require(
            isinstance(cases[kind], list) and len(cases[kind]) == count,
            f"need {count} {kind} cases",
        )
        for case in cases[kind]:
            _require(
                set(case) == {"description", "prompt", "tools_triggered", "expected_behavior"},
                "unexpected review case fields",
            )
            for key in ("description", "prompt", "expected_behavior"):
                _require(
                    isinstance(case[key], str) and bool(case[key].strip()), f"missing case {key}"
                )
            _require(isinstance(case["tools_triggered"], str), "tools_triggered must be text")
            if kind == "positive":
                _require(bool(case["tools_triggered"].strip()), "positive case needs tools")
    _require(not any(p.is_symlink() for p in root.rglob("*")), "package symlinks are not portable")
    _require(not (root / "hooks").exists(), "public package must have no hooks")
    return {
        "valid": True,
        "plugin_schema": "upstream 1.0.0",
        "mcp_schema": "upstream 1.0.0 portable projection plus documented OpenAI OAuth checks",
        "full_upstream_mcp_schema_acceptance": False,
        "portal_acceptance": "unrun",
        "notes": [SCHEMA_NOTE],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin_dir", type=Path, nargs="?", default=BASE.parent)
    args = parser.parse_args()
    try:
        report = validate_package(args.plugin_dir)
    except (
        ValueError,
        KeyError,
        TypeError,
        OSError,
        struct.error,
        jsonschema.ValidationError,
    ) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
