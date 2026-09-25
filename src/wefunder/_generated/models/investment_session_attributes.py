from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.investment_session_attributes_funding_status import InvestmentSessionAttributesFundingStatus
from ..models.investment_session_attributes_kyc_status import InvestmentSessionAttributesKycStatus
from ..models.investment_session_attributes_status import InvestmentSessionAttributesStatus
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.investment_session_attributes_events_item import InvestmentSessionAttributesEventsItem
  from ..models.investment_session_attributes_metadata import InvestmentSessionAttributesMetadata





T = TypeVar("T", bound="InvestmentSessionAttributes")



@_attrs_define
class InvestmentSessionAttributes:
    """ 
        Attributes:
            status (InvestmentSessionAttributesStatus | Unset):  Example: pending.
            url (str | Unset): The hosted URL the recipient opens to begin the flow. Example:
                https://wefunder.com/invest/session/is_abc123.
            spv_id (str | Unset):  Example: spv_abc123.
            email (None | str | Unset):  Example: investor@example.com.
            allocation_cents (int | None | Unset): The fixed amount the session locks to, in cents; null when the recipient
                chooses their own amount. Example: 5000000.
            kyc_status (InvestmentSessionAttributesKycStatus | Unset):  Example: pending.
            funding_status (InvestmentSessionAttributesFundingStatus | Unset):  Example: pending.
            investment_id (None | str | Unset): Populated once the session completes successfully. Example: invt_def789.
            metadata (InvestmentSessionAttributesMetadata | Unset): The key/value pairs supplied at creation.
            created_at (datetime.datetime | Unset):  Example: 2025-01-15T10:00:00Z.
            expires_at (datetime.datetime | None | Unset):
            events (list[InvestmentSessionAttributesEventsItem] | Unset): Durable platform events recorded about this
                session, oldest first. Only present on the single-session GET.
     """

    status: InvestmentSessionAttributesStatus | Unset = UNSET
    url: str | Unset = UNSET
    spv_id: str | Unset = UNSET
    email: None | str | Unset = UNSET
    allocation_cents: int | None | Unset = UNSET
    kyc_status: InvestmentSessionAttributesKycStatus | Unset = UNSET
    funding_status: InvestmentSessionAttributesFundingStatus | Unset = UNSET
    investment_id: None | str | Unset = UNSET
    metadata: InvestmentSessionAttributesMetadata | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    events: list[InvestmentSessionAttributesEventsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.investment_session_attributes_events_item import InvestmentSessionAttributesEventsItem # noqa: PLC0415
        from ..models.investment_session_attributes_metadata import InvestmentSessionAttributesMetadata # noqa: PLC0415
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        url = self.url

        spv_id = self.spv_id

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        allocation_cents: int | None | Unset
        if isinstance(self.allocation_cents, Unset):
            allocation_cents = UNSET
        else:
            allocation_cents = self.allocation_cents

        kyc_status: str | Unset = UNSET
        if not isinstance(self.kyc_status, Unset):
            kyc_status = self.kyc_status.value


        funding_status: str | Unset = UNSET
        if not isinstance(self.funding_status, Unset):
            funding_status = self.funding_status.value


        investment_id: None | str | Unset
        if isinstance(self.investment_id, Unset):
            investment_id = UNSET
        else:
            investment_id = self.investment_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

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
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url
        if spv_id is not UNSET:
            field_dict["spv_id"] = spv_id
        if email is not UNSET:
            field_dict["email"] = email
        if allocation_cents is not UNSET:
            field_dict["allocation_cents"] = allocation_cents
        if kyc_status is not UNSET:
            field_dict["kyc_status"] = kyc_status
        if funding_status is not UNSET:
            field_dict["funding_status"] = funding_status
        if investment_id is not UNSET:
            field_dict["investment_id"] = investment_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investment_session_attributes_events_item import InvestmentSessionAttributesEventsItem # noqa: PLC0415
        from ..models.investment_session_attributes_metadata import InvestmentSessionAttributesMetadata # noqa: PLC0415
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: InvestmentSessionAttributesStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = InvestmentSessionAttributesStatus(_status)




        url = d.pop("url", UNSET)

        spv_id = d.pop("spv_id", UNSET)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_allocation_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        allocation_cents = _parse_allocation_cents(d.pop("allocation_cents", UNSET))


        _kyc_status = d.pop("kyc_status", UNSET)
        kyc_status: InvestmentSessionAttributesKycStatus | Unset
        if isinstance(_kyc_status,  Unset):
            kyc_status = UNSET
        else:
            kyc_status = InvestmentSessionAttributesKycStatus(_kyc_status)




        _funding_status = d.pop("funding_status", UNSET)
        funding_status: InvestmentSessionAttributesFundingStatus | Unset
        if isinstance(_funding_status,  Unset):
            funding_status = UNSET
        else:
            funding_status = InvestmentSessionAttributesFundingStatus(_funding_status)




        def _parse_investment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investment_id = _parse_investment_id(d.pop("investment_id", UNSET))


        _metadata = d.pop("metadata", UNSET)
        metadata: InvestmentSessionAttributesMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = InvestmentSessionAttributesMetadata.from_dict(_metadata)




        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)



                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))


        _events = d.pop("events", UNSET)
        events: list[InvestmentSessionAttributesEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = InvestmentSessionAttributesEventsItem.from_dict(events_item_data)



                events.append(events_item)


        investment_session_attributes = cls(
            status=status,
            url=url,
            spv_id=spv_id,
            email=email,
            allocation_cents=allocation_cents,
            kyc_status=kyc_status,
            funding_status=funding_status,
            investment_id=investment_id,
            metadata=metadata,
            created_at=created_at,
            expires_at=expires_at,
            events=events,
        )


        investment_session_attributes.additional_properties = d
        return investment_session_attributes

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
