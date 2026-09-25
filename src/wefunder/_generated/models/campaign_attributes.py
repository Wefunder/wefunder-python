from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CampaignAttributes")



@_attrs_define
class CampaignAttributes:
    """ 
        Attributes:
            state (str | Unset):  Example: active.
            company_id (int | Unset): Internal integer id. Deprecated — use `company` (`co_...`) instead. Example: 101.
            company (None | str | Unset): The company's id (`co_...`). Example: co_8Kd0aB3xQ9k2vF8mNp1zT5wY.
            company_name (str | Unset):  Example: My Startup Inc..
            company_url (None | str | Unset):  Example: my-startup-inc.
            created_at (datetime.datetime | Unset):  Example: 2023-01-10T09:00:00Z.
            updated_at (datetime.datetime | Unset):  Example: 2023-03-15T14:30:00Z.
            closed_at (datetime.datetime | None | Unset):  Example: 2023-06-30T23:59:59Z.
            amount_raised (float | None | Unset):  Example: 25000.
            investor_count (int | Unset):  Example: 42.
     """

    state: str | Unset = UNSET
    company_id: int | Unset = UNSET
    company: None | str | Unset = UNSET
    company_name: str | Unset = UNSET
    company_url: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    amount_raised: float | None | Unset = UNSET
    investor_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        state = self.state

        company_id = self.company_id

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        company_name = self.company_name

        company_url: None | str | Unset
        if isinstance(self.company_url, Unset):
            company_url = UNSET
        else:
            company_url = self.company_url

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        amount_raised: float | None | Unset
        if isinstance(self.amount_raised, Unset):
            amount_raised = UNSET
        else:
            amount_raised = self.amount_raised

        investor_count = self.investor_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if state is not UNSET:
            field_dict["state"] = state
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if company is not UNSET:
            field_dict["company"] = company
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_url is not UNSET:
            field_dict["company_url"] = company_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if amount_raised is not UNSET:
            field_dict["amount_raised"] = amount_raised
        if investor_count is not UNSET:
            field_dict["investor_count"] = investor_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = d.pop("state", UNSET)

        company_id = d.pop("company_id", UNSET)

        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))


        company_name = d.pop("company_name", UNSET)

        def _parse_company_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_url = _parse_company_url(d.pop("company_url", UNSET))


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


        def _parse_amount_raised(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount_raised = _parse_amount_raised(d.pop("amount_raised", UNSET))


        investor_count = d.pop("investor_count", UNSET)

        campaign_attributes = cls(
            state=state,
            company_id=company_id,
            company=company,
            company_name=company_name,
            company_url=company_url,
            created_at=created_at,
            updated_at=updated_at,
            closed_at=closed_at,
            amount_raised=amount_raised,
            investor_count=investor_count,
        )


        campaign_attributes.additional_properties = d
        return campaign_attributes

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
