# examples/ — the source of truth for docs code samples

Mirrors `wefunder-node/examples/README.md` (the cross-language contract). Each file is a real,
type-checked module exporting `example(wf)`. A `# region <key>` … `# endregion` block marks the
snippet shown on docs.wefunder.com; everything outside it is harness. `<key>` is an
`operationId` (auto-binds to that operation's Python tab) or `guides/<name>`.

```
python scripts/build_examples_manifest.py   # → examples_manifest.json (lang "Python")
pyright examples                             # compile gate
pytest tests/test_examples.py                # coverage + freshness + shape gates
```

Every public `operationId` in `spec/openapi.yaml` must have an example here or be listed in
`coverage-allowlist.json` (curl-only). Files starting with `_` are hidden harness.
