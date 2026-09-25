from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_question_list_envelope import CompanyQuestionListEnvelope
from ...models.error import Error
from ...models.list_company_questions_sort import ListCompanyQuestionsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    sort: ListCompanyQuestionsSort | Unset = ListCompanyQuestionsSort.RELEVANCE,
    past_raises: bool | Unset = False,
    q: str | Unset = UNSET,
    unanswered_by_team: bool | Unset = False,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["past_raises"] = past_raises

    params["q"] = q

    params["unanswered_by_team"] = unanswered_by_team

    params["cursor"] = cursor

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/companies/{id}/questions".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CompanyQuestionListEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = CompanyQuestionListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
) -> Response[Any | CompanyQuestionListEnvelope | Error]:
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
    sort: ListCompanyQuestionsSort | Unset = ListCompanyQuestionsSort.RELEVANCE,
    past_raises: bool | Unset = False,
    q: str | Unset = UNSET,
    unanswered_by_team: bool | Unset = False,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 20,
) -> Response[Any | CompanyQuestionListEnvelope | Error]:
    """List a company's investor questions and answers

     The company page's Ask tab as data: the questions investors asked and the answers, as the
    tab lists them for this viewer (the same repository and visibility as the site). Like the tab,
    questions default to the current raise — those asked since it opened (`meta.questions_since`);
    `past_raises=true` includes every raise, which the site offers to any visitor because
    past-raise questions are public. `sort` is the tab's dropdown: `relevance` (default:
    highlighted, then answered, then most liked), `recent`, `upvoted`, `unanswered`. Text is plain.
    Questions and answers carry their id (`cmt_...`); the integer key never leaves the API.
    Answers are the founders' own words.

    `q` searches question and answer text (Postgres full text: quoted phrases and `-word` work;
    one- or two-word queries also prefix-match) and replaces the sort with match rank —
    `meta.sort` is then `search` and each result's `match` says whether its question or an
    answer matched. `unanswered_by_team=true` keeps only questions with no live answer from the
    company's team (the founder's queue; the `unanswered` sort merely orders by whether anyone
    replied).

    Args:
        id (str):
        sort (ListCompanyQuestionsSort | Unset):  Default: ListCompanyQuestionsSort.RELEVANCE.
        past_raises (bool | Unset):  Default: False.
        q (str | Unset):
        unanswered_by_team (bool | Unset):  Default: False.
        cursor (str | Unset):
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyQuestionListEnvelope | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        sort=sort,
        past_raises=past_raises,
        q=q,
        unanswered_by_team=unanswered_by_team,
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
    sort: ListCompanyQuestionsSort | Unset = ListCompanyQuestionsSort.RELEVANCE,
    past_raises: bool | Unset = False,
    q: str | Unset = UNSET,
    unanswered_by_team: bool | Unset = False,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 20,
) -> Any | CompanyQuestionListEnvelope | Error | None:
    """List a company's investor questions and answers

     The company page's Ask tab as data: the questions investors asked and the answers, as the
    tab lists them for this viewer (the same repository and visibility as the site). Like the tab,
    questions default to the current raise — those asked since it opened (`meta.questions_since`);
    `past_raises=true` includes every raise, which the site offers to any visitor because
    past-raise questions are public. `sort` is the tab's dropdown: `relevance` (default:
    highlighted, then answered, then most liked), `recent`, `upvoted`, `unanswered`. Text is plain.
    Questions and answers carry their id (`cmt_...`); the integer key never leaves the API.
    Answers are the founders' own words.

    `q` searches question and answer text (Postgres full text: quoted phrases and `-word` work;
    one- or two-word queries also prefix-match) and replaces the sort with match rank —
    `meta.sort` is then `search` and each result's `match` says whether its question or an
    answer matched. `unanswered_by_team=true` keeps only questions with no live answer from the
    company's team (the founder's queue; the `unanswered` sort merely orders by whether anyone
    replied).

    Args:
        id (str):
        sort (ListCompanyQuestionsSort | Unset):  Default: ListCompanyQuestionsSort.RELEVANCE.
        past_raises (bool | Unset):  Default: False.
        q (str | Unset):
        unanswered_by_team (bool | Unset):  Default: False.
        cursor (str | Unset):
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyQuestionListEnvelope | Error
    """

    return sync_detailed(
        id=id,
        client=client,
        sort=sort,
        past_raises=past_raises,
        q=q,
        unanswered_by_team=unanswered_by_team,
        cursor=cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    sort: ListCompanyQuestionsSort | Unset = ListCompanyQuestionsSort.RELEVANCE,
    past_raises: bool | Unset = False,
    q: str | Unset = UNSET,
    unanswered_by_team: bool | Unset = False,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 20,
) -> Response[Any | CompanyQuestionListEnvelope | Error]:
    """List a company's investor questions and answers

     The company page's Ask tab as data: the questions investors asked and the answers, as the
    tab lists them for this viewer (the same repository and visibility as the site). Like the tab,
    questions default to the current raise — those asked since it opened (`meta.questions_since`);
    `past_raises=true` includes every raise, which the site offers to any visitor because
    past-raise questions are public. `sort` is the tab's dropdown: `relevance` (default:
    highlighted, then answered, then most liked), `recent`, `upvoted`, `unanswered`. Text is plain.
    Questions and answers carry their id (`cmt_...`); the integer key never leaves the API.
    Answers are the founders' own words.

    `q` searches question and answer text (Postgres full text: quoted phrases and `-word` work;
    one- or two-word queries also prefix-match) and replaces the sort with match rank —
    `meta.sort` is then `search` and each result's `match` says whether its question or an
    answer matched. `unanswered_by_team=true` keeps only questions with no live answer from the
    company's team (the founder's queue; the `unanswered` sort merely orders by whether anyone
    replied).

    Args:
        id (str):
        sort (ListCompanyQuestionsSort | Unset):  Default: ListCompanyQuestionsSort.RELEVANCE.
        past_raises (bool | Unset):  Default: False.
        q (str | Unset):
        unanswered_by_team (bool | Unset):  Default: False.
        cursor (str | Unset):
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyQuestionListEnvelope | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        sort=sort,
        past_raises=past_raises,
        q=q,
        unanswered_by_team=unanswered_by_team,
        cursor=cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    sort: ListCompanyQuestionsSort | Unset = ListCompanyQuestionsSort.RELEVANCE,
    past_raises: bool | Unset = False,
    q: str | Unset = UNSET,
    unanswered_by_team: bool | Unset = False,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 20,
) -> Any | CompanyQuestionListEnvelope | Error | None:
    """List a company's investor questions and answers

     The company page's Ask tab as data: the questions investors asked and the answers, as the
    tab lists them for this viewer (the same repository and visibility as the site). Like the tab,
    questions default to the current raise — those asked since it opened (`meta.questions_since`);
    `past_raises=true` includes every raise, which the site offers to any visitor because
    past-raise questions are public. `sort` is the tab's dropdown: `relevance` (default:
    highlighted, then answered, then most liked), `recent`, `upvoted`, `unanswered`. Text is plain.
    Questions and answers carry their id (`cmt_...`); the integer key never leaves the API.
    Answers are the founders' own words.

    `q` searches question and answer text (Postgres full text: quoted phrases and `-word` work;
    one- or two-word queries also prefix-match) and replaces the sort with match rank —
    `meta.sort` is then `search` and each result's `match` says whether its question or an
    answer matched. `unanswered_by_team=true` keeps only questions with no live answer from the
    company's team (the founder's queue; the `unanswered` sort merely orders by whether anyone
    replied).

    Args:
        id (str):
        sort (ListCompanyQuestionsSort | Unset):  Default: ListCompanyQuestionsSort.RELEVANCE.
        past_raises (bool | Unset):  Default: False.
        q (str | Unset):
        unanswered_by_team (bool | Unset):  Default: False.
        cursor (str | Unset):
        per_page (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyQuestionListEnvelope | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            sort=sort,
            past_raises=past_raises,
            q=q,
            unanswered_by_team=unanswered_by_team,
            cursor=cursor,
            per_page=per_page,
        )
    ).parsed
