from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferralCodeVisits")


@_attrs_define
class ReferralCodeVisits:
    """
    Attributes:
        visits (int | Unset):  Example: 412.
        unique_visitors (int | Unset):  Example: 388.
        visits_as_of (datetime.date | Unset): The last full UTC day the visit numbers include. Example: 2026-10-12.
    """

    visits: int | Unset = UNSET
    unique_visitors: int | Unset = UNSET
    visits_as_of: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visits = self.visits

        unique_visitors = self.unique_visitors

        visits_as_of: str | Unset = UNSET
        if not isinstance(self.visits_as_of, Unset):
            visits_as_of = self.visits_as_of.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if visits is not UNSET:
            field_dict["visits"] = visits
        if unique_visitors is not UNSET:
            field_dict["unique_visitors"] = unique_visitors
        if visits_as_of is not UNSET:
            field_dict["visits_as_of"] = visits_as_of

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        visits = d.pop("visits", UNSET)

        unique_visitors = d.pop("unique_visitors", UNSET)

        _visits_as_of = d.pop("visits_as_of", UNSET)
        visits_as_of: datetime.date | Unset
        if isinstance(_visits_as_of, Unset):
            visits_as_of = UNSET
        else:
            visits_as_of = datetime.date.fromisoformat(_visits_as_of)

        referral_code_visits = cls(
            visits=visits,
            unique_visitors=unique_visitors,
            visits_as_of=visits_as_of,
        )

        referral_code_visits.additional_properties = d
        return referral_code_visits

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
