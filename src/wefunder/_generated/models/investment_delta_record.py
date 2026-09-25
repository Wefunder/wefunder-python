from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.investment_delta_record_reason import InvestmentDeltaRecordReason
from ..models.investment_delta_record_status import InvestmentDeltaRecordStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investment_delta_record_amounts import InvestmentDeltaRecordAmounts
    from ..models.investment_delta_record_blockers_item import InvestmentDeltaRecordBlockersItem
    from ..models.investment_delta_record_contracts_item import InvestmentDeltaRecordContractsItem
    from ..models.investment_delta_record_investor import InvestmentDeltaRecordInvestor


T = TypeVar("T", bound="InvestmentDeltaRecord")


@_attrs_define
class InvestmentDeltaRecord:
    """The record of one investment, or a tombstone (`visible: false`, only `id`). `visible` is
    founder visibility: a user's own canceled investment is a full record with `visible: false`
    and `status: canceled`. Investor PII keys are omitted without `read:investors:pii`, except on
    the user's own records.

        Attributes:
            id (str): Investment external id (`inv_…`), stable for the life of the investment.
            visible (bool):
            observed_at (datetime.datetime): When this payload was observed by the publisher. Not a version.
            status (InvestmentDeltaRecordStatus | Unset): Company/offering audiences receive canceled and converted
                investments as tombstones; the values appear for audiences that can see them (e.g. the investor's own).
            converted_to (None | str | Unset):
            converted_from (None | str | Unset):
            offering (str | Unset): Offering external id (`ofr_…`).
            company (str | Unset): Company external id (`co_…`).
            investment_type (str | Unset):
            offering_type (str | Unset):
            group (str | Unset): The founder dashboard's investment group label (e.g. CONFIRMED, IS READY).
            applied_at (datetime.datetime | Unset):
            amounts (InvestmentDeltaRecordAmounts | Unset):
            shares (None | str | Unset): Shares this investment buys at its committed amount, as a decimal string (`"295"`,
                `"1234.5"`). For an investment through the SPV this is the company shares allotted to it through the vehicle.
                `null` when the round has no share concept (SAFE, note, reservation) or no shares are computed for the
                investment. Computed per investment; not the investor's post-funding position. Example: 295.
            average_share_price (None | str | Unset): Weighted average price per share for this investment (total share
                price / `shares`), as a decimal string. With tiered or early-bird pricing this need not equal any single price
                on the round. `null` whenever `shares` is `null`. Example: 3.38.
            needs_whitelisting (bool | Unset):
            external_username (None | str | Unset): PII scope.
            message (None | str | Unset): PII scope.
            investor (InvestmentDeltaRecordInvestor | Unset):
            blockers (list[InvestmentDeltaRecordBlockersItem] | Unset):
            contracts (list[InvestmentDeltaRecordContractsItem] | Unset):
            cursor (None | str | Unset): Ledger position of the change that listed this record (delta pages only).
            reason (InvestmentDeltaRecordReason | Unset): Why the ledger row exists. `investor_deactivated` marks the first
                republish after the investor's
                account was deactivated (identity fields redacted). Delta pages only.
    """

    id: str
    visible: bool
    observed_at: datetime.datetime
    status: InvestmentDeltaRecordStatus | Unset = UNSET
    converted_to: None | str | Unset = UNSET
    converted_from: None | str | Unset = UNSET
    offering: str | Unset = UNSET
    company: str | Unset = UNSET
    investment_type: str | Unset = UNSET
    offering_type: str | Unset = UNSET
    group: str | Unset = UNSET
    applied_at: datetime.datetime | Unset = UNSET
    amounts: InvestmentDeltaRecordAmounts | Unset = UNSET
    shares: None | str | Unset = UNSET
    average_share_price: None | str | Unset = UNSET
    needs_whitelisting: bool | Unset = UNSET
    external_username: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    investor: InvestmentDeltaRecordInvestor | Unset = UNSET
    blockers: list[InvestmentDeltaRecordBlockersItem] | Unset = UNSET
    contracts: list[InvestmentDeltaRecordContractsItem] | Unset = UNSET
    cursor: None | str | Unset = UNSET
    reason: InvestmentDeltaRecordReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        visible = self.visible

        observed_at = self.observed_at.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        converted_to: None | str | Unset
        if isinstance(self.converted_to, Unset):
            converted_to = UNSET
        else:
            converted_to = self.converted_to

        converted_from: None | str | Unset
        if isinstance(self.converted_from, Unset):
            converted_from = UNSET
        else:
            converted_from = self.converted_from

        offering = self.offering

        company = self.company

        investment_type = self.investment_type

        offering_type = self.offering_type

        group = self.group

        applied_at: str | Unset = UNSET
        if not isinstance(self.applied_at, Unset):
            applied_at = self.applied_at.isoformat()

        amounts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amounts, Unset):
            amounts = self.amounts.to_dict()

        shares: None | str | Unset
        if isinstance(self.shares, Unset):
            shares = UNSET
        else:
            shares = self.shares

        average_share_price: None | str | Unset
        if isinstance(self.average_share_price, Unset):
            average_share_price = UNSET
        else:
            average_share_price = self.average_share_price

        needs_whitelisting = self.needs_whitelisting

        external_username: None | str | Unset
        if isinstance(self.external_username, Unset):
            external_username = UNSET
        else:
            external_username = self.external_username

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        investor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.investor, Unset):
            investor = self.investor.to_dict()

        blockers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blockers, Unset):
            blockers = []
            for blockers_item_data in self.blockers:
                blockers_item = blockers_item_data.to_dict()
                blockers.append(blockers_item)

        contracts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contracts, Unset):
            contracts = []
            for contracts_item_data in self.contracts:
                contracts_item = contracts_item_data.to_dict()
                contracts.append(contracts_item)

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "visible": visible,
                "observed_at": observed_at,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if converted_to is not UNSET:
            field_dict["converted_to"] = converted_to
        if converted_from is not UNSET:
            field_dict["converted_from"] = converted_from
        if offering is not UNSET:
            field_dict["offering"] = offering
        if company is not UNSET:
            field_dict["company"] = company
        if investment_type is not UNSET:
            field_dict["investment_type"] = investment_type
        if offering_type is not UNSET:
            field_dict["offering_type"] = offering_type
        if group is not UNSET:
            field_dict["group"] = group
        if applied_at is not UNSET:
            field_dict["applied_at"] = applied_at
        if amounts is not UNSET:
            field_dict["amounts"] = amounts
        if shares is not UNSET:
            field_dict["shares"] = shares
        if average_share_price is not UNSET:
            field_dict["average_share_price"] = average_share_price
        if needs_whitelisting is not UNSET:
            field_dict["needs_whitelisting"] = needs_whitelisting
        if external_username is not UNSET:
            field_dict["external_username"] = external_username
        if message is not UNSET:
            field_dict["message"] = message
        if investor is not UNSET:
            field_dict["investor"] = investor
        if blockers is not UNSET:
            field_dict["blockers"] = blockers
        if contracts is not UNSET:
            field_dict["contracts"] = contracts
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investment_delta_record_amounts import InvestmentDeltaRecordAmounts  # noqa: PLC0415
        from ..models.investment_delta_record_blockers_item import InvestmentDeltaRecordBlockersItem  # noqa: PLC0415
        from ..models.investment_delta_record_contracts_item import InvestmentDeltaRecordContractsItem  # noqa: PLC0415
        from ..models.investment_delta_record_investor import InvestmentDeltaRecordInvestor  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        visible = d.pop("visible")

        observed_at = datetime.datetime.fromisoformat(d.pop("observed_at"))

        _status = d.pop("status", UNSET)
        status: InvestmentDeltaRecordStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InvestmentDeltaRecordStatus(_status)

        def _parse_converted_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        converted_to = _parse_converted_to(d.pop("converted_to", UNSET))

        def _parse_converted_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        converted_from = _parse_converted_from(d.pop("converted_from", UNSET))

        offering = d.pop("offering", UNSET)

        company = d.pop("company", UNSET)

        investment_type = d.pop("investment_type", UNSET)

        offering_type = d.pop("offering_type", UNSET)

        group = d.pop("group", UNSET)

        _applied_at = d.pop("applied_at", UNSET)
        applied_at: datetime.datetime | Unset
        if isinstance(_applied_at, Unset):
            applied_at = UNSET
        else:
            applied_at = datetime.datetime.fromisoformat(_applied_at)

        _amounts = d.pop("amounts", UNSET)
        amounts: InvestmentDeltaRecordAmounts | Unset
        if isinstance(_amounts, Unset):
            amounts = UNSET
        else:
            amounts = InvestmentDeltaRecordAmounts.from_dict(_amounts)

        def _parse_shares(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shares = _parse_shares(d.pop("shares", UNSET))

        def _parse_average_share_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        average_share_price = _parse_average_share_price(d.pop("average_share_price", UNSET))

        needs_whitelisting = d.pop("needs_whitelisting", UNSET)

        def _parse_external_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_username = _parse_external_username(d.pop("external_username", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        _investor = d.pop("investor", UNSET)
        investor: InvestmentDeltaRecordInvestor | Unset
        if isinstance(_investor, Unset):
            investor = UNSET
        else:
            investor = InvestmentDeltaRecordInvestor.from_dict(_investor)

        _blockers = d.pop("blockers", UNSET)
        blockers: list[InvestmentDeltaRecordBlockersItem] | Unset = UNSET
        if _blockers is not UNSET:
            blockers = []
            for blockers_item_data in _blockers:
                blockers_item = InvestmentDeltaRecordBlockersItem.from_dict(blockers_item_data)

                blockers.append(blockers_item)

        _contracts = d.pop("contracts", UNSET)
        contracts: list[InvestmentDeltaRecordContractsItem] | Unset = UNSET
        if _contracts is not UNSET:
            contracts = []
            for contracts_item_data in _contracts:
                contracts_item = InvestmentDeltaRecordContractsItem.from_dict(contracts_item_data)

                contracts.append(contracts_item)

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        _reason = d.pop("reason", UNSET)
        reason: InvestmentDeltaRecordReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = InvestmentDeltaRecordReason(_reason)

        investment_delta_record = cls(
            id=id,
            visible=visible,
            observed_at=observed_at,
            status=status,
            converted_to=converted_to,
            converted_from=converted_from,
            offering=offering,
            company=company,
            investment_type=investment_type,
            offering_type=offering_type,
            group=group,
            applied_at=applied_at,
            amounts=amounts,
            shares=shares,
            average_share_price=average_share_price,
            needs_whitelisting=needs_whitelisting,
            external_username=external_username,
            message=message,
            investor=investor,
            blockers=blockers,
            contracts=contracts,
            cursor=cursor,
            reason=reason,
        )

        investment_delta_record.additional_properties = d
        return investment_delta_record

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
