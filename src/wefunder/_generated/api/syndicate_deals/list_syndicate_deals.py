from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.syndicate_deal_list_envelope import SyndicateDealListEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    syndicate_id: str,
    *,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/syndicates/{syndicate_id}/deals".format(
            syndicate_id=quote(str(syndicate_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SyndicateDealListEnvelope | None:
    if response.status_code == 200:
        response_200 = SyndicateDealListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | SyndicateDealListEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Error | SyndicateDealListEnvelope]:
    """List deals

     Returns the syndicate's **live** deals (open, oversubscribed, or closing) with status,
    terms, and metrics. Closed and upcoming rounds are not listed; `statistics.total_deals`
    counts all linked rounds.

    Args:
        syndicate_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateDealListEnvelope]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        cursor=cursor,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Error | SyndicateDealListEnvelope | None:
    """List deals

     Returns the syndicate's **live** deals (open, oversubscribed, or closing) with status,
    terms, and metrics. Closed and upcoming rounds are not listed; `statistics.total_deals`
    counts all linked rounds.

    Args:
        syndicate_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateDealListEnvelope
    """

    return sync_detailed(
        syndicate_id=syndicate_id,
        client=client,
        cursor=cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Error | SyndicateDealListEnvelope]:
    """List deals

     Returns the syndicate's **live** deals (open, oversubscribed, or closing) with status,
    terms, and metrics. Closed and upcoming rounds are not listed; `statistics.total_deals`
    counts all linked rounds.

    Args:
        syndicate_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateDealListEnvelope]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        cursor=cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Error | SyndicateDealListEnvelope | None:
    """List deals

     Returns the syndicate's **live** deals (open, oversubscribed, or closing) with status,
    terms, and metrics. Closed and upcoming rounds are not listed; `statistics.total_deals`
    counts all linked rounds.

    Args:
        syndicate_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateDealListEnvelope
    """

    return (
        await asyncio_detailed(
            syndicate_id=syndicate_id,
            client=client,
            cursor=cursor,
            per_page=per_page,
        )
    ).parsed
