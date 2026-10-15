from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.syndicate_deal_readiness_envelope_data_type import SyndicateDealReadinessEnvelopeDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.syndicate_deal_readiness_envelope_data_attributes import SyndicateDealReadinessEnvelopeDataAttributes


T = TypeVar("T", bound="SyndicateDealReadinessEnvelopeData")


@_attrs_define
class SyndicateDealReadinessEnvelopeData:
    """
    Attributes:
        id (str | Unset): The deal's `ofr_` id. Example: ofr_yw3OhusvpfJP4Pk3wRYV1F2R.
        type_ (SyndicateDealReadinessEnvelopeDataType | Unset):
        attributes (SyndicateDealReadinessEnvelopeDataAttributes | Unset):
    """

    id: str | Unset = UNSET
    type_: SyndicateDealReadinessEnvelopeDataType | Unset = UNSET
    attributes: SyndicateDealReadinessEnvelopeDataAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.syndicate_deal_readiness_envelope_data_attributes import (
            SyndicateDealReadinessEnvelopeDataAttributes,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SyndicateDealReadinessEnvelopeDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SyndicateDealReadinessEnvelopeDataType(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: SyndicateDealReadinessEnvelopeDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = SyndicateDealReadinessEnvelopeDataAttributes.from_dict(_attributes)

        syndicate_deal_readiness_envelope_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        syndicate_deal_readiness_envelope_data.additional_properties = d
        return syndicate_deal_readiness_envelope_data

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
