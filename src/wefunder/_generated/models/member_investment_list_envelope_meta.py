from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MemberInvestmentListEnvelopeMeta")



@_attrs_define
class MemberInvestmentListEnvelopeMeta:
    """ 
        Attributes:
            count (int | Unset): Number of investments
            total_amount (str | Unset): Sum of all investment amounts in cents, as a string Example: 800000.
     """

    count: int | Unset = UNSET
    total_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        total_amount = self.total_amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        total_amount = d.pop("total_amount", UNSET)

        member_investment_list_envelope_meta = cls(
            count=count,
            total_amount=total_amount,
        )


        member_investment_list_envelope_meta.additional_properties = d
        return member_investment_list_envelope_meta

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
