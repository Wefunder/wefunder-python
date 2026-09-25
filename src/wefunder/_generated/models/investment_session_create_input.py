from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.investment_session_create_input_metadata_type_0 import InvestmentSessionCreateInputMetadataType0





T = TypeVar("T", bound="InvestmentSessionCreateInput")



@_attrs_define
class InvestmentSessionCreateInput:
    """ Either `email` (invite an unknown recipient) or `wefunder_user_id` (target an
    existing Wefunder user) should be provided. `spv_id` is required on
    `POST /partner/investment_sessions`; on the deprecated SPV-nested path the
    SPV comes from the URL instead.

        Attributes:
            spv_id (None | str | Unset): The SPV to invest into (prefixed, e.g. `spv_abc123`). Example: spv_abc123.
            email (None | str | Unset):  Example: investor@example.com.
            wefunder_user_id (None | str | Unset):  Example: usr_existing123.
            allocation_cents (int | None | Unset): Fixed investment amount, in cents (whole dollars only). Locks the
                checkout to exactly this value, overriding the SPV's min/max
                purchase range. Omit to let the recipient choose an amount within
                that range.
                 Example: 5000000.
            success_url (None | str | Unset): Where to send the recipient after they complete the session. Example:
                https://partner.com/done.
            expires_in_hours (int | None | Unset): Session lifetime in hours (default 720, i.e. 30 days). Example: 72.
            metadata (InvestmentSessionCreateInputMetadataType0 | None | Unset): Free-form key/value pairs stored with the
                session and echoed back on reads.
            intent_id (None | str | Unset): The Intent that gated the SPV's creation, for audit; stored in `metadata`.
                Example: int_abc123.
     """

    spv_id: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    wefunder_user_id: None | str | Unset = UNSET
    allocation_cents: int | None | Unset = UNSET
    success_url: None | str | Unset = UNSET
    expires_in_hours: int | None | Unset = UNSET
    metadata: InvestmentSessionCreateInputMetadataType0 | None | Unset = UNSET
    intent_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.investment_session_create_input_metadata_type_0 import InvestmentSessionCreateInputMetadataType0 # noqa: PLC0415
        spv_id: None | str | Unset
        if isinstance(self.spv_id, Unset):
            spv_id = UNSET
        else:
            spv_id = self.spv_id

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

        allocation_cents: int | None | Unset
        if isinstance(self.allocation_cents, Unset):
            allocation_cents = UNSET
        else:
            allocation_cents = self.allocation_cents

        success_url: None | str | Unset
        if isinstance(self.success_url, Unset):
            success_url = UNSET
        else:
            success_url = self.success_url

        expires_in_hours: int | None | Unset
        if isinstance(self.expires_in_hours, Unset):
            expires_in_hours = UNSET
        else:
            expires_in_hours = self.expires_in_hours

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, InvestmentSessionCreateInputMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        intent_id: None | str | Unset
        if isinstance(self.intent_id, Unset):
            intent_id = UNSET
        else:
            intent_id = self.intent_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if spv_id is not UNSET:
            field_dict["spv_id"] = spv_id
        if email is not UNSET:
            field_dict["email"] = email
        if wefunder_user_id is not UNSET:
            field_dict["wefunder_user_id"] = wefunder_user_id
        if allocation_cents is not UNSET:
            field_dict["allocation_cents"] = allocation_cents
        if success_url is not UNSET:
            field_dict["success_url"] = success_url
        if expires_in_hours is not UNSET:
            field_dict["expires_in_hours"] = expires_in_hours
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if intent_id is not UNSET:
            field_dict["intent_id"] = intent_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investment_session_create_input_metadata_type_0 import InvestmentSessionCreateInputMetadataType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_spv_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spv_id = _parse_spv_id(d.pop("spv_id", UNSET))


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


        def _parse_allocation_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        allocation_cents = _parse_allocation_cents(d.pop("allocation_cents", UNSET))


        def _parse_success_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        success_url = _parse_success_url(d.pop("success_url", UNSET))


        def _parse_expires_in_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_in_hours = _parse_expires_in_hours(d.pop("expires_in_hours", UNSET))


        def _parse_metadata(data: object) -> InvestmentSessionCreateInputMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = InvestmentSessionCreateInputMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestmentSessionCreateInputMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_intent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intent_id = _parse_intent_id(d.pop("intent_id", UNSET))


        investment_session_create_input = cls(
            spv_id=spv_id,
            email=email,
            wefunder_user_id=wefunder_user_id,
            allocation_cents=allocation_cents,
            success_url=success_url,
            expires_in_hours=expires_in_hours,
            metadata=metadata,
            intent_id=intent_id,
        )


        investment_session_create_input.additional_properties = d
        return investment_session_create_input

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
