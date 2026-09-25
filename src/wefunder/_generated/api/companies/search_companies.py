from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.company_search_result_list_envelope import CompanySearchResultListEnvelope
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    q: str,
    limit: int | Unset = 8,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/companies/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CompanySearchResultListEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = CompanySearchResultListEnvelope.from_dict(response.json())



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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CompanySearchResultListEnvelope | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    limit: int | Unset = 8,

) -> Response[Any | CompanySearchResultListEnvelope | Error]:
    """ Search companies by name

     The wefunder.com search bar, companies only. Same Algolia request, same result ordering,
    and same page size as the site's top bar, so the results are what a visitor typing the
    same text would see, in that order — companies raising now and companies funded in the
    past, whether or not they appear on `/explore`. The order is the site's search order
    (match quality first, then the site's tie-breaks); nothing here recommends.

    Each result carries the company's `co_` id for `GET /companies/{id}`. With `read:explore`
    the accreditation gate matches the authorizing user (an accredited viewer sees the
    accredited-only companies the site would show them); with `read:public` it is the
    anonymous view.

    Args:
        q (str):
        limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanySearchResultListEnvelope | Error]
     """


    kwargs = _get_kwargs(
        q=q,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    q: str,
    limit: int | Unset = 8,

) -> Any | CompanySearchResultListEnvelope | Error | None:
    """ Search companies by name

     The wefunder.com search bar, companies only. Same Algolia request, same result ordering,
    and same page size as the site's top bar, so the results are what a visitor typing the
    same text would see, in that order — companies raising now and companies funded in the
    past, whether or not they appear on `/explore`. The order is the site's search order
    (match quality first, then the site's tie-breaks); nothing here recommends.

    Each result carries the company's `co_` id for `GET /companies/{id}`. With `read:explore`
    the accreditation gate matches the authorizing user (an accredited viewer sees the
    accredited-only companies the site would show them); with `read:public` it is the
    anonymous view.

    Args:
        q (str):
        limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanySearchResultListEnvelope | Error
     """


    return sync_detailed(
        client=client,
q=q,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    limit: int | Unset = 8,

) -> Response[Any | CompanySearchResultListEnvelope | Error]:
    """ Search companies by name

     The wefunder.com search bar, companies only. Same Algolia request, same result ordering,
    and same page size as the site's top bar, so the results are what a visitor typing the
    same text would see, in that order — companies raising now and companies funded in the
    past, whether or not they appear on `/explore`. The order is the site's search order
    (match quality first, then the site's tie-breaks); nothing here recommends.

    Each result carries the company's `co_` id for `GET /companies/{id}`. With `read:explore`
    the accreditation gate matches the authorizing user (an accredited viewer sees the
    accredited-only companies the site would show them); with `read:public` it is the
    anonymous view.

    Args:
        q (str):
        limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanySearchResultListEnvelope | Error]
     """


    kwargs = _get_kwargs(
        q=q,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str,
    limit: int | Unset = 8,

) -> Any | CompanySearchResultListEnvelope | Error | None:
    """ Search companies by name

     The wefunder.com search bar, companies only. Same Algolia request, same result ordering,
    and same page size as the site's top bar, so the results are what a visitor typing the
    same text would see, in that order — companies raising now and companies funded in the
    past, whether or not they appear on `/explore`. The order is the site's search order
    (match quality first, then the site's tie-breaks); nothing here recommends.

    Each result carries the company's `co_` id for `GET /companies/{id}`. With `read:explore`
    the accreditation gate matches the authorizing user (an accredited viewer sees the
    accredited-only companies the site would show them); with `read:public` it is the
    anonymous view.

    Args:
        q (str):
        limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanySearchResultListEnvelope | Error
     """


    return (await asyncio_detailed(
        client=client,
q=q,
limit=limit,

    )).parsed
