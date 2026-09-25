from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.investment_delta_record import InvestmentDeltaRecord
  from ..models.investment_envelope_meta import InvestmentEnvelopeMeta





T = TypeVar("T", bound="InvestmentEnvelope")



@_attrs_define
class InvestmentEnvelope:
    """ 
        Attributes:
            data (InvestmentDeltaRecord | Unset): The record of one investment, or a tombstone (`visible: false`, only
                `id`). `visible` is
                founder visibility: a user's own canceled investment is a full record with `visible: false`
                and `status: canceled`. Investor PII keys are omitted without `read:investors:pii`, except on
                the user's own records.
            meta (InvestmentEnvelopeMeta | Unset):
     """

    data: InvestmentDeltaRecord | Unset = UNSET
    meta: InvestmentEnvelopeMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.investment_delta_record import InvestmentDeltaRecord # noqa: PLC0415
        from ..models.investment_envelope_meta import InvestmentEnvelopeMeta # noqa: PLC0415
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investment_delta_record import InvestmentDeltaRecord # noqa: PLC0415
        from ..models.investment_envelope_meta import InvestmentEnvelopeMeta # noqa: PLC0415
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: InvestmentDeltaRecord | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = InvestmentDeltaRecord.from_dict(_data)




        _meta = d.pop("meta", UNSET)
        meta: InvestmentEnvelopeMeta | Unset
        if isinstance(_meta,  Unset):
            meta = UNSET
        else:
            meta = InvestmentEnvelopeMeta.from_dict(_meta)




        investment_envelope = cls(
            data=data,
            meta=meta,
        )


        investment_envelope.additional_properties = d
        return investment_envelope

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
