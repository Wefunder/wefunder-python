from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="SyndicateAttributes")



@_attrs_define
class SyndicateAttributes:
    """ 
        Attributes:
            name (str | Unset):  Example: Acme Syndicate.
            slug (str | Unset):  Example: acme-syndicate.
            tagline (None | str | Unset): Short description / tagline for the syndicate Example: Investing in the future of
                AI.
            description (None | str | Unset):  Example: Example text.
            avatar_url (None | str | Unset): Syndicate icon/avatar URL Example:
                https://uploads.wefunder.com/uploads/club/icon/42/large_avatar.png.
            published (bool | Unset):  Example: True.
            launched (bool | Unset):  Example: True.
            membership_open (bool | Unset): Whether the syndicate is accepting new members (nil defaults to true) Example:
                True.
            member_count (int | Unset):  Example: 47.
            deal_count (int | Unset): Number of linked deals (fundraises) in this syndicate Example: 3.
            primary_fund_company_id (int | None | Unset): Internal integer id. Deprecated — use `primary_fund_company`
                (`co_...`) instead. Example: 4242.
            primary_fund_company (None | str | Unset): The primary fund company's id (`co_...`), when the syndicate has one.
                Example: co_8Kd0aB3xQ9k2vF8mNp1zT5wY.
            created_by_user_id (int | Unset): Internal integer id. Deprecated — use `created_by` (`usr_...`) instead.
                Example: 123.
            created_by (None | str | Unset): The creating user's id (`usr_...`). Example: usr_8Kd0aB3xQ9k2vF8mNp1zT5wY.
            created_at (datetime.datetime | Unset):  Example: 2025-03-01T12:00:00Z.
            updated_at (datetime.datetime | Unset):  Example: 2025-03-01T12:00:00Z.
     """

    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    tagline: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    published: bool | Unset = UNSET
    launched: bool | Unset = UNSET
    membership_open: bool | Unset = UNSET
    member_count: int | Unset = UNSET
    deal_count: int | Unset = UNSET
    primary_fund_company_id: int | None | Unset = UNSET
    primary_fund_company: None | str | Unset = UNSET
    created_by_user_id: int | Unset = UNSET
    created_by: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        tagline: None | str | Unset
        if isinstance(self.tagline, Unset):
            tagline = UNSET
        else:
            tagline = self.tagline

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        published = self.published

        launched = self.launched

        membership_open = self.membership_open

        member_count = self.member_count

        deal_count = self.deal_count

        primary_fund_company_id: int | None | Unset
        if isinstance(self.primary_fund_company_id, Unset):
            primary_fund_company_id = UNSET
        else:
            primary_fund_company_id = self.primary_fund_company_id

        primary_fund_company: None | str | Unset
        if isinstance(self.primary_fund_company, Unset):
            primary_fund_company = UNSET
        else:
            primary_fund_company = self.primary_fund_company

        created_by_user_id = self.created_by_user_id

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if description is not UNSET:
            field_dict["description"] = description
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if published is not UNSET:
            field_dict["published"] = published
        if launched is not UNSET:
            field_dict["launched"] = launched
        if membership_open is not UNSET:
            field_dict["membership_open"] = membership_open
        if member_count is not UNSET:
            field_dict["member_count"] = member_count
        if deal_count is not UNSET:
            field_dict["deal_count"] = deal_count
        if primary_fund_company_id is not UNSET:
            field_dict["primary_fund_company_id"] = primary_fund_company_id
        if primary_fund_company is not UNSET:
            field_dict["primary_fund_company"] = primary_fund_company
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        def _parse_tagline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tagline = _parse_tagline(d.pop("tagline", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))


        published = d.pop("published", UNSET)

        launched = d.pop("launched", UNSET)

        membership_open = d.pop("membership_open", UNSET)

        member_count = d.pop("member_count", UNSET)

        deal_count = d.pop("deal_count", UNSET)

        def _parse_primary_fund_company_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        primary_fund_company_id = _parse_primary_fund_company_id(d.pop("primary_fund_company_id", UNSET))


        def _parse_primary_fund_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_fund_company = _parse_primary_fund_company(d.pop("primary_fund_company", UNSET))


        created_by_user_id = d.pop("created_by_user_id", UNSET)

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        syndicate_attributes = cls(
            name=name,
            slug=slug,
            tagline=tagline,
            description=description,
            avatar_url=avatar_url,
            published=published,
            launched=launched,
            membership_open=membership_open,
            member_count=member_count,
            deal_count=deal_count,
            primary_fund_company_id=primary_fund_company_id,
            primary_fund_company=primary_fund_company,
            created_by_user_id=created_by_user_id,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
        )


        syndicate_attributes.additional_properties = d
        return syndicate_attributes

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
