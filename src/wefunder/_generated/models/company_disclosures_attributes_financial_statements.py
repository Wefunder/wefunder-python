from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.fiscal_year_financials import FiscalYearFinancials





T = TypeVar("T", bound="CompanyDisclosuresAttributesFinancialStatements")



@_attrs_define
class CompanyDisclosuresAttributesFinancialStatements:
    """ One column per fiscal year on file; a year with no figures is omitted.

        Attributes:
            most_recent (FiscalYearFinancials | Unset): One fiscal year's figures from the Form C, USD decimal strings (null
                where not reported).
            prior (FiscalYearFinancials | Unset): One fiscal year's figures from the Form C, USD decimal strings (null where
                not reported).
            prior_prior (FiscalYearFinancials | Unset): One fiscal year's figures from the Form C, USD decimal strings (null
                where not reported).
     """

    most_recent: FiscalYearFinancials | Unset = UNSET
    prior: FiscalYearFinancials | Unset = UNSET
    prior_prior: FiscalYearFinancials | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.fiscal_year_financials import FiscalYearFinancials # noqa: PLC0415
        most_recent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.most_recent, Unset):
            most_recent = self.most_recent.to_dict()

        prior: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prior, Unset):
            prior = self.prior.to_dict()

        prior_prior: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prior_prior, Unset):
            prior_prior = self.prior_prior.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if most_recent is not UNSET:
            field_dict["most_recent"] = most_recent
        if prior is not UNSET:
            field_dict["prior"] = prior
        if prior_prior is not UNSET:
            field_dict["prior_prior"] = prior_prior

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fiscal_year_financials import FiscalYearFinancials # noqa: PLC0415
        d = dict(src_dict)
        _most_recent = d.pop("most_recent", UNSET)
        most_recent: FiscalYearFinancials | Unset
        if isinstance(_most_recent,  Unset):
            most_recent = UNSET
        else:
            most_recent = FiscalYearFinancials.from_dict(_most_recent)




        _prior = d.pop("prior", UNSET)
        prior: FiscalYearFinancials | Unset
        if isinstance(_prior,  Unset):
            prior = UNSET
        else:
            prior = FiscalYearFinancials.from_dict(_prior)




        _prior_prior = d.pop("prior_prior", UNSET)
        prior_prior: FiscalYearFinancials | Unset
        if isinstance(_prior_prior,  Unset):
            prior_prior = UNSET
        else:
            prior_prior = FiscalYearFinancials.from_dict(_prior_prior)




        company_disclosures_attributes_financial_statements = cls(
            most_recent=most_recent,
            prior=prior,
            prior_prior=prior_prior,
        )


        company_disclosures_attributes_financial_statements.additional_properties = d
        return company_disclosures_attributes_financial_statements

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
