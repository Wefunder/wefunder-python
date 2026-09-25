from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invite_link_attributes_status import InviteLinkAttributesStatus
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.invite_link_attributes_events_item import InviteLinkAttributesEventsItem





T = TypeVar("T", bound="InviteLinkAttributes")



@_attrs_define
class InviteLinkAttributes:
    """ 
        Attributes:
            url (str | Unset): Shareable invite URL. Carries the access token, not the id. Example:
                https://wefunder.com/i/abc123token.
            allocation_cents (int | None | Unset):  Example: 5000000.
            max_uses (int | None | Unset):  Example: 50.
            uses_count (int | Unset):  Example: 0.
            active (bool | Unset): False once the link is canceled (soft-deleted). Example: True.
            created_at (datetime.datetime | Unset):  Example: 2025-01-15T10:00:00Z.
            email (None | str | Unset): Per-person only — recipient email. Example: investor@example.com.
            wefunder_user_id (None | str | Unset): Per-person only — the recipient's id (`usr_...`), when they are an
                existing user. Example: usr_existing123.
            status (InviteLinkAttributesStatus | Unset): Per-person only — derived live, not stored. `pending` (sent, not
                yet
                opened), `opened` (link clicked), `invested` (a matching active
                investment exists), `revoked` (canceled).
                 Example: pending.
            opened_at (datetime.datetime | None | Unset): Per-person only.
            invested_at (datetime.datetime | None | Unset): Per-person only.
            investment_id (None | str | Unset): Per-person only — the id (`inv_...`) of the matching investment. Example:
                inv_def789.
            events (list[InviteLinkAttributesEventsItem] | Unset): Engagement timeline. Present on the show (get-one)
                endpoint only.
     """

    url: str | Unset = UNSET
    allocation_cents: int | None | Unset = UNSET
    max_uses: int | None | Unset = UNSET
    uses_count: int | Unset = UNSET
    active: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    email: None | str | Unset = UNSET
    wefunder_user_id: None | str | Unset = UNSET
    status: InviteLinkAttributesStatus | Unset = UNSET
    opened_at: datetime.datetime | None | Unset = UNSET
    invested_at: datetime.datetime | None | Unset = UNSET
    investment_id: None | str | Unset = UNSET
    events: list[InviteLinkAttributesEventsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.invite_link_attributes_events_item import InviteLinkAttributesEventsItem # noqa: PLC0415
        url = self.url

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

        active = self.active

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


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
        field_dict.update({
        })
        if url is not UNSET:
            field_dict["url"] = url
        if allocation_cents is not UNSET:
            field_dict["allocation_cents"] = allocation_cents
        if max_uses is not UNSET:
            field_dict["max_uses"] = max_uses
        if uses_count is not UNSET:
            field_dict["uses_count"] = uses_count
        if active is not UNSET:
            field_dict["active"] = active
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
        from ..models.invite_link_attributes_events_item import InviteLinkAttributesEventsItem # noqa: PLC0415
        d = dict(src_dict)
        url = d.pop("url", UNSET)

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

        active = d.pop("active", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
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


        _status = d.pop("status", UNSET)
        status: InviteLinkAttributesStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = InviteLinkAttributesStatus(_status)




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
            allocation_cents=allocation_cents,
            max_uses=max_uses,
            uses_count=uses_count,
            active=active,
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
