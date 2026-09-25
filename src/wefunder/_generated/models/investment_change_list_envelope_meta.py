from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investment_change_list_envelope_meta_mode import InvestmentChangeListEnvelopeMetaMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvestmentChangeListEnvelopeMeta")


@_attrs_define
class InvestmentChangeListEnvelopeMeta:
    """
    Attributes:
        mode (InvestmentChangeListEnvelopeMetaMode | Unset):
        has_more (bool | Unset):
        next_cursor (str | Unset): Always present. Pass it back as `cursor` on the next call, even when `has_more` is
            false.
        page_count (int | Unset):
        company_id (str | Unset):
    """

    mode: InvestmentChangeListEnvelopeMetaMode | Unset = UNSET
    has_more: bool | Unset = UNSET
    next_cursor: str | Unset = UNSET
    page_count: int | Unset = UNSET
    company_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        has_more = self.has_more

        next_cursor = self.next_cursor

        page_count = self.page_count

        company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if company_id is not UNSET:
            field_dict["company_id"] = company_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: InvestmentChangeListEnvelopeMetaMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = InvestmentChangeListEnvelopeMetaMode(_mode)

        has_more = d.pop("has_more", UNSET)

        next_cursor = d.pop("next_cursor", UNSET)

        page_count = d.pop("page_count", UNSET)

        company_id = d.pop("company_id", UNSET)

        investment_change_list_envelope_meta = cls(
            mode=mode,
            has_more=has_more,
            next_cursor=next_cursor,
            page_count=page_count,
            company_id=company_id,
        )

        investment_change_list_envelope_meta.additional_properties = d
        return investment_change_list_envelope_meta

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
