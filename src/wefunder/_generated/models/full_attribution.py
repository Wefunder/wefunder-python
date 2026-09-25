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
  from ..models.full_attribution_attribution import FullAttributionAttribution
  from ..models.full_attribution_investor import FullAttributionInvestor
  from ..models.full_attribution_status import FullAttributionStatus





T = TypeVar("T", bound="FullAttribution")



@_attrs_define
class FullAttribution:
    """ Full attribution data with investor PII (Tier 2 - founders only).
    Returned when detail_level=full is requested by an authorized founder.

        Attributes:
            investment_id (int | Unset): Real Wefunder investment ID Example: 12345.
            investment_token (str | Unset): Opaque token (same as anonymized response) Example:
                inv_abc123xyz789def456uvw012ghi345.
            investor (FullAttributionInvestor | Unset): Full investor details
            amount (float | Unset): Exact investment amount in dollars Example: 5000.
            invested_at (datetime.datetime | Unset):  Example: 2025-02-15T14:30:00Z.
            status (FullAttributionStatus | Unset):
            attribution (FullAttributionAttribution | Unset): UTM attribution data (same as anonymized)
     """

    investment_id: int | Unset = UNSET
    investment_token: str | Unset = UNSET
    investor: FullAttributionInvestor | Unset = UNSET
    amount: float | Unset = UNSET
    invested_at: datetime.datetime | Unset = UNSET
    status: FullAttributionStatus | Unset = UNSET
    attribution: FullAttributionAttribution | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.full_attribution_attribution import FullAttributionAttribution # noqa: PLC0415
        from ..models.full_attribution_investor import FullAttributionInvestor # noqa: PLC0415
        from ..models.full_attribution_status import FullAttributionStatus # noqa: PLC0415
        investment_id = self.investment_id

        investment_token = self.investment_token

        investor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.investor, Unset):
            investor = self.investor.to_dict()

        amount = self.amount

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
        if investment_id is not UNSET:
            field_dict["investment_id"] = investment_id
        if investment_token is not UNSET:
            field_dict["investment_token"] = investment_token
        if investor is not UNSET:
            field_dict["investor"] = investor
        if amount is not UNSET:
            field_dict["amount"] = amount
        if invested_at is not UNSET:
            field_dict["invested_at"] = invested_at
        if status is not UNSET:
            field_dict["status"] = status
        if attribution is not UNSET:
            field_dict["attribution"] = attribution

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.full_attribution_attribution import FullAttributionAttribution # noqa: PLC0415
        from ..models.full_attribution_investor import FullAttributionInvestor # noqa: PLC0415
        from ..models.full_attribution_status import FullAttributionStatus # noqa: PLC0415
        d = dict(src_dict)
        investment_id = d.pop("investment_id", UNSET)

        investment_token = d.pop("investment_token", UNSET)

        _investor = d.pop("investor", UNSET)
        investor: FullAttributionInvestor | Unset
        if isinstance(_investor,  Unset):
            investor = UNSET
        else:
            investor = FullAttributionInvestor.from_dict(_investor)




        amount = d.pop("amount", UNSET)

        _invested_at = d.pop("invested_at", UNSET)
        invested_at: datetime.datetime | Unset
        if isinstance(_invested_at,  Unset):
            invested_at = UNSET
        else:
            invested_at = datetime.datetime.fromisoformat(_invested_at)




        _status = d.pop("status", UNSET)
        status: FullAttributionStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = FullAttributionStatus.from_dict(_status)




        _attribution = d.pop("attribution", UNSET)
        attribution: FullAttributionAttribution | Unset
        if isinstance(_attribution,  Unset):
            attribution = UNSET
        else:
            attribution = FullAttributionAttribution.from_dict(_attribution)




        full_attribution = cls(
            investment_id=investment_id,
            investment_token=investment_token,
            investor=investor,
            amount=amount,
            invested_at=invested_at,
            status=status,
            attribution=attribution,
        )


        full_attribution.additional_properties = d
        return full_attribution

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
