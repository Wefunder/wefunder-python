from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AttributionCampaignSummary")



@_attrs_define
class AttributionCampaignSummary:
    """ 
        Attributes:
            id (int | Unset):  Example: 123.
            company_name (str | Unset):  Example: Example Name.
            company_id (int | Unset):  Example: 123.
            state (str | Unset):  Example: active.
            access_level (int | Unset): 1=anonymized, 2=detailed (future) Example: 1.
     """

    id: int | Unset = UNSET
    company_name: str | Unset = UNSET
    company_id: int | Unset = UNSET
    state: str | Unset = UNSET
    access_level: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_name = self.company_name

        company_id = self.company_id

        state = self.state

        access_level = self.access_level


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if state is not UNSET:
            field_dict["state"] = state
        if access_level is not UNSET:
            field_dict["access_level"] = access_level

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        company_name = d.pop("company_name", UNSET)

        company_id = d.pop("company_id", UNSET)

        state = d.pop("state", UNSET)

        access_level = d.pop("access_level", UNSET)

        attribution_campaign_summary = cls(
            id=id,
            company_name=company_name,
            company_id=company_id,
            state=state,
            access_level=access_level,
        )


        attribution_campaign_summary.additional_properties = d
        return attribution_campaign_summary

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
