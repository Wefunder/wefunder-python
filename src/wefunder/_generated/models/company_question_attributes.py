from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.company_question_attributes_match import CompanyQuestionAttributesMatch
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.company_question_attributes_answers_item import CompanyQuestionAttributesAnswersItem
  from ..models.company_question_person import CompanyQuestionPerson





T = TypeVar("T", bound="CompanyQuestionAttributes")



@_attrs_define
class CompanyQuestionAttributes:
    """ 
        Attributes:
            question (None | str | Unset):
            asked_at (datetime.datetime | None | Unset):
            asked_by (CompanyQuestionPerson | Unset):
            likes_count (int | Unset):
            highlighted (bool | Unset): The team highlighted this question on the tab.
            answered_by_team (bool | Unset):
            match (CompanyQuestionAttributesMatch | Unset): In a search (`q`), whether the question's own text or one of its
                answers matched. Null otherwise.
            answers (list[CompanyQuestionAttributesAnswersItem] | Unset):
            url (None | str | Unset): The company's Ask tab on wefunder.com.
     """

    question: None | str | Unset = UNSET
    asked_at: datetime.datetime | None | Unset = UNSET
    asked_by: CompanyQuestionPerson | Unset = UNSET
    likes_count: int | Unset = UNSET
    highlighted: bool | Unset = UNSET
    answered_by_team: bool | Unset = UNSET
    match: CompanyQuestionAttributesMatch | Unset = UNSET
    answers: list[CompanyQuestionAttributesAnswersItem] | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_question_attributes_answers_item import CompanyQuestionAttributesAnswersItem # noqa: PLC0415
        from ..models.company_question_person import CompanyQuestionPerson # noqa: PLC0415
        question: None | str | Unset
        if isinstance(self.question, Unset):
            question = UNSET
        else:
            question = self.question

        asked_at: None | str | Unset
        if isinstance(self.asked_at, Unset):
            asked_at = UNSET
        elif isinstance(self.asked_at, datetime.datetime):
            asked_at = self.asked_at.isoformat()
        else:
            asked_at = self.asked_at

        asked_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asked_by, Unset):
            asked_by = self.asked_by.to_dict()

        likes_count = self.likes_count

        highlighted = self.highlighted

        answered_by_team = self.answered_by_team

        match: str | Unset = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.value


        answers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item = answers_item_data.to_dict()
                answers.append(answers_item)



        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if question is not UNSET:
            field_dict["question"] = question
        if asked_at is not UNSET:
            field_dict["asked_at"] = asked_at
        if asked_by is not UNSET:
            field_dict["asked_by"] = asked_by
        if likes_count is not UNSET:
            field_dict["likes_count"] = likes_count
        if highlighted is not UNSET:
            field_dict["highlighted"] = highlighted
        if answered_by_team is not UNSET:
            field_dict["answered_by_team"] = answered_by_team
        if match is not UNSET:
            field_dict["match"] = match
        if answers is not UNSET:
            field_dict["answers"] = answers
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_question_attributes_answers_item import CompanyQuestionAttributesAnswersItem # noqa: PLC0415
        from ..models.company_question_person import CompanyQuestionPerson # noqa: PLC0415
        d = dict(src_dict)
        def _parse_question(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        question = _parse_question(d.pop("question", UNSET))


        def _parse_asked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                asked_at_type_0 = datetime.datetime.fromisoformat(data)



                return asked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        asked_at = _parse_asked_at(d.pop("asked_at", UNSET))


        _asked_by = d.pop("asked_by", UNSET)
        asked_by: CompanyQuestionPerson | Unset
        if isinstance(_asked_by,  Unset):
            asked_by = UNSET
        else:
            asked_by = CompanyQuestionPerson.from_dict(_asked_by)




        likes_count = d.pop("likes_count", UNSET)

        highlighted = d.pop("highlighted", UNSET)

        answered_by_team = d.pop("answered_by_team", UNSET)

        _match = d.pop("match", UNSET)
        match: CompanyQuestionAttributesMatch | Unset
        if isinstance(_match,  Unset):
            match = UNSET
        else:
            match = CompanyQuestionAttributesMatch(_match)




        _answers = d.pop("answers", UNSET)
        answers: list[CompanyQuestionAttributesAnswersItem] | Unset = UNSET
        if _answers is not UNSET:
            answers = []
            for answers_item_data in _answers:
                answers_item = CompanyQuestionAttributesAnswersItem.from_dict(answers_item_data)



                answers.append(answers_item)


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        company_question_attributes = cls(
            question=question,
            asked_at=asked_at,
            asked_by=asked_by,
            likes_count=likes_count,
            highlighted=highlighted,
            answered_by_team=answered_by_team,
            match=match,
            answers=answers,
            url=url,
        )


        company_question_attributes.additional_properties = d
        return company_question_attributes

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
