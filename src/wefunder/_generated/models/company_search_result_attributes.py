from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanySearchResultAttributes")


@_attrs_define
class CompanySearchResultAttributes:
    """
    Attributes:
        name (None | str | Unset):  Example: Acme Robotics.
        tagline (None | str | Unset):
        url (None | str | Unset): The company's Wefunder page. Example: https://wefunder.com/acme.
        logo_url (None | str | Unset):
        raising (bool | Unset): True when the company is raising now (the site's "Raising Now" badge). False means the
            site shows its "Funded" badge, which it also shows for companies with no live round
            (including ones whose last round was aborted); it is not a statement that a raise closed
            successfully.
        profile_available (bool | Unset): Whether `GET /companies/{id}` will serve this company to this viewer. Since
            the company
            page serves every publicly listed profile, this is false only for an index hit whose
            live row no longer clears the site's bar (or an accredited-only company seen without
            accreditation). Link to `url` when false.
    """

    name: None | str | Unset = UNSET
    tagline: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    raising: bool | Unset = UNSET
    profile_available: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
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

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        raising = self.raising

        profile_available = self.profile_available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if url is not UNSET:
            field_dict["url"] = url
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if raising is not UNSET:
            field_dict["raising"] = raising
        if profile_available is not UNSET:
            field_dict["profile_available"] = profile_available

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        raising = d.pop("raising", UNSET)

        profile_available = d.pop("profile_available", UNSET)

        company_search_result_attributes = cls(
            name=name,
            tagline=tagline,
            url=url,
            logo_url=logo_url,
            raising=raising,
            profile_available=profile_available,
        )

        company_search_result_attributes.additional_properties = d
        return company_search_result_attributes

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
