from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.syndicate_deal_attributes_status import SyndicateDealAttributesStatus
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.convertible_note_security import ConvertibleNoteSecurity
  from ..models.debt_security import DebtSecurity
  from ..models.equity_security import EquitySecurity
  from ..models.exemption import Exemption
  from ..models.fund_security import FundSecurity
  from ..models.other_security import OtherSecurity
  from ..models.revenue_share_security import RevenueShareSecurity
  from ..models.safe_security import SafeSecurity





T = TypeVar("T", bound="SyndicateDealAttributes")



@_attrs_define
class SyndicateDealAttributes:
    """ 
        Attributes:
            name (str | Unset):  Example: Acme Corp Series A.
            status (SyndicateDealAttributesStatus | Unset): Where the round is in its life (same values as an offering's
                `status`). Example: open.
            company_name (str | Unset):  Example: Acme Corp.
            company_id (int | Unset): Internal integer id. Deprecated — use `company` (`co_...`) instead. Example: 1234.
            company (None | str | Unset): The company's id (`co_...`). Example: co_8Kd0aB3xQ9k2vF8mNp1zT5wY.
            company_url (None | str | Unset): Company slug/URL path Example: acme-corp.
            company_logo_url (None | str | Unset): Company logo URL Example:
                https://uploads.wefunder.com/uploads/company/logo/1234/large_logo.png.
            amount_raised (None | str | Unset): Amount in escrow in cents, as a string to avoid floating-point precision
                issues Example: 23000000.
            investor_count (int | Unset): Count of distinct active investors Example: 47.
            funding_target (None | str | Unset): Target funding amount in cents, as a string Example: 50000000.
            exemption (Exemption | None | Unset): The SEC exemption the deal is offered under, in market vocabulary.
            security (ConvertibleNoteSecurity | DebtSecurity | EquitySecurity | FundSecurity | None | OtherSecurity |
                RevenueShareSecurity | SafeSecurity | Unset): What the deal issues, as a discriminated union on `type` (see
                `Security`).
            min_investment (None | str | Unset): Minimum investment amount in cents, as a string Example: 10000.
            max_investment (None | str | Unset): Maximum investment amount in cents, as a string Example: 5000000.
            description (None | str | Unset): Deal funding purpose / description Example: Example text.
            created_at (datetime.datetime | Unset):  Example: 2025-03-01T12:00:00Z.
            updated_at (datetime.datetime | Unset):  Example: 2025-03-01T12:00:00Z.
            closed_at (datetime.datetime | None | Unset):  Example: 2025-03-01T12:00:00Z.
            funding_started_at (datetime.datetime | None | Unset): ISO 8601 timestamp when funding opened Example:
                2025-03-01T12:00:00Z.
     """

    name: str | Unset = UNSET
    status: SyndicateDealAttributesStatus | Unset = UNSET
    company_name: str | Unset = UNSET
    company_id: int | Unset = UNSET
    company: None | str | Unset = UNSET
    company_url: None | str | Unset = UNSET
    company_logo_url: None | str | Unset = UNSET
    amount_raised: None | str | Unset = UNSET
    investor_count: int | Unset = UNSET
    funding_target: None | str | Unset = UNSET
    exemption: Exemption | None | Unset = UNSET
    security: ConvertibleNoteSecurity | DebtSecurity | EquitySecurity | FundSecurity | None | OtherSecurity | RevenueShareSecurity | SafeSecurity | Unset = UNSET
    min_investment: None | str | Unset = UNSET
    max_investment: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    funding_started_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.convertible_note_security import ConvertibleNoteSecurity # noqa: PLC0415
        from ..models.debt_security import DebtSecurity # noqa: PLC0415
        from ..models.equity_security import EquitySecurity # noqa: PLC0415
        from ..models.exemption import Exemption # noqa: PLC0415
        from ..models.fund_security import FundSecurity # noqa: PLC0415
        from ..models.other_security import OtherSecurity # noqa: PLC0415
        from ..models.revenue_share_security import RevenueShareSecurity # noqa: PLC0415
        from ..models.safe_security import SafeSecurity # noqa: PLC0415
        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        company_name = self.company_name

        company_id = self.company_id

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        company_url: None | str | Unset
        if isinstance(self.company_url, Unset):
            company_url = UNSET
        else:
            company_url = self.company_url

        company_logo_url: None | str | Unset
        if isinstance(self.company_logo_url, Unset):
            company_logo_url = UNSET
        else:
            company_logo_url = self.company_logo_url

        amount_raised: None | str | Unset
        if isinstance(self.amount_raised, Unset):
            amount_raised = UNSET
        else:
            amount_raised = self.amount_raised

        investor_count = self.investor_count

        funding_target: None | str | Unset
        if isinstance(self.funding_target, Unset):
            funding_target = UNSET
        else:
            funding_target = self.funding_target

        exemption: dict[str, Any] | None | Unset
        if isinstance(self.exemption, Unset):
            exemption = UNSET
        elif isinstance(self.exemption, Exemption):
            exemption = self.exemption.to_dict()
        else:
            exemption = self.exemption

        security: dict[str, Any] | None | Unset
        if isinstance(self.security, Unset):
            security = UNSET
        elif isinstance(self.security, SafeSecurity):
            security = self.security.to_dict()
        elif isinstance(self.security, EquitySecurity):
            security = self.security.to_dict()
        elif isinstance(self.security, ConvertibleNoteSecurity):
            security = self.security.to_dict()
        elif isinstance(self.security, RevenueShareSecurity):
            security = self.security.to_dict()
        elif isinstance(self.security, DebtSecurity):
            security = self.security.to_dict()
        elif isinstance(self.security, FundSecurity):
            security = self.security.to_dict()
        elif isinstance(self.security, OtherSecurity):
            security = self.security.to_dict()
        else:
            security = self.security

        min_investment: None | str | Unset
        if isinstance(self.min_investment, Unset):
            min_investment = UNSET
        else:
            min_investment = self.min_investment

        max_investment: None | str | Unset
        if isinstance(self.max_investment, Unset):
            max_investment = UNSET
        else:
            max_investment = self.max_investment

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        funding_started_at: None | str | Unset
        if isinstance(self.funding_started_at, Unset):
            funding_started_at = UNSET
        elif isinstance(self.funding_started_at, datetime.datetime):
            funding_started_at = self.funding_started_at.isoformat()
        else:
            funding_started_at = self.funding_started_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if company is not UNSET:
            field_dict["company"] = company
        if company_url is not UNSET:
            field_dict["company_url"] = company_url
        if company_logo_url is not UNSET:
            field_dict["company_logo_url"] = company_logo_url
        if amount_raised is not UNSET:
            field_dict["amount_raised"] = amount_raised
        if investor_count is not UNSET:
            field_dict["investor_count"] = investor_count
        if funding_target is not UNSET:
            field_dict["funding_target"] = funding_target
        if exemption is not UNSET:
            field_dict["exemption"] = exemption
        if security is not UNSET:
            field_dict["security"] = security
        if min_investment is not UNSET:
            field_dict["min_investment"] = min_investment
        if max_investment is not UNSET:
            field_dict["max_investment"] = max_investment
        if description is not UNSET:
            field_dict["description"] = description
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if funding_started_at is not UNSET:
            field_dict["funding_started_at"] = funding_started_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.convertible_note_security import ConvertibleNoteSecurity # noqa: PLC0415
        from ..models.debt_security import DebtSecurity # noqa: PLC0415
        from ..models.equity_security import EquitySecurity # noqa: PLC0415
        from ..models.exemption import Exemption # noqa: PLC0415
        from ..models.fund_security import FundSecurity # noqa: PLC0415
        from ..models.other_security import OtherSecurity # noqa: PLC0415
        from ..models.revenue_share_security import RevenueShareSecurity # noqa: PLC0415
        from ..models.safe_security import SafeSecurity # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: SyndicateDealAttributesStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = SyndicateDealAttributesStatus(_status)




        company_name = d.pop("company_name", UNSET)

        company_id = d.pop("company_id", UNSET)

        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))


        def _parse_company_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_url = _parse_company_url(d.pop("company_url", UNSET))


        def _parse_company_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_logo_url = _parse_company_logo_url(d.pop("company_logo_url", UNSET))


        def _parse_amount_raised(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount_raised = _parse_amount_raised(d.pop("amount_raised", UNSET))


        investor_count = d.pop("investor_count", UNSET)

        def _parse_funding_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        funding_target = _parse_funding_target(d.pop("funding_target", UNSET))


        def _parse_exemption(data: object) -> Exemption | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                exemption_type_0 = Exemption.from_dict(data)



                return exemption_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Exemption | None | Unset, data)

        exemption = _parse_exemption(d.pop("exemption", UNSET))


        def _parse_security(data: object) -> ConvertibleNoteSecurity | DebtSecurity | EquitySecurity | FundSecurity | None | OtherSecurity | RevenueShareSecurity | SafeSecurity | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_type_0 = SafeSecurity.from_dict(data)



                return componentsschemas_security_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_type_1 = EquitySecurity.from_dict(data)



                return componentsschemas_security_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_type_2 = ConvertibleNoteSecurity.from_dict(data)



                return componentsschemas_security_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_type_3 = RevenueShareSecurity.from_dict(data)



                return componentsschemas_security_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_type_4 = DebtSecurity.from_dict(data)



                return componentsschemas_security_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_type_5 = FundSecurity.from_dict(data)



                return componentsschemas_security_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_type_6 = OtherSecurity.from_dict(data)



                return componentsschemas_security_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConvertibleNoteSecurity | DebtSecurity | EquitySecurity | FundSecurity | None | OtherSecurity | RevenueShareSecurity | SafeSecurity | Unset, data)

        security = _parse_security(d.pop("security", UNSET))


        def _parse_min_investment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        min_investment = _parse_min_investment(d.pop("min_investment", UNSET))


        def _parse_max_investment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_investment = _parse_max_investment(d.pop("max_investment", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


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


        def _parse_funding_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                funding_started_at_type_0 = datetime.datetime.fromisoformat(data)



                return funding_started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        funding_started_at = _parse_funding_started_at(d.pop("funding_started_at", UNSET))


        syndicate_deal_attributes = cls(
            name=name,
            status=status,
            company_name=company_name,
            company_id=company_id,
            company=company,
            company_url=company_url,
            company_logo_url=company_logo_url,
            amount_raised=amount_raised,
            investor_count=investor_count,
            funding_target=funding_target,
            exemption=exemption,
            security=security,
            min_investment=min_investment,
            max_investment=max_investment,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            closed_at=closed_at,
            funding_started_at=funding_started_at,
        )


        syndicate_deal_attributes.additional_properties = d
        return syndicate_deal_attributes

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
