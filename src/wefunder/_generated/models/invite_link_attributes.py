from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invite_link_attributes_status_type_1 import InviteLinkAttributesStatusType1
from ..models.invite_link_attributes_status_type_2_type_1 import InviteLinkAttributesStatusType2Type1
from ..models.invite_link_attributes_status_type_3_type_1 import InviteLinkAttributesStatusType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invite_link_attributes_events_item import InviteLinkAttributesEventsItem


T = TypeVar("T", bound="InviteLinkAttributes")


@_attrs_define
class InviteLinkAttributes:
    """
    Attributes:
        url (None | str | Unset): Shareable invite URL. Carries the access token, not the id. A link
            made through the API opens the hosted investment flow
            (`/invest/link/...`); a link made on wefunder.com opens the deal page
            with its token (`/{company}?invite_token=...`), the URL wefunder.com
            sends.
            Null on a per-person invite whose recipient the caller may not see
            (see `email`): the URL carries the invite's access token and its page
            shows the recipient. Cancel, update and resend still work. An invite
            your app addressed by `wefunder_user_id` keeps its URL: its page names
            no address.
             Example: https://wefunder.com/i/abc123token.
        reuse (bool | Unset): `true` for a reusable (shareable) link, `false` for a per-person
            invite. Fixed at creation. Use this, not the presence of `email`, to
            tell the two apart.
             Example: True.
        allocation_cents (int | None | Unset):  Example: 5000000.
        max_uses (int | None | Unset):  Example: 50.
        uses_count (int | Unset):  Example: 0.
        click_count (int | Unset): How many times the link was clicked through: a click is recorded when
            the recipient continues past the link's landing page into the
            investment flow (loading the page alone is not counted, since mail
            clients prefetch links). Visits that found the link canceled or the
            offering closed are not clicks, nor are sends. Recorded for per-person
            links only; a reusable link reports 0 (use `uses_count` for its
            claims).
             Example: 0.
        first_clicked_at (datetime.datetime | None | Unset): When the link was first clicked; null if it never was. A
            click, not an email open.
        active (bool | Unset): False once the link is canceled (soft-deleted). Example: True.
        canceled_at (datetime.datetime | None | Unset): When the link was canceled; null while it is active.
        created_at (datetime.datetime | Unset):  Example: 2025-01-15T10:00:00Z.
        email (None | str | Unset): Per-person only — recipient email. Always `null` for an invite
            addressed by `wefunder_user_id`, which never returns the account's
            email. Otherwise null unless the token holds `read:investors:pii`
            (on an install, the install must grant it too), except that the app
            which created the invite through the API with an `email` always sees
            the address it supplied. The invite still sends, resends and reports
            status when the email is null.
             Example: investor@example.com.
        wefunder_user_id (None | str | Unset): Per-person only — the recipient's id (`usr_...`), when they are an
            existing user. Example: usr_existing123.
        status (InviteLinkAttributesStatusType1 | InviteLinkAttributesStatusType2Type1 |
            InviteLinkAttributesStatusType3Type1 | None | Unset): Per-person only — derived live, not stored. `pending`
            (sent, not yet
            opened), `opened` (link clicked), `invested` (a matching active
            investment exists), `revoked` (canceled).
             Example: pending.
        opened_at (datetime.datetime | None | Unset): Per-person only. The first click, not an email open (deprecated:
            use
            `first_clicked_at`, which has the same value).
        invested_at (datetime.datetime | None | Unset): Per-person only.
        investment_id (None | str | Unset): Per-person only — the id (`inv_...`) of the matching investment. Example:
            inv_def789.
        events (list[InviteLinkAttributesEventsItem] | Unset): Engagement timeline. Present on the show (get-one)
            endpoint only.
    """

    url: None | str | Unset = UNSET
    reuse: bool | Unset = UNSET
    allocation_cents: int | None | Unset = UNSET
    max_uses: int | None | Unset = UNSET
    uses_count: int | Unset = UNSET
    click_count: int | Unset = UNSET
    first_clicked_at: datetime.datetime | None | Unset = UNSET
    active: bool | Unset = UNSET
    canceled_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    email: None | str | Unset = UNSET
    wefunder_user_id: None | str | Unset = UNSET
    status: (
        InviteLinkAttributesStatusType1
        | InviteLinkAttributesStatusType2Type1
        | InviteLinkAttributesStatusType3Type1
        | None
        | Unset
    ) = UNSET
    opened_at: datetime.datetime | None | Unset = UNSET
    invested_at: datetime.datetime | None | Unset = UNSET
    investment_id: None | str | Unset = UNSET
    events: list[InviteLinkAttributesEventsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        reuse = self.reuse

        allocation_cents: int | None | Unset
        if isinstance(self.allocation_cents, Unset):
            allocation_cents = UNSET
        else:
            allocation_cents = self.allocation_cents

        max_uses: int | None | Unset
        if isinstance(self.max_uses, Unset):
            max_uses = UNSET
        else:
            max_uses = self.max_uses

        uses_count = self.uses_count

        click_count = self.click_count

        first_clicked_at: None | str | Unset
        if isinstance(self.first_clicked_at, Unset):
            first_clicked_at = UNSET
        elif isinstance(self.first_clicked_at, datetime.datetime):
            first_clicked_at = self.first_clicked_at.isoformat()
        else:
            first_clicked_at = self.first_clicked_at

        active = self.active

        canceled_at: None | str | Unset
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        elif isinstance(self.canceled_at, datetime.datetime):
            canceled_at = self.canceled_at.isoformat()
        else:
            canceled_at = self.canceled_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        wefunder_user_id: None | str | Unset
        if isinstance(self.wefunder_user_id, Unset):
            wefunder_user_id = UNSET
        else:
            wefunder_user_id = self.wefunder_user_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif (
            isinstance(self.status, InviteLinkAttributesStatusType1)
            or isinstance(self.status, InviteLinkAttributesStatusType2Type1)
            or isinstance(self.status, InviteLinkAttributesStatusType3Type1)
        ):
            status = self.status.value
        else:
            status = self.status

        opened_at: None | str | Unset
        if isinstance(self.opened_at, Unset):
            opened_at = UNSET
        elif isinstance(self.opened_at, datetime.datetime):
            opened_at = self.opened_at.isoformat()
        else:
            opened_at = self.opened_at

        invested_at: None | str | Unset
        if isinstance(self.invested_at, Unset):
            invested_at = UNSET
        elif isinstance(self.invested_at, datetime.datetime):
            invested_at = self.invested_at.isoformat()
        else:
            invested_at = self.invested_at

        investment_id: None | str | Unset
        if isinstance(self.investment_id, Unset):
            investment_id = UNSET
        else:
            investment_id = self.investment_id

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if reuse is not UNSET:
            field_dict["reuse"] = reuse
        if allocation_cents is not UNSET:
            field_dict["allocation_cents"] = allocation_cents
        if max_uses is not UNSET:
            field_dict["max_uses"] = max_uses
        if uses_count is not UNSET:
            field_dict["uses_count"] = uses_count
        if click_count is not UNSET:
            field_dict["click_count"] = click_count
        if first_clicked_at is not UNSET:
            field_dict["first_clicked_at"] = first_clicked_at
        if active is not UNSET:
            field_dict["active"] = active
        if canceled_at is not UNSET:
            field_dict["canceled_at"] = canceled_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if email is not UNSET:
            field_dict["email"] = email
        if wefunder_user_id is not UNSET:
            field_dict["wefunder_user_id"] = wefunder_user_id
        if status is not UNSET:
            field_dict["status"] = status
        if opened_at is not UNSET:
            field_dict["opened_at"] = opened_at
        if invested_at is not UNSET:
            field_dict["invested_at"] = invested_at
        if investment_id is not UNSET:
            field_dict["investment_id"] = investment_id
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invite_link_attributes_events_item import InviteLinkAttributesEventsItem  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        reuse = d.pop("reuse", UNSET)

        def _parse_allocation_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        allocation_cents = _parse_allocation_cents(d.pop("allocation_cents", UNSET))

        def _parse_max_uses(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_uses = _parse_max_uses(d.pop("max_uses", UNSET))

        uses_count = d.pop("uses_count", UNSET)

        click_count = d.pop("click_count", UNSET)

        def _parse_first_clicked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_clicked_at_type_0 = datetime.datetime.fromisoformat(data)

                return first_clicked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_clicked_at = _parse_first_clicked_at(d.pop("first_clicked_at", UNSET))

        active = d.pop("active", UNSET)

        def _parse_canceled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                canceled_at_type_0 = datetime.datetime.fromisoformat(data)

                return canceled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        canceled_at = _parse_canceled_at(d.pop("canceled_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_wefunder_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wefunder_user_id = _parse_wefunder_user_id(d.pop("wefunder_user_id", UNSET))

        def _parse_status(
            data: object,
        ) -> (
            InviteLinkAttributesStatusType1
            | InviteLinkAttributesStatusType2Type1
            | InviteLinkAttributesStatusType3Type1
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
                status_type_1 = InviteLinkAttributesStatusType1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = InviteLinkAttributesStatusType2Type1(data)

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = InviteLinkAttributesStatusType3Type1(data)

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                InviteLinkAttributesStatusType1
                | InviteLinkAttributesStatusType2Type1
                | InviteLinkAttributesStatusType3Type1
                | None
                | Unset,
                data,
            )

        status = _parse_status(d.pop("status", UNSET))

        def _parse_opened_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_at_type_0 = datetime.datetime.fromisoformat(data)

                return opened_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        opened_at = _parse_opened_at(d.pop("opened_at", UNSET))

        def _parse_invested_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invested_at_type_0 = datetime.datetime.fromisoformat(data)

                return invested_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        invested_at = _parse_invested_at(d.pop("invested_at", UNSET))

        def _parse_investment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investment_id = _parse_investment_id(d.pop("investment_id", UNSET))

        _events = d.pop("events", UNSET)
        events: list[InviteLinkAttributesEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = InviteLinkAttributesEventsItem.from_dict(events_item_data)

                events.append(events_item)

        invite_link_attributes = cls(
            url=url,
            reuse=reuse,
            allocation_cents=allocation_cents,
            max_uses=max_uses,
            uses_count=uses_count,
            click_count=click_count,
            first_clicked_at=first_clicked_at,
            active=active,
            canceled_at=canceled_at,
            created_at=created_at,
            email=email,
            wefunder_user_id=wefunder_user_id,
            status=status,
            opened_at=opened_at,
            invested_at=invested_at,
            investment_id=investment_id,
            events=events,
        )

        invite_link_attributes.additional_properties = d
        return invite_link_attributes

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
