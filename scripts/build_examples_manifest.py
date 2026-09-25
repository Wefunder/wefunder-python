#!/usr/bin/env python
"""Build examples_manifest.json — the verified-JSON artifact the docs site consumes.

Same contract as wefunder-node/scripts/build-examples-manifest.mjs: a `# region <key>` …
`# endregion` block per snippet, keyed by operationId or `guides/<name>`; `lang` MUST equal
the docs tab label ("Python"). See examples/README.md.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
OUT = ROOT / "examples_manifest.json"
REGION = re.compile(r"^\s*#\s*region\s+(\S+)\s*$")
ENDREGION = re.compile(r"^\s*#\s*endregion\b")


def dedent(lines: list[str]) -> str:
    body = list(lines)
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    indents = [len(line) - len(line.lstrip()) for line in body if line.strip()]
    cut = min(indents) if indents else 0
    return "\n".join(line[cut:] for line in body)


def extract_regions(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    key: str | None = None
    buf: list[str] = []
    for line in text.splitlines():
        if m := REGION.match(line):
            if key:
                raise ValueError(f"nested region {m.group(1)} inside {key}")
            key, buf = m.group(1), []
            continue
        if ENDREGION.match(line):
            if not key:
                raise ValueError("endregion without region")
            if key in out:
                raise ValueError(f"duplicate region key: {key}")
            out[key] = dedent(buf)
            key = None
            continue
        if key:
            buf.append(line)
    if key:
        raise ValueError(f"unterminated region: {key}")
    return out


def read_version() -> str:
    m = re.search(r'__version__\s*=\s*"([^"]+)"', (ROOT / "src/wefunder/_version.py").read_text())
    assert m
    return m.group(1)


def read_api_version() -> str | None:
    m = re.search(r'DEFAULT_API_VERSION\s*=\s*"([^"]+)"', (ROOT / "src/wefunder/client.py").read_text())
    return m.group(1) if m else None


def build_manifest() -> dict[str, object]:
    samples: dict[str, str] = {}
    skipped: list[str] = []
    for path in sorted(EXAMPLES.glob("*.py")):
        if path.name.startswith("_"):
            continue
        regions = extract_regions(path.read_text())
        if not regions:
            skipped.append(path.name)
            continue
        for key, source in regions.items():
            if key in samples:
                raise ValueError(f"duplicate sample key across files: {key} (in {path.name})")
            samples[key] = source
    if skipped:
        print(f"build_examples_manifest: no region in {', '.join(skipped)} — not in manifest", file=sys.stderr)
    return {
        "manifestVersion": 1,
        "lang": "Python",  # MUST equal the docs tab label, or the merge no-ops.
        "label": "wefunder",
        "sdkVersion": read_version(),
        "apiVersion": read_api_version(),
        "generatedBy": "scripts/build_examples_manifest.py",
        "samples": dict(sorted(samples.items())),
    }


def serialize(manifest: dict[str, object]) -> str:
    return json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"


if __name__ == "__main__":
    OUT.write_text(serialize(build_manifest()))
    print(f"wrote {OUT}")
