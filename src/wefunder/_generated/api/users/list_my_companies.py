from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.my_company_list_envelope import MyCompanyListEnvelope
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/me/companies",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | MyCompanyListEnvelope | None:
    if response.status_code == 200:
        response_200 = MyCompanyListEnvelope.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | MyCompanyListEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Error | MyCompanyListEnvelope]:
    """ List the companies you edit

     The companies the authenticated user is a founder or team member of — precisely the
    companies the founder-scoped endpoints under `/companies/{company_id}/...` (dashboard,
    investors, fundraises) will accept. Anyone else's company returns 403 there, so call this
    first to learn which `co_` ids you hold. Not paginated.

    `raising` is true when the company has a round currently accepting investments or
    reservations. `roles` are the user's roles on the company (`founder`, `employee`, ...).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MyCompanyListEnvelope]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Error | MyCompanyListEnvelope | None:
    """ List the companies you edit

     The companies the authenticated user is a founder or team member of — precisely the
    companies the founder-scoped endpoints under `/companies/{company_id}/...` (dashboard,
    investors, fundraises) will accept. Anyone else's company returns 403 there, so call this
    first to learn which `co_` ids you hold. Not paginated.

    `raising` is true when the company has a round currently accepting investments or
    reservations. `roles` are the user's roles on the company (`founder`, `employee`, ...).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MyCompanyListEnvelope
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Error | MyCompanyListEnvelope]:
    """ List the companies you edit

     The companies the authenticated user is a founder or team member of — precisely the
    companies the founder-scoped endpoints under `/companies/{company_id}/...` (dashboard,
    investors, fundraises) will accept. Anyone else's company returns 403 there, so call this
    first to learn which `co_` ids you hold. Not paginated.

    `raising` is true when the company has a round currently accepting investments or
    reservations. `roles` are the user's roles on the company (`founder`, `employee`, ...).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MyCompanyListEnvelope]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Error | MyCompanyListEnvelope | None:
    """ List the companies you edit

     The companies the authenticated user is a founder or team member of — precisely the
    companies the founder-scoped endpoints under `/companies/{company_id}/...` (dashboard,
    investors, fundraises) will accept. Anyone else's company returns 403 there, so call this
    first to learn which `co_` ids you hold. Not paginated.

    `raising` is true when the company has a round currently accepting investments or
    reservations. `roles` are the user's roles on the company (`founder`, `employee`, ...).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MyCompanyListEnvelope
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
