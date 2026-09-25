from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.reorder_syndicate_members_body import ReorderSyndicateMembersBody
from typing import cast



def _get_kwargs(
    syndicate_id: str,
    *,
    body: ReorderSyndicateMembersBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/syndicates/{syndicate_id}/members/reorder".format(syndicate_id=quote(str(syndicate_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    body: ReorderSyndicateMembersBody,

) -> Response[Any | Error]:
    """ Reorder members

     Set the display order for the member directory.

    Args:
        syndicate_id (str):
        body (ReorderSyndicateMembersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    body: ReorderSyndicateMembersBody,

) -> Any | Error | None:
    """ Reorder members

     Set the display order for the member directory.

    Args:
        syndicate_id (str):
        body (ReorderSyndicateMembersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        syndicate_id=syndicate_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    body: ReorderSyndicateMembersBody,

) -> Response[Any | Error]:
    """ Reorder members

     Set the display order for the member directory.

    Args:
        syndicate_id (str):
        body (ReorderSyndicateMembersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    body: ReorderSyndicateMembersBody,

) -> Any | Error | None:
    """ Reorder members

     Set the display order for the member directory.

    Args:
        syndicate_id (str):
        body (ReorderSyndicateMembersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        syndicate_id=syndicate_id,
client=client,
body=body,

    )).parsed
