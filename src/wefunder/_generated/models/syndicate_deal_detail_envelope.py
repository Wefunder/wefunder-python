from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.syndicate_deal import SyndicateDeal





T = TypeVar("T", bound="SyndicateDealDetailEnvelope")



@_attrs_define
class SyndicateDealDetailEnvelope:
    """ 
        Attributes:
            data (SyndicateDeal | Unset): JSON:API resource representing a syndicate deal (Fundraise)
     """

    data: SyndicateDeal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.syndicate_deal import SyndicateDeal # noqa: PLC0415
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.syndicate_deal import SyndicateDeal # noqa: PLC0415
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: SyndicateDeal | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = SyndicateDeal.from_dict(_data)




        syndicate_deal_detail_envelope = cls(
            data=data,
        )


        syndicate_deal_detail_envelope.additional_properties = d
        return syndicate_deal_detail_envelope

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
