from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CurrentRaise")



@_attrs_define
class CurrentRaise:
    """ The round the page shows this viewer, with its linked legs combined.

        Attributes:
            offering_id (str | Unset): The displayed offering (`ofr_...`); fetch it with `/offerings/{id}`.
            offering_ids (list[str] | Unset): Every live leg combined into `amount_raised` that the viewer may see (e.g. a
                Reg CF round and its Reg D round).
            testing_the_waters (bool | Unset): True when the current raise collects non-binding reservations, not
                investments.
            amount_raised (None | str | Unset): Raised across the combined legs, on Wefunder, USD decimal string.
            funding_target (None | str | Unset):
            investor_count (int | None | Unset):
            oversubscribed (bool | Unset):
            closes_at (datetime.datetime | None | Unset):
     """

    offering_id: str | Unset = UNSET
    offering_ids: list[str] | Unset = UNSET
    testing_the_waters: bool | Unset = UNSET
    amount_raised: None | str | Unset = UNSET
    funding_target: None | str | Unset = UNSET
    investor_count: int | None | Unset = UNSET
    oversubscribed: bool | Unset = UNSET
    closes_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        offering_id = self.offering_id

        offering_ids: list[str] | Unset = UNSET
        if not isinstance(self.offering_ids, Unset):
            offering_ids = self.offering_ids



        testing_the_waters = self.testing_the_waters

        amount_raised: None | str | Unset
        if isinstance(self.amount_raised, Unset):
            amount_raised = UNSET
        else:
            amount_raised = self.amount_raised

        funding_target: None | str | Unset
        if isinstance(self.funding_target, Unset):
            funding_target = UNSET
        else:
            funding_target = self.funding_target

        investor_count: int | None | Unset
        if isinstance(self.investor_count, Unset):
            investor_count = UNSET
        else:
            investor_count = self.investor_count

        oversubscribed = self.oversubscribed

        closes_at: None | str | Unset
        if isinstance(self.closes_at, Unset):
            closes_at = UNSET
        elif isinstance(self.closes_at, datetime.datetime):
            closes_at = self.closes_at.isoformat()
        else:
            closes_at = self.closes_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if offering_id is not UNSET:
            field_dict["offering_id"] = offering_id
        if offering_ids is not UNSET:
            field_dict["offering_ids"] = offering_ids
        if testing_the_waters is not UNSET:
            field_dict["testing_the_waters"] = testing_the_waters
        if amount_raised is not UNSET:
            field_dict["amount_raised"] = amount_raised
        if funding_target is not UNSET:
            field_dict["funding_target"] = funding_target
        if investor_count is not UNSET:
            field_dict["investor_count"] = investor_count
        if oversubscribed is not UNSET:
            field_dict["oversubscribed"] = oversubscribed
        if closes_at is not UNSET:
            field_dict["closes_at"] = closes_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offering_id = d.pop("offering_id", UNSET)

        offering_ids = cast(list[str], d.pop("offering_ids", UNSET))


        testing_the_waters = d.pop("testing_the_waters", UNSET)

        def _parse_amount_raised(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount_raised = _parse_amount_raised(d.pop("amount_raised", UNSET))


        def _parse_funding_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        funding_target = _parse_funding_target(d.pop("funding_target", UNSET))


        def _parse_investor_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        investor_count = _parse_investor_count(d.pop("investor_count", UNSET))


        oversubscribed = d.pop("oversubscribed", UNSET)

        def _parse_closes_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closes_at_type_0 = datetime.datetime.fromisoformat(data)



                return closes_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closes_at = _parse_closes_at(d.pop("closes_at", UNSET))


        current_raise = cls(
            offering_id=offering_id,
            offering_ids=offering_ids,
            testing_the_waters=testing_the_waters,
            amount_raised=amount_raised,
            funding_target=funding_target,
            investor_count=investor_count,
            oversubscribed=oversubscribed,
            closes_at=closes_at,
        )


        current_raise.additional_properties = d
        return current_raise

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
