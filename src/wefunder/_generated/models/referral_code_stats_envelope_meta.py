from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferralCodeStatsEnvelopeMeta")


@_attrs_define
class ReferralCodeStatsEnvelopeMeta:
    """
    Attributes:
        has_more (bool | Unset):  Example: False.
        page_count (int | Unset):  Example: 1.
        next_cursor (int | Unset): Present when has_more is true.
        request_id (str | Unset):
    """

    has_more: bool | Unset = UNSET
    page_count: int | Unset = UNSET
    next_cursor: int | Unset = UNSET
    request_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        page_count = self.page_count

        next_cursor = self.next_cursor

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_more = d.pop("has_more", UNSET)

        page_count = d.pop("page_count", UNSET)

        next_cursor = d.pop("next_cursor", UNSET)

        request_id = d.pop("request_id", UNSET)

        referral_code_stats_envelope_meta = cls(
            has_more=has_more,
            page_count=page_count,
            next_cursor=next_cursor,
            request_id=request_id,
        )

        referral_code_stats_envelope_meta.additional_properties = d
        return referral_code_stats_envelope_meta

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
