from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_code_stats_envelope_data import ReferralCodeStatsEnvelopeData
    from ..models.referral_code_stats_envelope_meta import ReferralCodeStatsEnvelopeMeta


T = TypeVar("T", bound="ReferralCodeStatsEnvelope")


@_attrs_define
class ReferralCodeStatsEnvelope:
    """
    Attributes:
        data (ReferralCodeStatsEnvelopeData | Unset):
        meta (ReferralCodeStatsEnvelopeMeta | Unset):
    """

    data: ReferralCodeStatsEnvelopeData | Unset = UNSET
    meta: ReferralCodeStatsEnvelopeMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.referral_code_stats_envelope_data import ReferralCodeStatsEnvelopeData  # noqa: PLC0415
        from ..models.referral_code_stats_envelope_meta import ReferralCodeStatsEnvelopeMeta  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ReferralCodeStatsEnvelopeData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ReferralCodeStatsEnvelopeData.from_dict(_data)

        _meta = d.pop("meta", UNSET)
        meta: ReferralCodeStatsEnvelopeMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ReferralCodeStatsEnvelopeMeta.from_dict(_meta)

        referral_code_stats_envelope = cls(
            data=data,
            meta=meta,
        )

        referral_code_stats_envelope.additional_properties = d
        return referral_code_stats_envelope

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
