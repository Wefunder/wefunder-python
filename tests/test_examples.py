"""Gates that keep doc examples honest (hermetic): COVERAGE — every public operationId has
an example or is explicitly curl-only; FRESHNESS — the committed manifest matches the
builder; SHAPE — `lang` is a docs tab label."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_examples_manifest import build_manifest, serialize  # noqa: E402

SPEC_OPS = re.findall(r"^\s*operationId:\s*(\w+)", (ROOT / "spec/openapi.yaml").read_text(), re.M)
MANIFEST = json.loads((ROOT / "examples_manifest.json").read_text())
ALLOW = set(json.loads((ROOT / "examples/coverage-allowlist.json").read_text())["curlOnly"])
KEYS = set(MANIFEST["samples"])


def test_every_operation_has_an_example_or_is_curl_only() -> None:
    assert [o for o in SPEC_OPS if o not in KEYS and o not in ALLOW] == []


def test_no_operation_is_both_exampled_and_allowlisted() -> None:
    assert sorted(ALLOW & KEYS) == []


def test_allowlist_has_no_stale_ids() -> None:
    assert sorted(ALLOW - set(SPEC_OPS)) == []


def test_manifest_is_fresh() -> None:
    assert serialize(build_manifest()) == (ROOT / "examples_manifest.json").read_text()


def test_manifest_lang_is_a_docs_tab() -> None:
    assert MANIFEST["lang"] in {"JavaScript", "Python", "Ruby"}
