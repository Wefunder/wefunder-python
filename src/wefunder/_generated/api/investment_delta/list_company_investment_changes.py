from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.investment_change_list_envelope import InvestmentChangeListEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
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
        "url": "/companies/{company_id}/investments/changes".format(
            company_id=quote(str(company_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | InvestmentChangeListEnvelope | None:
    if response.status_code == 200:
        response_200 = InvestmentChangeListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

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
) -> Response[Any | Error | InvestmentChangeListEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Any | Error | InvestmentChangeListEnvelope]:
    """Bootstrap or page investment changes for a company

     The Investment Delta API: keep a copy of a company's investment records in sync by
    polling. Call without `cursor` to **bootstrap** (list every current record for the
    company); every response carries `meta.next_cursor`; call again with that cursor to
    receive only the records whose published state changed since. Records are the same
    shape in both modes.

    - Records are **published state**, not live rows: Wefunder publishes a record when the
      investment's founder-visible state changes, and serves exactly what was published.
    - `visible: false` records are **tombstones**: the investment is no longer visible to the
      company (canceled, converted to another round, hidden, or deleted). Delete your copy.
    - Apply records in `cursor` order. `observed_at` is when the payload was observed, not a
      version; a record you read late carries the *current* published state.
    - **410 Gone** means your cursor predates the 90-day retention window. Bootstrap again and
      **replace** your dataset for the company from the result (records absent from the
      bootstrap are deleted).
    - Investor identity fields (`investor.name`, `investor.legal_name`, `investor.email`,
      `investor.address`, `investor.bio`, `message`, `external_username`) are **omitted**
      unless the token carries `read:investors:pii`.
    - Money is integer minor units plus `amounts.currency` (`committed_cents`,
      `investment_size_cents`, `in_escrow_cents`, `contracts[].override_amount_cents`).
      `shares` and `average_share_price` are decimal strings, `null` on rounds without shares.
      `amounts.raised_cents` is the row's contribution to the public raised figure (0 while
      `needs_whitelisting`); sum it, not `committed_cents`, to match the deal page.

    Args:
        company_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | InvestmentChangeListEnvelope]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        cursor=cursor,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Any | Error | InvestmentChangeListEnvelope | None:
    """Bootstrap or page investment changes for a company

     The Investment Delta API: keep a copy of a company's investment records in sync by
    polling. Call without `cursor` to **bootstrap** (list every current record for the
    company); every response carries `meta.next_cursor`; call again with that cursor to
    receive only the records whose published state changed since. Records are the same
    shape in both modes.

    - Records are **published state**, not live rows: Wefunder publishes a record when the
      investment's founder-visible state changes, and serves exactly what was published.
    - `visible: false` records are **tombstones**: the investment is no longer visible to the
      company (canceled, converted to another round, hidden, or deleted). Delete your copy.
    - Apply records in `cursor` order. `observed_at` is when the payload was observed, not a
      version; a record you read late carries the *current* published state.
    - **410 Gone** means your cursor predates the 90-day retention window. Bootstrap again and
      **replace** your dataset for the company from the result (records absent from the
      bootstrap are deleted).
    - Investor identity fields (`investor.name`, `investor.legal_name`, `investor.email`,
      `investor.address`, `investor.bio`, `message`, `external_username`) are **omitted**
      unless the token carries `read:investors:pii`.
    - Money is integer minor units plus `amounts.currency` (`committed_cents`,
      `investment_size_cents`, `in_escrow_cents`, `contracts[].override_amount_cents`).
      `shares` and `average_share_price` are decimal strings, `null` on rounds without shares.
      `amounts.raised_cents` is the row's contribution to the public raised figure (0 while
      `needs_whitelisting`); sum it, not `committed_cents`, to match the deal page.

    Args:
        company_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | InvestmentChangeListEnvelope
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        cursor=cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Any | Error | InvestmentChangeListEnvelope]:
    """Bootstrap or page investment changes for a company

     The Investment Delta API: keep a copy of a company's investment records in sync by
    polling. Call without `cursor` to **bootstrap** (list every current record for the
    company); every response carries `meta.next_cursor`; call again with that cursor to
    receive only the records whose published state changed since. Records are the same
    shape in both modes.

    - Records are **published state**, not live rows: Wefunder publishes a record when the
      investment's founder-visible state changes, and serves exactly what was published.
    - `visible: false` records are **tombstones**: the investment is no longer visible to the
      company (canceled, converted to another round, hidden, or deleted). Delete your copy.
    - Apply records in `cursor` order. `observed_at` is when the payload was observed, not a
      version; a record you read late carries the *current* published state.
    - **410 Gone** means your cursor predates the 90-day retention window. Bootstrap again and
      **replace** your dataset for the company from the result (records absent from the
      bootstrap are deleted).
    - Investor identity fields (`investor.name`, `investor.legal_name`, `investor.email`,
      `investor.address`, `investor.bio`, `message`, `external_username`) are **omitted**
      unless the token carries `read:investors:pii`.
    - Money is integer minor units plus `amounts.currency` (`committed_cents`,
      `investment_size_cents`, `in_escrow_cents`, `contracts[].override_amount_cents`).
      `shares` and `average_share_price` are decimal strings, `null` on rounds without shares.
      `amounts.raised_cents` is the row's contribution to the public raised figure (0 while
      `needs_whitelisting`); sum it, not `committed_cents`, to match the deal page.

    Args:
        company_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | InvestmentChangeListEnvelope]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        cursor=cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Any | Error | InvestmentChangeListEnvelope | None:
    """Bootstrap or page investment changes for a company

     The Investment Delta API: keep a copy of a company's investment records in sync by
    polling. Call without `cursor` to **bootstrap** (list every current record for the
    company); every response carries `meta.next_cursor`; call again with that cursor to
    receive only the records whose published state changed since. Records are the same
    shape in both modes.

    - Records are **published state**, not live rows: Wefunder publishes a record when the
      investment's founder-visible state changes, and serves exactly what was published.
    - `visible: false` records are **tombstones**: the investment is no longer visible to the
      company (canceled, converted to another round, hidden, or deleted). Delete your copy.
    - Apply records in `cursor` order. `observed_at` is when the payload was observed, not a
      version; a record you read late carries the *current* published state.
    - **410 Gone** means your cursor predates the 90-day retention window. Bootstrap again and
      **replace** your dataset for the company from the result (records absent from the
      bootstrap are deleted).
    - Investor identity fields (`investor.name`, `investor.legal_name`, `investor.email`,
      `investor.address`, `investor.bio`, `message`, `external_username`) are **omitted**
      unless the token carries `read:investors:pii`.
    - Money is integer minor units plus `amounts.currency` (`committed_cents`,
      `investment_size_cents`, `in_escrow_cents`, `contracts[].override_amount_cents`).
      `shares` and `average_share_price` are decimal strings, `null` on rounds without shares.
      `amounts.raised_cents` is the row's contribution to the public raised figure (0 while
      `needs_whitelisting`); sum it, not `committed_cents`, to match the deal page.

    Args:
        company_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | InvestmentChangeListEnvelope
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            cursor=cursor,
            per_page=per_page,
        )
    ).parsed
