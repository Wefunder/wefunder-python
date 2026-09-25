#!/usr/bin/env python
"""Regenerate src/wefunder/_generated from spec/openapi.yaml.

The generated layer is committed. CI's `generated-in-sync` job re-runs this and fails on
any diff, so run it after `scripts/sync_spec.py` and commit both spec/ and _generated/.
Requires the pinned openapi-python-client (see pyproject [dev]) and ruff on PATH — the
generator formats its output with ruff, so a different ruff version changes the diff.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "src" / "wefunder" / "_generated"


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    cmd = [
        sys.executable,
        "-m",
        "openapi_python_client",
        "generate",
        "--path",
        str(ROOT / "spec" / "openapi.yaml"),
        "--output-path",
        str(OUT),
        "--config",
        str(ROOT / "openapi-python-client.yaml"),
        "--meta",
        "none",
        "--overwrite",
    ]
    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    noise = ("Skipping Integration", "ruff is not in PATH", "If you believe this was a mistake")
    for line in (proc.stdout + proc.stderr).splitlines():
        if line.strip() and not any(n in line for n in noise):
            print(line)
    if proc.returncode != 0:
        return proc.returncode
    (OUT / "py.typed").touch()
    ops = sum(1 for _ in (ROOT / "spec" / "openapi.yaml").read_text().splitlines() if "operationId:" in _)
    print(f"generated {OUT.relative_to(ROOT)} from spec/openapi.yaml ({ops} public operations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
