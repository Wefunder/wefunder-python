from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.investment_session_create_input import InvestmentSessionCreateInput


T = TypeVar("T", bound="CreateOfferingInvestmentSessionBody")


@_attrs_define
class CreateOfferingInvestmentSessionBody:
    """
    Attributes:
        investment_session (InvestmentSessionCreateInput): Either `email` (invite an unknown recipient) or
            `wefunder_user_id` (target an
            existing Wefunder user) should be provided. `spv_id` is required on
            `POST /partner/investment_sessions`; on the deprecated SPV-nested path the
            SPV comes from the URL instead.
    """

    investment_session: InvestmentSessionCreateInput
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        investment_session = self.investment_session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "investment_session": investment_session,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investment_session_create_input import InvestmentSessionCreateInput  # noqa: PLC0415

        d = dict(src_dict)
        investment_session = InvestmentSessionCreateInput.from_dict(d.pop("investment_session"))

        create_offering_investment_session_body = cls(
            investment_session=investment_session,
        )

        create_offering_investment_session_body.additional_properties = d
        return create_offering_investment_session_body

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
