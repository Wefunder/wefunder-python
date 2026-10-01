from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DealInvestorListEnvelopeMeta")


@_attrs_define
class DealInvestorListEnvelopeMeta:
    """
    Attributes:
        count (int | Unset): Number of investors on this page
        total_count (int | Unset): Total investors in the deal
        offset (int | Unset):
        per_page (int | Unset):
        has_more (bool | Unset):
    """

    count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    offset: int | Unset = UNSET
    per_page: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        total_count = self.total_count

        offset = self.offset

        per_page = self.per_page

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if offset is not UNSET:
            field_dict["offset"] = offset
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        total_count = d.pop("total_count", UNSET)

        offset = d.pop("offset", UNSET)

        per_page = d.pop("per_page", UNSET)

        has_more = d.pop("has_more", UNSET)

        deal_investor_list_envelope_meta = cls(
            count=count,
            total_count=total_count,
            offset=offset,
            per_page=per_page,
            has_more=has_more,
        )

        deal_investor_list_envelope_meta.additional_properties = d
        return deal_investor_list_envelope_meta

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
