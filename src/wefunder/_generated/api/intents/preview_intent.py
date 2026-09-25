from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.intent_preview_envelope import IntentPreviewEnvelope
from ...models.preview_intent_body import PreviewIntentBody
from ...types import Response


def _get_kwargs(
    *,
    body: PreviewIntentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/intents/preview",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | IntentPreviewEnvelope | None:
    if response.status_code == 200:
        response_200 = IntentPreviewEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | IntentPreviewEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PreviewIntentBody,
) -> Response[Error | IntentPreviewEnvelope]:
    """Preview an intent without proposing it

     Runs every check `POST /intents` runs — the action's feature flag, resource type and id,
    token binding, who may propose, and the handler's own validation — and returns what the
    reviewer would read, without minting anything. The draft step for agents: admitted by any
    proposing scope **or** `read:explore`, and the action's own scope is not required, so a user
    can shape the text before granting the write permission. Same request body as `POST /intents`
    (without `idempotency_key`). Errors are the same as `POST /intents` would give.

    Args:
        body (PreviewIntentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IntentPreviewEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PreviewIntentBody,
) -> Error | IntentPreviewEnvelope | None:
    """Preview an intent without proposing it

     Runs every check `POST /intents` runs — the action's feature flag, resource type and id,
    token binding, who may propose, and the handler's own validation — and returns what the
    reviewer would read, without minting anything. The draft step for agents: admitted by any
    proposing scope **or** `read:explore`, and the action's own scope is not required, so a user
    can shape the text before granting the write permission. Same request body as `POST /intents`
    (without `idempotency_key`). Errors are the same as `POST /intents` would give.

    Args:
        body (PreviewIntentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IntentPreviewEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PreviewIntentBody,
) -> Response[Error | IntentPreviewEnvelope]:
    """Preview an intent without proposing it

     Runs every check `POST /intents` runs — the action's feature flag, resource type and id,
    token binding, who may propose, and the handler's own validation — and returns what the
    reviewer would read, without minting anything. The draft step for agents: admitted by any
    proposing scope **or** `read:explore`, and the action's own scope is not required, so a user
    can shape the text before granting the write permission. Same request body as `POST /intents`
    (without `idempotency_key`). Errors are the same as `POST /intents` would give.

    Args:
        body (PreviewIntentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IntentPreviewEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PreviewIntentBody,
) -> Error | IntentPreviewEnvelope | None:
    """Preview an intent without proposing it

     Runs every check `POST /intents` runs — the action's feature flag, resource type and id,
    token binding, who may propose, and the handler's own validation — and returns what the
    reviewer would read, without minting anything. The draft step for agents: admitted by any
    proposing scope **or** `read:explore`, and the action's own scope is not required, so a user
    can shape the text before granting the write permission. Same request body as `POST /intents`
    (without `idempotency_key`). Errors are the same as `POST /intents` would give.

    Args:
        body (PreviewIntentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IntentPreviewEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
