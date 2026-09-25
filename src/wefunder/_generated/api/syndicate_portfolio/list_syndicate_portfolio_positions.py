from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_syndicate_portfolio_positions_status import ListSyndicatePortfolioPositionsStatus
from ...models.portfolio_position_list_envelope import PortfolioPositionListEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    syndicate_id: str,
    *,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
    status: ListSyndicatePortfolioPositionsStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["per_page"] = per_page

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["company"] = company

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/syndicates/{syndicate_id}/portfolio/positions".format(
            syndicate_id=quote(str(syndicate_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PortfolioPositionListEnvelope | None:
    if response.status_code == 200:
        response_200 = PortfolioPositionListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | PortfolioPositionListEnvelope]:
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
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
    status: ListSyndicatePortfolioPositionsStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Response[Error | PortfolioPositionListEnvelope]:
    """List syndicate portfolio positions

     Returns the syndicate's portfolio one deal at a time, newest first. Each
    position is one fundraise ("offering"), aggregated across everyone holding
    its securities, with `investor_count` at both the position and security
    level.

    `securities` breaks each position down by security offering (for example,
    an early bird tier vs the regular terms) — most deals have a single entry.
    Fund and SPV deals identify the companies the vehicle invested in under
    `holdings`; some older vehicles have no recorded holdings and return an
    empty array.

    Args:
        syndicate_id (str):
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.
        status (ListSyndicatePortfolioPositionsStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PortfolioPositionListEnvelope]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        cursor=cursor,
        per_page=per_page,
        status=status,
        company=company,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
    status: ListSyndicatePortfolioPositionsStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Error | PortfolioPositionListEnvelope | None:
    """List syndicate portfolio positions

     Returns the syndicate's portfolio one deal at a time, newest first. Each
    position is one fundraise ("offering"), aggregated across everyone holding
    its securities, with `investor_count` at both the position and security
    level.

    `securities` breaks each position down by security offering (for example,
    an early bird tier vs the regular terms) — most deals have a single entry.
    Fund and SPV deals identify the companies the vehicle invested in under
    `holdings`; some older vehicles have no recorded holdings and return an
    empty array.

    Args:
        syndicate_id (str):
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.
        status (ListSyndicatePortfolioPositionsStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PortfolioPositionListEnvelope
    """

    return sync_detailed(
        syndicate_id=syndicate_id,
        client=client,
        cursor=cursor,
        per_page=per_page,
        status=status,
        company=company,
    ).parsed


async def asyncio_detailed(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
    status: ListSyndicatePortfolioPositionsStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Response[Error | PortfolioPositionListEnvelope]:
    """List syndicate portfolio positions

     Returns the syndicate's portfolio one deal at a time, newest first. Each
    position is one fundraise ("offering"), aggregated across everyone holding
    its securities, with `investor_count` at both the position and security
    level.

    `securities` breaks each position down by security offering (for example,
    an early bird tier vs the regular terms) — most deals have a single entry.
    Fund and SPV deals identify the companies the vehicle invested in under
    `holdings`; some older vehicles have no recorded holdings and return an
    empty array.

    Args:
        syndicate_id (str):
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.
        status (ListSyndicatePortfolioPositionsStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PortfolioPositionListEnvelope]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        cursor=cursor,
        per_page=per_page,
        status=status,
        company=company,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
    status: ListSyndicatePortfolioPositionsStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Error | PortfolioPositionListEnvelope | None:
    """List syndicate portfolio positions

     Returns the syndicate's portfolio one deal at a time, newest first. Each
    position is one fundraise ("offering"), aggregated across everyone holding
    its securities, with `investor_count` at both the position and security
    level.

    `securities` breaks each position down by security offering (for example,
    an early bird tier vs the regular terms) — most deals have a single entry.
    Fund and SPV deals identify the companies the vehicle invested in under
    `holdings`; some older vehicles have no recorded holdings and return an
    empty array.

    Args:
        syndicate_id (str):
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.
        status (ListSyndicatePortfolioPositionsStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PortfolioPositionListEnvelope
    """

    return (
        await asyncio_detailed(
            syndicate_id=syndicate_id,
            client=client,
            cursor=cursor,
            per_page=per_page,
            status=status,
            company=company,
        )
    ).parsed
