from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.offering_attributes_status import OfferingAttributesStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.convertible_note_security import ConvertibleNoteSecurity
    from ..models.debt_security import DebtSecurity
    from ..models.equity_security import EquitySecurity
    from ..models.exemption import Exemption
    from ..models.fund_security import FundSecurity
    from ..models.offering_attributes_intended_security_type_0 import OfferingAttributesIntendedSecurityType0
    from ..models.other_security import OtherSecurity
    from ..models.revenue_share_security import RevenueShareSecurity
    from ..models.safe_security import SafeSecurity
    from ..models.tag_ref import TagRef


T = TypeVar("T", bound="OfferingAttributes")


@_attrs_define
class OfferingAttributes:
    """
    Attributes:
        company_name (str | Unset):  Example: ZeroBorder Self-Banking Centers.
        tagline (None | str | Unset):  Example: Example tagline.
        url (str | Unset): The company's Wefunder profile URL. Example: https://wefunder.com/zeroborder.
        card_image_url (None | str | Unset): Absolute URL of the explore card image, or null if the company has none.
            Example: https://uploads.wefunder.com/uploads/company/custom_card_photo/189517/large_card.jpg.
        logo_url (None | str | Unset): Absolute URL of the company logo, or null if the company has none. Example:
            https://uploads.wefunder.com/uploads/company/logo/189517/large_logo.png.
        exemption (Exemption | Unset): The offering's SEC exemption, in market vocabulary.
        security (ConvertibleNoteSecurity | DebtSecurity | EquitySecurity | FundSecurity | None | OtherSecurity |
            RevenueShareSecurity | SafeSecurity | Unset): What the offering issues, as a discriminated union on `type` (see
            `Security`).
            Null for a Testing-the-Waters round, which has no final terms yet — see
            `intended_security` for what it plans to issue.
        intended_security (None | OfferingAttributesIntendedSecurityType0 | Unset): Testing-the-Waters rounds only: the
            kind of security the company says it intends to
            issue when the round opens, with no terms (none are final). Null for a live round,
            and for a TTW round whose terms are still to be decided.
        industries (list[TagRef] | Unset): The company's curated industry tags (the ones the site's explore page filters
            by),
            as `{ type, label }`. Empty when none are set. Filterable via `industry`.
        business_models (list[TagRef] | Unset): The company's curated business-model tags, as `{ type, label }`.
            Filterable via `business_model`.
        status (OfferingAttributesStatus | Unset): Where the round is in its life. `open` accepts investments (or
            reservations, for
            a Testing-the-Waters round); `closed` finished raising; `upcoming` is not yet
            accepting (insiders only); `canceled` was aborted. How close an open round is
            to closing is `closes_at`; whether it is over target is `amount_raised` vs
            `funding_target`.
             Example: open.
        testing_the_waters (bool | Unset): True for Testing-the-Waters rounds, which collect non-binding
            **reservations**, not
            investments. Use "reserve"/"reservation" copy for these, "invest"/"investment" otherwise.
             Example: False.
        funding_target (None | str | Unset): Funding target in USD, as a decimal string. Example: 1000000.
        min_investment (None | str | Unset): Minimum investment in USD, as a decimal string. Example: 100.
        amount_raised (None | str | Unset): Amount raised so far **by this offering** in USD, as a decimal string
            (hellbanned
            investors excluded). Not the company's lifetime total, and not the combined figure
            the company's Wefunder page shows when a Reg D round runs alongside — see `warnings`.
             Example: 642300.
        investor_count (int | None | Unset): Distinct investor count for this offering (hellbanned investors excluded).
            Example: 1203.
        started_at (datetime.datetime | None | Unset):  Example: 2025-03-01T12:00:00Z.
        closes_at (datetime.datetime | None | Unset): When an open round is scheduled to stop accepting investments.
            Null when no date is set or the round is not open. Example: 2025-04-30T03:59:59Z.
        closed_at (datetime.datetime | None | Unset):  Example: 2025-03-01T12:00:00Z.
        publicly_visible (bool | Unset): **Logged-in view only** (`read:explore`). `false` when a logged-out visitor
            could
            not see this offering — it is in the response only because of who the authorizing
            user is (accredited, invited, Vault/syndicate member). Absent in the public view.
             Example: True.
        invested (bool | Unset): **Logged-in view only** (`read:explore`). Whether the authorizing user has an
            active investment in this offering. Absent in the public view.
             Example: False.
        followed (bool | Unset): **Logged-in view only** (`read:explore`). Whether the authorizing user follows this
            company on wefunder.com (their watchlist). Absent in the public view.
             Example: False.
    """

    company_name: str | Unset = UNSET
    tagline: None | str | Unset = UNSET
    url: str | Unset = UNSET
    card_image_url: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    exemption: Exemption | Unset = UNSET
    security: (
        ConvertibleNoteSecurity
        | DebtSecurity
        | EquitySecurity
        | FundSecurity
        | None
        | OtherSecurity
        | RevenueShareSecurity
        | SafeSecurity
        | Unset
    ) = UNSET
    intended_security: None | OfferingAttributesIntendedSecurityType0 | Unset = UNSET
    industries: list[TagRef] | Unset = UNSET
    business_models: list[TagRef] | Unset = UNSET
    status: OfferingAttributesStatus | Unset = UNSET
    testing_the_waters: bool | Unset = UNSET
    funding_target: None | str | Unset = UNSET
    min_investment: None | str | Unset = UNSET
    amount_raised: None | str | Unset = UNSET
    investor_count: int | None | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    closes_at: datetime.datetime | None | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    publicly_visible: bool | Unset = UNSET
    invested: bool | Unset = UNSET
    followed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.convertible_note_security import ConvertibleNoteSecurity  # noqa: PLC0415
        from ..models.debt_security import DebtSecurity  # noqa: PLC0415
        from ..models.equity_security import EquitySecurity  # noqa: PLC0415
        from ..models.fund_security import FundSecurity  # noqa: PLC0415
        from ..models.offering_attributes_intended_security_type_0 import (
            OfferingAttributesIntendedSecurityType0,  # noqa: PLC0415
        )
        from ..models.other_security import OtherSecurity  # noqa: PLC0415
        from ..models.revenue_share_security import RevenueShareSecurity  # noqa: PLC0415
        from ..models.safe_security import SafeSecurity  # noqa: PLC0415

        company_name = self.company_name

        tagline: None | str | Unset
        if isinstance(self.tagline, Unset):
            tagline = UNSET
        else:
            tagline = self.tagline

        url = self.url

        card_image_url: None | str | Unset
        if isinstance(self.card_image_url, Unset):
            card_image_url = UNSET
        else:
            card_image_url = self.card_image_url

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        exemption: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exemption, Unset):
            exemption = self.exemption.to_dict()

        security: dict[str, Any] | None | Unset
        if isinstance(self.security, Unset):
            security = UNSET
        elif (
            isinstance(self.security, SafeSecurity)
            or isinstance(self.security, EquitySecurity)
            or isinstance(self.security, ConvertibleNoteSecurity)
            or isinstance(self.security, RevenueShareSecurity)
            or isinstance(self.security, DebtSecurity)
            or isinstance(self.security, FundSecurity)
            or isinstance(self.security, OtherSecurity)
        ):
            security = self.security.to_dict()
        else:
            security = self.security

        intended_security: dict[str, Any] | None | Unset
        if isinstance(self.intended_security, Unset):
            intended_security = UNSET
        elif isinstance(self.intended_security, OfferingAttributesIntendedSecurityType0):
            intended_security = self.intended_security.to_dict()
        else:
            intended_security = self.intended_security

        industries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.industries, Unset):
            industries = []
            for industries_item_data in self.industries:
                industries_item = industries_item_data.to_dict()
                industries.append(industries_item)

        business_models: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.business_models, Unset):
            business_models = []
            for business_models_item_data in self.business_models:
                business_models_item = business_models_item_data.to_dict()
                business_models.append(business_models_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        testing_the_waters = self.testing_the_waters

        funding_target: None | str | Unset
        if isinstance(self.funding_target, Unset):
            funding_target = UNSET
        else:
            funding_target = self.funding_target

        min_investment: None | str | Unset
        if isinstance(self.min_investment, Unset):
            min_investment = UNSET
        else:
            min_investment = self.min_investment

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

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        closes_at: None | str | Unset
        if isinstance(self.closes_at, Unset):
            closes_at = UNSET
        elif isinstance(self.closes_at, datetime.datetime):
            closes_at = self.closes_at.isoformat()
        else:
            closes_at = self.closes_at

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        publicly_visible = self.publicly_visible

        invested = self.invested

        followed = self.followed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if url is not UNSET:
            field_dict["url"] = url
        if card_image_url is not UNSET:
            field_dict["card_image_url"] = card_image_url
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if exemption is not UNSET:
            field_dict["exemption"] = exemption
        if security is not UNSET:
            field_dict["security"] = security
        if intended_security is not UNSET:
            field_dict["intended_security"] = intended_security
        if industries is not UNSET:
            field_dict["industries"] = industries
        if business_models is not UNSET:
            field_dict["business_models"] = business_models
        if status is not UNSET:
            field_dict["status"] = status
        if testing_the_waters is not UNSET:
            field_dict["testing_the_waters"] = testing_the_waters
        if funding_target is not UNSET:
            field_dict["funding_target"] = funding_target
        if min_investment is not UNSET:
            field_dict["min_investment"] = min_investment
        if amount_raised is not UNSET:
            field_dict["amount_raised"] = amount_raised
        if investor_count is not UNSET:
            field_dict["investor_count"] = investor_count
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if closes_at is not UNSET:
            field_dict["closes_at"] = closes_at
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if publicly_visible is not UNSET:
            field_dict["publicly_visible"] = publicly_visible
        if invested is not UNSET:
            field_dict["invested"] = invested
        if followed is not UNSET:
            field_dict["followed"] = followed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.convertible_note_security import ConvertibleNoteSecurity  # noqa: PLC0415
        from ..models.debt_security import DebtSecurity  # noqa: PLC0415
        from ..models.equity_security import EquitySecurity  # noqa: PLC0415
        from ..models.exemption import Exemption  # noqa: PLC0415
        from ..models.fund_security import FundSecurity  # noqa: PLC0415
        from ..models.offering_attributes_intended_security_type_0 import (
            OfferingAttributesIntendedSecurityType0,  # noqa: PLC0415
        )
        from ..models.other_security import OtherSecurity  # noqa: PLC0415
        from ..models.revenue_share_security import RevenueShareSecurity  # noqa: PLC0415
        from ..models.safe_security import SafeSecurity  # noqa: PLC0415
        from ..models.tag_ref import TagRef  # noqa: PLC0415

        d = dict(src_dict)
        company_name = d.pop("company_name", UNSET)

        def _parse_tagline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tagline = _parse_tagline(d.pop("tagline", UNSET))

        url = d.pop("url", UNSET)

        def _parse_card_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_image_url = _parse_card_image_url(d.pop("card_image_url", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        _exemption = d.pop("exemption", UNSET)
        exemption: Exemption | Unset
        if isinstance(_exemption, Unset):
            exemption = UNSET
        else:
            exemption = Exemption.from_dict(_exemption)

        def _parse_security(
            data: object,
        ) -> (
            ConvertibleNoteSecurity
            | DebtSecurity
            | EquitySecurity
            | FundSecurity
            | None
            | OtherSecurity
            | RevenueShareSecurity
            | SafeSecurity
            | Unset
        ):
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
            return cast(
                ConvertibleNoteSecurity
                | DebtSecurity
                | EquitySecurity
                | FundSecurity
                | None
                | OtherSecurity
                | RevenueShareSecurity
                | SafeSecurity
                | Unset,
                data,
            )

        security = _parse_security(d.pop("security", UNSET))

        def _parse_intended_security(data: object) -> None | OfferingAttributesIntendedSecurityType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                intended_security_type_0 = OfferingAttributesIntendedSecurityType0.from_dict(data)

                return intended_security_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfferingAttributesIntendedSecurityType0 | Unset, data)

        intended_security = _parse_intended_security(d.pop("intended_security", UNSET))

        _industries = d.pop("industries", UNSET)
        industries: list[TagRef] | Unset = UNSET
        if _industries is not UNSET:
            industries = []
            for industries_item_data in _industries:
                industries_item = TagRef.from_dict(industries_item_data)

                industries.append(industries_item)

        _business_models = d.pop("business_models", UNSET)
        business_models: list[TagRef] | Unset = UNSET
        if _business_models is not UNSET:
            business_models = []
            for business_models_item_data in _business_models:
                business_models_item = TagRef.from_dict(business_models_item_data)

                business_models.append(business_models_item)

        _status = d.pop("status", UNSET)
        status: OfferingAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OfferingAttributesStatus(_status)

        testing_the_waters = d.pop("testing_the_waters", UNSET)

        def _parse_funding_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        funding_target = _parse_funding_target(d.pop("funding_target", UNSET))

        def _parse_min_investment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        min_investment = _parse_min_investment(d.pop("min_investment", UNSET))

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

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

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

        publicly_visible = d.pop("publicly_visible", UNSET)

        invested = d.pop("invested", UNSET)

        followed = d.pop("followed", UNSET)

        offering_attributes = cls(
            company_name=company_name,
            tagline=tagline,
            url=url,
            card_image_url=card_image_url,
            logo_url=logo_url,
            exemption=exemption,
            security=security,
            intended_security=intended_security,
            industries=industries,
            business_models=business_models,
            status=status,
            testing_the_waters=testing_the_waters,
            funding_target=funding_target,
            min_investment=min_investment,
            amount_raised=amount_raised,
            investor_count=investor_count,
            started_at=started_at,
            closes_at=closes_at,
            closed_at=closed_at,
            publicly_visible=publicly_visible,
            invested=invested,
            followed=followed,
        )

        offering_attributes.additional_properties = d
        return offering_attributes

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
