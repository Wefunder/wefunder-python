from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortfolioCompanyRef")


@_attrs_define
class PortfolioCompanyRef:
    """The company behind a portfolio position or holding.

    Attributes:
        id (str | Unset): The company's id (`co_...`) Example: co_2bt9eJn6X8C9gnShl63qlzkK.
        name (str | Unset):  Example: Acme Robotics.
        slug (None | str | Unset):  Example: acme-robotics.
        url (None | str | Unset): The company's page on wefunder.com, absolute. This is the link target the [attribution
            rule](/resources/acceptable-use#attribution) asks for wherever you show the position; do not link to the
            investor's Wefunder portfolio instead. Null when the company no longer has a public page. Example:
            https://wefunder.com/acme-robotics.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    slug: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        portfolio_company_ref = cls(
            id=id,
            name=name,
            slug=slug,
            url=url,
        )

        portfolio_company_ref.additional_properties = d
        return portfolio_company_ref

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
