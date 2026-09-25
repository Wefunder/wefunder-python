from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AttributionStatsQualityBreakdown")



@_attrs_define
class AttributionStatsQualityBreakdown:
    """ Attribution quality metrics

        Attributes:
            direct (int | Unset): Conversions within 1 hour of click Example: 98.
            assisted (int | Unset): Conversions 1-24 hours after click Example: 35.
            delayed (int | Unset): Conversions over 24 hours after click Example: 9.
     """

    direct: int | Unset = UNSET
    assisted: int | Unset = UNSET
    delayed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        direct = self.direct

        assisted = self.assisted

        delayed = self.delayed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if direct is not UNSET:
            field_dict["direct"] = direct
        if assisted is not UNSET:
            field_dict["assisted"] = assisted
        if delayed is not UNSET:
            field_dict["delayed"] = delayed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        direct = d.pop("direct", UNSET)

        assisted = d.pop("assisted", UNSET)

        delayed = d.pop("delayed", UNSET)

        attribution_stats_quality_breakdown = cls(
            direct=direct,
            assisted=assisted,
            delayed=delayed,
        )


        attribution_stats_quality_breakdown.additional_properties = d
        return attribution_stats_quality_breakdown

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
