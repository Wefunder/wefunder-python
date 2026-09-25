from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_update_attributes_visibility_type_1 import CompanyUpdateAttributesVisibilityType1
from ..models.company_update_attributes_visibility_type_2_type_1 import CompanyUpdateAttributesVisibilityType2Type1
from ..models.company_update_attributes_visibility_type_3_type_1 import CompanyUpdateAttributesVisibilityType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_update_attributes_author_type_0 import CompanyUpdateAttributesAuthorType0


T = TypeVar("T", bound="CompanyUpdateAttributes")


@_attrs_define
class CompanyUpdateAttributes:
    """
    Attributes:
        kind (str | Unset): `update`, `note`, `spotlight`, `bounty`, ...
        title (None | str | Unset):
        excerpt (None | str | Unset): The first ~280 characters, plain text.
        content (None | str | Unset): Full plain text. Present on the single-post endpoint; null in lists.
        published_at (datetime.datetime | None | Unset):
        pinned (bool | Unset):
        visibility (CompanyUpdateAttributesVisibilityType1 | CompanyUpdateAttributesVisibilityType2Type1 |
            CompanyUpdateAttributesVisibilityType3Type1 | None | Unset): Who the site shows the post to. You only ever
            receive posts you may see.
        author (CompanyUpdateAttributesAuthorType0 | None | Unset):
        comments_count (int | Unset):
        likes_count (int | Unset):
        url (None | str | Unset): The post's page on wefunder.com.
    """

    kind: str | Unset = UNSET
    title: None | str | Unset = UNSET
    excerpt: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    published_at: datetime.datetime | None | Unset = UNSET
    pinned: bool | Unset = UNSET
    visibility: (
        CompanyUpdateAttributesVisibilityType1
        | CompanyUpdateAttributesVisibilityType2Type1
        | CompanyUpdateAttributesVisibilityType3Type1
        | None
        | Unset
    ) = UNSET
    author: CompanyUpdateAttributesAuthorType0 | None | Unset = UNSET
    comments_count: int | Unset = UNSET
    likes_count: int | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_update_attributes_author_type_0 import CompanyUpdateAttributesAuthorType0  # noqa: PLC0415

        kind = self.kind

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        excerpt: None | str | Unset
        if isinstance(self.excerpt, Unset):
            excerpt = UNSET
        else:
            excerpt = self.excerpt

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        pinned = self.pinned

        visibility: None | str | Unset
        if isinstance(self.visibility, Unset):
            visibility = UNSET
        elif (
            isinstance(self.visibility, CompanyUpdateAttributesVisibilityType1)
            or isinstance(self.visibility, CompanyUpdateAttributesVisibilityType2Type1)
            or isinstance(self.visibility, CompanyUpdateAttributesVisibilityType3Type1)
        ):
            visibility = self.visibility.value
        else:
            visibility = self.visibility

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, CompanyUpdateAttributesAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author

        comments_count = self.comments_count

        likes_count = self.likes_count

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if title is not UNSET:
            field_dict["title"] = title
        if excerpt is not UNSET:
            field_dict["excerpt"] = excerpt
        if content is not UNSET:
            field_dict["content"] = content
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if pinned is not UNSET:
            field_dict["pinned"] = pinned
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if author is not UNSET:
            field_dict["author"] = author
        if comments_count is not UNSET:
            field_dict["comments_count"] = comments_count
        if likes_count is not UNSET:
            field_dict["likes_count"] = likes_count
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_update_attributes_author_type_0 import CompanyUpdateAttributesAuthorType0  # noqa: PLC0415

        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_excerpt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        excerpt = _parse_excerpt(d.pop("excerpt", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_at = _parse_published_at(d.pop("published_at", UNSET))

        pinned = d.pop("pinned", UNSET)

        def _parse_visibility(
            data: object,
        ) -> (
            CompanyUpdateAttributesVisibilityType1
            | CompanyUpdateAttributesVisibilityType2Type1
            | CompanyUpdateAttributesVisibilityType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                visibility_type_1 = CompanyUpdateAttributesVisibilityType1(data)

                return visibility_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                visibility_type_2_type_1 = CompanyUpdateAttributesVisibilityType2Type1(data)

                return visibility_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                visibility_type_3_type_1 = CompanyUpdateAttributesVisibilityType3Type1(data)

                return visibility_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanyUpdateAttributesVisibilityType1
                | CompanyUpdateAttributesVisibilityType2Type1
                | CompanyUpdateAttributesVisibilityType3Type1
                | None
                | Unset,
                data,
            )

        visibility = _parse_visibility(d.pop("visibility", UNSET))

        def _parse_author(data: object) -> CompanyUpdateAttributesAuthorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = CompanyUpdateAttributesAuthorType0.from_dict(data)

                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyUpdateAttributesAuthorType0 | None | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        comments_count = d.pop("comments_count", UNSET)

        likes_count = d.pop("likes_count", UNSET)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        company_update_attributes = cls(
            kind=kind,
            title=title,
            excerpt=excerpt,
            content=content,
            published_at=published_at,
            pinned=pinned,
            visibility=visibility,
            author=author,
            comments_count=comments_count,
            likes_count=likes_count,
            url=url,
        )

        company_update_attributes.additional_properties = d
        return company_update_attributes

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
