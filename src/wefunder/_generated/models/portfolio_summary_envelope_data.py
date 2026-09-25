from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portfolio_summary_envelope_data_attributes import PortfolioSummaryEnvelopeDataAttributes


T = TypeVar("T", bound="PortfolioSummaryEnvelopeData")


@_attrs_define
class PortfolioSummaryEnvelopeData:
    """
    Attributes:
        type_ (str | Unset):  Example: portfolio_summary.
        attributes (PortfolioSummaryEnvelopeDataAttributes | Unset):
    """

    type_: str | Unset = UNSET
    attributes: PortfolioSummaryEnvelopeDataAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portfolio_summary_envelope_data_attributes import (
            PortfolioSummaryEnvelopeDataAttributes,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: PortfolioSummaryEnvelopeDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = PortfolioSummaryEnvelopeDataAttributes.from_dict(_attributes)

        portfolio_summary_envelope_data = cls(
            type_=type_,
            attributes=attributes,
        )

        portfolio_summary_envelope_data.additional_properties = d
        return portfolio_summary_envelope_data

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
