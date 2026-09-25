from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SyndicatePortfolioSummaryEnvelopeDataAttributesDealCounts")



@_attrs_define
class SyndicatePortfolioSummaryEnvelopeDataAttributesDealCounts:
    """ Distinct deals per status.

        Attributes:
            active (int | Unset):
            exited (int | Unset):
            sold (int | Unset):
            failed (int | Unset):
     """

    active: int | Unset = UNSET
    exited: int | Unset = UNSET
    sold: int | Unset = UNSET
    failed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        active = self.active

        exited = self.exited

        sold = self.sold

        failed = self.failed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if active is not UNSET:
            field_dict["active"] = active
        if exited is not UNSET:
            field_dict["exited"] = exited
        if sold is not UNSET:
            field_dict["sold"] = sold
        if failed is not UNSET:
            field_dict["failed"] = failed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        exited = d.pop("exited", UNSET)

        sold = d.pop("sold", UNSET)

        failed = d.pop("failed", UNSET)

        syndicate_portfolio_summary_envelope_data_attributes_deal_counts = cls(
            active=active,
            exited=exited,
            sold=sold,
            failed=failed,
        )


        syndicate_portfolio_summary_envelope_data_attributes_deal_counts.additional_properties = d
        return syndicate_portfolio_summary_envelope_data_attributes_deal_counts

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
