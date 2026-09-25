from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.syndicate_member_attributes_syndicate_permission import SyndicateMemberAttributesSyndicatePermission
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="SyndicateMemberAttributes")



@_attrs_define
class SyndicateMemberAttributes:
    """ 
        Attributes:
            user_id (int | None | Unset): Internal integer id. Deprecated — use `user` (`usr_...`) instead. Example: 123.
            user (None | str | Unset): The member's user id (`usr_...`); null for invitees who haven't signed up. Example:
                usr_8Kd0aB3xQ9k2vF8mNp1zT5wY.
            user_name (None | str | Unset):  Example: Jane Smith.
            user_email (None | str | Unset): **Moderator-only.** User email (or invite_email for pending invitees).
                Returns null for non-moderator callers. Requires the requesting user
                to be a manager/operator of the syndicate.
                 Example: user@example.com.
            role (str | Unset): Current role (creator, manager, member, invitee, applicant, exiled, resigned, etc.) Example:
                member.
            invite_role (None | str | Unset): The role the member was invited as Example: admin.
            syndicate_permission (SyndicateMemberAttributesSyndicatePermission | Unset): Permission level within the
                syndicate
            title (None | str | Unset): Custom title for the member Example: Example title.
            sort_order (int | None | Unset): Display order position Example: 5.
            carry_percentage_override (int | None | Unset): Override carry percentage for this member Example: 20.
            avatar_url (None | str | Unset): User profile photo URL (null for invitees without a user account) Example:
                https://uploads.wefunder.com/uploads/user/avatar/456/large_photo.jpg.
            bio (None | str | Unset): User bio with fallback chain (bio -> thesis -> about). Null for invitees without a
                user account. Example: Example text.
            city (None | str | Unset): User's city Example: San Francisco.
            country (None | str | Unset): User's country Example: US.
            last_activity_at (datetime.datetime | None | Unset): ISO 8601 timestamp of user's last login. Null for invitees
                without a user account. Example: 2025-03-01T12:00:00Z.
            profile_url (None | str | Unset): Relative path to user's profile (e.g. '/janedoe'). Null for invitees without a
                user account. Example: /janedoe.
            tags (list[str] | Unset): 'Can help with' tags from the user's investor profile. Empty array for invitees.
                Example: ['Fundraising', 'Product Strategy'].
            joined_at (datetime.datetime | Unset): ISO 8601 join date (alias for created_at) Example: 2025-03-01T12:00:00Z.
            investment_total (None | str | Unset): Total amount invested in syndicate deals, in cents. String to avoid
                floating-point precision issues. Example: 500000.
            deal_count (int | None | Unset): Number of syndicate deals the member has invested in Example: 2.
            accredited (bool | Unset): **Moderator-only.** Whether the user is an accredited investor.
                Only included when the requesting user is a manager/operator.
                 Example: True.
            legal_name (None | str | Unset): **Moderator-only.** Full legal name of the user.
                Only included when the requesting user is a manager/operator.
                 Example: Example Name.
            starred (bool | Unset): **Moderator-only.** Whether the current moderator has starred this member.
                Only included when the requesting user is a manager/operator.
                 Example: True.
            private_tags (list[str] | Unset): **Moderator-only.** Labels assigned by moderators via ClubMemberLabel.
                Only included when the requesting user is a manager/operator.
                 Example: ['VIP', 'Follow up'].
            created_at (datetime.datetime | Unset):  Example: 2025-03-01T12:00:00Z.
            updated_at (datetime.datetime | Unset):  Example: 2025-03-01T12:00:00Z.
     """

    user_id: int | None | Unset = UNSET
    user: None | str | Unset = UNSET
    user_name: None | str | Unset = UNSET
    user_email: None | str | Unset = UNSET
    role: str | Unset = UNSET
    invite_role: None | str | Unset = UNSET
    syndicate_permission: SyndicateMemberAttributesSyndicatePermission | Unset = UNSET
    title: None | str | Unset = UNSET
    sort_order: int | None | Unset = UNSET
    carry_percentage_override: int | None | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    last_activity_at: datetime.datetime | None | Unset = UNSET
    profile_url: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    joined_at: datetime.datetime | Unset = UNSET
    investment_total: None | str | Unset = UNSET
    deal_count: int | None | Unset = UNSET
    accredited: bool | Unset = UNSET
    legal_name: None | str | Unset = UNSET
    starred: bool | Unset = UNSET
    private_tags: list[str] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        user: None | str | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        role = self.role

        invite_role: None | str | Unset
        if isinstance(self.invite_role, Unset):
            invite_role = UNSET
        else:
            invite_role = self.invite_role

        syndicate_permission: str | Unset = UNSET
        if not isinstance(self.syndicate_permission, Unset):
            syndicate_permission = self.syndicate_permission.value


        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        sort_order: int | None | Unset
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = self.sort_order

        carry_percentage_override: int | None | Unset
        if isinstance(self.carry_percentage_override, Unset):
            carry_percentage_override = UNSET
        else:
            carry_percentage_override = self.carry_percentage_override

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

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

        last_activity_at: None | str | Unset
        if isinstance(self.last_activity_at, Unset):
            last_activity_at = UNSET
        elif isinstance(self.last_activity_at, datetime.datetime):
            last_activity_at = self.last_activity_at.isoformat()
        else:
            last_activity_at = self.last_activity_at

        profile_url: None | str | Unset
        if isinstance(self.profile_url, Unset):
            profile_url = UNSET
        else:
            profile_url = self.profile_url

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



        joined_at: str | Unset = UNSET
        if not isinstance(self.joined_at, Unset):
            joined_at = self.joined_at.isoformat()

        investment_total: None | str | Unset
        if isinstance(self.investment_total, Unset):
            investment_total = UNSET
        else:
            investment_total = self.investment_total

        deal_count: int | None | Unset
        if isinstance(self.deal_count, Unset):
            deal_count = UNSET
        else:
            deal_count = self.deal_count

        accredited = self.accredited

        legal_name: None | str | Unset
        if isinstance(self.legal_name, Unset):
            legal_name = UNSET
        else:
            legal_name = self.legal_name

        starred = self.starred

        private_tags: list[str] | Unset = UNSET
        if not isinstance(self.private_tags, Unset):
            private_tags = self.private_tags



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
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user is not UNSET:
            field_dict["user"] = user
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if role is not UNSET:
            field_dict["role"] = role
        if invite_role is not UNSET:
            field_dict["invite_role"] = invite_role
        if syndicate_permission is not UNSET:
            field_dict["syndicate_permission"] = syndicate_permission
        if title is not UNSET:
            field_dict["title"] = title
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if carry_percentage_override is not UNSET:
            field_dict["carry_percentage_override"] = carry_percentage_override
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if bio is not UNSET:
            field_dict["bio"] = bio
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if last_activity_at is not UNSET:
            field_dict["last_activity_at"] = last_activity_at
        if profile_url is not UNSET:
            field_dict["profile_url"] = profile_url
        if tags is not UNSET:
            field_dict["tags"] = tags
        if joined_at is not UNSET:
            field_dict["joined_at"] = joined_at
        if investment_total is not UNSET:
            field_dict["investment_total"] = investment_total
        if deal_count is not UNSET:
            field_dict["deal_count"] = deal_count
        if accredited is not UNSET:
            field_dict["accredited"] = accredited
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if starred is not UNSET:
            field_dict["starred"] = starred
        if private_tags is not UNSET:
            field_dict["private_tags"] = private_tags
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        def _parse_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user = _parse_user(d.pop("user", UNSET))


        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("user_name", UNSET))


        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))


        role = d.pop("role", UNSET)

        def _parse_invite_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invite_role = _parse_invite_role(d.pop("invite_role", UNSET))


        _syndicate_permission = d.pop("syndicate_permission", UNSET)
        syndicate_permission: SyndicateMemberAttributesSyndicatePermission | Unset
        if isinstance(_syndicate_permission,  Unset):
            syndicate_permission = UNSET
        else:
            syndicate_permission = SyndicateMemberAttributesSyndicatePermission(_syndicate_permission)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_sort_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sort_order = _parse_sort_order(d.pop("sort_order", UNSET))


        def _parse_carry_percentage_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        carry_percentage_override = _parse_carry_percentage_override(d.pop("carry_percentage_override", UNSET))


        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))


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


        def _parse_last_activity_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_activity_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity_at = _parse_last_activity_at(d.pop("last_activity_at", UNSET))


        def _parse_profile_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_url = _parse_profile_url(d.pop("profile_url", UNSET))


        tags = cast(list[str], d.pop("tags", UNSET))


        _joined_at = d.pop("joined_at", UNSET)
        joined_at: datetime.datetime | Unset
        if isinstance(_joined_at,  Unset):
            joined_at = UNSET
        else:
            joined_at = datetime.datetime.fromisoformat(_joined_at)




        def _parse_investment_total(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investment_total = _parse_investment_total(d.pop("investment_total", UNSET))


        def _parse_deal_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        deal_count = _parse_deal_count(d.pop("deal_count", UNSET))


        accredited = d.pop("accredited", UNSET)

        def _parse_legal_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_name = _parse_legal_name(d.pop("legal_name", UNSET))


        starred = d.pop("starred", UNSET)

        private_tags = cast(list[str], d.pop("private_tags", UNSET))


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




        syndicate_member_attributes = cls(
            user_id=user_id,
            user=user,
            user_name=user_name,
            user_email=user_email,
            role=role,
            invite_role=invite_role,
            syndicate_permission=syndicate_permission,
            title=title,
            sort_order=sort_order,
            carry_percentage_override=carry_percentage_override,
            avatar_url=avatar_url,
            bio=bio,
            city=city,
            country=country,
            last_activity_at=last_activity_at,
            profile_url=profile_url,
            tags=tags,
            joined_at=joined_at,
            investment_total=investment_total,
            deal_count=deal_count,
            accredited=accredited,
            legal_name=legal_name,
            starred=starred,
            private_tags=private_tags,
            created_at=created_at,
            updated_at=updated_at,
        )


        syndicate_member_attributes.additional_properties = d
        return syndicate_member_attributes

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
