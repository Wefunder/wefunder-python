from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comment_proposal_envelope_proposal_target_type import CommentProposalEnvelopeProposalTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentProposalEnvelopeProposal")


@_attrs_define
class CommentProposalEnvelopeProposal:
    """The arguments, as normalized, to pass to write_comment_intent once the user confirms.

    Attributes:
        company_id (str | Unset):
        target_type (CommentProposalEnvelopeProposalTargetType | Unset):
        target (str | Unset):
        body (str | Unset):
        disclosure_key (None | str | Unset):
    """

    company_id: str | Unset = UNSET
    target_type: CommentProposalEnvelopeProposalTargetType | Unset = UNSET
    target: str | Unset = UNSET
    body: str | Unset = UNSET
    disclosure_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        target_type: str | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        target = self.target

        body = self.body

        disclosure_key: None | str | Unset
        if isinstance(self.disclosure_key, Unset):
            disclosure_key = UNSET
        else:
            disclosure_key = self.disclosure_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if target_type is not UNSET:
            field_dict["target_type"] = target_type
        if target is not UNSET:
            field_dict["target"] = target
        if body is not UNSET:
            field_dict["body"] = body
        if disclosure_key is not UNSET:
            field_dict["disclosure_key"] = disclosure_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("company_id", UNSET)

        _target_type = d.pop("target_type", UNSET)
        target_type: CommentProposalEnvelopeProposalTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = CommentProposalEnvelopeProposalTargetType(_target_type)

        target = d.pop("target", UNSET)

        body = d.pop("body", UNSET)

        def _parse_disclosure_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disclosure_key = _parse_disclosure_key(d.pop("disclosure_key", UNSET))

        comment_proposal_envelope_proposal = cls(
            company_id=company_id,
            target_type=target_type,
            target=target,
            body=body,
            disclosure_key=disclosure_key,
        )

        comment_proposal_envelope_proposal.additional_properties = d
        return comment_proposal_envelope_proposal

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
