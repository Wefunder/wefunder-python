from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortfolioSecurityTerms")


@_attrs_define
class PortfolioSecurityTerms:
    """The offering's issue terms. A field is null when the term does not apply to the security type, and also when the
    security has none: an uncapped SAFE or note has a null `note_cap_cents` (with `uncapped: true`), and a security with
    no discount, including one recorded as zero, has a null `note_discount`.

        Attributes:
            share_price (None | str | Unset): Issue price per share as a decimal string Example: 10.0.
            currency (str | Unset): Lower-case ISO 4217 code of `note_cap_cents` and `premoney_valuation_cents`, the
                currency the founder entered them in. USD when the round's terms are explicitly USD-denominated (checkout prices
                them in USD then); otherwise a SAFE's cap is in the round's declared financials currency (falling back to the
                round's), while equity pre-money and a convertible note's valuation are in the round currency. A EUR-funded SAFE
                can therefore carry a `usd` or `dkk` cap. `share_price` and every other `_cents` field on the position stay in
                the position's top-level `currency`. Example: usd.
            note_cap_cents (int | None | Unset): The valuation cap of a SAFE or convertible note, in cents of
                `terms.currency`. Null when the security is uncapped (see `uncapped`) or has no cap.
            uncapped (bool | None | Unset): `true` when a SAFE or convertible note has no valuation cap, `false` when it has
                one. Null for securities that never carry a cap (equity, revenue share, debt, fund, other). Same rule as
                `uncapped` in an offering's `security.terms`. Example: False.
            note_discount (None | str | Unset): Conversion discount as a decimal string percentage (`"20.0"` is 20%). Null
                when there is no discount, including a discount recorded as zero, the same as `discount_percent` in an
                offering's `security.terms`. Example: 20.0.
            premoney_valuation_cents (int | None | Unset):
    """

    share_price: None | str | Unset = UNSET
    currency: str | Unset = UNSET
    note_cap_cents: int | None | Unset = UNSET
    uncapped: bool | None | Unset = UNSET
    note_discount: None | str | Unset = UNSET
    premoney_valuation_cents: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        share_price: None | str | Unset
        if isinstance(self.share_price, Unset):
            share_price = UNSET
        else:
            share_price = self.share_price

        currency = self.currency

        note_cap_cents: int | None | Unset
        if isinstance(self.note_cap_cents, Unset):
            note_cap_cents = UNSET
        else:
            note_cap_cents = self.note_cap_cents

        uncapped: bool | None | Unset
        if isinstance(self.uncapped, Unset):
            uncapped = UNSET
        else:
            uncapped = self.uncapped

        note_discount: None | str | Unset
        if isinstance(self.note_discount, Unset):
            note_discount = UNSET
        else:
            note_discount = self.note_discount

        premoney_valuation_cents: int | None | Unset
        if isinstance(self.premoney_valuation_cents, Unset):
            premoney_valuation_cents = UNSET
        else:
            premoney_valuation_cents = self.premoney_valuation_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if share_price is not UNSET:
            field_dict["share_price"] = share_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if note_cap_cents is not UNSET:
            field_dict["note_cap_cents"] = note_cap_cents
        if uncapped is not UNSET:
            field_dict["uncapped"] = uncapped
        if note_discount is not UNSET:
            field_dict["note_discount"] = note_discount
        if premoney_valuation_cents is not UNSET:
            field_dict["premoney_valuation_cents"] = premoney_valuation_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_share_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        share_price = _parse_share_price(d.pop("share_price", UNSET))

        currency = d.pop("currency", UNSET)

        def _parse_note_cap_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        note_cap_cents = _parse_note_cap_cents(d.pop("note_cap_cents", UNSET))

        def _parse_uncapped(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        uncapped = _parse_uncapped(d.pop("uncapped", UNSET))

        def _parse_note_discount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note_discount = _parse_note_discount(d.pop("note_discount", UNSET))

        def _parse_premoney_valuation_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        premoney_valuation_cents = _parse_premoney_valuation_cents(d.pop("premoney_valuation_cents", UNSET))

        portfolio_security_terms = cls(
            share_price=share_price,
            currency=currency,
            note_cap_cents=note_cap_cents,
            uncapped=uncapped,
            note_discount=note_discount,
            premoney_valuation_cents=premoney_valuation_cents,
        )

        portfolio_security_terms.additional_properties = d
        return portfolio_security_terms

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
