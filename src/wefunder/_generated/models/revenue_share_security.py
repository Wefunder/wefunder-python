from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.revenue_share_security_type import RevenueShareSecurityType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.revenue_share_security_terms import RevenueShareSecurityTerms





T = TypeVar("T", bound="RevenueShareSecurity")



@_attrs_define
class RevenueShareSecurity:
    """ 
        Attributes:
            type_ (RevenueShareSecurityType | Unset):
            label (str | Unset):  Example: Revenue Share.
            terms (RevenueShareSecurityTerms | Unset):
     """

    type_: RevenueShareSecurityType | Unset = UNSET
    label: str | Unset = UNSET
    terms: RevenueShareSecurityTerms | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.revenue_share_security_terms import RevenueShareSecurityTerms # noqa: PLC0415
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        label = self.label

        terms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.terms, Unset):
            terms = self.terms.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if label is not UNSET:
            field_dict["label"] = label
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.revenue_share_security_terms import RevenueShareSecurityTerms # noqa: PLC0415
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RevenueShareSecurityType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = RevenueShareSecurityType(_type_)




        label = d.pop("label", UNSET)

        _terms = d.pop("terms", UNSET)
        terms: RevenueShareSecurityTerms | Unset
        if isinstance(_terms,  Unset):
            terms = UNSET
        else:
            terms = RevenueShareSecurityTerms.from_dict(_terms)




        revenue_share_security = cls(
            type_=type_,
            label=label,
            terms=terms,
        )


        revenue_share_security.additional_properties = d
        return revenue_share_security

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
