from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_intent_body import CreateIntentBody
from ...models.error import Error
from ...models.intent_envelope import IntentEnvelope
from typing import cast



def _get_kwargs(
    *,
    body: CreateIntentBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/intents",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | IntentEnvelope | None:
    if response.status_code == 200:
        response_200 = IntentEnvelope.from_dict(response.json())



        return response_200

    if response.status_code == 201:
        response_201 = IntentEnvelope.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | IntentEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateIntentBody,

) -> Response[Error | IntentEnvelope]:
    """ Propose an intent

     Propose a dangerous or irreversible action for human approval. Returns a `review_url`
    where a human must review the impact and approve before the action executes.

    The entity that proposes an intent can never approve it. Approval always happens
    on Wefunder's UI by a user with permission on the resource.

    Each action names the scope that may propose it and the resource type it targets
    (`syndicates.*` → `write:syndicates` on a syndicate; `comments.create` → `write:comments`
    on a `Company`). The token must hold that action's scope; holding another proposing scope
    is not enough (403 `insufficient_scope`).

    `comments.create` posts a question on a company's Ask tab, or an answer to one, as the
    requesting user once they approve on wefunder.com. `resource_id` is the company (`co_...`);
    `params` is `{ target_type: "company" | "comment", target: "co_..." | "cmt_...", body,
    disclosure_key? }` (`disclosure_key` ∈ investor, stockholder, promoter, financial_stakeholder).
    Who may post is the site's own rule: anyone the page is available to may ask (unless the
    company has closed questions); only the company's team may answer. Only the requester can
    approve. 20 proposals per user per day (429).

    An `idempotency_key` names one operation. Reusing it for the same operation returns the
    existing intent (200) while that intent is pending, approved, executing, or executed;
    reusing it for a different action, resource, or params is a 409 `idempotency_conflict`.

    See [Intents documentation](/concepts/intents) for the full pattern.

    Args:
        body (CreateIntentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IntentEnvelope]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: CreateIntentBody,

) -> Error | IntentEnvelope | None:
    """ Propose an intent

     Propose a dangerous or irreversible action for human approval. Returns a `review_url`
    where a human must review the impact and approve before the action executes.

    The entity that proposes an intent can never approve it. Approval always happens
    on Wefunder's UI by a user with permission on the resource.

    Each action names the scope that may propose it and the resource type it targets
    (`syndicates.*` → `write:syndicates` on a syndicate; `comments.create` → `write:comments`
    on a `Company`). The token must hold that action's scope; holding another proposing scope
    is not enough (403 `insufficient_scope`).

    `comments.create` posts a question on a company's Ask tab, or an answer to one, as the
    requesting user once they approve on wefunder.com. `resource_id` is the company (`co_...`);
    `params` is `{ target_type: "company" | "comment", target: "co_..." | "cmt_...", body,
    disclosure_key? }` (`disclosure_key` ∈ investor, stockholder, promoter, financial_stakeholder).
    Who may post is the site's own rule: anyone the page is available to may ask (unless the
    company has closed questions); only the company's team may answer. Only the requester can
    approve. 20 proposals per user per day (429).

    An `idempotency_key` names one operation. Reusing it for the same operation returns the
    existing intent (200) while that intent is pending, approved, executing, or executed;
    reusing it for a different action, resource, or params is a 409 `idempotency_conflict`.

    See [Intents documentation](/concepts/intents) for the full pattern.

    Args:
        body (CreateIntentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IntentEnvelope
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateIntentBody,

) -> Response[Error | IntentEnvelope]:
    """ Propose an intent

     Propose a dangerous or irreversible action for human approval. Returns a `review_url`
    where a human must review the impact and approve before the action executes.

    The entity that proposes an intent can never approve it. Approval always happens
    on Wefunder's UI by a user with permission on the resource.

    Each action names the scope that may propose it and the resource type it targets
    (`syndicates.*` → `write:syndicates` on a syndicate; `comments.create` → `write:comments`
    on a `Company`). The token must hold that action's scope; holding another proposing scope
    is not enough (403 `insufficient_scope`).

    `comments.create` posts a question on a company's Ask tab, or an answer to one, as the
    requesting user once they approve on wefunder.com. `resource_id` is the company (`co_...`);
    `params` is `{ target_type: "company" | "comment", target: "co_..." | "cmt_...", body,
    disclosure_key? }` (`disclosure_key` ∈ investor, stockholder, promoter, financial_stakeholder).
    Who may post is the site's own rule: anyone the page is available to may ask (unless the
    company has closed questions); only the company's team may answer. Only the requester can
    approve. 20 proposals per user per day (429).

    An `idempotency_key` names one operation. Reusing it for the same operation returns the
    existing intent (200) while that intent is pending, approved, executing, or executed;
    reusing it for a different action, resource, or params is a 409 `idempotency_conflict`.

    See [Intents documentation](/concepts/intents) for the full pattern.

    Args:
        body (CreateIntentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IntentEnvelope]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateIntentBody,

) -> Error | IntentEnvelope | None:
    """ Propose an intent

     Propose a dangerous or irreversible action for human approval. Returns a `review_url`
    where a human must review the impact and approve before the action executes.

    The entity that proposes an intent can never approve it. Approval always happens
    on Wefunder's UI by a user with permission on the resource.

    Each action names the scope that may propose it and the resource type it targets
    (`syndicates.*` → `write:syndicates` on a syndicate; `comments.create` → `write:comments`
    on a `Company`). The token must hold that action's scope; holding another proposing scope
    is not enough (403 `insufficient_scope`).

    `comments.create` posts a question on a company's Ask tab, or an answer to one, as the
    requesting user once they approve on wefunder.com. `resource_id` is the company (`co_...`);
    `params` is `{ target_type: "company" | "comment", target: "co_..." | "cmt_...", body,
    disclosure_key? }` (`disclosure_key` ∈ investor, stockholder, promoter, financial_stakeholder).
    Who may post is the site's own rule: anyone the page is available to may ask (unless the
    company has closed questions); only the company's team may answer. Only the requester can
    approve. 20 proposals per user per day (429).

    An `idempotency_key` names one operation. Reusing it for the same operation returns the
    existing intent (200) while that intent is pending, approved, executing, or executed;
    reusing it for a different action, resource, or params is a 409 `idempotency_conflict`.

    See [Intents documentation](/concepts/intents) for the full pattern.

    Args:
        body (CreateIntentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IntentEnvelope
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
