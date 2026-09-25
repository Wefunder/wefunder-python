from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.portfolio_position_attributes_asset_type import PortfolioPositionAttributesAssetType
from ..models.portfolio_position_attributes_exit_reason import PortfolioPositionAttributesExitReason
from ..models.portfolio_position_attributes_status import PortfolioPositionAttributesStatus
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.portfolio_company_ref import PortfolioCompanyRef
  from ..models.portfolio_holding import PortfolioHolding
  from ..models.portfolio_security import PortfolioSecurity
  from ..models.security_summary import SecuritySummary





T = TypeVar("T", bound="PortfolioPositionAttributes")



@_attrs_define
class PortfolioPositionAttributes:
    """ 
        Attributes:
            offering_id (str | Unset):  Example: ofr_9aKxQ2vF8mNp1zT5wY7Qb3Cd.
            company (PortfolioCompanyRef | Unset): The company behind a portfolio position or holding.
            asset_type (PortfolioPositionAttributesAssetType | Unset): `fund` for SPV and fund vehicles; the underlying
                companies appear in `holdings` where recorded.
            security (None | SecuritySummary | Unset): What the round issued, as `{ type, label }`. Null when the round has
                no security recorded.
            status (PortfolioPositionAttributesStatus | Unset): `sold` means the stake was transferred away (secondary
                sale).
            exit_reason (PortfolioPositionAttributesExitReason | Unset): Why the position ended. Set only for `exited` and
                `failed`
                positions — a `sold` position ended with the transfer itself, and
                some older positions have no recorded ending. `ipo` means the
                company went public; distributions, if any, appear in
                `realized_gain_cents`.
            invested_at (datetime.datetime | None | Unset):
            currency (str | Unset):  Example: usd.
            cost_basis_cents (int | Unset):
            current_value_cents (int | Unset): Estimated current value; based on cost basis when no newer valuation has been
                recorded.
            unrealized_gain_cents (int | Unset): Can be negative.
            realized_gain_cents (int | Unset):
            return_multiple (None | str | Unset): Decimal string. Null when cost basis is zero. Example: 1.6492.
            shares_held (None | str | Unset):
            current_share_price (None | str | Unset): Null when the position's securities carry different prices — see the
                per-entry values.
            securities (list[PortfolioSecurity] | Unset):
            holdings (list[PortfolioHolding] | Unset): Companies the vehicle invested in, for fund positions. Empty for non-
                fund positions and for vehicles without recorded holdings.
            investor_count (int | Unset): The number of distinct investors in this deal. Present on the syndicate endpoint
                only.
            as_of (datetime.datetime | Unset): When the values in this position were last calculated (the oldest timestamp
                when several underlying records are combined).
     """

    offering_id: str | Unset = UNSET
    company: PortfolioCompanyRef | Unset = UNSET
    asset_type: PortfolioPositionAttributesAssetType | Unset = UNSET
    security: None | SecuritySummary | Unset = UNSET
    status: PortfolioPositionAttributesStatus | Unset = UNSET
    exit_reason: PortfolioPositionAttributesExitReason | Unset = UNSET
    invested_at: datetime.datetime | None | Unset = UNSET
    currency: str | Unset = UNSET
    cost_basis_cents: int | Unset = UNSET
    current_value_cents: int | Unset = UNSET
    unrealized_gain_cents: int | Unset = UNSET
    realized_gain_cents: int | Unset = UNSET
    return_multiple: None | str | Unset = UNSET
    shares_held: None | str | Unset = UNSET
    current_share_price: None | str | Unset = UNSET
    securities: list[PortfolioSecurity] | Unset = UNSET
    holdings: list[PortfolioHolding] | Unset = UNSET
    investor_count: int | Unset = UNSET
    as_of: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.portfolio_company_ref import PortfolioCompanyRef # noqa: PLC0415
        from ..models.portfolio_holding import PortfolioHolding # noqa: PLC0415
        from ..models.portfolio_security import PortfolioSecurity # noqa: PLC0415
        from ..models.security_summary import SecuritySummary # noqa: PLC0415
        offering_id = self.offering_id

        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        asset_type: str | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type.value


        security: dict[str, Any] | None | Unset
        if isinstance(self.security, Unset):
            security = UNSET
        elif isinstance(self.security, SecuritySummary):
            security = self.security.to_dict()
        else:
            security = self.security

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        exit_reason: str | Unset = UNSET
        if not isinstance(self.exit_reason, Unset):
            exit_reason = self.exit_reason.value


        invested_at: None | str | Unset
        if isinstance(self.invested_at, Unset):
            invested_at = UNSET
        elif isinstance(self.invested_at, datetime.datetime):
            invested_at = self.invested_at.isoformat()
        else:
            invested_at = self.invested_at

        currency = self.currency

        cost_basis_cents = self.cost_basis_cents

        current_value_cents = self.current_value_cents

        unrealized_gain_cents = self.unrealized_gain_cents

        realized_gain_cents = self.realized_gain_cents

        return_multiple: None | str | Unset
        if isinstance(self.return_multiple, Unset):
            return_multiple = UNSET
        else:
            return_multiple = self.return_multiple

        shares_held: None | str | Unset
        if isinstance(self.shares_held, Unset):
            shares_held = UNSET
        else:
            shares_held = self.shares_held

        current_share_price: None | str | Unset
        if isinstance(self.current_share_price, Unset):
            current_share_price = UNSET
        else:
            current_share_price = self.current_share_price

        securities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.securities, Unset):
            securities = []
            for securities_item_data in self.securities:
                securities_item = securities_item_data.to_dict()
                securities.append(securities_item)



        holdings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.holdings, Unset):
            holdings = []
            for holdings_item_data in self.holdings:
                holdings_item = holdings_item_data.to_dict()
                holdings.append(holdings_item)



        investor_count = self.investor_count

        as_of: str | Unset = UNSET
        if not isinstance(self.as_of, Unset):
            as_of = self.as_of.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if offering_id is not UNSET:
            field_dict["offering_id"] = offering_id
        if company is not UNSET:
            field_dict["company"] = company
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
        if security is not UNSET:
            field_dict["security"] = security
        if status is not UNSET:
            field_dict["status"] = status
        if exit_reason is not UNSET:
            field_dict["exit_reason"] = exit_reason
        if invested_at is not UNSET:
            field_dict["invested_at"] = invested_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if cost_basis_cents is not UNSET:
            field_dict["cost_basis_cents"] = cost_basis_cents
        if current_value_cents is not UNSET:
            field_dict["current_value_cents"] = current_value_cents
        if unrealized_gain_cents is not UNSET:
            field_dict["unrealized_gain_cents"] = unrealized_gain_cents
        if realized_gain_cents is not UNSET:
            field_dict["realized_gain_cents"] = realized_gain_cents
        if return_multiple is not UNSET:
            field_dict["return_multiple"] = return_multiple
        if shares_held is not UNSET:
            field_dict["shares_held"] = shares_held
        if current_share_price is not UNSET:
            field_dict["current_share_price"] = current_share_price
        if securities is not UNSET:
            field_dict["securities"] = securities
        if holdings is not UNSET:
            field_dict["holdings"] = holdings
        if investor_count is not UNSET:
            field_dict["investor_count"] = investor_count
        if as_of is not UNSET:
            field_dict["as_of"] = as_of

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portfolio_company_ref import PortfolioCompanyRef # noqa: PLC0415
        from ..models.portfolio_holding import PortfolioHolding # noqa: PLC0415
        from ..models.portfolio_security import PortfolioSecurity # noqa: PLC0415
        from ..models.security_summary import SecuritySummary # noqa: PLC0415
        d = dict(src_dict)
        offering_id = d.pop("offering_id", UNSET)

        _company = d.pop("company", UNSET)
        company: PortfolioCompanyRef | Unset
        if isinstance(_company,  Unset):
            company = UNSET
        else:
            company = PortfolioCompanyRef.from_dict(_company)




        _asset_type = d.pop("asset_type", UNSET)
        asset_type: PortfolioPositionAttributesAssetType | Unset
        if isinstance(_asset_type,  Unset):
            asset_type = UNSET
        else:
            asset_type = PortfolioPositionAttributesAssetType(_asset_type)




        def _parse_security(data: object) -> None | SecuritySummary | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                security_type_1 = SecuritySummary.from_dict(data)



                return security_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SecuritySummary | Unset, data)

        security = _parse_security(d.pop("security", UNSET))


        _status = d.pop("status", UNSET)
        status: PortfolioPositionAttributesStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = PortfolioPositionAttributesStatus(_status)




        _exit_reason = d.pop("exit_reason", UNSET)
        exit_reason: PortfolioPositionAttributesExitReason | Unset
        if isinstance(_exit_reason,  Unset):
            exit_reason = UNSET
        else:
            exit_reason = PortfolioPositionAttributesExitReason(_exit_reason)




        def _parse_invested_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invested_at_type_0 = datetime.datetime.fromisoformat(data)



                return invested_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        invested_at = _parse_invested_at(d.pop("invested_at", UNSET))


        currency = d.pop("currency", UNSET)

        cost_basis_cents = d.pop("cost_basis_cents", UNSET)

        current_value_cents = d.pop("current_value_cents", UNSET)

        unrealized_gain_cents = d.pop("unrealized_gain_cents", UNSET)

        realized_gain_cents = d.pop("realized_gain_cents", UNSET)

        def _parse_return_multiple(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_multiple = _parse_return_multiple(d.pop("return_multiple", UNSET))


        def _parse_shares_held(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shares_held = _parse_shares_held(d.pop("shares_held", UNSET))


        def _parse_current_share_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_share_price = _parse_current_share_price(d.pop("current_share_price", UNSET))


        _securities = d.pop("securities", UNSET)
        securities: list[PortfolioSecurity] | Unset = UNSET
        if _securities is not UNSET:
            securities = []
            for securities_item_data in _securities:
                securities_item = PortfolioSecurity.from_dict(securities_item_data)



                securities.append(securities_item)


        _holdings = d.pop("holdings", UNSET)
        holdings: list[PortfolioHolding] | Unset = UNSET
        if _holdings is not UNSET:
            holdings = []
            for holdings_item_data in _holdings:
                holdings_item = PortfolioHolding.from_dict(holdings_item_data)



                holdings.append(holdings_item)


        investor_count = d.pop("investor_count", UNSET)

        _as_of = d.pop("as_of", UNSET)
        as_of: datetime.datetime | Unset
        if isinstance(_as_of,  Unset):
            as_of = UNSET
        else:
            as_of = datetime.datetime.fromisoformat(_as_of)




        portfolio_position_attributes = cls(
            offering_id=offering_id,
            company=company,
            asset_type=asset_type,
            security=security,
            status=status,
            exit_reason=exit_reason,
            invested_at=invested_at,
            currency=currency,
            cost_basis_cents=cost_basis_cents,
            current_value_cents=current_value_cents,
            unrealized_gain_cents=unrealized_gain_cents,
            realized_gain_cents=realized_gain_cents,
            return_multiple=return_multiple,
            shares_held=shares_held,
            current_share_price=current_share_price,
            securities=securities,
            holdings=holdings,
            investor_count=investor_count,
            as_of=as_of,
        )


        portfolio_position_attributes.additional_properties = d
        return portfolio_position_attributes

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
