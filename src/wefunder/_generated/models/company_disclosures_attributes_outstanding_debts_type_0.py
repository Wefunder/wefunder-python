from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_disclosures_attributes_outstanding_debts_type_0_items_item import (
        CompanyDisclosuresAttributesOutstandingDebtsType0ItemsItem,
    )


T = TypeVar("T", bound="CompanyDisclosuresAttributesOutstandingDebtsType0")


@_attrs_define
class CompanyDisclosuresAttributesOutstandingDebtsType0:
    """
    Attributes:
        note (None | str | Unset): A company-specific note the site shows instead of the table, when set.
        items (list[CompanyDisclosuresAttributesOutstandingDebtsType0ItemsItem] | Unset):
    """

    note: None | str | Unset = UNSET
    items: list[CompanyDisclosuresAttributesOutstandingDebtsType0ItemsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note is not UNSET:
            field_dict["note"] = note
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_disclosures_attributes_outstanding_debts_type_0_items_item import (
            CompanyDisclosuresAttributesOutstandingDebtsType0ItemsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        _items = d.pop("items", UNSET)
        items: list[CompanyDisclosuresAttributesOutstandingDebtsType0ItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = CompanyDisclosuresAttributesOutstandingDebtsType0ItemsItem.from_dict(items_item_data)

                items.append(items_item)

        company_disclosures_attributes_outstanding_debts_type_0 = cls(
            note=note,
            items=items,
        )

        company_disclosures_attributes_outstanding_debts_type_0.additional_properties = d
        return company_disclosures_attributes_outstanding_debts_type_0

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
