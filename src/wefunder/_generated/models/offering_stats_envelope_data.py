from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offering_stats_envelope_data_by_status import OfferingStatsEnvelopeDataByStatus
    from ..models.offering_stats_envelope_data_total import OfferingStatsEnvelopeDataTotal


T = TypeVar("T", bound="OfferingStatsEnvelopeData")


@_attrs_define
class OfferingStatsEnvelopeData:
    """
    Attributes:
        offering (str | Unset):
        company (str | Unset):
        currency (None | str | Unset):
        by_status (OfferingStatsEnvelopeDataByStatus | Unset):
        total (OfferingStatsEnvelopeDataTotal | Unset):
    """

    offering: str | Unset = UNSET
    company: str | Unset = UNSET
    currency: None | str | Unset = UNSET
    by_status: OfferingStatsEnvelopeDataByStatus | Unset = UNSET
    total: OfferingStatsEnvelopeDataTotal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offering = self.offering

        company = self.company

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        by_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_status, Unset):
            by_status = self.by_status.to_dict()

        total: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offering is not UNSET:
            field_dict["offering"] = offering
        if company is not UNSET:
            field_dict["company"] = company
        if currency is not UNSET:
            field_dict["currency"] = currency
        if by_status is not UNSET:
            field_dict["by_status"] = by_status
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_stats_envelope_data_by_status import OfferingStatsEnvelopeDataByStatus  # noqa: PLC0415
        from ..models.offering_stats_envelope_data_total import OfferingStatsEnvelopeDataTotal  # noqa: PLC0415

        d = dict(src_dict)
        offering = d.pop("offering", UNSET)

        company = d.pop("company", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        _by_status = d.pop("by_status", UNSET)
        by_status: OfferingStatsEnvelopeDataByStatus | Unset
        if isinstance(_by_status, Unset):
            by_status = UNSET
        else:
            by_status = OfferingStatsEnvelopeDataByStatus.from_dict(_by_status)

        _total = d.pop("total", UNSET)
        total: OfferingStatsEnvelopeDataTotal | Unset
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = OfferingStatsEnvelopeDataTotal.from_dict(_total)

        offering_stats_envelope_data = cls(
            offering=offering,
            company=company,
            currency=currency,
            by_status=by_status,
            total=total,
        )

        offering_stats_envelope_data.additional_properties = d
        return offering_stats_envelope_data

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
