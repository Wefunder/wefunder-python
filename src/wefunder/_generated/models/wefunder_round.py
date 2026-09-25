from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wefunder_round_status import WefunderRoundStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.convertible_note_security import ConvertibleNoteSecurity
    from ..models.debt_security import DebtSecurity
    from ..models.equity_security import EquitySecurity
    from ..models.exemption import Exemption
    from ..models.fund_security import FundSecurity
    from ..models.other_security import OtherSecurity
    from ..models.revenue_share_security import RevenueShareSecurity
    from ..models.safe_security import SafeSecurity


T = TypeVar("T", bound="WefunderRound")


@_attrs_define
class WefunderRound:
    """
    Attributes:
        offering_id (str | Unset): The round's offering id (`ofr_...`).
        current (bool | Unset): True for the displayed round and any other live round.
        status (WefunderRoundStatus | Unset):
        exemption (Exemption | None | Unset):
        security (ConvertibleNoteSecurity | DebtSecurity | EquitySecurity | FundSecurity | None | OtherSecurity |
            RevenueShareSecurity | SafeSecurity | Unset):
        amount_raised (None | str | Unset): This round's own soft-confirmed amount, USD decimal string.
        investor_count (int | None | Unset):
        opened_at (datetime.datetime | None | Unset):
        closed_at (datetime.datetime | None | Unset):
    """

    offering_id: str | Unset = UNSET
    current: bool | Unset = UNSET
    status: WefunderRoundStatus | Unset = UNSET
    exemption: Exemption | None | Unset = UNSET
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
    amount_raised: None | str | Unset = UNSET
    investor_count: int | None | Unset = UNSET
    opened_at: datetime.datetime | None | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.convertible_note_security import ConvertibleNoteSecurity  # noqa: PLC0415
        from ..models.debt_security import DebtSecurity  # noqa: PLC0415
        from ..models.equity_security import EquitySecurity  # noqa: PLC0415
        from ..models.exemption import Exemption  # noqa: PLC0415
        from ..models.fund_security import FundSecurity  # noqa: PLC0415
        from ..models.other_security import OtherSecurity  # noqa: PLC0415
        from ..models.revenue_share_security import RevenueShareSecurity  # noqa: PLC0415
        from ..models.safe_security import SafeSecurity  # noqa: PLC0415

        offering_id = self.offering_id

        current = self.current

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        field_dict.update({})
        if offering_id is not UNSET:
            field_dict["offering_id"] = offering_id
        if current is not UNSET:
            field_dict["current"] = current
        if status is not UNSET:
            field_dict["status"] = status
        if exemption is not UNSET:
            field_dict["exemption"] = exemption
        if security is not UNSET:
            field_dict["security"] = security
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
        from ..models.convertible_note_security import ConvertibleNoteSecurity  # noqa: PLC0415
        from ..models.debt_security import DebtSecurity  # noqa: PLC0415
        from ..models.equity_security import EquitySecurity  # noqa: PLC0415
        from ..models.exemption import Exemption  # noqa: PLC0415
        from ..models.fund_security import FundSecurity  # noqa: PLC0415
        from ..models.other_security import OtherSecurity  # noqa: PLC0415
        from ..models.revenue_share_security import RevenueShareSecurity  # noqa: PLC0415
        from ..models.safe_security import SafeSecurity  # noqa: PLC0415

        d = dict(src_dict)
        offering_id = d.pop("offering_id", UNSET)

        current = d.pop("current", UNSET)

        _status = d.pop("status", UNSET)
        status: WefunderRoundStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WefunderRoundStatus(_status)

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

        wefunder_round = cls(
            offering_id=offering_id,
            current=current,
            status=status,
            exemption=exemption,
            security=security,
            amount_raised=amount_raised,
            investor_count=investor_count,
            opened_at=opened_at,
            closed_at=closed_at,
        )

        wefunder_round.additional_properties = d
        return wefunder_round

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
