from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_investment_attributes_status import MemberInvestmentAttributesStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberInvestmentAttributes")


@_attrs_define
class MemberInvestmentAttributes:
    """
    Attributes:
        fundraise_id (int | Unset): Internal integer id. Deprecated — use `offering` (`ofr_...`) instead. Example:
            75496.
        offering (None | str | Unset): The deal's id (`ofr_...`), accepted by the deal endpoints. Example:
            ofr_8Kd0aB3xQ9k2vF8mNp1zT5wY.
        company_name (None | str | Unset): Name of the company the deal is for Example: Substack.
        amount (str | Unset): Investment amount in whole dollars, as a string Example: 5000.
        status (MemberInvestmentAttributesStatus | Unset): `confirmed` is final; `pending` is committed but not yet
            final. Example: confirmed.
        created_at (datetime.datetime | Unset): ISO 8601 timestamp when the investment was created Example:
            2025-03-01T12:00:00Z.
    """

    fundraise_id: int | Unset = UNSET
    offering: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    amount: str | Unset = UNSET
    status: MemberInvestmentAttributesStatus | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fundraise_id = self.fundraise_id

        offering: None | str | Unset
        if isinstance(self.offering, Unset):
            offering = UNSET
        else:
            offering = self.offering

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        amount = self.amount

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fundraise_id is not UNSET:
            field_dict["fundraise_id"] = fundraise_id
        if offering is not UNSET:
            field_dict["offering"] = offering
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fundraise_id = d.pop("fundraise_id", UNSET)

        def _parse_offering(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        offering = _parse_offering(d.pop("offering", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        amount = d.pop("amount", UNSET)

        _status = d.pop("status", UNSET)
        status: MemberInvestmentAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MemberInvestmentAttributesStatus(_status)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        member_investment_attributes = cls(
            fundraise_id=fundraise_id,
            offering=offering,
            company_name=company_name,
            amount=amount,
            status=status,
            created_at=created_at,
        )

        member_investment_attributes.additional_properties = d
        return member_investment_attributes

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
