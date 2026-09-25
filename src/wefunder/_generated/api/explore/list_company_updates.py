from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_update_list_envelope import CompanyUpdateListEnvelope
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/companies/{id}/updates".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CompanyUpdateListEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = CompanyUpdateListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CompanyUpdateListEnvelope | Error]:
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
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 20,
) -> Response[Any | CompanyUpdateListEnvelope | Error]:
    """List a company's posts

     The company page's Posts tab as data: the published updates, notes, and spotlights the
    viewer may see, pinned first then newest, with a plain-text excerpt each. With
    `read:explore` the viewer is the authorizing user, so a follower or investor sees the
    community- and investors-only posts the site shows them; with `read:public` it is the
    anonymous view. Same query as the tab (`FeedItem.viewable_by`); investments, Q&A threads,
    and investor quotes belong to other tabs and are not here. Fetch one post in full with
    `GET /companies/{id}/updates/{update_id}`. Posts are the issuer's own words.

    Args:
        id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyUpdateListEnvelope | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
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
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 20,
) -> Any | CompanyUpdateListEnvelope | Error | None:
    """List a company's posts

     The company page's Posts tab as data: the published updates, notes, and spotlights the
    viewer may see, pinned first then newest, with a plain-text excerpt each. With
    `read:explore` the viewer is the authorizing user, so a follower or investor sees the
    community- and investors-only posts the site shows them; with `read:public` it is the
    anonymous view. Same query as the tab (`FeedItem.viewable_by`); investments, Q&A threads,
    and investor quotes belong to other tabs and are not here. Fetch one post in full with
    `GET /companies/{id}/updates/{update_id}`. Posts are the issuer's own words.

    Args:
        id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyUpdateListEnvelope | Error
    """

    return sync_detailed(
        id=id,
        client=client,
        cursor=cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 20,
) -> Response[Any | CompanyUpdateListEnvelope | Error]:
    """List a company's posts

     The company page's Posts tab as data: the published updates, notes, and spotlights the
    viewer may see, pinned first then newest, with a plain-text excerpt each. With
    `read:explore` the viewer is the authorizing user, so a follower or investor sees the
    community- and investors-only posts the site shows them; with `read:public` it is the
    anonymous view. Same query as the tab (`FeedItem.viewable_by`); investments, Q&A threads,
    and investor quotes belong to other tabs and are not here. Fetch one post in full with
    `GET /companies/{id}/updates/{update_id}`. Posts are the issuer's own words.

    Args:
        id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyUpdateListEnvelope | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 20,
) -> Any | CompanyUpdateListEnvelope | Error | None:
    """List a company's posts

     The company page's Posts tab as data: the published updates, notes, and spotlights the
    viewer may see, pinned first then newest, with a plain-text excerpt each. With
    `read:explore` the viewer is the authorizing user, so a follower or investor sees the
    community- and investors-only posts the site shows them; with `read:public` it is the
    anonymous view. Same query as the tab (`FeedItem.viewable_by`); investments, Q&A threads,
    and investor quotes belong to other tabs and are not here. Fetch one post in full with
    `GET /companies/{id}/updates/{update_id}`. Posts are the issuer's own words.

    Args:
        id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyUpdateListEnvelope | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            cursor=cursor,
            per_page=per_page,
        )
    ).parsed
