from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_code_stats_company import ReferralCodeStatsCompany


T = TypeVar("T", bound="ReferralCodeStatsEnvelopeDataAttributes")


@_attrs_define
class ReferralCodeStatsEnvelopeDataAttributes:
    """
    Attributes:
        visits (int | Unset):  Example: 412.
        unique_visitors (int | Unset):  Example: 388.
        visits_as_of (datetime.date | Unset): The last full UTC day the visit numbers include. Example: 2026-10-12.
        label (str | Unset):  Example: October newsletter.
        companies (list[ReferralCodeStatsCompany] | Unset):
    """

    visits: int | Unset = UNSET
    unique_visitors: int | Unset = UNSET
    visits_as_of: datetime.date | Unset = UNSET
    label: str | Unset = UNSET
    companies: list[ReferralCodeStatsCompany] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visits = self.visits

        unique_visitors = self.unique_visitors

        visits_as_of: str | Unset = UNSET
        if not isinstance(self.visits_as_of, Unset):
            visits_as_of = self.visits_as_of.isoformat()

        label = self.label

        companies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.companies, Unset):
            companies = []
            for companies_item_data in self.companies:
                companies_item = companies_item_data.to_dict()
                companies.append(companies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if visits is not UNSET:
            field_dict["visits"] = visits
        if unique_visitors is not UNSET:
            field_dict["unique_visitors"] = unique_visitors
        if visits_as_of is not UNSET:
            field_dict["visits_as_of"] = visits_as_of
        if label is not UNSET:
            field_dict["label"] = label
        if companies is not UNSET:
            field_dict["companies"] = companies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.referral_code_stats_company import ReferralCodeStatsCompany  # noqa: PLC0415

        d = dict(src_dict)
        visits = d.pop("visits", UNSET)

        unique_visitors = d.pop("unique_visitors", UNSET)

        _visits_as_of = d.pop("visits_as_of", UNSET)
        visits_as_of: datetime.date | Unset
        if isinstance(_visits_as_of, Unset):
            visits_as_of = UNSET
        else:
            visits_as_of = datetime.date.fromisoformat(_visits_as_of)

        label = d.pop("label", UNSET)

        _companies = d.pop("companies", UNSET)
        companies: list[ReferralCodeStatsCompany] | Unset = UNSET
        if _companies is not UNSET:
            companies = []
            for companies_item_data in _companies:
                companies_item = ReferralCodeStatsCompany.from_dict(companies_item_data)

                companies.append(companies_item)

        referral_code_stats_envelope_data_attributes = cls(
            visits=visits,
            unique_visitors=unique_visitors,
            visits_as_of=visits_as_of,
            label=label,
            companies=companies,
        )

        referral_code_stats_envelope_data_attributes.additional_properties = d
        return referral_code_stats_envelope_data_attributes

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
