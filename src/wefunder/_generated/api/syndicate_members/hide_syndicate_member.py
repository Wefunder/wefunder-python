from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.syndicate_member_envelope import SyndicateMemberEnvelope
from typing import cast



def _get_kwargs(
    syndicate_id: str,
    member_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/syndicates/{syndicate_id}/members/{member_id}/hide".format(syndicate_id=quote(str(syndicate_id), safe=""),member_id=quote(str(member_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SyndicateMemberEnvelope | None:
    if response.status_code == 200:
        response_200 = SyndicateMemberEnvelope.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SyndicateMemberEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    syndicate_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | SyndicateMemberEnvelope]:
    """ Exile member

     Exile (hide) a member from the syndicate. Sets their role to exiled.

    Args:
        syndicate_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateMemberEnvelope]
     """


    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
member_id=member_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    syndicate_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,

) -> Error | SyndicateMemberEnvelope | None:
    """ Exile member

     Exile (hide) a member from the syndicate. Sets their role to exiled.

    Args:
        syndicate_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateMemberEnvelope
     """


    return sync_detailed(
        syndicate_id=syndicate_id,
member_id=member_id,
client=client,

    ).parsed

async def asyncio_detailed(
    syndicate_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | SyndicateMemberEnvelope]:
    """ Exile member

     Exile (hide) a member from the syndicate. Sets their role to exiled.

    Args:
        syndicate_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateMemberEnvelope]
     """


    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
member_id=member_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    syndicate_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,

) -> Error | SyndicateMemberEnvelope | None:
    """ Exile member

     Exile (hide) a member from the syndicate. Sets their role to exiled.

    Args:
        syndicate_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateMemberEnvelope
     """


    return (await asyncio_detailed(
        syndicate_id=syndicate_id,
member_id=member_id,
client=client,

    )).parsed
