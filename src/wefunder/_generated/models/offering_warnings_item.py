from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.offering_warnings_item_code import OfferingWarningsItemCode
from ..types import UNSET, Unset






T = TypeVar("T", bound="OfferingWarningsItem")



@_attrs_define
class OfferingWarningsItem:
    """ 
        Attributes:
            code (OfferingWarningsItemCode | Unset):  Example: prior_rounds.
            message (str | Unset):  Example: This company completed 2 earlier rounds on Wefunder. amount_raised and
                investor_count cover this offering only, not the company's lifetime total..
     """

    code: OfferingWarningsItemCode | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code: str | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value


        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _code = d.pop("code", UNSET)
        code: OfferingWarningsItemCode | Unset
        if isinstance(_code,  Unset):
            code = UNSET
        else:
            code = OfferingWarningsItemCode(_code)




        message = d.pop("message", UNSET)

        offering_warnings_item = cls(
            code=code,
            message=message,
        )


        offering_warnings_item.additional_properties = d
        return offering_warnings_item

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
