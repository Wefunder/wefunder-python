from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BulkInviteLinkEnvelopeErrorsItem")



@_attrs_define
class BulkInviteLinkEnvelopeErrorsItem:
    """ 
        Attributes:
            index (int | Unset): Position of the failed item in the request array. Example: 2.
            type_ (str | Unset):  Example: mutually_exclusive_params.
            detail (str | Unset):  Example: provide either email or wefunder_user_id, not both.
     """

    index: int | Unset = UNSET
    type_: str | Unset = UNSET
    detail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        index = self.index

        type_ = self.type_

        detail = self.detail


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if index is not UNSET:
            field_dict["index"] = index
        if type_ is not UNSET:
            field_dict["type"] = type_
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        type_ = d.pop("type", UNSET)

        detail = d.pop("detail", UNSET)

        bulk_invite_link_envelope_errors_item = cls(
            index=index,
            type_=type_,
            detail=detail,
        )


        bulk_invite_link_envelope_errors_item.additional_properties = d
        return bulk_invite_link_envelope_errors_item

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
