from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.member_link_create_input import MemberLinkCreateInput


T = TypeVar("T", bound="CreateOfferingMemberLinkBody")


@_attrs_define
class CreateOfferingMemberLinkBody:
    """
    Attributes:
        member_link (MemberLinkCreateInput | Unset):
    """

    member_link: MemberLinkCreateInput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.member_link, Unset):
            member_link = self.member_link.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if member_link is not UNSET:
            field_dict["member_link"] = member_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.member_link_create_input import MemberLinkCreateInput  # noqa: PLC0415

        d = dict(src_dict)
        _member_link = d.pop("member_link", UNSET)
        member_link: MemberLinkCreateInput | Unset
        if isinstance(_member_link, Unset):
            member_link = UNSET
        else:
            member_link = MemberLinkCreateInput.from_dict(_member_link)

        create_offering_member_link_body = cls(
            member_link=member_link,
        )

        create_offering_member_link_body.additional_properties = d
        return create_offering_member_link_body

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
