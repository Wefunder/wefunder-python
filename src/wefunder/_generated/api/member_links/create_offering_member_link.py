from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_offering_member_link_body import CreateOfferingMemberLinkBody
from ...models.error import Error
from ...models.member_link_envelope import MemberLinkEnvelope
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: CreateOfferingMemberLinkBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/offerings/{id}/member_links".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MemberLinkEnvelope | ValidationError | None:
    if response.status_code == 200:
        response_200 = MemberLinkEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = MemberLinkEnvelope.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | MemberLinkEnvelope | ValidationError]:
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
    body: CreateOfferingMemberLinkBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[Error | MemberLinkEnvelope | ValidationError]:
    """Create a member link

     Mints a link that sends one of your members to this offering's deal page. It
    carries no email: it binds to the first Wefunder account that invests through
    it, whatever address that account uses, or up front when you pass the
    `wefunder_user_id` of a member whose account you already know. A bound link
    answers only to its account: anyone else (logged out, or another account) gets
    no private access and no invited pricing, and is asked to sign in with the
    invited account.

    The member gets what an invitation from the offering's manager or founder
    gets: access to a private round and invited pricing.

    Pass `reference` (your member id) to make the create idempotent per offering:
    repeating it returns the live link with 200. The same reference on another
    offering mints that offering's own link, since a member gets one link per
    deal. Requires a syndicate- or company-owned token of an app installed on the
    offering's syndicate or company; user tokens get 404.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CreateOfferingMemberLinkBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MemberLinkEnvelope | ValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateOfferingMemberLinkBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Error | MemberLinkEnvelope | ValidationError | None:
    """Create a member link

     Mints a link that sends one of your members to this offering's deal page. It
    carries no email: it binds to the first Wefunder account that invests through
    it, whatever address that account uses, or up front when you pass the
    `wefunder_user_id` of a member whose account you already know. A bound link
    answers only to its account: anyone else (logged out, or another account) gets
    no private access and no invited pricing, and is asked to sign in with the
    invited account.

    The member gets what an invitation from the offering's manager or founder
    gets: access to a private round and invited pricing.

    Pass `reference` (your member id) to make the create idempotent per offering:
    repeating it returns the live link with 200. The same reference on another
    offering mints that offering's own link, since a member gets one link per
    deal. Requires a syndicate- or company-owned token of an app installed on the
    offering's syndicate or company; user tokens get 404.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CreateOfferingMemberLinkBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MemberLinkEnvelope | ValidationError
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateOfferingMemberLinkBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[Error | MemberLinkEnvelope | ValidationError]:
    """Create a member link

     Mints a link that sends one of your members to this offering's deal page. It
    carries no email: it binds to the first Wefunder account that invests through
    it, whatever address that account uses, or up front when you pass the
    `wefunder_user_id` of a member whose account you already know. A bound link
    answers only to its account: anyone else (logged out, or another account) gets
    no private access and no invited pricing, and is asked to sign in with the
    invited account.

    The member gets what an invitation from the offering's manager or founder
    gets: access to a private round and invited pricing.

    Pass `reference` (your member id) to make the create idempotent per offering:
    repeating it returns the live link with 200. The same reference on another
    offering mints that offering's own link, since a member gets one link per
    deal. Requires a syndicate- or company-owned token of an app installed on the
    offering's syndicate or company; user tokens get 404.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CreateOfferingMemberLinkBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MemberLinkEnvelope | ValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateOfferingMemberLinkBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Error | MemberLinkEnvelope | ValidationError | None:
    """Create a member link

     Mints a link that sends one of your members to this offering's deal page. It
    carries no email: it binds to the first Wefunder account that invests through
    it, whatever address that account uses, or up front when you pass the
    `wefunder_user_id` of a member whose account you already know. A bound link
    answers only to its account: anyone else (logged out, or another account) gets
    no private access and no invited pricing, and is asked to sign in with the
    invited account.

    The member gets what an invitation from the offering's manager or founder
    gets: access to a private round and invited pricing.

    Pass `reference` (your member id) to make the create idempotent per offering:
    repeating it returns the live link with 200. The same reference on another
    offering mints that offering's own link, since a member gets one link per
    deal. Requires a syndicate- or company-owned token of an app installed on the
    offering's syndicate or company; user tokens get 404.

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CreateOfferingMemberLinkBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MemberLinkEnvelope | ValidationError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
