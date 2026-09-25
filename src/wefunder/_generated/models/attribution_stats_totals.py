from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributionStatsTotals")


@_attrs_define
class AttributionStatsTotals:
    """
    Attributes:
        investment_count (int | Unset): Total number of attributed investments Example: 142.
        total_amount (float | Unset): Total dollar amount of attributed investments Example: 425000.
        unique_investors (int | Unset): Count of unique investors Example: 138.
        conversion_rate (float | Unset): UTM clicks to investments (percentage) Example: 3.08.
    """

    investment_count: int | Unset = UNSET
    total_amount: float | Unset = UNSET
    unique_investors: int | Unset = UNSET
    conversion_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        investment_count = self.investment_count

        total_amount = self.total_amount

        unique_investors = self.unique_investors

        conversion_rate = self.conversion_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if investment_count is not UNSET:
            field_dict["investment_count"] = investment_count
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount
        if unique_investors is not UNSET:
            field_dict["unique_investors"] = unique_investors
        if conversion_rate is not UNSET:
            field_dict["conversion_rate"] = conversion_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        investment_count = d.pop("investment_count", UNSET)

        total_amount = d.pop("total_amount", UNSET)

        unique_investors = d.pop("unique_investors", UNSET)

        conversion_rate = d.pop("conversion_rate", UNSET)

        attribution_stats_totals = cls(
            investment_count=investment_count,
            total_amount=total_amount,
            unique_investors=unique_investors,
            conversion_rate=conversion_rate,
        )

        attribution_stats_totals.additional_properties = d
        return attribution_stats_totals

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
