# wefunder

Official Python SDK for the [Wefunder API](https://docs.wefunder.com). **Beta** — the API is
pre-launch and `0.x` releases may include breaking changes.

- Sync (`Wefunder`) and asyncio (`AsyncWefunder`) clients on [httpx](https://www.python-httpx.org)
- OAuth 2.0: `client_credentials` for server-to-server, `authorization_code` + PKCE for user consent,
  refresh-token rotation handled for you
- Automatic retries (rate limits, transient errors) and one-shot token recovery on 401
- Lazy auto-pagination over opaque cursors
- Typed errors with the `request_id` support asks for
- Webhook signature verification, envelope parsing, and dispatch
- A generated, typed layer for every public operation, plus a `request()` escape hatch

Requires Python 3.11+.

## Install

```bash
pip install wefunder
```

The SDK follows semantic versioning from `1.0.0`: breaking changes only in a new major version, announced in the changelog.

## Authentication

Wefunder supports two OAuth grants:

- Use `client_credentials` for server-to-server access to public data.
- Use `authorization_code` with PKCE when acting on behalf of a user.

### Server-to-server

```python
import os
from wefunder import Wefunder

wf = Wefunder.from_client_credentials(
    client_id=os.environ["WEFUNDER_CLIENT_ID"],
    client_secret=os.environ["WEFUNDER_CLIENT_SECRET"],
    scopes=["read:public"],
)
page = wf.offerings.list()
```

Client-credentials tokens represent the application, not a user. They cannot call user-scoped
endpoints such as `wf.users.me()` or `wf.portfolio.get()`. The SDK mints a new token automatically
when a client-credentials token expires.

### User authorization with PKCE

Generate the authorization URL on your server. Store `state` and the PKCE verifier in the user's
session before redirecting them:

```python
import secrets
from wefunder import create_authorization_url, generate_pkce

pkce = generate_pkce()
state = secrets.token_urlsafe(32)
save_oauth_attempt(state=state, code_verifier=pkce.code_verifier)

url = create_authorization_url(
    client_id=client_id,
    redirect_uri=redirect_uri,
    scopes=["read:investments"],
    state=state,
    pkce=pkce,
)
```

The consent host is chosen from the `client_id`: `pk_test_` ids go to the sandbox, everything else to
wefunder.com. On the callback, validate `state` and exchange the code:

```python
from wefunder import Wefunder, exchange_code

attempt = consume_oauth_attempt(state)
tokens = exchange_code(
    client_id=client_id,
    client_secret=client_secret,  # omit for public clients
    code=code,
    redirect_uri=redirect_uri,
    code_verifier=attempt.code_verifier,
)

wf = Wefunder(tokens=tokens, client_id=client_id, client_secret=client_secret, store=TokenStore())
```

### Refresh tokens

Refresh tokens rotate. When the SDK refreshes an access token it calls `store.save(tokens)` with the
new set **before** retrying the request. Persist the entire token set each time, and load it yourself
when constructing a client after a restart:

```python
class TokenStore:
    def save(self, tokens):  # may be sync or async
        db.save_tokens(tokens.access_token, tokens.refresh_token, tokens.expires_at)

wf = Wefunder(tokens=load_tokens(), client_id=client_id, client_secret=client_secret, store=TokenStore())
```

Concurrent requests that hit a 401 at the same time share one refresh. If several application
instances can use the same OAuth connection, serialize refreshes for that connection yourself.

## Calling the API

```python
offerings = wf.offerings.list(sort="newest")
investments = wf.investments.list(company_id="co_example")
portfolio = wf.portfolio.get()
```

Namespaces: `users`, `offerings`, `investments`, `portfolio`, `campaigns`, `syndicates`, `intents`,
`attribution`, `installations`, and `webhook_endpoints`. `wf.installations` lets your app act as a
company or syndicate: `eligible_targets()`, `create()`, `mint_token()`, `list()`, `get()`, `revoke()`,
and `install_or_mint_token()`, which handles the API's 409 `already_installed` answer by minting a
token for the existing install with the same scopes. Enum-typed query parameters accept plain strings, and
`datetime` parameters accept ISO-8601 strings.

`wf.investments` is the Investment Delta API. `list()` without a cursor bootstraps; pass `updated_since`
or the `meta.next_cursor` you saved from your last page to receive only records that changed since then.
`next_cursor` is always present, even on the final page, so persist it after every sync.

The API base URL is `https://api.wefunder.com`. Paths are version-free; the SDK sends the API version in
the `Wefunder-Version` request header.

## Pagination

```python
# One page, and its cursor.
page = wf.offerings.list(sort="newest")
print(page.data, page.meta.next_cursor)

# Every item, one page fetched at a time.
for offering in wf.offerings.all(sort="most_raised"):
    print(offering.id)

# Everything in one list.
investments = wf.investments.collect()
```

Cursors are opaque. Pass the value returned by the API without modifying it.

## Errors and retries

API failures raise `WefunderError`:

```python
from wefunder import WefunderError

try:
    wf.syndicates.get("syn_aB3xQ9k2vF8mNp1zT5wY7Qc4")
except WefunderError as err:
    print(err.status, err.type, err.message, err.request_id, err.remediation)
```

The SDK retries idempotent `GET` requests after transient network errors, `5xx` responses, and rate
limits (honouring `X-RateLimit-Reset`). Write requests are not retried automatically, except once after
a `401` has been recovered.

## Async

```python
from wefunder import AsyncWefunder

async with await AsyncWefunder.from_client_credentials(client_id=..., client_secret=...) as wf:
    async for offering in wf.offerings.all():
        print(offering.id)
```

`AsyncWefunder` has the same plumbing (auth, recovery, retries, typed errors, `raw`, `request()`) and
namespaces for `users`, `offerings`, `investments`, `portfolio`, `installations`, and `webhook_endpoints`. Reach every
other operation with `await wf.call(op, ...)` (see below).

## Webhooks

Webhooks deliver platform events (`investment.executed`, `offering.opened`, `investment.changed`, …) to
an HTTPS endpoint you register. Every delivery is signed; the SDK verifies the signature, parses the
envelope, and hands you an event.

### 1. Register an endpoint

Endpoints belong to your application and are managed through the live API (scope `write:webhooks`).
The signing secret is returned only on create and rotate, so store it immediately.

```python
endpoint = wf.webhook_endpoints.create(
    url="https://yourapp.com/webhooks/wefunder",  # public HTTPS; localhost and private IPs are rejected
    events=["offering.opened", "investment.executed"],
    mode="live",  # "test" endpoints receive sandbox events
)
save_secret(endpoint.attributes.secret)
```

`wf.webhook_endpoints` also provides `list`, `get`, `update`, `remove`, `rotate_secret`, `reenable`,
and `test`.

### 2. Verify and handle deliveries

Pass the **raw** request body, the headers, and your secret to `construct_event`. It raises
`WebhookSignatureError` (with a `reason`) when a delivery is not authentic.

```python
from wefunder import WebhookSignatureError, construct_event, dispatch_webhook

@app.post("/webhooks/wefunder")
def receive(request):
    try:
        event = construct_event(request.get_data(), request.headers, WEBHOOK_SECRET)
    except WebhookSignatureError as err:
        return err.reason, 400

    dispatch_webhook(event, {
        "investment.executed": lambda e: record_funding(e.data["id"], e.data["amounts"]["committed"]),
        "offering.opened": lambda e: announce(e.data["company"]["name"]),
        "default": lambda e: log.info("unhandled %s", e.event),
    })
    return "", 200
```

Deliveries are at-least-once and unordered. Deduplicate on `event.id`, and where a payload carries
`occurred_at`, keep the state from the latest one you have seen. `async_dispatch_webhook` accepts
coroutine handlers.

### 3. Test your handler

`wf.webhook_endpoints.test(endpoint.id)` sends a real, signed example event and reports the outcome.
To unit-test your handler without the API, sign a fixture yourself:

```python
from wefunder import sign_webhook

header = sign_webhook(body, secret)
# POST `body` to your handler with `Wefunder-Signature: <header>`
```

### Signature scheme

Each delivery carries `Wefunder-Signature: t=<unix seconds>,v1=<hex>` where `v1` is
`HMAC-SHA256(secret, "<t>.<raw body>")`. Requests whose `t` is more than five minutes from now are
rejected (`tolerance_seconds` adjusts this). During a secret rotation the header carries one `v1` per
active secret and `construct_event` accepts either. `verify_webhook` and `check_webhook_signature`
expose the check without parsing, and `construct_event` still accepts the retired attribution headers
(`X-Wefunder-Signature` / `X-Wefunder-Timestamp`).

## Generated operations

Typed namespaces cover the common resources. Every operation in the public OpenAPI specification is
generated under `wefunder._generated.api.<tag>`; call one through the client to get the same auth,
retries, and error handling:

```python
from wefunder._generated.api.syndicate_members import list_syndicate_members

members = wf.call(list_syndicate_members, syndicate_id="syn_aB3xQ9k2vF8mNp1zT5wY7Qc4")
```

For a path the generated layer does not know yet, `wf.request(method, path, query=..., body=...,
headers=...)` sends a fully-wrapped request and returns the decoded JSON.

## Development

```bash
python -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
ruff check src tests scripts examples && ruff format --check src tests scripts examples
pyright
pytest
```

`pytest tests/e2e -o addopts=""` runs against the sandbox when `WEFUNDER_CLIENT_ID` and
`WEFUNDER_CLIENT_SECRET` are set.

Generated files in `src/wefunder/_generated/` come from `spec/openapi.yaml` and are never edited by
hand.

### Conformance vectors

`conformance/*.json` is the cross-language behavioural contract shared with `wefunder-node` (and the
Ruby SDK): signatures, token rotation, pagination, retries, errors. `tests/test_conformance.py` runs
every case against both clients. The files are vendored from `Wefunder/wefunder-node` at the ref in
`conformance/PIN`; refresh with `python scripts/sync_conformance.py [ref]`. Never edit a vector to make
the shell pass.

### Examples

`examples/` is the source of truth for the Python snippets on docs.wefunder.com; see
`examples/README.md`. After adding one, run `python scripts/build_examples_manifest.py` and remove its
`operationId` from `examples/coverage-allowlist.json`.

### Updating the API specification

```bash
python scripts/sync_spec.py /path/to/wefunder   # public-tier spec → spec/openapi.yaml
python scripts/generate.py                      # → src/wefunder/_generated
pyright && pytest
```

Commit the specification and generated client together.

### Releasing

Set the version in `src/wefunder/_version.py` (PEP 440, e.g. `0.1.0b1`), rebuild
`examples_manifest.json`, commit, then:

```bash
git tag v0.1.0b1
git push --follow-tags
```

The release workflow verifies the tag, runs the checks, builds, and publishes to PyPI via trusted
publishing.
