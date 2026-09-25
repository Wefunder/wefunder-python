from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CompanyDisclosuresAttributesUseOfFundsType0Item")



@_attrs_define
class CompanyDisclosuresAttributesUseOfFundsType0Item:
    """ 
        Attributes:
            if_raised (None | str | Unset): USD, decimal string.
            plan (None | str | Unset):
     """

    if_raised: None | str | Unset = UNSET
    plan: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        if_raised: None | str | Unset
        if isinstance(self.if_raised, Unset):
            if_raised = UNSET
        else:
            if_raised = self.if_raised

        plan: None | str | Unset
        if isinstance(self.plan, Unset):
            plan = UNSET
        else:
            plan = self.plan


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if if_raised is not UNSET:
            field_dict["if_raised"] = if_raised
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_if_raised(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        if_raised = _parse_if_raised(d.pop("if_raised", UNSET))


        def _parse_plan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan = _parse_plan(d.pop("plan", UNSET))


        company_disclosures_attributes_use_of_funds_type_0_item = cls(
            if_raised=if_raised,
            plan=plan,
        )


        company_disclosures_attributes_use_of_funds_type_0_item.additional_properties = d
        return company_disclosures_attributes_use_of_funds_type_0_item

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
