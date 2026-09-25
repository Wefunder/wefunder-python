from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.syndicate_deal_close_intent_envelope import SyndicateDealCloseIntentEnvelope
from ...types import Response


def _get_kwargs(
    syndicate_id: str,
    fundraise_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/syndicates/{syndicate_id}/deals/{fundraise_id}/close".format(
            syndicate_id=quote(str(syndicate_id), safe=""),
            fundraise_id=quote(str(fundraise_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SyndicateDealCloseIntentEnvelope | None:
    if response.status_code == 200:
        response_200 = SyndicateDealCloseIntentEnvelope.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | SyndicateDealCloseIntentEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    syndicate_id: str,
    fundraise_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | SyndicateDealCloseIntentEnvelope]:
    """Close deal

     Closing a deal is irreversible and requires human approval through the Intent system.
    This endpoint server-mints a pending `syndicates.close_deal` intent and returns the deal
    under `data` plus the intent's `review_url` under `meta.close_deal_intent`. The deal is
    not transitioned until a permitted human approves the intent in the Wefunder UI.
    Idempotent: a repeated call returns the same pending intent rather than minting a duplicate.

    Args:
        syndicate_id (str):
        fundraise_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateDealCloseIntentEnvelope]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        fundraise_id=fundraise_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    syndicate_id: str,
    fundraise_id: str,
    *,
    client: AuthenticatedClient,
) -> Error | SyndicateDealCloseIntentEnvelope | None:
    """Close deal

     Closing a deal is irreversible and requires human approval through the Intent system.
    This endpoint server-mints a pending `syndicates.close_deal` intent and returns the deal
    under `data` plus the intent's `review_url` under `meta.close_deal_intent`. The deal is
    not transitioned until a permitted human approves the intent in the Wefunder UI.
    Idempotent: a repeated call returns the same pending intent rather than minting a duplicate.

    Args:
        syndicate_id (str):
        fundraise_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateDealCloseIntentEnvelope
    """

    return sync_detailed(
        syndicate_id=syndicate_id,
        fundraise_id=fundraise_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    syndicate_id: str,
    fundraise_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | SyndicateDealCloseIntentEnvelope]:
    """Close deal

     Closing a deal is irreversible and requires human approval through the Intent system.
    This endpoint server-mints a pending `syndicates.close_deal` intent and returns the deal
    under `data` plus the intent's `review_url` under `meta.close_deal_intent`. The deal is
    not transitioned until a permitted human approves the intent in the Wefunder UI.
    Idempotent: a repeated call returns the same pending intent rather than minting a duplicate.

    Args:
        syndicate_id (str):
        fundraise_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateDealCloseIntentEnvelope]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        fundraise_id=fundraise_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    syndicate_id: str,
    fundraise_id: str,
    *,
    client: AuthenticatedClient,
) -> Error | SyndicateDealCloseIntentEnvelope | None:
    """Close deal

     Closing a deal is irreversible and requires human approval through the Intent system.
    This endpoint server-mints a pending `syndicates.close_deal` intent and returns the deal
    under `data` plus the intent's `review_url` under `meta.close_deal_intent`. The deal is
    not transitioned until a permitted human approves the intent in the Wefunder UI.
    Idempotent: a repeated call returns the same pending intent rather than minting a duplicate.

    Args:
        syndicate_id (str):
        fundraise_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateDealCloseIntentEnvelope
    """

    return (
        await asyncio_detailed(
            syndicate_id=syndicate_id,
            fundraise_id=fundraise_id,
            client=client,
        )
    ).parsed
