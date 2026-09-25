import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.investment_list_envelope import InvestmentListEnvelope
from ...models.list_investments_status import ListInvestmentsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    company_id: str | Unset = UNSET,
    offering_id: str | Unset = UNSET,
    investor_id: str | Unset = UNSET,
    status: ListInvestmentsStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["company_id"] = company_id

    params["offering_id"] = offering_id

    params["investor_id"] = investor_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_updated_since: str | Unset = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updated_since"] = json_updated_since

    params["cursor"] = cursor

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/investments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | InvestmentListEnvelope | None:
    if response.status_code == 200:
        response_200 = InvestmentListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 410:
        response_410 = cast(Any, None)
        return response_410

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error | InvestmentListEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    company_id: str | Unset = UNSET,
    offering_id: str | Unset = UNSET,
    investor_id: str | Unset = UNSET,
    status: ListInvestmentsStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Any | Error | InvestmentListEnvelope]:
    """List or sync investments

     The investment records the token may see, served from **published** state
    (docs: *Investments: list, sync, retrieve*). The audience is the union of the companies
    the token's user edits (their founder-visible records) and the user's own investments
    (every applied record of theirs, whatever its status). Filters narrow within that
    audience; they never widen it.

    Three ways to call it:
    - **List** (no `cursor`, no `updated_since`): the current records, tombstones excluded,
      ordered by investment. Page with `meta.next_cursor` while `meta.has_more`; the final
      page's cursor is a sync cursor positioned at the moment the listing started.
    - **Sync by cursor**: only the records whose published state changed since the cursor,
      one record per investment, tombstones (`visible: false`, only `id`) included. Apply in
      `cursor` order; always store `meta.next_cursor`.
    - **Sync by time**: `updated_since=<ISO 8601>` is sugar for a cursor at the ledger position
      just before that time (with a 60 s safety margin). The response is a normal sync page,
      so continue with its `meta.next_cursor`.

    Records are eventually consistent (about ten minutes on the common paths); each carries
    `observed_at`. `GET /investments/{id}` returns the same shape derived now. Investor
    identity fields on other investors' records require `read:investors:pii`; a user always
    sees their own. Money is integer minor units plus `amounts.currency`.

    **410 Gone** means the cursor or `updated_since` predates the 90-day retention window:
    list again and replace your dataset. `status` cannot be combined with sync (a record
    leaving the status would never be delivered).

    Args:
        company_id (str | Unset):
        offering_id (str | Unset):
        investor_id (str | Unset):
        status (ListInvestmentsStatus | Unset):
        updated_since (datetime.datetime | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | InvestmentListEnvelope]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        offering_id=offering_id,
        investor_id=investor_id,
        status=status,
        updated_since=updated_since,
        cursor=cursor,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    company_id: str | Unset = UNSET,
    offering_id: str | Unset = UNSET,
    investor_id: str | Unset = UNSET,
    status: ListInvestmentsStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Any | Error | InvestmentListEnvelope | None:
    """List or sync investments

     The investment records the token may see, served from **published** state
    (docs: *Investments: list, sync, retrieve*). The audience is the union of the companies
    the token's user edits (their founder-visible records) and the user's own investments
    (every applied record of theirs, whatever its status). Filters narrow within that
    audience; they never widen it.

    Three ways to call it:
    - **List** (no `cursor`, no `updated_since`): the current records, tombstones excluded,
      ordered by investment. Page with `meta.next_cursor` while `meta.has_more`; the final
      page's cursor is a sync cursor positioned at the moment the listing started.
    - **Sync by cursor**: only the records whose published state changed since the cursor,
      one record per investment, tombstones (`visible: false`, only `id`) included. Apply in
      `cursor` order; always store `meta.next_cursor`.
    - **Sync by time**: `updated_since=<ISO 8601>` is sugar for a cursor at the ledger position
      just before that time (with a 60 s safety margin). The response is a normal sync page,
      so continue with its `meta.next_cursor`.

    Records are eventually consistent (about ten minutes on the common paths); each carries
    `observed_at`. `GET /investments/{id}` returns the same shape derived now. Investor
    identity fields on other investors' records require `read:investors:pii`; a user always
    sees their own. Money is integer minor units plus `amounts.currency`.

    **410 Gone** means the cursor or `updated_since` predates the 90-day retention window:
    list again and replace your dataset. `status` cannot be combined with sync (a record
    leaving the status would never be delivered).

    Args:
        company_id (str | Unset):
        offering_id (str | Unset):
        investor_id (str | Unset):
        status (ListInvestmentsStatus | Unset):
        updated_since (datetime.datetime | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | InvestmentListEnvelope
    """

    return sync_detailed(
        client=client,
        company_id=company_id,
        offering_id=offering_id,
        investor_id=investor_id,
        status=status,
        updated_since=updated_since,
        cursor=cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    company_id: str | Unset = UNSET,
    offering_id: str | Unset = UNSET,
    investor_id: str | Unset = UNSET,
    status: ListInvestmentsStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Any | Error | InvestmentListEnvelope]:
    """List or sync investments

     The investment records the token may see, served from **published** state
    (docs: *Investments: list, sync, retrieve*). The audience is the union of the companies
    the token's user edits (their founder-visible records) and the user's own investments
    (every applied record of theirs, whatever its status). Filters narrow within that
    audience; they never widen it.

    Three ways to call it:
    - **List** (no `cursor`, no `updated_since`): the current records, tombstones excluded,
      ordered by investment. Page with `meta.next_cursor` while `meta.has_more`; the final
      page's cursor is a sync cursor positioned at the moment the listing started.
    - **Sync by cursor**: only the records whose published state changed since the cursor,
      one record per investment, tombstones (`visible: false`, only `id`) included. Apply in
      `cursor` order; always store `meta.next_cursor`.
    - **Sync by time**: `updated_since=<ISO 8601>` is sugar for a cursor at the ledger position
      just before that time (with a 60 s safety margin). The response is a normal sync page,
      so continue with its `meta.next_cursor`.

    Records are eventually consistent (about ten minutes on the common paths); each carries
    `observed_at`. `GET /investments/{id}` returns the same shape derived now. Investor
    identity fields on other investors' records require `read:investors:pii`; a user always
    sees their own. Money is integer minor units plus `amounts.currency`.

    **410 Gone** means the cursor or `updated_since` predates the 90-day retention window:
    list again and replace your dataset. `status` cannot be combined with sync (a record
    leaving the status would never be delivered).

    Args:
        company_id (str | Unset):
        offering_id (str | Unset):
        investor_id (str | Unset):
        status (ListInvestmentsStatus | Unset):
        updated_since (datetime.datetime | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | InvestmentListEnvelope]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        offering_id=offering_id,
        investor_id=investor_id,
        status=status,
        updated_since=updated_since,
        cursor=cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    company_id: str | Unset = UNSET,
    offering_id: str | Unset = UNSET,
    investor_id: str | Unset = UNSET,
    status: ListInvestmentsStatus | Unset = UNSET,
    updated_since: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Any | Error | InvestmentListEnvelope | None:
    """List or sync investments

     The investment records the token may see, served from **published** state
    (docs: *Investments: list, sync, retrieve*). The audience is the union of the companies
    the token's user edits (their founder-visible records) and the user's own investments
    (every applied record of theirs, whatever its status). Filters narrow within that
    audience; they never widen it.

    Three ways to call it:
    - **List** (no `cursor`, no `updated_since`): the current records, tombstones excluded,
      ordered by investment. Page with `meta.next_cursor` while `meta.has_more`; the final
      page's cursor is a sync cursor positioned at the moment the listing started.
    - **Sync by cursor**: only the records whose published state changed since the cursor,
      one record per investment, tombstones (`visible: false`, only `id`) included. Apply in
      `cursor` order; always store `meta.next_cursor`.
    - **Sync by time**: `updated_since=<ISO 8601>` is sugar for a cursor at the ledger position
      just before that time (with a 60 s safety margin). The response is a normal sync page,
      so continue with its `meta.next_cursor`.

    Records are eventually consistent (about ten minutes on the common paths); each carries
    `observed_at`. `GET /investments/{id}` returns the same shape derived now. Investor
    identity fields on other investors' records require `read:investors:pii`; a user always
    sees their own. Money is integer minor units plus `amounts.currency`.

    **410 Gone** means the cursor or `updated_since` predates the 90-day retention window:
    list again and replace your dataset. `status` cannot be combined with sync (a record
    leaving the status would never be delivered).

    Args:
        company_id (str | Unset):
        offering_id (str | Unset):
        investor_id (str | Unset):
        status (ListInvestmentsStatus | Unset):
        updated_since (datetime.datetime | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | InvestmentListEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            company_id=company_id,
            offering_id=offering_id,
            investor_id=investor_id,
            status=status,
            updated_since=updated_since,
            cursor=cursor,
            per_page=per_page,
        )
    ).parsed
