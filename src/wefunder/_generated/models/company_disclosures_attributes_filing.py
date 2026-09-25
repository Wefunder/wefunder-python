from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.exemption import Exemption





T = TypeVar("T", bound="CompanyDisclosuresAttributesFiling")



@_attrs_define
class CompanyDisclosuresAttributesFiling:
    """ 
        Attributes:
            exemption (Exemption | Unset): The offering's SEC exemption, in market vocabulary.
            sec_filing_url (None | str | Unset): The filing on sec.gov, when filed.
            filed (bool | Unset):
            statement_date (datetime.date | None | Unset): The date the financial statements are as of.
            fiscal_year_end (None | str | Unset): `--MM-DD` (ISO 8601 recurring date), e.g. `--12-31`.
     """

    exemption: Exemption | Unset = UNSET
    sec_filing_url: None | str | Unset = UNSET
    filed: bool | Unset = UNSET
    statement_date: datetime.date | None | Unset = UNSET
    fiscal_year_end: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.exemption import Exemption # noqa: PLC0415
        exemption: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exemption, Unset):
            exemption = self.exemption.to_dict()

        sec_filing_url: None | str | Unset
        if isinstance(self.sec_filing_url, Unset):
            sec_filing_url = UNSET
        else:
            sec_filing_url = self.sec_filing_url

        filed = self.filed

        statement_date: None | str | Unset
        if isinstance(self.statement_date, Unset):
            statement_date = UNSET
        elif isinstance(self.statement_date, datetime.date):
            statement_date = self.statement_date.isoformat()
        else:
            statement_date = self.statement_date

        fiscal_year_end: None | str | Unset
        if isinstance(self.fiscal_year_end, Unset):
            fiscal_year_end = UNSET
        else:
            fiscal_year_end = self.fiscal_year_end


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if exemption is not UNSET:
            field_dict["exemption"] = exemption
        if sec_filing_url is not UNSET:
            field_dict["sec_filing_url"] = sec_filing_url
        if filed is not UNSET:
            field_dict["filed"] = filed
        if statement_date is not UNSET:
            field_dict["statement_date"] = statement_date
        if fiscal_year_end is not UNSET:
            field_dict["fiscal_year_end"] = fiscal_year_end

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exemption import Exemption # noqa: PLC0415
        d = dict(src_dict)
        _exemption = d.pop("exemption", UNSET)
        exemption: Exemption | Unset
        if isinstance(_exemption,  Unset):
            exemption = UNSET
        else:
            exemption = Exemption.from_dict(_exemption)




        def _parse_sec_filing_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sec_filing_url = _parse_sec_filing_url(d.pop("sec_filing_url", UNSET))


        filed = d.pop("filed", UNSET)

        def _parse_statement_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                statement_date_type_0 = datetime.date.fromisoformat(data)



                return statement_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        statement_date = _parse_statement_date(d.pop("statement_date", UNSET))


        def _parse_fiscal_year_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fiscal_year_end = _parse_fiscal_year_end(d.pop("fiscal_year_end", UNSET))


        company_disclosures_attributes_filing = cls(
            exemption=exemption,
            sec_filing_url=sec_filing_url,
            filed=filed,
            statement_date=statement_date,
            fiscal_year_end=fiscal_year_end,
        )


        company_disclosures_attributes_filing.additional_properties = d
        return company_disclosures_attributes_filing

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
