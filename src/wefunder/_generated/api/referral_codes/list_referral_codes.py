from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.referral_code_list_envelope import ReferralCodeListEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: bool | Unset = UNSET,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["active"] = active

    params["cursor"] = cursor

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/referral_codes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ReferralCodeListEnvelope | None:
    if response.status_code == 200:
        response_200 = ReferralCodeListEnvelope.from_dict(response.json())

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
) -> Response[Error | ReferralCodeListEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Error | ReferralCodeListEnvelope]:
    """List referral codes

     The referral codes your application created, newest first. A referral code records that a
    visitor arrived through your link (`?wfr=ref_…`); it never changes what the visitor sees and
    grants no access. Filter with `active=true` or `active=false`.

    Every referral code operation takes your application's own server key (a
    `client_credentials` token). A user or installation token gets `403 app_credentials_required`.

    Args:
        active (bool | Unset):
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReferralCodeListEnvelope]
    """

    kwargs = _get_kwargs(
        active=active,
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
    active: bool | Unset = UNSET,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Error | ReferralCodeListEnvelope | None:
    """List referral codes

     The referral codes your application created, newest first. A referral code records that a
    visitor arrived through your link (`?wfr=ref_…`); it never changes what the visitor sees and
    grants no access. Filter with `active=true` or `active=false`.

    Every referral code operation takes your application's own server key (a
    `client_credentials` token). A user or installation token gets `403 app_credentials_required`.

    Args:
        active (bool | Unset):
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReferralCodeListEnvelope
    """

    return sync_detailed(
        client=client,
        active=active,
        cursor=cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Error | ReferralCodeListEnvelope]:
    """List referral codes

     The referral codes your application created, newest first. A referral code records that a
    visitor arrived through your link (`?wfr=ref_…`); it never changes what the visitor sees and
    grants no access. Filter with `active=true` or `active=false`.

    Every referral code operation takes your application's own server key (a
    `client_credentials` token). A user or installation token gets `403 app_credentials_required`.

    Args:
        active (bool | Unset):
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReferralCodeListEnvelope]
    """

    kwargs = _get_kwargs(
        active=active,
        cursor=cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Error | ReferralCodeListEnvelope | None:
    """List referral codes

     The referral codes your application created, newest first. A referral code records that a
    visitor arrived through your link (`?wfr=ref_…`); it never changes what the visitor sees and
    grants no access. Filter with `active=true` or `active=false`.

    Every referral code operation takes your application's own server key (a
    `client_credentials` token). A user or installation token gets `403 app_credentials_required`.

    Args:
        active (bool | Unset):
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReferralCodeListEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            active=active,
            cursor=cursor,
            per_page=per_page,
        )
    ).parsed
