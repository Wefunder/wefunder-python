from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.comment_proposal_envelope_draft_type_0_params import CommentProposalEnvelopeDraftType0Params





T = TypeVar("T", bound="CommentProposalEnvelopeDraftType0")



@_attrs_define
class CommentProposalEnvelopeDraftType0:
    """ The dry run (null when `allowed` is false). Same shape as IntentPreviewEnvelope's attributes.

        Attributes:
            action (str | Unset):
            resource_type (str | Unset):
            resource_id (str | Unset):
            params (CommentProposalEnvelopeDraftType0Params | Unset):
            impact_summary (str | Unset):
            scope (str | Unset):
     """

    action: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    params: CommentProposalEnvelopeDraftType0Params | Unset = UNSET
    impact_summary: str | Unset = UNSET
    scope: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.comment_proposal_envelope_draft_type_0_params import CommentProposalEnvelopeDraftType0Params # noqa: PLC0415
        action = self.action

        resource_type = self.resource_type

        resource_id = self.resource_id

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        impact_summary = self.impact_summary

        scope = self.scope


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if action is not UNSET:
            field_dict["action"] = action
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if params is not UNSET:
            field_dict["params"] = params
        if impact_summary is not UNSET:
            field_dict["impact_summary"] = impact_summary
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment_proposal_envelope_draft_type_0_params import CommentProposalEnvelopeDraftType0Params # noqa: PLC0415
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        _params = d.pop("params", UNSET)
        params: CommentProposalEnvelopeDraftType0Params | Unset
        if isinstance(_params,  Unset):
            params = UNSET
        else:
            params = CommentProposalEnvelopeDraftType0Params.from_dict(_params)




        impact_summary = d.pop("impact_summary", UNSET)

        scope = d.pop("scope", UNSET)

        comment_proposal_envelope_draft_type_0 = cls(
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            params=params,
            impact_summary=impact_summary,
            scope=scope,
        )


        comment_proposal_envelope_draft_type_0.additional_properties = d
        return comment_proposal_envelope_draft_type_0

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
