from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_installation_body_target_type import CreateInstallationBodyTargetType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreateInstallationBody")



@_attrs_define
class CreateInstallationBody:
    """ 
        Attributes:
            target_type (CreateInstallationBodyTargetType):
            target_id (str): The company (`co_…`) or syndicate (`syn_…`) external id.
            scopes (list[str] | Unset): Subset of the app's declared scopes to grant. Defaults to all of them.
            tier (str | Unset): Optional higher tier (`founder` / `full_access`), honored only when the caller holds it.
     """

    target_type: CreateInstallationBodyTargetType
    target_id: str
    scopes: list[str] | Unset = UNSET
    tier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type.value

        target_id = self.target_id

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes



        tier = self.tier


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "target_type": target_type,
            "target_id": target_id,
        })
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if tier is not UNSET:
            field_dict["tier"] = tier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_type = CreateInstallationBodyTargetType(d.pop("target_type"))




        target_id = d.pop("target_id")

        scopes = cast(list[str], d.pop("scopes", UNSET))


        tier = d.pop("tier", UNSET)

        create_installation_body = cls(
            target_type=target_type,
            target_id=target_id,
            scopes=scopes,
            tier=tier,
        )


        create_installation_body.additional_properties = d
        return create_installation_body

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
