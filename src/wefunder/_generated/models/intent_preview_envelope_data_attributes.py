from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.intent_preview_envelope_data_attributes_params import IntentPreviewEnvelopeDataAttributesParams





T = TypeVar("T", bound="IntentPreviewEnvelopeDataAttributes")



@_attrs_define
class IntentPreviewEnvelopeDataAttributes:
    """ 
        Attributes:
            action (str | Unset):
            resource_type (str | Unset):
            resource_id (str | Unset): The resource's external id (`co_...`, `syn_...`).
            params (IntentPreviewEnvelopeDataAttributesParams | Unset):
            impact_summary (str | Unset): What the review page would show the approver.
            scope (str | Unset): The scope `POST /intents` requires for this action.
     """

    action: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    params: IntentPreviewEnvelopeDataAttributesParams | Unset = UNSET
    impact_summary: str | Unset = UNSET
    scope: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.intent_preview_envelope_data_attributes_params import IntentPreviewEnvelopeDataAttributesParams # noqa: PLC0415
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
        from ..models.intent_preview_envelope_data_attributes_params import IntentPreviewEnvelopeDataAttributesParams # noqa: PLC0415
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        _params = d.pop("params", UNSET)
        params: IntentPreviewEnvelopeDataAttributesParams | Unset
        if isinstance(_params,  Unset):
            params = UNSET
        else:
            params = IntentPreviewEnvelopeDataAttributesParams.from_dict(_params)




        impact_summary = d.pop("impact_summary", UNSET)

        scope = d.pop("scope", UNSET)

        intent_preview_envelope_data_attributes = cls(
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            params=params,
            impact_summary=impact_summary,
            scope=scope,
        )


        intent_preview_envelope_data_attributes.additional_properties = d
        return intent_preview_envelope_data_attributes

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
