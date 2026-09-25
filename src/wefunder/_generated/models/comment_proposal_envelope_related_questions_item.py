from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentProposalEnvelopeRelatedQuestionsItem")


@_attrs_define
class CommentProposalEnvelopeRelatedQuestionsItem:
    """
    Attributes:
        id (str | Unset):
        question (None | str | Unset):
        asked_at (None | str | Unset):
        answered_by_team (bool | Unset):
        answers (list[None | str] | Unset):
        url (None | str | Unset):
    """

    id: str | Unset = UNSET
    question: None | str | Unset = UNSET
    asked_at: None | str | Unset = UNSET
    answered_by_team: bool | Unset = UNSET
    answers: list[None | str] | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        question: None | str | Unset
        if isinstance(self.question, Unset):
            question = UNSET
        else:
            question = self.question

        asked_at: None | str | Unset
        if isinstance(self.asked_at, Unset):
            asked_at = UNSET
        else:
            asked_at = self.asked_at

        answered_by_team = self.answered_by_team

        answers: list[None | str] | Unset = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item: None | str
                answers_item = answers_item_data
                answers.append(answers_item)

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if question is not UNSET:
            field_dict["question"] = question
        if asked_at is not UNSET:
            field_dict["asked_at"] = asked_at
        if answered_by_team is not UNSET:
            field_dict["answered_by_team"] = answered_by_team
        if answers is not UNSET:
            field_dict["answers"] = answers
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_question(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        question = _parse_question(d.pop("question", UNSET))

        def _parse_asked_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asked_at = _parse_asked_at(d.pop("asked_at", UNSET))

        answered_by_team = d.pop("answered_by_team", UNSET)

        _answers = d.pop("answers", UNSET)
        answers: list[None | str] | Unset = UNSET
        if _answers is not UNSET:
            answers = []
            for answers_item_data in _answers:

                def _parse_answers_item(data: object) -> None | str:
                    if data is None:
                        return data
                    return cast(None | str, data)

                answers_item = _parse_answers_item(answers_item_data)

                answers.append(answers_item)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        comment_proposal_envelope_related_questions_item = cls(
            id=id,
            question=question,
            asked_at=asked_at,
            answered_by_team=answered_by_team,
            answers=answers,
            url=url,
        )

        comment_proposal_envelope_related_questions_item.additional_properties = d
        return comment_proposal_envelope_related_questions_item

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
