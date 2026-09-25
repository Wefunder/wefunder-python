from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview_intent_body_params import PreviewIntentBodyParams


T = TypeVar("T", bound="PreviewIntentBody")


@_attrs_define
class PreviewIntentBody:
    """
    Attributes:
        action_name (str):
        resource_type (str):
        resource_id (str):
        params (PreviewIntentBodyParams | Unset):
    """

    action_name: str
    resource_type: str
    resource_id: str
    params: PreviewIntentBodyParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_name = self.action_name

        resource_type = self.resource_type

        resource_id = self.resource_id

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_name": action_name,
                "resource_type": resource_type,
                "resource_id": resource_id,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_intent_body_params import PreviewIntentBodyParams  # noqa: PLC0415

        d = dict(src_dict)
        action_name = d.pop("action_name")

        resource_type = d.pop("resource_type")

        resource_id = d.pop("resource_id")

        _params = d.pop("params", UNSET)
        params: PreviewIntentBodyParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = PreviewIntentBodyParams.from_dict(_params)

        preview_intent_body = cls(
            action_name=action_name,
            resource_type=resource_type,
            resource_id=resource_id,
            params=params,
        )

        preview_intent_body.additional_properties = d
        return preview_intent_body

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
