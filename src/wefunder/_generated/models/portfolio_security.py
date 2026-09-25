from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.portfolio_security_owner_type_0 import PortfolioSecurityOwnerType0
  from ..models.portfolio_security_terms import PortfolioSecurityTerms
  from ..models.security_summary import SecuritySummary





T = TypeVar("T", bound="PortfolioSecurity")



@_attrs_define
class PortfolioSecurity:
    """ One security offering within the position's fundraise, such as an early bird
    tier or the regular terms. Most positions have a single entry. A position has
    several when the round sold multiple tiers, or (investor endpoint) when the
    investor holds the same offering through more than one legal owner. Entries
    do not have ids; each is described by its `terms`, and occasionally a round
    has more than one offering record with identical terms.

        Attributes:
            security (None | SecuritySummary | Unset): What this tier issues, as `{ type, label }` (the terms are in `terms`
                below).
                May be null on legacy offerings — fall back to the position-level `security`.
            early_bird (bool | Unset):
            terms (PortfolioSecurityTerms | Unset): The offering's issue terms. Fields are null when the term does not apply
                to the security type.
            cost_basis_cents (int | Unset):
            current_value_cents (int | Unset):
            unrealized_gain_cents (int | Unset):
            realized_gain_cents (int | Unset):
            shares_held (None | str | Unset): Decimal string. Null for non-share structures and multiple-of-basis
                valuations.
            current_share_price (None | str | Unset): Decimal string, split-adjusted.
            invested_at (datetime.datetime | None | Unset):
            owner (None | PortfolioSecurityOwnerType0 | Unset): The legal owner of this stake — `{"kind": "individual"}` for
                personally-held stakes, `{"kind": "entity", "name": "..."}` for stakes
                held through the investor's own entity (IRA, LLC). Present on the
                investor endpoint only.
            investor_count (int | Unset): The number of distinct investors aggregated into this entry. Present on the
                syndicate endpoint only.
     """

    security: None | SecuritySummary | Unset = UNSET
    early_bird: bool | Unset = UNSET
    terms: PortfolioSecurityTerms | Unset = UNSET
    cost_basis_cents: int | Unset = UNSET
    current_value_cents: int | Unset = UNSET
    unrealized_gain_cents: int | Unset = UNSET
    realized_gain_cents: int | Unset = UNSET
    shares_held: None | str | Unset = UNSET
    current_share_price: None | str | Unset = UNSET
    invested_at: datetime.datetime | None | Unset = UNSET
    owner: None | PortfolioSecurityOwnerType0 | Unset = UNSET
    investor_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.portfolio_security_owner_type_0 import PortfolioSecurityOwnerType0 # noqa: PLC0415
        from ..models.portfolio_security_terms import PortfolioSecurityTerms # noqa: PLC0415
        from ..models.security_summary import SecuritySummary # noqa: PLC0415
        security: dict[str, Any] | None | Unset
        if isinstance(self.security, Unset):
            security = UNSET
        elif isinstance(self.security, SecuritySummary):
            security = self.security.to_dict()
        else:
            security = self.security

        early_bird = self.early_bird

        terms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.terms, Unset):
            terms = self.terms.to_dict()

        cost_basis_cents = self.cost_basis_cents

        current_value_cents = self.current_value_cents

        unrealized_gain_cents = self.unrealized_gain_cents

        realized_gain_cents = self.realized_gain_cents

        shares_held: None | str | Unset
        if isinstance(self.shares_held, Unset):
            shares_held = UNSET
        else:
            shares_held = self.shares_held

        current_share_price: None | str | Unset
        if isinstance(self.current_share_price, Unset):
            current_share_price = UNSET
        else:
            current_share_price = self.current_share_price

        invested_at: None | str | Unset
        if isinstance(self.invested_at, Unset):
            invested_at = UNSET
        elif isinstance(self.invested_at, datetime.datetime):
            invested_at = self.invested_at.isoformat()
        else:
            invested_at = self.invested_at

        owner: dict[str, Any] | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        elif isinstance(self.owner, PortfolioSecurityOwnerType0):
            owner = self.owner.to_dict()
        else:
            owner = self.owner

        investor_count = self.investor_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if security is not UNSET:
            field_dict["security"] = security
        if early_bird is not UNSET:
            field_dict["early_bird"] = early_bird
        if terms is not UNSET:
            field_dict["terms"] = terms
        if cost_basis_cents is not UNSET:
            field_dict["cost_basis_cents"] = cost_basis_cents
        if current_value_cents is not UNSET:
            field_dict["current_value_cents"] = current_value_cents
        if unrealized_gain_cents is not UNSET:
            field_dict["unrealized_gain_cents"] = unrealized_gain_cents
        if realized_gain_cents is not UNSET:
            field_dict["realized_gain_cents"] = realized_gain_cents
        if shares_held is not UNSET:
            field_dict["shares_held"] = shares_held
        if current_share_price is not UNSET:
            field_dict["current_share_price"] = current_share_price
        if invested_at is not UNSET:
            field_dict["invested_at"] = invested_at
        if owner is not UNSET:
            field_dict["owner"] = owner
        if investor_count is not UNSET:
            field_dict["investor_count"] = investor_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portfolio_security_owner_type_0 import PortfolioSecurityOwnerType0 # noqa: PLC0415
        from ..models.portfolio_security_terms import PortfolioSecurityTerms # noqa: PLC0415
        from ..models.security_summary import SecuritySummary # noqa: PLC0415
        d = dict(src_dict)
        def _parse_security(data: object) -> None | SecuritySummary | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                security_type_1 = SecuritySummary.from_dict(data)



                return security_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SecuritySummary | Unset, data)

        security = _parse_security(d.pop("security", UNSET))


        early_bird = d.pop("early_bird", UNSET)

        _terms = d.pop("terms", UNSET)
        terms: PortfolioSecurityTerms | Unset
        if isinstance(_terms,  Unset):
            terms = UNSET
        else:
            terms = PortfolioSecurityTerms.from_dict(_terms)




        cost_basis_cents = d.pop("cost_basis_cents", UNSET)

        current_value_cents = d.pop("current_value_cents", UNSET)

        unrealized_gain_cents = d.pop("unrealized_gain_cents", UNSET)

        realized_gain_cents = d.pop("realized_gain_cents", UNSET)

        def _parse_shares_held(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shares_held = _parse_shares_held(d.pop("shares_held", UNSET))


        def _parse_current_share_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_share_price = _parse_current_share_price(d.pop("current_share_price", UNSET))


        def _parse_invested_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invested_at_type_0 = datetime.datetime.fromisoformat(data)



                return invested_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        invested_at = _parse_invested_at(d.pop("invested_at", UNSET))


        def _parse_owner(data: object) -> None | PortfolioSecurityOwnerType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                owner_type_0 = PortfolioSecurityOwnerType0.from_dict(data)



                return owner_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PortfolioSecurityOwnerType0 | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))


        investor_count = d.pop("investor_count", UNSET)

        portfolio_security = cls(
            security=security,
            early_bird=early_bird,
            terms=terms,
            cost_basis_cents=cost_basis_cents,
            current_value_cents=current_value_cents,
            unrealized_gain_cents=unrealized_gain_cents,
            realized_gain_cents=realized_gain_cents,
            shares_held=shares_held,
            current_share_price=current_share_price,
            invested_at=invested_at,
            owner=owner,
            investor_count=investor_count,
        )


        portfolio_security.additional_properties = d
        return portfolio_security

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
