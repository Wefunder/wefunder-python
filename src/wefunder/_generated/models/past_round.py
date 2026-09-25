from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.past_round_source import PastRoundSource
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.exemption import Exemption





T = TypeVar("T", bound="PastRound")



@_attrs_define
class PastRound:
    """ 
        Attributes:
            offering_id (None | str | Unset): The Wefunder offering (`ofr_...`) when `source` is `wefunder`; null for a
                reported round.
            source (PastRoundSource | Unset): `wefunder`: observed on this platform. `reported`: disclosed by the founder as
                raised off-platform (verified per the page's rules, but not observed here).
            exemption (Exemption | Unset): The offering's SEC exemption, in market vocabulary.
            amount_raised (None | str | Unset):
            investor_count (int | None | Unset):
            opened_at (datetime.datetime | None | Unset):
            closed_at (datetime.datetime | None | Unset):
     """

    offering_id: None | str | Unset = UNSET
    source: PastRoundSource | Unset = UNSET
    exemption: Exemption | Unset = UNSET
    amount_raised: None | str | Unset = UNSET
    investor_count: int | None | Unset = UNSET
    opened_at: datetime.datetime | None | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.exemption import Exemption # noqa: PLC0415
        offering_id: None | str | Unset
        if isinstance(self.offering_id, Unset):
            offering_id = UNSET
        else:
            offering_id = self.offering_id

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value


        exemption: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exemption, Unset):
            exemption = self.exemption.to_dict()

        amount_raised: None | str | Unset
        if isinstance(self.amount_raised, Unset):
            amount_raised = UNSET
        else:
            amount_raised = self.amount_raised

        investor_count: int | None | Unset
        if isinstance(self.investor_count, Unset):
            investor_count = UNSET
        else:
            investor_count = self.investor_count

        opened_at: None | str | Unset
        if isinstance(self.opened_at, Unset):
            opened_at = UNSET
        elif isinstance(self.opened_at, datetime.datetime):
            opened_at = self.opened_at.isoformat()
        else:
            opened_at = self.opened_at

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if offering_id is not UNSET:
            field_dict["offering_id"] = offering_id
        if source is not UNSET:
            field_dict["source"] = source
        if exemption is not UNSET:
            field_dict["exemption"] = exemption
        if amount_raised is not UNSET:
            field_dict["amount_raised"] = amount_raised
        if investor_count is not UNSET:
            field_dict["investor_count"] = investor_count
        if opened_at is not UNSET:
            field_dict["opened_at"] = opened_at
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exemption import Exemption # noqa: PLC0415
        d = dict(src_dict)
        def _parse_offering_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        offering_id = _parse_offering_id(d.pop("offering_id", UNSET))


        _source = d.pop("source", UNSET)
        source: PastRoundSource | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = PastRoundSource(_source)




        _exemption = d.pop("exemption", UNSET)
        exemption: Exemption | Unset
        if isinstance(_exemption,  Unset):
            exemption = UNSET
        else:
            exemption = Exemption.from_dict(_exemption)




        def _parse_amount_raised(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount_raised = _parse_amount_raised(d.pop("amount_raised", UNSET))


        def _parse_investor_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        investor_count = _parse_investor_count(d.pop("investor_count", UNSET))


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


        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)



                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))


        past_round = cls(
            offering_id=offering_id,
            source=source,
            exemption=exemption,
            amount_raised=amount_raised,
            investor_count=investor_count,
            opened_at=opened_at,
            closed_at=closed_at,
        )


        past_round.additional_properties = d
        return past_round

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
