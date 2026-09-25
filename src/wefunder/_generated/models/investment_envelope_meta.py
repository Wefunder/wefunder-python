from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.investment_envelope_meta_source import InvestmentEnvelopeMetaSource
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="InvestmentEnvelopeMeta")



@_attrs_define
class InvestmentEnvelopeMeta:
    """ 
        Attributes:
            source (InvestmentEnvelopeMetaSource | Unset):
            published_observed_at (datetime.datetime | None | Unset): `observed_at` of the published record, or null if
                never published.
            published_matches (bool | None | Unset): Whether the published record equals this current one; null if never
                published.
     """

    source: InvestmentEnvelopeMetaSource | Unset = UNSET
    published_observed_at: datetime.datetime | None | Unset = UNSET
    published_matches: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value


        published_observed_at: None | str | Unset
        if isinstance(self.published_observed_at, Unset):
            published_observed_at = UNSET
        elif isinstance(self.published_observed_at, datetime.datetime):
            published_observed_at = self.published_observed_at.isoformat()
        else:
            published_observed_at = self.published_observed_at

        published_matches: bool | None | Unset
        if isinstance(self.published_matches, Unset):
            published_matches = UNSET
        else:
            published_matches = self.published_matches


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if source is not UNSET:
            field_dict["source"] = source
        if published_observed_at is not UNSET:
            field_dict["published_observed_at"] = published_observed_at
        if published_matches is not UNSET:
            field_dict["published_matches"] = published_matches

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _source = d.pop("source", UNSET)
        source: InvestmentEnvelopeMetaSource | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = InvestmentEnvelopeMetaSource(_source)




        def _parse_published_observed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_observed_at_type_0 = datetime.datetime.fromisoformat(data)



                return published_observed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_observed_at = _parse_published_observed_at(d.pop("published_observed_at", UNSET))


        def _parse_published_matches(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        published_matches = _parse_published_matches(d.pop("published_matches", UNSET))


        investment_envelope_meta = cls(
            source=source,
            published_observed_at=published_observed_at,
            published_matches=published_matches,
        )


        investment_envelope_meta.additional_properties = d
        return investment_envelope_meta

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
