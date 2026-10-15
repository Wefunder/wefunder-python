from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.referral_code_stats_company_level import ReferralCodeStatsCompanyLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_code_stats_company_investments_item import ReferralCodeStatsCompanyInvestmentsItem
    from ..models.referral_cohort import ReferralCohort


T = TypeVar("T", bound="ReferralCodeStatsCompany")


@_attrs_define
class ReferralCodeStatsCompany:
    """
    Attributes:
        company (str | Unset):  Example: co_7hQExampleCompany0001.
        level (ReferralCodeStatsCompanyLevel | Unset): What your app may see for this company, from its installation on
            it.
        verification_url (str | Unset): Where the company's founders verify referrals in their own dashboard. Example:
            https://wefunder.com/acme/marketing/reports#partners.
        in_scope_since (str | Unset): Counts level only. The first week this company has cells for. Example: 2026-W42.
        weeks (list[ReferralCohort] | Unset): Counts level only. Every completed week since in_scope_since.
        investments (list[ReferralCodeStatsCompanyInvestmentsItem] | Unset): Anonymized or full level only, replacing
            `weeks`. Anonymized rows carry opaque
            `investment` and `investor` tokens, `week`, `amount_tier`, `status` and
            `time_to_invest`; full rows carry the investment id, the investor's name and email,
            the exact `amount`, `status`, `clicked_at`, `applied_at` and the UTM attribution.
        investments_next_cursor (int | Unset): Present when the company has more rows; pass it as `investments_cursor`
            with `company_id`.
    """

    company: str | Unset = UNSET
    level: ReferralCodeStatsCompanyLevel | Unset = UNSET
    verification_url: str | Unset = UNSET
    in_scope_since: str | Unset = UNSET
    weeks: list[ReferralCohort] | Unset = UNSET
    investments: list[ReferralCodeStatsCompanyInvestmentsItem] | Unset = UNSET
    investments_next_cursor: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company = self.company

        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        verification_url = self.verification_url

        in_scope_since = self.in_scope_since

        weeks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.weeks, Unset):
            weeks = []
            for weeks_item_data in self.weeks:
                weeks_item = weeks_item_data.to_dict()
                weeks.append(weeks_item)

        investments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.investments, Unset):
            investments = []
            for investments_item_data in self.investments:
                investments_item = investments_item_data.to_dict()
                investments.append(investments_item)

        investments_next_cursor = self.investments_next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company is not UNSET:
            field_dict["company"] = company
        if level is not UNSET:
            field_dict["level"] = level
        if verification_url is not UNSET:
            field_dict["verification_url"] = verification_url
        if in_scope_since is not UNSET:
            field_dict["in_scope_since"] = in_scope_since
        if weeks is not UNSET:
            field_dict["weeks"] = weeks
        if investments is not UNSET:
            field_dict["investments"] = investments
        if investments_next_cursor is not UNSET:
            field_dict["investments_next_cursor"] = investments_next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.referral_code_stats_company_investments_item import (
            ReferralCodeStatsCompanyInvestmentsItem,  # noqa: PLC0415
        )
        from ..models.referral_cohort import ReferralCohort  # noqa: PLC0415

        d = dict(src_dict)
        company = d.pop("company", UNSET)

        _level = d.pop("level", UNSET)
        level: ReferralCodeStatsCompanyLevel | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = ReferralCodeStatsCompanyLevel(_level)

        verification_url = d.pop("verification_url", UNSET)

        in_scope_since = d.pop("in_scope_since", UNSET)

        _weeks = d.pop("weeks", UNSET)
        weeks: list[ReferralCohort] | Unset = UNSET
        if _weeks is not UNSET:
            weeks = []
            for weeks_item_data in _weeks:
                weeks_item = ReferralCohort.from_dict(weeks_item_data)

                weeks.append(weeks_item)

        _investments = d.pop("investments", UNSET)
        investments: list[ReferralCodeStatsCompanyInvestmentsItem] | Unset = UNSET
        if _investments is not UNSET:
            investments = []
            for investments_item_data in _investments:
                investments_item = ReferralCodeStatsCompanyInvestmentsItem.from_dict(investments_item_data)

                investments.append(investments_item)

        investments_next_cursor = d.pop("investments_next_cursor", UNSET)

        referral_code_stats_company = cls(
            company=company,
            level=level,
            verification_url=verification_url,
            in_scope_since=in_scope_since,
            weeks=weeks,
            investments=investments,
            investments_next_cursor=investments_next_cursor,
        )

        referral_code_stats_company.additional_properties = d
        return referral_code_stats_company

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
