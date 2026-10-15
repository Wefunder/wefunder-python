from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.referral_code_stats_envelope import ReferralCodeStatsEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    cursor: int | Unset = UNSET,
    company_id: str | Unset = UNSET,
    investments_cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["company_id"] = company_id

    params["investments_cursor"] = investments_cursor

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/referral_codes/{id}/stats".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ReferralCodeStatsEnvelope | None:
    if response.status_code == 200:
        response_200 = ReferralCodeStatsEnvelope.from_dict(response.json())

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
) -> Response[Error | ReferralCodeStatsEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    company_id: str | Unset = UNSET,
    investments_cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Error | ReferralCodeStatsEnvelope]:
    """Referral code stats

     What your code produced, per company. Your access to each company decides what you see:

    - **Counts** (any app): for each company in the code's scope, one cell per ISO week (Monday
      to Sunday, UTC) with the unique investors referred that week as a range, `{min, max}`.
      Ranges are never exact, currently of width 3 and starting at zero, so `{0, 2}` also means
      none. Each week is published once, early on the following Monday, and never revised; the
      current week has no cell. There are no totals across weeks or companies, and no amounts.
    - **Rows** (your app is installed on the company with `read:attribution:anonymized`, or at
      founder tier with `read:attribution:full`): that company's referred investments instead of
      ranges, anonymized or in full.

    A targeted code's scope is its target; an untargeted code's scope is every company its
    visitors landed on. `visits` and `unique_visitors` are a daily snapshot up to the end of
    `visits_as_of` (UTC). Paginated over companies; each company's weekly series is complete.

    Args:
        id (str):
        cursor (int | Unset):
        company_id (str | Unset):
        investments_cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReferralCodeStatsEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
        company_id=company_id,
        investments_cursor=investments_cursor,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    company_id: str | Unset = UNSET,
    investments_cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Error | ReferralCodeStatsEnvelope | None:
    """Referral code stats

     What your code produced, per company. Your access to each company decides what you see:

    - **Counts** (any app): for each company in the code's scope, one cell per ISO week (Monday
      to Sunday, UTC) with the unique investors referred that week as a range, `{min, max}`.
      Ranges are never exact, currently of width 3 and starting at zero, so `{0, 2}` also means
      none. Each week is published once, early on the following Monday, and never revised; the
      current week has no cell. There are no totals across weeks or companies, and no amounts.
    - **Rows** (your app is installed on the company with `read:attribution:anonymized`, or at
      founder tier with `read:attribution:full`): that company's referred investments instead of
      ranges, anonymized or in full.

    A targeted code's scope is its target; an untargeted code's scope is every company its
    visitors landed on. `visits` and `unique_visitors` are a daily snapshot up to the end of
    `visits_as_of` (UTC). Paginated over companies; each company's weekly series is complete.

    Args:
        id (str):
        cursor (int | Unset):
        company_id (str | Unset):
        investments_cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReferralCodeStatsEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        cursor=cursor,
        company_id=company_id,
        investments_cursor=investments_cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    company_id: str | Unset = UNSET,
    investments_cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Error | ReferralCodeStatsEnvelope]:
    """Referral code stats

     What your code produced, per company. Your access to each company decides what you see:

    - **Counts** (any app): for each company in the code's scope, one cell per ISO week (Monday
      to Sunday, UTC) with the unique investors referred that week as a range, `{min, max}`.
      Ranges are never exact, currently of width 3 and starting at zero, so `{0, 2}` also means
      none. Each week is published once, early on the following Monday, and never revised; the
      current week has no cell. There are no totals across weeks or companies, and no amounts.
    - **Rows** (your app is installed on the company with `read:attribution:anonymized`, or at
      founder tier with `read:attribution:full`): that company's referred investments instead of
      ranges, anonymized or in full.

    A targeted code's scope is its target; an untargeted code's scope is every company its
    visitors landed on. `visits` and `unique_visitors` are a daily snapshot up to the end of
    `visits_as_of` (UTC). Paginated over companies; each company's weekly series is complete.

    Args:
        id (str):
        cursor (int | Unset):
        company_id (str | Unset):
        investments_cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReferralCodeStatsEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
        company_id=company_id,
        investments_cursor=investments_cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    company_id: str | Unset = UNSET,
    investments_cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Error | ReferralCodeStatsEnvelope | None:
    """Referral code stats

     What your code produced, per company. Your access to each company decides what you see:

    - **Counts** (any app): for each company in the code's scope, one cell per ISO week (Monday
      to Sunday, UTC) with the unique investors referred that week as a range, `{min, max}`.
      Ranges are never exact, currently of width 3 and starting at zero, so `{0, 2}` also means
      none. Each week is published once, early on the following Monday, and never revised; the
      current week has no cell. There are no totals across weeks or companies, and no amounts.
    - **Rows** (your app is installed on the company with `read:attribution:anonymized`, or at
      founder tier with `read:attribution:full`): that company's referred investments instead of
      ranges, anonymized or in full.

    A targeted code's scope is its target; an untargeted code's scope is every company its
    visitors landed on. `visits` and `unique_visitors` are a daily snapshot up to the end of
    `visits_as_of` (UTC). Paginated over companies; each company's weekly series is complete.

    Args:
        id (str):
        cursor (int | Unset):
        company_id (str | Unset):
        investments_cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReferralCodeStatsEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            cursor=cursor,
            company_id=company_id,
            investments_cursor=investments_cursor,
            per_page=per_page,
        )
    ).parsed
