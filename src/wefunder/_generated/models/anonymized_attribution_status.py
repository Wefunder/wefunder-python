from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.anonymized_attribution_status_bucket import AnonymizedAttributionStatusBucket
from ..types import UNSET, Unset






T = TypeVar("T", bound="AnonymizedAttributionStatus")



@_attrs_define
class AnonymizedAttributionStatus:
    """ Current investment status

        Attributes:
            bucket (AnonymizedAttributionStatusBucket | Unset): Investment processing stage (matches /manage page) Example:
                confirmed.
            progress_bar (bool | Unset): Whether the investment appears on founder progress bar (likely to complete)
                Example: True.
     """

    bucket: AnonymizedAttributionStatusBucket | Unset = UNSET
    progress_bar: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        bucket: str | Unset = UNSET
        if not isinstance(self.bucket, Unset):
            bucket = self.bucket.value


        progress_bar = self.progress_bar


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if progress_bar is not UNSET:
            field_dict["progress_bar"] = progress_bar

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _bucket = d.pop("bucket", UNSET)
        bucket: AnonymizedAttributionStatusBucket | Unset
        if isinstance(_bucket,  Unset):
            bucket = UNSET
        else:
            bucket = AnonymizedAttributionStatusBucket(_bucket)




        progress_bar = d.pop("progress_bar", UNSET)

        anonymized_attribution_status = cls(
            bucket=bucket,
            progress_bar=progress_bar,
        )


        anonymized_attribution_status.additional_properties = d
        return anonymized_attribution_status

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
