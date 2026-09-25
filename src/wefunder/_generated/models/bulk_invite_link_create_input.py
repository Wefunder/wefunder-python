from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.invite_link_create_input import InviteLinkCreateInput





T = TypeVar("T", bound="BulkInviteLinkCreateInput")



@_attrs_define
class BulkInviteLinkCreateInput:
    """ 
        Attributes:
            invite_links (list[InviteLinkCreateInput]): Up to 100 per-person invites. Each item must include `email` or
                `wefunder_user_id`.
     """

    invite_links: list[InviteLinkCreateInput]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.invite_link_create_input import InviteLinkCreateInput # noqa: PLC0415
        invite_links = []
        for invite_links_item_data in self.invite_links:
            invite_links_item = invite_links_item_data.to_dict()
            invite_links.append(invite_links_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "invite_links": invite_links,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invite_link_create_input import InviteLinkCreateInput # noqa: PLC0415
        d = dict(src_dict)
        invite_links = []
        _invite_links = d.pop("invite_links")
        for invite_links_item_data in (_invite_links):
            invite_links_item = InviteLinkCreateInput.from_dict(invite_links_item_data)



            invite_links.append(invite_links_item)


        bulk_invite_link_create_input = cls(
            invite_links=invite_links,
        )


        bulk_invite_link_create_input.additional_properties = d
        return bulk_invite_link_create_input

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
