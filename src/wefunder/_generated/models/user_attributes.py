from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAttributes")


@_attrs_define
class UserAttributes:
    """
    Attributes:
        email (str | Unset):  Example: user@example.com.
        username (str | Unset):  Example: john_doe.
        name (str | Unset):  Example: John.
        full_name (str | Unset):  Example: John Doe.
        bio (None | str | Unset):  Example: Entrepreneur and investor.
        city (None | str | Unset):  Example: San Francisco.
        country (None | str | Unset):  Example: USA.
        avatar_url (None | str | Unset):  Example: https://example.com/avatar.jpg.
        created_at (datetime.datetime | Unset):  Example: 2023-01-15T10:30:00Z.
        certified_at (datetime.datetime | None | Unset):  Example: 2023-02-01T14:20:00Z.
    """

    email: str | Unset = UNSET
    username: str | Unset = UNSET
    name: str | Unset = UNSET
    full_name: str | Unset = UNSET
    bio: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    certified_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        username = self.username

        name = self.name

        full_name = self.full_name

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        certified_at: None | str | Unset
        if isinstance(self.certified_at, Unset):
            certified_at = UNSET
        elif isinstance(self.certified_at, datetime.datetime):
            certified_at = self.certified_at.isoformat()
        else:
            certified_at = self.certified_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if username is not UNSET:
            field_dict["username"] = username
        if name is not UNSET:
            field_dict["name"] = name
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if bio is not UNSET:
            field_dict["bio"] = bio
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if certified_at is not UNSET:
            field_dict["certified_at"] = certified_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        username = d.pop("username", UNSET)

        name = d.pop("name", UNSET)

        full_name = d.pop("full_name", UNSET)

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        def _parse_certified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                certified_at_type_0 = datetime.datetime.fromisoformat(data)

                return certified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        certified_at = _parse_certified_at(d.pop("certified_at", UNSET))

        user_attributes = cls(
            email=email,
            username=username,
            name=name,
            full_name=full_name,
            bio=bio,
            city=city,
            country=country,
            avatar_url=avatar_url,
            created_at=created_at,
            certified_at=certified_at,
        )

        user_attributes.additional_properties = d
        return user_attributes

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
