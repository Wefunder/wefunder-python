from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_cohort_investors import ReferralCohortInvestors


T = TypeVar("T", bound="ReferralCohort")


@_attrs_define
class ReferralCohort:
    """
    Attributes:
        week (str | Unset): ISO week, Monday to Sunday UTC. Example: 2026-W42.
        investors (ReferralCohortInvestors | Unset): Unique investors referred that week, as a range. Never exact.
        policy_version (int | Unset):  Example: 1.
        published_at (datetime.datetime | Unset):  Example: 2026-10-19T06:05:00Z.
    """

    week: str | Unset = UNSET
    investors: ReferralCohortInvestors | Unset = UNSET
    policy_version: int | Unset = UNSET
    published_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        week = self.week

        investors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.investors, Unset):
            investors = self.investors.to_dict()

        policy_version = self.policy_version

        published_at: str | Unset = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if week is not UNSET:
            field_dict["week"] = week
        if investors is not UNSET:
            field_dict["investors"] = investors
        if policy_version is not UNSET:
            field_dict["policy_version"] = policy_version
        if published_at is not UNSET:
            field_dict["published_at"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.referral_cohort_investors import ReferralCohortInvestors  # noqa: PLC0415

        d = dict(src_dict)
        week = d.pop("week", UNSET)

        _investors = d.pop("investors", UNSET)
        investors: ReferralCohortInvestors | Unset
        if isinstance(_investors, Unset):
            investors = UNSET
        else:
            investors = ReferralCohortInvestors.from_dict(_investors)

        policy_version = d.pop("policy_version", UNSET)

        _published_at = d.pop("published_at", UNSET)
        published_at: datetime.datetime | Unset
        if isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = datetime.datetime.fromisoformat(_published_at)

        referral_cohort = cls(
            week=week,
            investors=investors,
            policy_version=policy_version,
            published_at=published_at,
        )

        referral_cohort.additional_properties = d
        return referral_cohort

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
