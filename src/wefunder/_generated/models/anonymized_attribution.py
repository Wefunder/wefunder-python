from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.anonymized_attribution_amount_tier import AnonymizedAttributionAmountTier
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.anonymized_attribution_attribution import AnonymizedAttributionAttribution
  from ..models.anonymized_attribution_status import AnonymizedAttributionStatus





T = TypeVar("T", bound="AnonymizedAttribution")



@_attrs_define
class AnonymizedAttribution:
    """ An attributed investment with anonymized investor data.
    No PII is exposed - investor identity is represented by opaque tokens.

        Attributes:
            investment_token (str | Unset): Opaque token identifying the investment (32 characters) Example:
                inv_abc123xyz789def456uvw012ghi345.
            investor_token (str | Unset): Opaque token identifying the investor (32 characters).
                Same investor gets different tokens for different campaigns.
                 Example: usr_def456uvw789abc123xyz012ghi345.
            amount_tier (AnonymizedAttributionAmountTier | Unset): Investment amount tier (not exact value).
                Ranges: small ($1-999), medium ($1,000-9,999), large ($10,000+)
                 Example: medium.
            invested_at (datetime.datetime | Unset): When the investment was applied Example: 2025-02-15T14:30:00Z.
            status (AnonymizedAttributionStatus | Unset): Current investment status
            attribution (AnonymizedAttributionAttribution | Unset): UTM attribution data
     """

    investment_token: str | Unset = UNSET
    investor_token: str | Unset = UNSET
    amount_tier: AnonymizedAttributionAmountTier | Unset = UNSET
    invested_at: datetime.datetime | Unset = UNSET
    status: AnonymizedAttributionStatus | Unset = UNSET
    attribution: AnonymizedAttributionAttribution | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.anonymized_attribution_attribution import AnonymizedAttributionAttribution # noqa: PLC0415
        from ..models.anonymized_attribution_status import AnonymizedAttributionStatus # noqa: PLC0415
        investment_token = self.investment_token

        investor_token = self.investor_token

        amount_tier: str | Unset = UNSET
        if not isinstance(self.amount_tier, Unset):
            amount_tier = self.amount_tier.value


        invested_at: str | Unset = UNSET
        if not isinstance(self.invested_at, Unset):
            invested_at = self.invested_at.isoformat()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        attribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attribution, Unset):
            attribution = self.attribution.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if investment_token is not UNSET:
            field_dict["investment_token"] = investment_token
        if investor_token is not UNSET:
            field_dict["investor_token"] = investor_token
        if amount_tier is not UNSET:
            field_dict["amount_tier"] = amount_tier
        if invested_at is not UNSET:
            field_dict["invested_at"] = invested_at
        if status is not UNSET:
            field_dict["status"] = status
        if attribution is not UNSET:
            field_dict["attribution"] = attribution

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.anonymized_attribution_attribution import AnonymizedAttributionAttribution # noqa: PLC0415
        from ..models.anonymized_attribution_status import AnonymizedAttributionStatus # noqa: PLC0415
        d = dict(src_dict)
        investment_token = d.pop("investment_token", UNSET)

        investor_token = d.pop("investor_token", UNSET)

        _amount_tier = d.pop("amount_tier", UNSET)
        amount_tier: AnonymizedAttributionAmountTier | Unset
        if isinstance(_amount_tier,  Unset):
            amount_tier = UNSET
        else:
            amount_tier = AnonymizedAttributionAmountTier(_amount_tier)




        _invested_at = d.pop("invested_at", UNSET)
        invested_at: datetime.datetime | Unset
        if isinstance(_invested_at,  Unset):
            invested_at = UNSET
        else:
            invested_at = datetime.datetime.fromisoformat(_invested_at)




        _status = d.pop("status", UNSET)
        status: AnonymizedAttributionStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = AnonymizedAttributionStatus.from_dict(_status)




        _attribution = d.pop("attribution", UNSET)
        attribution: AnonymizedAttributionAttribution | Unset
        if isinstance(_attribution,  Unset):
            attribution = UNSET
        else:
            attribution = AnonymizedAttributionAttribution.from_dict(_attribution)




        anonymized_attribution = cls(
            investment_token=investment_token,
            investor_token=investor_token,
            amount_tier=amount_tier,
            invested_at=invested_at,
            status=status,
            attribution=attribution,
        )


        anonymized_attribution.additional_properties = d
        return anonymized_attribution

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
