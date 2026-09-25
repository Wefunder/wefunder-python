from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConnectedAppRevocation")



@_attrs_define
class ConnectedAppRevocation:
    """ 
        Attributes:
            revoked (bool | Unset):  Example: True.
            tokens_revoked (int | Unset):  Example: 2.
     """

    revoked: bool | Unset = UNSET
    tokens_revoked: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        revoked = self.revoked

        tokens_revoked = self.tokens_revoked


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if revoked is not UNSET:
            field_dict["revoked"] = revoked
        if tokens_revoked is not UNSET:
            field_dict["tokens_revoked"] = tokens_revoked

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revoked = d.pop("revoked", UNSET)

        tokens_revoked = d.pop("tokens_revoked", UNSET)

        connected_app_revocation = cls(
            revoked=revoked,
            tokens_revoked=tokens_revoked,
        )


        connected_app_revocation.additional_properties = d
        return connected_app_revocation

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
