from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MyCompanyAttributes")


@_attrs_define
class MyCompanyAttributes:
    """
    Attributes:
        name (str | Unset):  Example: Acme Robotics.
        tagline (None | str | Unset):
        url (None | str | Unset): The company's Wefunder page. Example: https://wefunder.com/acme.
        roles (list[str] | Unset): The user's roles on this company. Example: ['founder'].
        raising (bool | Unset): True when a round is currently accepting investments or reservations.
    """

    name: str | Unset = UNSET
    tagline: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    roles: list[str] | Unset = UNSET
    raising: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        tagline: None | str | Unset
        if isinstance(self.tagline, Unset):
            tagline = UNSET
        else:
            tagline = self.tagline

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        raising = self.raising

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if url is not UNSET:
            field_dict["url"] = url
        if roles is not UNSET:
            field_dict["roles"] = roles
        if raising is not UNSET:
            field_dict["raising"] = raising

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_tagline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tagline = _parse_tagline(d.pop("tagline", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        roles = cast(list[str], d.pop("roles", UNSET))

        raising = d.pop("raising", UNSET)

        my_company_attributes = cls(
            name=name,
            tagline=tagline,
            url=url,
            roles=roles,
            raising=raising,
        )

        my_company_attributes.additional_properties = d
        return my_company_attributes

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
