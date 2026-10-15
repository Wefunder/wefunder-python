from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.referral_code_attributes_target_type_0_type import ReferralCodeAttributesTargetType0Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferralCodeAttributesTargetType0")


@_attrs_define
class ReferralCodeAttributesTargetType0:
    """The company or offering this code credits, or null for any company. If the target
    no longer exists, `id` is null and `unavailable` is true: the code credits nothing.

        Attributes:
            type_ (ReferralCodeAttributesTargetType0Type | Unset):
            id (None | str | Unset):  Example: co_7hQExampleCompany0001.
            unavailable (bool | Unset): Present and true when the target no longer exists.
    """

    type_: ReferralCodeAttributesTargetType0Type | Unset = UNSET
    id: None | str | Unset = UNSET
    unavailable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        unavailable = self.unavailable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if unavailable is not UNSET:
            field_dict["unavailable"] = unavailable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ReferralCodeAttributesTargetType0Type | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ReferralCodeAttributesTargetType0Type(_type_)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        unavailable = d.pop("unavailable", UNSET)

        referral_code_attributes_target_type_0 = cls(
            type_=type_,
            id=id,
            unavailable=unavailable,
        )

        referral_code_attributes_target_type_0.additional_properties = d
        return referral_code_attributes_target_type_0

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
