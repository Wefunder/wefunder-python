from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="InstallationTokenEnvelopeToken")



@_attrs_define
class InstallationTokenEnvelopeToken:
    """ Shown once. Owned by the installed-on company or syndicate, scoped to the install, no expiry; revoking the install
    revokes it.

        Attributes:
            access_token (str | Unset):  Example: at_live_….
            token_type (str | Unset):  Example: Bearer.
            scope (str | Unset):
            installation (str | Unset): `inst_…`
            created_at (int | Unset):
     """

    access_token: str | Unset = UNSET
    token_type: str | Unset = UNSET
    scope: str | Unset = UNSET
    installation: str | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        token_type = self.token_type

        scope = self.scope

        installation = self.installation

        created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if scope is not UNSET:
            field_dict["scope"] = scope
        if installation is not UNSET:
            field_dict["installation"] = installation
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token", UNSET)

        token_type = d.pop("token_type", UNSET)

        scope = d.pop("scope", UNSET)

        installation = d.pop("installation", UNSET)

        created_at = d.pop("created_at", UNSET)

        installation_token_envelope_token = cls(
            access_token=access_token,
            token_type=token_type,
            scope=scope,
            installation=installation,
            created_at=created_at,
        )


        installation_token_envelope_token.additional_properties = d
        return installation_token_envelope_token

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
