from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CompanyDisclosuresAttributesRatiosType0")



@_attrs_define
class CompanyDisclosuresAttributesRatiosType0:
    """ The page's at-a-glance ratios for the most recent fiscal year, percentages as decimal strings; null where the page
    shows N/A, or the whole block null when hidden for this company.

        Attributes:
            net_margin_percent (None | str | Unset): Net income / revenue × 100.
            gross_margin_percent (None | str | Unset): (Revenue − cost of goods sold) / revenue × 100.
            return_on_assets_percent (None | str | Unset): Net income / total assets × 100.
            debt_to_assets_percent (None | str | Unset): (Short-term + long-term debt) / total assets × 100.
            cash_to_assets_percent (None | str | Unset): Cash / total assets × 100.
            revenue_per_employee (None | str | Unset): USD, decimal string.
     """

    net_margin_percent: None | str | Unset = UNSET
    gross_margin_percent: None | str | Unset = UNSET
    return_on_assets_percent: None | str | Unset = UNSET
    debt_to_assets_percent: None | str | Unset = UNSET
    cash_to_assets_percent: None | str | Unset = UNSET
    revenue_per_employee: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        net_margin_percent: None | str | Unset
        if isinstance(self.net_margin_percent, Unset):
            net_margin_percent = UNSET
        else:
            net_margin_percent = self.net_margin_percent

        gross_margin_percent: None | str | Unset
        if isinstance(self.gross_margin_percent, Unset):
            gross_margin_percent = UNSET
        else:
            gross_margin_percent = self.gross_margin_percent

        return_on_assets_percent: None | str | Unset
        if isinstance(self.return_on_assets_percent, Unset):
            return_on_assets_percent = UNSET
        else:
            return_on_assets_percent = self.return_on_assets_percent

        debt_to_assets_percent: None | str | Unset
        if isinstance(self.debt_to_assets_percent, Unset):
            debt_to_assets_percent = UNSET
        else:
            debt_to_assets_percent = self.debt_to_assets_percent

        cash_to_assets_percent: None | str | Unset
        if isinstance(self.cash_to_assets_percent, Unset):
            cash_to_assets_percent = UNSET
        else:
            cash_to_assets_percent = self.cash_to_assets_percent

        revenue_per_employee: None | str | Unset
        if isinstance(self.revenue_per_employee, Unset):
            revenue_per_employee = UNSET
        else:
            revenue_per_employee = self.revenue_per_employee


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if net_margin_percent is not UNSET:
            field_dict["net_margin_percent"] = net_margin_percent
        if gross_margin_percent is not UNSET:
            field_dict["gross_margin_percent"] = gross_margin_percent
        if return_on_assets_percent is not UNSET:
            field_dict["return_on_assets_percent"] = return_on_assets_percent
        if debt_to_assets_percent is not UNSET:
            field_dict["debt_to_assets_percent"] = debt_to_assets_percent
        if cash_to_assets_percent is not UNSET:
            field_dict["cash_to_assets_percent"] = cash_to_assets_percent
        if revenue_per_employee is not UNSET:
            field_dict["revenue_per_employee"] = revenue_per_employee

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_net_margin_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        net_margin_percent = _parse_net_margin_percent(d.pop("net_margin_percent", UNSET))


        def _parse_gross_margin_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gross_margin_percent = _parse_gross_margin_percent(d.pop("gross_margin_percent", UNSET))


        def _parse_return_on_assets_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_on_assets_percent = _parse_return_on_assets_percent(d.pop("return_on_assets_percent", UNSET))


        def _parse_debt_to_assets_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        debt_to_assets_percent = _parse_debt_to_assets_percent(d.pop("debt_to_assets_percent", UNSET))


        def _parse_cash_to_assets_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cash_to_assets_percent = _parse_cash_to_assets_percent(d.pop("cash_to_assets_percent", UNSET))


        def _parse_revenue_per_employee(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revenue_per_employee = _parse_revenue_per_employee(d.pop("revenue_per_employee", UNSET))


        company_disclosures_attributes_ratios_type_0 = cls(
            net_margin_percent=net_margin_percent,
            gross_margin_percent=gross_margin_percent,
            return_on_assets_percent=return_on_assets_percent,
            debt_to_assets_percent=debt_to_assets_percent,
            cash_to_assets_percent=cash_to_assets_percent,
            revenue_per_employee=revenue_per_employee,
        )


        company_disclosures_attributes_ratios_type_0.additional_properties = d
        return company_disclosures_attributes_ratios_type_0

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
