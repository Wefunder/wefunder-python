from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FiscalYearFinancials")



@_attrs_define
class FiscalYearFinancials:
    """ One fiscal year's figures from the Form C, USD decimal strings (null where not reported).

        Attributes:
            total_assets (None | str | Unset):
            cash_and_equivalents (None | str | Unset):
            accounts_receivable (None | str | Unset):
            short_term_debt (None | str | Unset):
            long_term_debt (None | str | Unset):
            revenue (None | str | Unset):
            cost_of_goods_sold (None | str | Unset):
            taxes_paid (None | str | Unset):
            net_income (None | str | Unset):
     """

    total_assets: None | str | Unset = UNSET
    cash_and_equivalents: None | str | Unset = UNSET
    accounts_receivable: None | str | Unset = UNSET
    short_term_debt: None | str | Unset = UNSET
    long_term_debt: None | str | Unset = UNSET
    revenue: None | str | Unset = UNSET
    cost_of_goods_sold: None | str | Unset = UNSET
    taxes_paid: None | str | Unset = UNSET
    net_income: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total_assets: None | str | Unset
        if isinstance(self.total_assets, Unset):
            total_assets = UNSET
        else:
            total_assets = self.total_assets

        cash_and_equivalents: None | str | Unset
        if isinstance(self.cash_and_equivalents, Unset):
            cash_and_equivalents = UNSET
        else:
            cash_and_equivalents = self.cash_and_equivalents

        accounts_receivable: None | str | Unset
        if isinstance(self.accounts_receivable, Unset):
            accounts_receivable = UNSET
        else:
            accounts_receivable = self.accounts_receivable

        short_term_debt: None | str | Unset
        if isinstance(self.short_term_debt, Unset):
            short_term_debt = UNSET
        else:
            short_term_debt = self.short_term_debt

        long_term_debt: None | str | Unset
        if isinstance(self.long_term_debt, Unset):
            long_term_debt = UNSET
        else:
            long_term_debt = self.long_term_debt

        revenue: None | str | Unset
        if isinstance(self.revenue, Unset):
            revenue = UNSET
        else:
            revenue = self.revenue

        cost_of_goods_sold: None | str | Unset
        if isinstance(self.cost_of_goods_sold, Unset):
            cost_of_goods_sold = UNSET
        else:
            cost_of_goods_sold = self.cost_of_goods_sold

        taxes_paid: None | str | Unset
        if isinstance(self.taxes_paid, Unset):
            taxes_paid = UNSET
        else:
            taxes_paid = self.taxes_paid

        net_income: None | str | Unset
        if isinstance(self.net_income, Unset):
            net_income = UNSET
        else:
            net_income = self.net_income


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total_assets is not UNSET:
            field_dict["total_assets"] = total_assets
        if cash_and_equivalents is not UNSET:
            field_dict["cash_and_equivalents"] = cash_and_equivalents
        if accounts_receivable is not UNSET:
            field_dict["accounts_receivable"] = accounts_receivable
        if short_term_debt is not UNSET:
            field_dict["short_term_debt"] = short_term_debt
        if long_term_debt is not UNSET:
            field_dict["long_term_debt"] = long_term_debt
        if revenue is not UNSET:
            field_dict["revenue"] = revenue
        if cost_of_goods_sold is not UNSET:
            field_dict["cost_of_goods_sold"] = cost_of_goods_sold
        if taxes_paid is not UNSET:
            field_dict["taxes_paid"] = taxes_paid
        if net_income is not UNSET:
            field_dict["net_income"] = net_income

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_total_assets(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_assets = _parse_total_assets(d.pop("total_assets", UNSET))


        def _parse_cash_and_equivalents(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cash_and_equivalents = _parse_cash_and_equivalents(d.pop("cash_and_equivalents", UNSET))


        def _parse_accounts_receivable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accounts_receivable = _parse_accounts_receivable(d.pop("accounts_receivable", UNSET))


        def _parse_short_term_debt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_term_debt = _parse_short_term_debt(d.pop("short_term_debt", UNSET))


        def _parse_long_term_debt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long_term_debt = _parse_long_term_debt(d.pop("long_term_debt", UNSET))


        def _parse_revenue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revenue = _parse_revenue(d.pop("revenue", UNSET))


        def _parse_cost_of_goods_sold(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_of_goods_sold = _parse_cost_of_goods_sold(d.pop("cost_of_goods_sold", UNSET))


        def _parse_taxes_paid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        taxes_paid = _parse_taxes_paid(d.pop("taxes_paid", UNSET))


        def _parse_net_income(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        net_income = _parse_net_income(d.pop("net_income", UNSET))


        fiscal_year_financials = cls(
            total_assets=total_assets,
            cash_and_equivalents=cash_and_equivalents,
            accounts_receivable=accounts_receivable,
            short_term_debt=short_term_debt,
            long_term_debt=long_term_debt,
            revenue=revenue,
            cost_of_goods_sold=cost_of_goods_sold,
            taxes_paid=taxes_paid,
            net_income=net_income,
        )


        fiscal_year_financials.additional_properties = d
        return fiscal_year_financials

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
