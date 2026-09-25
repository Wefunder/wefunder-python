from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribution_partner_type_0_status import AttributionPartnerType0Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributionPartnerType0")


@_attrs_define
class AttributionPartnerType0:
    """
    Attributes:
        id (int | Unset):  Example: 123.
        company_name (str | Unset):  Example: Example Name.
        website (str | Unset):  Example: https://example.com.
        status (AttributionPartnerType0Status | Unset):
    """

    id: int | Unset = UNSET
    company_name: str | Unset = UNSET
    website: str | Unset = UNSET
    status: AttributionPartnerType0Status | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_name = self.company_name

        website = self.website

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if website is not UNSET:
            field_dict["website"] = website
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        company_name = d.pop("company_name", UNSET)

        website = d.pop("website", UNSET)

        _status = d.pop("status", UNSET)
        status: AttributionPartnerType0Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AttributionPartnerType0Status(_status)

        attribution_partner_type_0 = cls(
            id=id,
            company_name=company_name,
            website=website,
            status=status,
        )

        attribution_partner_type_0.additional_properties = d
        return attribution_partner_type_0

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
