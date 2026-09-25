from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.spv_status_attributes_status import SpvStatusAttributesStatus
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="SpvStatusAttributes")



@_attrs_define
class SpvStatusAttributes:
    """ 
        Attributes:
            status (SpvStatusAttributesStatus | Unset):  Example: closing.
            requires_ops_review (bool | Unset): The offering is awaiting Wefunder review before it can open. Example: False.
            disbursement_scheduled (bool | Unset): A disbursement is queued for this SPV but funds have not moved yet.
                Example: True.
            expected_disbursement_at (datetime.datetime | None | Unset): Estimated date funds will be disbursed — 3 business
                days from when the close executed and the SPV entered the disbursement queue. Present only while `status` is
                `closing` (awaiting disbursement); null before close and once funds have moved. Example: 2026-07-28T00:00:00Z.
            finalized_investor_list (bool | Unset): The investor roster has been finalized. Example: False.
     """

    status: SpvStatusAttributesStatus | Unset = UNSET
    requires_ops_review: bool | Unset = UNSET
    disbursement_scheduled: bool | Unset = UNSET
    expected_disbursement_at: datetime.datetime | None | Unset = UNSET
    finalized_investor_list: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        requires_ops_review = self.requires_ops_review

        disbursement_scheduled = self.disbursement_scheduled

        expected_disbursement_at: None | str | Unset
        if isinstance(self.expected_disbursement_at, Unset):
            expected_disbursement_at = UNSET
        elif isinstance(self.expected_disbursement_at, datetime.datetime):
            expected_disbursement_at = self.expected_disbursement_at.isoformat()
        else:
            expected_disbursement_at = self.expected_disbursement_at

        finalized_investor_list = self.finalized_investor_list


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if requires_ops_review is not UNSET:
            field_dict["requires_ops_review"] = requires_ops_review
        if disbursement_scheduled is not UNSET:
            field_dict["disbursement_scheduled"] = disbursement_scheduled
        if expected_disbursement_at is not UNSET:
            field_dict["expected_disbursement_at"] = expected_disbursement_at
        if finalized_investor_list is not UNSET:
            field_dict["finalized_investor_list"] = finalized_investor_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: SpvStatusAttributesStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = SpvStatusAttributesStatus(_status)




        requires_ops_review = d.pop("requires_ops_review", UNSET)

        disbursement_scheduled = d.pop("disbursement_scheduled", UNSET)

        def _parse_expected_disbursement_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expected_disbursement_at_type_0 = datetime.datetime.fromisoformat(data)



                return expected_disbursement_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expected_disbursement_at = _parse_expected_disbursement_at(d.pop("expected_disbursement_at", UNSET))


        finalized_investor_list = d.pop("finalized_investor_list", UNSET)

        spv_status_attributes = cls(
            status=status,
            requires_ops_review=requires_ops_review,
            disbursement_scheduled=disbursement_scheduled,
            expected_disbursement_at=expected_disbursement_at,
            finalized_investor_list=finalized_investor_list,
        )


        spv_status_attributes.additional_properties = d
        return spv_status_attributes

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
