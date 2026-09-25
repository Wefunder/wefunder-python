from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.portfolio_holding_status import PortfolioHoldingStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.portfolio_company_ref import PortfolioCompanyRef





T = TypeVar("T", bound="PortfolioHolding")



@_attrs_define
class PortfolioHolding:
    """ A company a fund vehicle invested in — one entry per company, with the
    status of the most recent investment when the fund invested in the same
    company more than once.

        Attributes:
            company (PortfolioCompanyRef | Unset): The company behind a portfolio position or holding.
            status (PortfolioHoldingStatus | Unset):
     """

    company: PortfolioCompanyRef | Unset = UNSET
    status: PortfolioHoldingStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.portfolio_company_ref import PortfolioCompanyRef # noqa: PLC0415
        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if company is not UNSET:
            field_dict["company"] = company
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portfolio_company_ref import PortfolioCompanyRef # noqa: PLC0415
        d = dict(src_dict)
        _company = d.pop("company", UNSET)
        company: PortfolioCompanyRef | Unset
        if isinstance(_company,  Unset):
            company = UNSET
        else:
            company = PortfolioCompanyRef.from_dict(_company)




        _status = d.pop("status", UNSET)
        status: PortfolioHoldingStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = PortfolioHoldingStatus(_status)




        portfolio_holding = cls(
            company=company,
            status=status,
        )


        portfolio_holding.additional_properties = d
        return portfolio_holding

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
