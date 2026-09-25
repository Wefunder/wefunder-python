from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.eligible_target_list_envelope_data_item_type import EligibleTargetListEnvelopeDataItemType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.installation import Installation





T = TypeVar("T", bound="EligibleTargetListEnvelopeDataItem")



@_attrs_define
class EligibleTargetListEnvelopeDataItem:
    """ 
        Attributes:
            type_ (EligibleTargetListEnvelopeDataItemType | Unset):
            id (str | Unset):
            name (str | Unset):
            tier (str | Unset): The tier an install would be granted at.
            installed (bool | Unset):
            installation (Installation | None | Unset):
     """

    type_: EligibleTargetListEnvelopeDataItemType | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    tier: str | Unset = UNSET
    installed: bool | Unset = UNSET
    installation: Installation | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.installation import Installation # noqa: PLC0415
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        id = self.id

        name = self.name

        tier = self.tier

        installed = self.installed

        installation: dict[str, Any] | None | Unset
        if isinstance(self.installation, Unset):
            installation = UNSET
        elif isinstance(self.installation, Installation):
            installation = self.installation.to_dict()
        else:
            installation = self.installation


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if tier is not UNSET:
            field_dict["tier"] = tier
        if installed is not UNSET:
            field_dict["installed"] = installed
        if installation is not UNSET:
            field_dict["installation"] = installation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation import Installation # noqa: PLC0415
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: EligibleTargetListEnvelopeDataItemType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = EligibleTargetListEnvelopeDataItemType(_type_)




        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        tier = d.pop("tier", UNSET)

        installed = d.pop("installed", UNSET)

        def _parse_installation(data: object) -> Installation | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                installation_type_1 = Installation.from_dict(data)



                return installation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Installation | None | Unset, data)

        installation = _parse_installation(d.pop("installation", UNSET))


        eligible_target_list_envelope_data_item = cls(
            type_=type_,
            id=id,
            name=name,
            tier=tier,
            installed=installed,
            installation=installation,
        )


        eligible_target_list_envelope_data_item.additional_properties = d
        return eligible_target_list_envelope_data_item

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
