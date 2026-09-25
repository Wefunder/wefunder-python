from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CompanyQuestionListEnvelopeMeta")



@_attrs_define
class CompanyQuestionListEnvelopeMeta:
    """ 
        Attributes:
            company (str | Unset):
            sort (str | Unset): The sort applied; `search` when `q` was given (results are ranked by match).
            q (None | str | Unset):
            unanswered_by_team (bool | Unset):
            past_raises (bool | Unset):
            questions_since (datetime.date | None | Unset): The current raise's opening date when `past_raises` is false;
                null otherwise.
            total (int | Unset): Questions matching, across all pages.
            has_more (bool | Unset):
            page_count (int | Unset):
            next_cursor (int | None | Unset):
     """

    company: str | Unset = UNSET
    sort: str | Unset = UNSET
    q: None | str | Unset = UNSET
    unanswered_by_team: bool | Unset = UNSET
    past_raises: bool | Unset = UNSET
    questions_since: datetime.date | None | Unset = UNSET
    total: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    page_count: int | Unset = UNSET
    next_cursor: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        company = self.company

        sort = self.sort

        q: None | str | Unset
        if isinstance(self.q, Unset):
            q = UNSET
        else:
            q = self.q

        unanswered_by_team = self.unanswered_by_team

        past_raises = self.past_raises

        questions_since: None | str | Unset
        if isinstance(self.questions_since, Unset):
            questions_since = UNSET
        elif isinstance(self.questions_since, datetime.date):
            questions_since = self.questions_since.isoformat()
        else:
            questions_since = self.questions_since

        total = self.total

        has_more = self.has_more

        page_count = self.page_count

        next_cursor: int | None | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if company is not UNSET:
            field_dict["company"] = company
        if sort is not UNSET:
            field_dict["sort"] = sort
        if q is not UNSET:
            field_dict["q"] = q
        if unanswered_by_team is not UNSET:
            field_dict["unanswered_by_team"] = unanswered_by_team
        if past_raises is not UNSET:
            field_dict["past_raises"] = past_raises
        if questions_since is not UNSET:
            field_dict["questions_since"] = questions_since
        if total is not UNSET:
            field_dict["total"] = total
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company = d.pop("company", UNSET)

        sort = d.pop("sort", UNSET)

        def _parse_q(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        q = _parse_q(d.pop("q", UNSET))


        unanswered_by_team = d.pop("unanswered_by_team", UNSET)

        past_raises = d.pop("past_raises", UNSET)

        def _parse_questions_since(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                questions_since_type_0 = datetime.date.fromisoformat(data)



                return questions_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        questions_since = _parse_questions_since(d.pop("questions_since", UNSET))


        total = d.pop("total", UNSET)

        has_more = d.pop("has_more", UNSET)

        page_count = d.pop("page_count", UNSET)

        def _parse_next_cursor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))


        company_question_list_envelope_meta = cls(
            company=company,
            sort=sort,
            q=q,
            unanswered_by_team=unanswered_by_team,
            past_raises=past_raises,
            questions_since=questions_since,
            total=total,
            has_more=has_more,
            page_count=page_count,
            next_cursor=next_cursor,
        )


        company_question_list_envelope_meta.additional_properties = d
        return company_question_list_envelope_meta

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
