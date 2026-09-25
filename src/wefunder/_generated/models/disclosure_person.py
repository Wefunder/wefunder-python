from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DisclosurePerson")


@_attrs_define
class DisclosurePerson:
    """
    Attributes:
        name (None | str | Unset):
        titles (None | str | Unset):
        since (int | None | Unset): Year joined.
        director (bool | Unset):
        officer (bool | Unset):
    """

    name: None | str | Unset = UNSET
    titles: None | str | Unset = UNSET
    since: int | None | Unset = UNSET
    director: bool | Unset = UNSET
    officer: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        titles: None | str | Unset
        if isinstance(self.titles, Unset):
            titles = UNSET
        else:
            titles = self.titles

        since: int | None | Unset
        if isinstance(self.since, Unset):
            since = UNSET
        else:
            since = self.since

        director = self.director

        officer = self.officer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if titles is not UNSET:
            field_dict["titles"] = titles
        if since is not UNSET:
            field_dict["since"] = since
        if director is not UNSET:
            field_dict["director"] = director
        if officer is not UNSET:
            field_dict["officer"] = officer

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

        def _parse_titles(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        titles = _parse_titles(d.pop("titles", UNSET))

        def _parse_since(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        since = _parse_since(d.pop("since", UNSET))

        director = d.pop("director", UNSET)

        officer = d.pop("officer", UNSET)

        disclosure_person = cls(
            name=name,
            titles=titles,
            since=since,
            director=director,
            officer=officer,
        )

        disclosure_person.additional_properties = d
        return disclosure_person

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
