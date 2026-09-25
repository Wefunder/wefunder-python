from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_envelope import CompanyEnvelope
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/companies/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CompanyEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = CompanyEnvelope.from_dict(response.json())

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
) -> Response[Any | CompanyEnvelope | Error]:
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
) -> Response[Any | CompanyEnvelope | Error]:
    """Get a company page

     The company page behind an offering, as structured data — the "click a company" step after
    `/explore`. Addressed by the `co_...` id every offering carries in `company.id`.

    Keeps apart the three raised numbers the page shows and readers conflate:
    `current_raise.amount_raised` (this campaign's live rounds combined, on Wefunder),
    `past_rounds[]` (prior rounds the page lists, each tagged `source: wefunder` for rounds
    observed here or `reported` for founder-disclosed off-platform rounds), and
    `totals.profile_total_raised` (the number on the page's ticker bar). Every figure comes
    from the same policy the page uses, so the API never disagrees with the site.

    **Who has a page.** Every company whose profile wefunder.com lists publicly — the same set
    the site's search bar returns (published, not invite-only, searchable or with a live Form C;
    accredited-only companies need an accredited viewer) — plus the `/explore` set. A funded
    company, or one the viewer may see no round of, renders with `raising: false` and
    `current_raise: null`; its history is in `wefunder_rounds`. **Logged-in view
    (`read:explore`)** additionally covers the vault / syndicate-led companies the site shows an
    accredited viewer, and the round described is the one the page would show that viewer. A
    valid id for a company outside the viewer's set is a `404`, never a partial payload.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyEnvelope | Error]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Any | CompanyEnvelope | Error | None:
    """Get a company page

     The company page behind an offering, as structured data — the "click a company" step after
    `/explore`. Addressed by the `co_...` id every offering carries in `company.id`.

    Keeps apart the three raised numbers the page shows and readers conflate:
    `current_raise.amount_raised` (this campaign's live rounds combined, on Wefunder),
    `past_rounds[]` (prior rounds the page lists, each tagged `source: wefunder` for rounds
    observed here or `reported` for founder-disclosed off-platform rounds), and
    `totals.profile_total_raised` (the number on the page's ticker bar). Every figure comes
    from the same policy the page uses, so the API never disagrees with the site.

    **Who has a page.** Every company whose profile wefunder.com lists publicly — the same set
    the site's search bar returns (published, not invite-only, searchable or with a live Form C;
    accredited-only companies need an accredited viewer) — plus the `/explore` set. A funded
    company, or one the viewer may see no round of, renders with `raising: false` and
    `current_raise: null`; its history is in `wefunder_rounds`. **Logged-in view
    (`read:explore`)** additionally covers the vault / syndicate-led companies the site shows an
    accredited viewer, and the round described is the one the page would show that viewer. A
    valid id for a company outside the viewer's set is a `404`, never a partial payload.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyEnvelope | Error
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CompanyEnvelope | Error]:
    """Get a company page

     The company page behind an offering, as structured data — the "click a company" step after
    `/explore`. Addressed by the `co_...` id every offering carries in `company.id`.

    Keeps apart the three raised numbers the page shows and readers conflate:
    `current_raise.amount_raised` (this campaign's live rounds combined, on Wefunder),
    `past_rounds[]` (prior rounds the page lists, each tagged `source: wefunder` for rounds
    observed here or `reported` for founder-disclosed off-platform rounds), and
    `totals.profile_total_raised` (the number on the page's ticker bar). Every figure comes
    from the same policy the page uses, so the API never disagrees with the site.

    **Who has a page.** Every company whose profile wefunder.com lists publicly — the same set
    the site's search bar returns (published, not invite-only, searchable or with a live Form C;
    accredited-only companies need an accredited viewer) — plus the `/explore` set. A funded
    company, or one the viewer may see no round of, renders with `raising: false` and
    `current_raise: null`; its history is in `wefunder_rounds`. **Logged-in view
    (`read:explore`)** additionally covers the vault / syndicate-led companies the site shows an
    accredited viewer, and the round described is the one the page would show that viewer. A
    valid id for a company outside the viewer's set is a `404`, never a partial payload.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyEnvelope | Error]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Any | CompanyEnvelope | Error | None:
    """Get a company page

     The company page behind an offering, as structured data — the "click a company" step after
    `/explore`. Addressed by the `co_...` id every offering carries in `company.id`.

    Keeps apart the three raised numbers the page shows and readers conflate:
    `current_raise.amount_raised` (this campaign's live rounds combined, on Wefunder),
    `past_rounds[]` (prior rounds the page lists, each tagged `source: wefunder` for rounds
    observed here or `reported` for founder-disclosed off-platform rounds), and
    `totals.profile_total_raised` (the number on the page's ticker bar). Every figure comes
    from the same policy the page uses, so the API never disagrees with the site.

    **Who has a page.** Every company whose profile wefunder.com lists publicly — the same set
    the site's search bar returns (published, not invite-only, searchable or with a live Form C;
    accredited-only companies need an accredited viewer) — plus the `/explore` set. A funded
    company, or one the viewer may see no round of, renders with `raising: false` and
    `current_raise: null`; its history is in `wefunder_rounds`. **Logged-in view
    (`read:explore`)** additionally covers the vault / syndicate-led companies the site shows an
    accredited viewer, and the round described is the one the page would show that viewer. A
    valid id for a company outside the viewer's set is a `404`, never a partial payload.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyEnvelope | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
