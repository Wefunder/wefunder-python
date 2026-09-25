from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.company_question_person import CompanyQuestionPerson





T = TypeVar("T", bound="CompanyQuestionAttributesAnswersItem")



@_attrs_define
class CompanyQuestionAttributesAnswersItem:
    """ 
        Attributes:
            id (str | Unset): The answer's id (`cmt_...`).
            answer (None | str | Unset):
            answered_at (datetime.datetime | None | Unset):
            answered_by (CompanyQuestionPerson | Unset):
            likes_count (int | Unset):
     """

    id: str | Unset = UNSET
    answer: None | str | Unset = UNSET
    answered_at: datetime.datetime | None | Unset = UNSET
    answered_by: CompanyQuestionPerson | Unset = UNSET
    likes_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_question_person import CompanyQuestionPerson # noqa: PLC0415
        id = self.id

        answer: None | str | Unset
        if isinstance(self.answer, Unset):
            answer = UNSET
        else:
            answer = self.answer

        answered_at: None | str | Unset
        if isinstance(self.answered_at, Unset):
            answered_at = UNSET
        elif isinstance(self.answered_at, datetime.datetime):
            answered_at = self.answered_at.isoformat()
        else:
            answered_at = self.answered_at

        answered_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.answered_by, Unset):
            answered_by = self.answered_by.to_dict()

        likes_count = self.likes_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if answer is not UNSET:
            field_dict["answer"] = answer
        if answered_at is not UNSET:
            field_dict["answered_at"] = answered_at
        if answered_by is not UNSET:
            field_dict["answered_by"] = answered_by
        if likes_count is not UNSET:
            field_dict["likes_count"] = likes_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_question_person import CompanyQuestionPerson # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_answer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        answer = _parse_answer(d.pop("answer", UNSET))


        def _parse_answered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                answered_at_type_0 = datetime.datetime.fromisoformat(data)



                return answered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        answered_at = _parse_answered_at(d.pop("answered_at", UNSET))


        _answered_by = d.pop("answered_by", UNSET)
        answered_by: CompanyQuestionPerson | Unset
        if isinstance(_answered_by,  Unset):
            answered_by = UNSET
        else:
            answered_by = CompanyQuestionPerson.from_dict(_answered_by)




        likes_count = d.pop("likes_count", UNSET)

        company_question_attributes_answers_item = cls(
            id=id,
            answer=answer,
            answered_at=answered_at,
            answered_by=answered_by,
            likes_count=likes_count,
        )


        company_question_attributes_answers_item.additional_properties = d
        return company_question_attributes_answers_item

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
