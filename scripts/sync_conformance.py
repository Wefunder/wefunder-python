#!/usr/bin/env python
"""Vendor the cross-language conformance vectors from Wefunder/wefunder-node.

The vectors (see conformance/README.md in that repo) are the behavioural contract every
Wefunder SDK must pass identically. This copies conformance/*.json + manifest.json at a
pinned git ref (default: the one recorded in conformance/PIN; pass a tag/sha to repin) via
raw.githubusercontent.com, verifies each file's SHA-256 against the manifest, and rewrites
PIN. tests/test_conformance.py then runs every case against this SDK.
"""

from __future__ import annotations

import hashlib
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "conformance"
PIN = DEST / "PIN"


def read_pin() -> tuple[str, str]:
    values = dict(
        line.split("=", 1) for line in PIN.read_text().splitlines() if "=" in line and not line.startswith("#")
    )
    return values["repo"], values["ref"]


def fetch(repo: str, ref: str, path: str) -> bytes:
    url = f"https://raw.githubusercontent.com/{repo}/{ref}/conformance/{path}"
    with urllib.request.urlopen(url) as resp:  # noqa: S310 — fixed GitHub host
        return resp.read()


def main(argv: list[str]) -> int:
    repo, ref = read_pin()
    if len(argv) > 1:
        ref = argv[1]
    manifest_bytes = fetch(repo, ref, "manifest.json")
    manifest = json.loads(manifest_bytes)
    for name, sha in manifest["files"].items():
        data = fetch(repo, ref, name)
        actual = hashlib.sha256(data).hexdigest()
        if actual != sha:
            print(f"error: {name} sha256 {actual} != manifest {sha}", file=sys.stderr)
            return 1
        (DEST / name).write_bytes(data)
    (DEST / "manifest.json").write_bytes(manifest_bytes)
    PIN.write_text(
        "# Source of the vendored vectors: Wefunder/wefunder-node, conformance/*.json at this ref.\n"
        "# Refresh with:  python scripts/sync_conformance.py [ref]\n"
        f"repo={repo}\nref={ref}\n"
    )
    n, version = len(manifest["files"]), manifest["conformance_version"]
    print(f"vendored {n} vector files from {repo}@{ref} (conformance_version {version})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
