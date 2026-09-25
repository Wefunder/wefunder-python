from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.portfolio_position_type import PortfolioPositionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.portfolio_position_attributes import PortfolioPositionAttributes





T = TypeVar("T", bound="PortfolioPosition")



@_attrs_define
class PortfolioPosition:
    """ One position per offering (fundraise). On the investor endpoint the totals
    sum the authenticated investor's stakes; on the syndicate endpoint they sum
    every holder's stakes and `investor_count` is present.

        Attributes:
            id (str | Unset): The offering's id (`ofr_...`) — a position's identity is its offering. Example:
                ofr_9aKxQ2vF8mNp1zT5wY7Qb3Cd.
            type_ (PortfolioPositionType | Unset):
            attributes (PortfolioPositionAttributes | Unset):
     """

    id: str | Unset = UNSET
    type_: PortfolioPositionType | Unset = UNSET
    attributes: PortfolioPositionAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.portfolio_position_attributes import PortfolioPositionAttributes # noqa: PLC0415
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portfolio_position_attributes import PortfolioPositionAttributes # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PortfolioPositionType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = PortfolioPositionType(_type_)




        _attributes = d.pop("attributes", UNSET)
        attributes: PortfolioPositionAttributes | Unset
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = PortfolioPositionAttributes.from_dict(_attributes)




        portfolio_position = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )


        portfolio_position.additional_properties = d
        return portfolio_position

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
