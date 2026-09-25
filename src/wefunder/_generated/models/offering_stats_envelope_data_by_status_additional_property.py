from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfferingStatsEnvelopeDataByStatusAdditionalProperty")



@_attrs_define
class OfferingStatsEnvelopeDataByStatusAdditionalProperty:
    """ 
        Attributes:
            count (int | Unset):
            committed_cents (int | Unset):
            raised_cents (int | Unset):
     """

    count: int | Unset = UNSET
    committed_cents: int | Unset = UNSET
    raised_cents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        committed_cents = self.committed_cents

        raised_cents = self.raised_cents


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if committed_cents is not UNSET:
            field_dict["committed_cents"] = committed_cents
        if raised_cents is not UNSET:
            field_dict["raised_cents"] = raised_cents

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        committed_cents = d.pop("committed_cents", UNSET)

        raised_cents = d.pop("raised_cents", UNSET)

        offering_stats_envelope_data_by_status_additional_property = cls(
            count=count,
            committed_cents=committed_cents,
            raised_cents=raised_cents,
        )


        offering_stats_envelope_data_by_status_additional_property.additional_properties = d
        return offering_stats_envelope_data_by_status_additional_property

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
