from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.anonymized_attribution import AnonymizedAttribution
  from ..models.attributed_investment_list_envelope_meta import AttributedInvestmentListEnvelopeMeta
  from ..models.full_attribution import FullAttribution





T = TypeVar("T", bound="AttributedInvestmentListEnvelope")



@_attrs_define
class AttributedInvestmentListEnvelope:
    """ 
        Attributes:
            data (list[AnonymizedAttribution | FullAttribution] | Unset): Returns AnonymizedAttribution or FullAttribution
                objects
                depending on detail_level and user permissions.
            meta (AttributedInvestmentListEnvelopeMeta | Unset):
     """

    data: list[AnonymizedAttribution | FullAttribution] | Unset = UNSET
    meta: AttributedInvestmentListEnvelopeMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.anonymized_attribution import AnonymizedAttribution # noqa: PLC0415
        from ..models.attributed_investment_list_envelope_meta import AttributedInvestmentListEnvelopeMeta # noqa: PLC0415
        from ..models.full_attribution import FullAttribution # noqa: PLC0415
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item: dict[str, Any]
                if isinstance(data_item_data, AnonymizedAttribution):
                    data_item = data_item_data.to_dict()
                else:
                    data_item = data_item_data.to_dict()

                data.append(data_item)



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
        from ..models.anonymized_attribution import AnonymizedAttribution # noqa: PLC0415
        from ..models.attributed_investment_list_envelope_meta import AttributedInvestmentListEnvelopeMeta # noqa: PLC0415
        from ..models.full_attribution import FullAttribution # noqa: PLC0415
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[AnonymizedAttribution | FullAttribution] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                def _parse_data_item(data: object) -> AnonymizedAttribution | FullAttribution:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        data_item_type_0 = AnonymizedAttribution.from_dict(data)



                        return data_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = FullAttribution.from_dict(data)



                    return data_item_type_1

                data_item = _parse_data_item(data_item_data)

                data.append(data_item)


        _meta = d.pop("meta", UNSET)
        meta: AttributedInvestmentListEnvelopeMeta | Unset
        if isinstance(_meta,  Unset):
            meta = UNSET
        else:
            meta = AttributedInvestmentListEnvelopeMeta.from_dict(_meta)




        attributed_investment_list_envelope = cls(
            data=data,
            meta=meta,
        )


        attributed_investment_list_envelope.additional_properties = d
        return attributed_investment_list_envelope

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
