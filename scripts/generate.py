#!/usr/bin/env python
"""Regenerate src/wefunder/_generated from spec/openapi.yaml.

The generated layer is committed. CI's `generated-in-sync` job re-runs this and fails on
any diff, so run it after `scripts/sync_spec.py` and commit both spec/ and _generated/.
Requires the pinned openapi-python-client and ruff (see pyproject [dev]). The generator's
own PATH-dependent ruff hooks are disabled (openapi-python-client.yaml `post_hooks: []`);
this script runs the same two ruff passes explicitly through the current interpreter, so
local and CI output are byte-identical regardless of what is on PATH.
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
    # Same passes the generator would run, but via this interpreter's pinned ruff.
    subprocess.run(
        [sys.executable, "-m", "ruff", "check", str(OUT), "--fix-only", "--extend-select=I", "-q"], cwd=ROOT, check=True
    )
    subprocess.run([sys.executable, "-m", "ruff", "format", str(OUT), "-q"], cwd=ROOT, check=True)
    (OUT / "py.typed").touch()
    ops = sum(1 for _ in (ROOT / "spec" / "openapi.yaml").read_text().splitlines() if "operationId:" in _)
    print(f"generated {OUT.relative_to(ROOT)} from spec/openapi.yaml ({ops} public operations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
