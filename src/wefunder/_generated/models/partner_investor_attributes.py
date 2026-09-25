from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerInvestorAttributes")


@_attrs_define
class PartnerInvestorAttributes:
    """
    Attributes:
        full_name (None | str | Unset):  Example: Ada Lovelace.
        email (None | str | Unset):  Example: ada@example.com.
        accredited (bool | Unset):  Example: True.
        total_invested_cents (int | Unset): Sum of the investor's active investments in this SPV. Example: 500000.
        investment_count (int | Unset):  Example: 2.
        created_at (datetime.datetime | None | Unset): When the investor first invested in this SPV. Example:
            2025-01-15T12:00:00Z.
    """

    full_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    accredited: bool | Unset = UNSET
    total_invested_cents: int | Unset = UNSET
    investment_count: int | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        accredited = self.accredited

        total_invested_cents = self.total_invested_cents

        investment_count = self.investment_count

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if email is not UNSET:
            field_dict["email"] = email
        if accredited is not UNSET:
            field_dict["accredited"] = accredited
        if total_invested_cents is not UNSET:
            field_dict["total_invested_cents"] = total_invested_cents
        if investment_count is not UNSET:
            field_dict["investment_count"] = investment_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        accredited = d.pop("accredited", UNSET)

        total_invested_cents = d.pop("total_invested_cents", UNSET)

        investment_count = d.pop("investment_count", UNSET)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        partner_investor_attributes = cls(
            full_name=full_name,
            email=email,
            accredited=accredited,
            total_invested_cents=total_invested_cents,
            investment_count=investment_count,
            created_at=created_at,
        )

        partner_investor_attributes.additional_properties = d
        return partner_investor_attributes

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
