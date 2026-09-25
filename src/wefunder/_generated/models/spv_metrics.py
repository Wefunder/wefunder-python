from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpvMetrics")


@_attrs_define
class SpvMetrics:
    """
    Attributes:
        total_raised_cents (int | Unset):  Example: 5000000.
        investor_count (int | Unset): Investors with an active investment in this SPV. Example: 12.
        documented_soft_cap (int | Unset): The documented per-SPV investor soft cap (247). Advisory only — it is not
            enforced, and `investor_count` may exceed it. Example: 247.
        confirmed_count (int | Unset):  Example: 8.
        pending_count (int | Unset):  Example: 4.
        average_investment_cents (int | Unset):  Example: 416666.
    """

    total_raised_cents: int | Unset = UNSET
    investor_count: int | Unset = UNSET
    documented_soft_cap: int | Unset = UNSET
    confirmed_count: int | Unset = UNSET
    pending_count: int | Unset = UNSET
    average_investment_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_raised_cents = self.total_raised_cents

        investor_count = self.investor_count

        documented_soft_cap = self.documented_soft_cap

        confirmed_count = self.confirmed_count

        pending_count = self.pending_count

        average_investment_cents = self.average_investment_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_raised_cents is not UNSET:
            field_dict["total_raised_cents"] = total_raised_cents
        if investor_count is not UNSET:
            field_dict["investor_count"] = investor_count
        if documented_soft_cap is not UNSET:
            field_dict["documented_soft_cap"] = documented_soft_cap
        if confirmed_count is not UNSET:
            field_dict["confirmed_count"] = confirmed_count
        if pending_count is not UNSET:
            field_dict["pending_count"] = pending_count
        if average_investment_cents is not UNSET:
            field_dict["average_investment_cents"] = average_investment_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_raised_cents = d.pop("total_raised_cents", UNSET)

        investor_count = d.pop("investor_count", UNSET)

        documented_soft_cap = d.pop("documented_soft_cap", UNSET)

        confirmed_count = d.pop("confirmed_count", UNSET)

        pending_count = d.pop("pending_count", UNSET)

        average_investment_cents = d.pop("average_investment_cents", UNSET)

        spv_metrics = cls(
            total_raised_cents=total_raised_cents,
            investor_count=investor_count,
            documented_soft_cap=documented_soft_cap,
            confirmed_count=confirmed_count,
            pending_count=pending_count,
            average_investment_cents=average_investment_cents,
        )

        spv_metrics.additional_properties = d
        return spv_metrics

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
