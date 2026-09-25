from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.offering_stats_envelope_meta_source import OfferingStatsEnvelopeMetaSource
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfferingStatsEnvelopeMeta")



@_attrs_define
class OfferingStatsEnvelopeMeta:
    """ 
        Attributes:
            source (OfferingStatsEnvelopeMetaSource | Unset):
            published_through (datetime.datetime | None | Unset):
     """

    source: OfferingStatsEnvelopeMetaSource | Unset = UNSET
    published_through: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value


        published_through: None | str | Unset
        if isinstance(self.published_through, Unset):
            published_through = UNSET
        elif isinstance(self.published_through, datetime.datetime):
            published_through = self.published_through.isoformat()
        else:
            published_through = self.published_through


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if source is not UNSET:
            field_dict["source"] = source
        if published_through is not UNSET:
            field_dict["published_through"] = published_through

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _source = d.pop("source", UNSET)
        source: OfferingStatsEnvelopeMetaSource | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = OfferingStatsEnvelopeMetaSource(_source)




        def _parse_published_through(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_through_type_0 = datetime.datetime.fromisoformat(data)



                return published_through_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_through = _parse_published_through(d.pop("published_through", UNSET))


        offering_stats_envelope_meta = cls(
            source=source,
            published_through=published_through,
        )


        offering_stats_envelope_meta.additional_properties = d
        return offering_stats_envelope_meta

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
