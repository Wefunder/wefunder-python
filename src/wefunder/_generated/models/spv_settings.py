from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.spv_settings_accreditation_type import SpvSettingsAccreditationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpvSettings")


@_attrs_define
class SpvSettings:
    """
    Attributes:
        accreditation_type (SpvSettingsAccreditationType | Unset): `self_attestation` (506b) or `verified` (506c).
            Default: SpvSettingsAccreditationType.SELF_ATTESTATION.
        auto_close_on_target (bool | Unset): Automatically begin closing when the target raise is reached. Default:
            False.
        notify_on_investment (bool | Unset): Send a partner webhook on each new investment. Default: True.
    """

    accreditation_type: SpvSettingsAccreditationType | Unset = SpvSettingsAccreditationType.SELF_ATTESTATION
    auto_close_on_target: bool | Unset = False
    notify_on_investment: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accreditation_type: str | Unset = UNSET
        if not isinstance(self.accreditation_type, Unset):
            accreditation_type = self.accreditation_type.value

        auto_close_on_target = self.auto_close_on_target

        notify_on_investment = self.notify_on_investment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accreditation_type is not UNSET:
            field_dict["accreditation_type"] = accreditation_type
        if auto_close_on_target is not UNSET:
            field_dict["auto_close_on_target"] = auto_close_on_target
        if notify_on_investment is not UNSET:
            field_dict["notify_on_investment"] = notify_on_investment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _accreditation_type = d.pop("accreditation_type", UNSET)
        accreditation_type: SpvSettingsAccreditationType | Unset
        if isinstance(_accreditation_type, Unset):
            accreditation_type = UNSET
        else:
            accreditation_type = SpvSettingsAccreditationType(_accreditation_type)

        auto_close_on_target = d.pop("auto_close_on_target", UNSET)

        notify_on_investment = d.pop("notify_on_investment", UNSET)

        spv_settings = cls(
            accreditation_type=accreditation_type,
            auto_close_on_target=auto_close_on_target,
            notify_on_investment=notify_on_investment,
        )

        spv_settings.additional_properties = d
        return spv_settings

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
