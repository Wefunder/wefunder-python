from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyndicateAttributesAnnualSubscription")


@_attrs_define
class SyndicateAttributesAnnualSubscription:
    """Present only when `syndicate_type` is `annual_subscription`.

    Attributes:
        fund_investment_amount (None | str | Unset):
        deals_per_year (int | None | Unset):
        amount_per_deal (None | str | Unset):
    """

    fund_investment_amount: None | str | Unset = UNSET
    deals_per_year: int | None | Unset = UNSET
    amount_per_deal: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fund_investment_amount: None | str | Unset
        if isinstance(self.fund_investment_amount, Unset):
            fund_investment_amount = UNSET
        else:
            fund_investment_amount = self.fund_investment_amount

        deals_per_year: int | None | Unset
        if isinstance(self.deals_per_year, Unset):
            deals_per_year = UNSET
        else:
            deals_per_year = self.deals_per_year

        amount_per_deal: None | str | Unset
        if isinstance(self.amount_per_deal, Unset):
            amount_per_deal = UNSET
        else:
            amount_per_deal = self.amount_per_deal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fund_investment_amount is not UNSET:
            field_dict["fund_investment_amount"] = fund_investment_amount
        if deals_per_year is not UNSET:
            field_dict["deals_per_year"] = deals_per_year
        if amount_per_deal is not UNSET:
            field_dict["amount_per_deal"] = amount_per_deal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_fund_investment_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fund_investment_amount = _parse_fund_investment_amount(d.pop("fund_investment_amount", UNSET))

        def _parse_deals_per_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        deals_per_year = _parse_deals_per_year(d.pop("deals_per_year", UNSET))

        def _parse_amount_per_deal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount_per_deal = _parse_amount_per_deal(d.pop("amount_per_deal", UNSET))

        syndicate_attributes_annual_subscription = cls(
            fund_investment_amount=fund_investment_amount,
            deals_per_year=deals_per_year,
            amount_per_deal=amount_per_deal,
        )

        syndicate_attributes_annual_subscription.additional_properties = d
        return syndicate_attributes_annual_subscription

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
