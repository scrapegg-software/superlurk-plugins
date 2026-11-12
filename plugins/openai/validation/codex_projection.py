"""Generate the older-Codex transport projection from the canonical OpenAI package.

The public package keeps its documented OpenAI OAuth extension. Codex 0.162.1
rejects that extension in portable mcp.json, so this generated package changes
only that file to the standard transport declaration. The host must still
discover and complete the same backend's OAuth flow; no credentials are added.
Generation and validation do not connect, authenticate, or invoke any tools.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import shutil
from pathlib import Path

import jsonschema

BASE = Path(__file__).resolve().parent
COPY_MEMBERS = (
    "plugin.json",
    "assets/icon.png",
    "skills/setup/SKILL.md",
    "skills/search/SKILL.md",
    "skills/results/SKILL.md",
    "skills/balance/SKILL.md",
)
MEMBERS = (*COPY_MEMBERS, "mcp.json")
_SPEC = importlib.util.spec_from_file_location("canonical_openai_validation", BASE / "validate.py")
assert _SPEC and _SPEC.loader
_VALIDATION = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_VALIDATION)
ProjectionInvalid = _VALIDATION.PackageInvalid


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ProjectionInvalid(message)


def _hashes(root: Path) -> dict[str, str]:
    return {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in MEMBERS}


def _portable_mcp(canonical: Path) -> dict:
    mcp = json.loads((canonical / "mcp.json").read_text(encoding="utf-8"))
    return {
        "$schema": mcp["$schema"],
        "mcpServers": {
            name: {"type": server["type"], "url": server["url"]}
            for name, server in mcp["mcpServers"].items()
        },
    }


def validate_projection(canonical: Path, projected: Path) -> dict:
    """Require exact source identity/content and only the declared MCP projection."""
    _VALIDATION.validate_package(canonical)
    _require(not projected.is_symlink() and projected.is_dir(), "projection must be a directory")
    paths = list(projected.rglob("*"))
    _require(not any(path.is_symlink() for path in paths), "projection symlinks are forbidden")
    _require(
        {path.relative_to(projected).as_posix() for path in paths if path.is_file()}
        == set(MEMBERS),
        "projection must contain exactly the generated runtime members",
    )
    expected_dirs = {
        parent for name in MEMBERS for parent in Path(name).parents if parent != Path(".")
    }
    _require(
        {path.relative_to(projected) for path in paths if path.is_dir()} == expected_dirs,
        "unexpected projection directory",
    )
    for name in COPY_MEMBERS:
        _require(
            (projected / name).read_bytes() == (canonical / name).read_bytes(),
            f"projection changed canonical {name}",
        )
    mcp = json.loads((projected / "mcp.json").read_text(encoding="utf-8"))
    _require(
        mcp == _portable_mcp(canonical),
        "projection MCP transport differs from the canonical source",
    )
    schema = json.loads((BASE / "upstream" / "mcp.schema.json").read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(mcp)
    manifest = json.loads((projected / "plugin.json").read_text(encoding="utf-8"))
    return {
        "valid": True,
        "kind": "generated-codex-transport-projection",
        "name": manifest["name"],
        "version": manifest["version"],
        "canonical_files": _hashes(canonical),
        "projected_files": _hashes(projected),
        "only_transformed_file": "mcp.json",
        "transformation": "omit OpenAI OAuth hint; retain standard HTTPS transport and server identity",
        "authentication": "backend OAuth via host discovery; no embedded credentials",
        "upstream_mcp_schema_acceptance": True,
        "runtime_acceptance": "unrun",
        "oauth_acceptance": "unrun",
        "model_mediated_workflow": "unrun",
    }


def build_projection(canonical: Path, destination: Path) -> dict:
    """Write a fresh output only; never modify or overwrite the canonical source."""
    canonical = canonical.absolute()
    destination = destination.absolute()
    _require(not canonical.is_symlink(), "canonical package root must not be a symlink")
    _VALIDATION.validate_package(canonical)
    resolved_canonical = canonical.resolve()
    _require(
        not destination.resolve().is_relative_to(resolved_canonical),
        "projection output must be outside the canonical package",
    )
    _require(
        not any(parent.is_symlink() for parent in (destination, *destination.parents)),
        "projection output must not traverse a symlink",
    )
    _require(not destination.exists(), "projection destination already exists")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.mkdir(mode=0o700)
    try:
        for name in COPY_MEMBERS:
            target = destination / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(canonical / name, target)
        (destination / "mcp.json").write_text(
            json.dumps(_portable_mcp(canonical), indent=2) + "\n", encoding="utf-8"
        )
        return validate_projection(canonical, destination)
    except BaseException:
        shutil.rmtree(destination)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "destination", type=Path, help="new output directory, normally under .local/"
    )
    parser.add_argument("--canonical", type=Path, default=BASE.parent)
    args = parser.parse_args()
    try:
        report = build_projection(args.canonical, args.destination)
    except (ValueError, KeyError, TypeError, OSError, jsonschema.ValidationError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}))
        return 1
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
