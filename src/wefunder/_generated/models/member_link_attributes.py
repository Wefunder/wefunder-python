from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_link_attributes_state import MemberLinkAttributesState
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberLinkAttributes")


@_attrs_define
class MemberLinkAttributes:
    """
    Attributes:
        url (str | Unset): The offering's deal page carrying this link's token. Send the member here. Example:
            https://wefunder.com/arc-hockey?invite_token=kL273wxd4DGb896V87ddtLE9.
        state (MemberLinkAttributesState | Unset): `created` nobody has redeemed it; `bound` a Wefunder account holds
            it;
            `invested` that account invested in this offering after the link was
            minted (kept after a cancel); `canceled` canceled before any investment.
        reference (None | str | Unset): Your member id, as passed at create. Example: member_8812.
        wefunder_user_id (None | str | Unset): The bound account's `usr_` id. Never an email. Example:
            usr_4fQ8sLm2Vx9TbR7nKc3YdHpW.
        investment_id (None | str | Unset): The `inv_` id of the investment made through this link. Example:
            inv_7hTk2PqW9mXc4RbN8vLs3DyF.
        offering (str | Unset): The offering's id. Example: ofr_2nVb8KxQ4tLm9RcW7pHs3FdY.
        created_at (datetime.datetime | Unset):
    """

    url: str | Unset = UNSET
    state: MemberLinkAttributesState | Unset = UNSET
    reference: None | str | Unset = UNSET
    wefunder_user_id: None | str | Unset = UNSET
    investment_id: None | str | Unset = UNSET
    offering: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        wefunder_user_id: None | str | Unset
        if isinstance(self.wefunder_user_id, Unset):
            wefunder_user_id = UNSET
        else:
            wefunder_user_id = self.wefunder_user_id

        investment_id: None | str | Unset
        if isinstance(self.investment_id, Unset):
            investment_id = UNSET
        else:
            investment_id = self.investment_id

        offering = self.offering

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if state is not UNSET:
            field_dict["state"] = state
        if reference is not UNSET:
            field_dict["reference"] = reference
        if wefunder_user_id is not UNSET:
            field_dict["wefunder_user_id"] = wefunder_user_id
        if investment_id is not UNSET:
            field_dict["investment_id"] = investment_id
        if offering is not UNSET:
            field_dict["offering"] = offering
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _state = d.pop("state", UNSET)
        state: MemberLinkAttributesState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = MemberLinkAttributesState(_state)

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        def _parse_wefunder_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wefunder_user_id = _parse_wefunder_user_id(d.pop("wefunder_user_id", UNSET))

        def _parse_investment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investment_id = _parse_investment_id(d.pop("investment_id", UNSET))

        offering = d.pop("offering", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        member_link_attributes = cls(
            url=url,
            state=state,
            reference=reference,
            wefunder_user_id=wefunder_user_id,
            investment_id=investment_id,
            offering=offering,
            created_at=created_at,
        )

        member_link_attributes.additional_properties = d
        return member_link_attributes

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
