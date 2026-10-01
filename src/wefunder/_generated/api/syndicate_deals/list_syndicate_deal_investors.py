from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deal_investor_list_envelope import DealInvestorListEnvelope
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    syndicate_id: str,
    fundraise_id: str,
    *,
    offset: int | Unset = 0,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/syndicates/{syndicate_id}/deals/{fundraise_id}/investors".format(
            syndicate_id=quote(str(syndicate_id), safe=""),
            fundraise_id=quote(str(fundraise_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DealInvestorListEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = DealInvestorListEnvelope.from_dict(response.json())

        return response_200

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
) -> Response[DealInvestorListEnvelope | Error]:
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
    offset: int | Unset = 0,
    per_page: int | Unset = UNSET,
) -> Response[DealInvestorListEnvelope | Error]:
    """List deal investors

     Returns syndicate members who invested in this deal. Results are scoped to
    syndicate member user IDs only and sorted by amount descending.

    The `user_email` field is **moderator-only** — it returns null for non-moderator
    callers (i.e., users who are not a manager/operator of the syndicate).

    `amount` is whole dollars as a string (e.g. `"5000"` is $5,000).

    Offset-paginated: pass `offset` and `per_page`; `meta` carries `total_count`,
    `offset`, `per_page`, and `has_more`. Without `per_page` the full list is returned.

    Args:
        syndicate_id (str):
        fundraise_id (str):
        offset (int | Unset):  Default: 0.
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DealInvestorListEnvelope | Error]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        fundraise_id=fundraise_id,
        offset=offset,
        per_page=per_page,
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
    offset: int | Unset = 0,
    per_page: int | Unset = UNSET,
) -> DealInvestorListEnvelope | Error | None:
    """List deal investors

     Returns syndicate members who invested in this deal. Results are scoped to
    syndicate member user IDs only and sorted by amount descending.

    The `user_email` field is **moderator-only** — it returns null for non-moderator
    callers (i.e., users who are not a manager/operator of the syndicate).

    `amount` is whole dollars as a string (e.g. `"5000"` is $5,000).

    Offset-paginated: pass `offset` and `per_page`; `meta` carries `total_count`,
    `offset`, `per_page`, and `has_more`. Without `per_page` the full list is returned.

    Args:
        syndicate_id (str):
        fundraise_id (str):
        offset (int | Unset):  Default: 0.
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DealInvestorListEnvelope | Error
    """

    return sync_detailed(
        syndicate_id=syndicate_id,
        fundraise_id=fundraise_id,
        client=client,
        offset=offset,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    syndicate_id: str,
    fundraise_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    per_page: int | Unset = UNSET,
) -> Response[DealInvestorListEnvelope | Error]:
    """List deal investors

     Returns syndicate members who invested in this deal. Results are scoped to
    syndicate member user IDs only and sorted by amount descending.

    The `user_email` field is **moderator-only** — it returns null for non-moderator
    callers (i.e., users who are not a manager/operator of the syndicate).

    `amount` is whole dollars as a string (e.g. `"5000"` is $5,000).

    Offset-paginated: pass `offset` and `per_page`; `meta` carries `total_count`,
    `offset`, `per_page`, and `has_more`. Without `per_page` the full list is returned.

    Args:
        syndicate_id (str):
        fundraise_id (str):
        offset (int | Unset):  Default: 0.
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DealInvestorListEnvelope | Error]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        fundraise_id=fundraise_id,
        offset=offset,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    syndicate_id: str,
    fundraise_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    per_page: int | Unset = UNSET,
) -> DealInvestorListEnvelope | Error | None:
    """List deal investors

     Returns syndicate members who invested in this deal. Results are scoped to
    syndicate member user IDs only and sorted by amount descending.

    The `user_email` field is **moderator-only** — it returns null for non-moderator
    callers (i.e., users who are not a manager/operator of the syndicate).

    `amount` is whole dollars as a string (e.g. `"5000"` is $5,000).

    Offset-paginated: pass `offset` and `per_page`; `meta` carries `total_count`,
    `offset`, `per_page`, and `has_more`. Without `per_page` the full list is returned.

    Args:
        syndicate_id (str):
        fundraise_id (str):
        offset (int | Unset):  Default: 0.
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DealInvestorListEnvelope | Error
    """

    return (
        await asyncio_detailed(
            syndicate_id=syndicate_id,
            fundraise_id=fundraise_id,
            client=client,
            offset=offset,
            per_page=per_page,
        )
    ).parsed
