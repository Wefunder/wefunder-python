from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvestmentDeltaRecordAmounts")


@_attrs_define
class InvestmentDeltaRecordAmounts:
    """
    Attributes:
        committed_cents (int | Unset):
        investment_size_cents (int | Unset):
        in_escrow_cents (int | Unset):
        raised_cents (int | Unset): What this investment contributes to the offering's public raised figure (the deal
            page, company card and directory header). Equals `investment_size_cents` once the investment is soft-confirmed;
            0 until then (see `needs_whitelisting`). Summing `raised_cents` over an offering's records reproduces the site's
            number; summing `committed_cents` does not.
        currency (str | Unset):  Example: usd.
    """

    committed_cents: int | Unset = UNSET
    investment_size_cents: int | Unset = UNSET
    in_escrow_cents: int | Unset = UNSET
    raised_cents: int | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        committed_cents = self.committed_cents

        investment_size_cents = self.investment_size_cents

        in_escrow_cents = self.in_escrow_cents

        raised_cents = self.raised_cents

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if committed_cents is not UNSET:
            field_dict["committed_cents"] = committed_cents
        if investment_size_cents is not UNSET:
            field_dict["investment_size_cents"] = investment_size_cents
        if in_escrow_cents is not UNSET:
            field_dict["in_escrow_cents"] = in_escrow_cents
        if raised_cents is not UNSET:
            field_dict["raised_cents"] = raised_cents
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        committed_cents = d.pop("committed_cents", UNSET)

        investment_size_cents = d.pop("investment_size_cents", UNSET)

        in_escrow_cents = d.pop("in_escrow_cents", UNSET)

        raised_cents = d.pop("raised_cents", UNSET)

        currency = d.pop("currency", UNSET)

        investment_delta_record_amounts = cls(
            committed_cents=committed_cents,
            investment_size_cents=investment_size_cents,
            in_escrow_cents=in_escrow_cents,
            raised_cents=raised_cents,
            currency=currency,
        )

        investment_delta_record_amounts.additional_properties = d
        return investment_delta_record_amounts

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
