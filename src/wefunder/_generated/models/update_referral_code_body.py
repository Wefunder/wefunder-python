from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_code_utm import ReferralCodeUtm


T = TypeVar("T", bound="UpdateReferralCodeBody")


@_attrs_define
class UpdateReferralCodeBody:
    """
    Attributes:
        label (str | Unset):
        active (bool | Unset):
        utm (ReferralCodeUtm | Unset): Optional UTM presets. On a visit that carries this code, each preset fills the
            matching
            `utm_*` field when the link leaves it blank; a value on the link always wins. Each value is
            at most 100 printable ASCII characters. `source` and `campaign` may not start with `wf_`.
    """

    label: str | Unset = UNSET
    active: bool | Unset = UNSET
    utm: ReferralCodeUtm | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        active = self.active

        utm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.utm, Unset):
            utm = self.utm.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if active is not UNSET:
            field_dict["active"] = active
        if utm is not UNSET:
            field_dict["utm"] = utm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.referral_code_utm import ReferralCodeUtm  # noqa: PLC0415

        d = dict(src_dict)
        label = d.pop("label", UNSET)

        active = d.pop("active", UNSET)

        _utm = d.pop("utm", UNSET)
        utm: ReferralCodeUtm | Unset
        if isinstance(_utm, Unset):
            utm = UNSET
        else:
            utm = ReferralCodeUtm.from_dict(_utm)

        update_referral_code_body = cls(
            label=label,
            active=active,
            utm=utm,
        )

        update_referral_code_body.additional_properties = d
        return update_referral_code_body

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
