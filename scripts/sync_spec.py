#!/usr/bin/env python
"""Sync spec/openapi.yaml from the canonical Wefunder swagger.

The SDK ships the PUBLIC tier only (stable + beta). Filtering is owned by the wefunder
repo's api-docs/scripts/build-filtered-spec.js — the single source of truth for which
x-wf-stability tiers are public — so this runs it and copies its output rather than
reimplementing the filter. Maintainer step (needs a local wefunder checkout):

    python scripts/sync_spec.py /path/to/wefunder    # or WEFUNDER_REPO=...
    python scripts/generate.py

Commit spec/ and src/wefunder/_generated together.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main(argv: list[str]) -> int:
    repo_arg = os.environ.get("WEFUNDER_REPO") or (argv[1] if len(argv) > 1 else None)
    if not repo_arg:
        print("error: set WEFUNDER_REPO=/path/to/wefunder (or pass it as an argument).", file=sys.stderr)
        return 1
    repo = Path(repo_arg).resolve()
    builder = repo / "api-docs" / "scripts" / "build-filtered-spec.js"
    if not builder.exists():
        print(f"error: {builder} not found — is {repo} a wefunder checkout?", file=sys.stderr)
        return 1
    print("→ building public-tier spec via the canonical filter…")
    subprocess.run(["node", "scripts/build-filtered-spec.js"], cwd=repo / "api-docs", check=True)
    src = repo / "swagger" / "v2" / "swagger.public.yaml"
    dest = ROOT / "spec" / "openapi.yaml"
    shutil.copyfile(src, dest)
    ops = len(re.findall(r"^\s+operationId:", dest.read_text(), re.M))
    print(f"✓ wrote spec/openapi.yaml ({ops} public operations)")
    print("  next: python scripts/generate.py && git add spec src/wefunder/_generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
