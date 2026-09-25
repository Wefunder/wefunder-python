from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AttributionStatsByCampaignItem")



@_attrs_define
class AttributionStatsByCampaignItem:
    """ 
        Attributes:
            utm_campaign (str | Unset):  Example: winter_2025.
            investment_count (int | Unset):  Example: 47.
            total_amount (float | Unset):  Example: 142500.
     """

    utm_campaign: str | Unset = UNSET
    investment_count: int | Unset = UNSET
    total_amount: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        utm_campaign = self.utm_campaign

        investment_count = self.investment_count

        total_amount = self.total_amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if utm_campaign is not UNSET:
            field_dict["utm_campaign"] = utm_campaign
        if investment_count is not UNSET:
            field_dict["investment_count"] = investment_count
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        utm_campaign = d.pop("utm_campaign", UNSET)

        investment_count = d.pop("investment_count", UNSET)

        total_amount = d.pop("total_amount", UNSET)

        attribution_stats_by_campaign_item = cls(
            utm_campaign=utm_campaign,
            investment_count=investment_count,
            total_amount=total_amount,
        )


        attribution_stats_by_campaign_item.additional_properties = d
        return attribution_stats_by_campaign_item

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
