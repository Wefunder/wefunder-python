from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="FollowedCompanyAttributes")



@_attrs_define
class FollowedCompanyAttributes:
    """ 
        Attributes:
            name (None | str | Unset):
            tagline (None | str | Unset):
            url (None | str | Unset):
            logo_url (None | str | Unset):
            raising (bool | Unset): True when the company has a round accepting investments right now.
            profile_available (bool | Unset): Whether `GET /companies/{id}` will serve this company to this user.
            followed_at (datetime.datetime | None | Unset):
     """

    name: None | str | Unset = UNSET
    tagline: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    raising: bool | Unset = UNSET
    profile_available: bool | Unset = UNSET
    followed_at: datetime.datetime | None | Unset = UNSET
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

        followed_at: None | str | Unset
        if isinstance(self.followed_at, Unset):
            followed_at = UNSET
        elif isinstance(self.followed_at, datetime.datetime):
            followed_at = self.followed_at.isoformat()
        else:
            followed_at = self.followed_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        if followed_at is not UNSET:
            field_dict["followed_at"] = followed_at

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

        def _parse_followed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                followed_at_type_0 = datetime.datetime.fromisoformat(data)



                return followed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        followed_at = _parse_followed_at(d.pop("followed_at", UNSET))


        followed_company_attributes = cls(
            name=name,
            tagline=tagline,
            url=url,
            logo_url=logo_url,
            raising=raising,
            profile_available=profile_available,
            followed_at=followed_at,
        )


        followed_company_attributes.additional_properties = d
        return followed_company_attributes

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
