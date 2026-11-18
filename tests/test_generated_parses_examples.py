"""Every documented 2xx response example must parse through the generated layer.

Nothing else exercises `_generated` end to end, and pyright excludes it, so a spec sync can pass
ruff, pyright and pytest while an operation cannot parse a real response: openapi-python-client
skips a schema it cannot process and still emits imports of the model it skipped
(`ModuleNotFoundError` at the first response), and an enum the generator typed rejects a value
the example carries. This feeds each operation's own example to its own `_parse_response`."""

from __future__ import annotations

import importlib
import pkgutil
import re
from pathlib import Path
from typing import Any

import httpx
import pytest
import yaml

import wefunder._generated.api as generated_api
from wefunder._generated import Client

ROOT = Path(__file__).resolve().parent.parent
SPEC = yaml.safe_load((ROOT / "spec/openapi.yaml").read_text())
METHODS = ("get", "post", "put", "patch", "delete")
OPERATIONS = [op for item in SPEC["paths"].values() for method, op in item.items() if method in METHODS]


def _generated_modules() -> dict[str, str]:
    """`list_offerings` -> `wefunder._generated.api.explore.list_offerings`, for every tag."""
    found: dict[str, str] = {}
    for tag in pkgutil.iter_modules(generated_api.__path__):
        package = importlib.import_module(f"{generated_api.__name__}.{tag.name}")
        for module in pkgutil.iter_modules(package.__path__):
            found[module.name] = f"{package.__name__}.{module.name}"
    return found


def _snake(operation_id: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", operation_id).lower()


MODULES = _generated_modules()
EXAMPLES = [
    pytest.param(op["operationId"], int(status), media["example"], id=f"{op['operationId']}-{status}")
    for op in OPERATIONS
    for status, response in op.get("responses", {}).items()
    if status.startswith("2")
    for media in [(response.get("content") or {}).get("application/json") or {}]
    if "example" in media
]


def test_every_operation_has_a_generated_module() -> None:
    assert [op["operationId"] for op in OPERATIONS if _snake(op["operationId"]) not in MODULES] == []


def test_the_spec_documents_response_examples() -> None:
    # Guards the parametrized test below against passing vacuously if the spec's shape changes.
    assert len(EXAMPLES) >= 70


@pytest.mark.parametrize(("operation_id", "status", "example"), EXAMPLES)
def test_generated_layer_parses_the_documented_example(operation_id: str, status: int, example: Any) -> None:
    module = importlib.import_module(MODULES[_snake(operation_id)])
    client = Client(base_url="https://api.wefunder.invalid", raise_on_unexpected_status=True)
    parsed = module._parse_response(client=client, response=httpx.Response(status, json=example))
    assert parsed is not None
