from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invite_syndicate_member_body_syndicate_permission import InviteSyndicateMemberBodySyndicatePermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="InviteSyndicateMemberBody")


@_attrs_define
class InviteSyndicateMemberBody:
    """
    Attributes:
        email (str):  Example: jane@example.com.
        name (str | Unset): Display name for the invitee
        syndicate_permission (InviteSyndicateMemberBodySyndicatePermission | Unset): Permission level. Only the
            syndicate creator can assign full_access (admin). Default:
            InviteSyndicateMemberBodySyndicatePermission.OPERATOR.
    """

    email: str
    name: str | Unset = UNSET
    syndicate_permission: InviteSyndicateMemberBodySyndicatePermission | Unset = (
        InviteSyndicateMemberBodySyndicatePermission.OPERATOR
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name = self.name

        syndicate_permission: str | Unset = UNSET
        if not isinstance(self.syndicate_permission, Unset):
            syndicate_permission = self.syndicate_permission.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if syndicate_permission is not UNSET:
            field_dict["syndicate_permission"] = syndicate_permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        name = d.pop("name", UNSET)

        _syndicate_permission = d.pop("syndicate_permission", UNSET)
        syndicate_permission: InviteSyndicateMemberBodySyndicatePermission | Unset
        if isinstance(_syndicate_permission, Unset):
            syndicate_permission = UNSET
        else:
            syndicate_permission = InviteSyndicateMemberBodySyndicatePermission(_syndicate_permission)

        invite_syndicate_member_body = cls(
            email=email,
            name=name,
            syndicate_permission=syndicate_permission,
        )

        invite_syndicate_member_body.additional_properties = d
        return invite_syndicate_member_body

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
