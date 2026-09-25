from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.spv_create_input_metadata import SpvCreateInputMetadata
  from ..models.spv_settings import SpvSettings
  from ..models.spv_terms import SpvTerms
  from ..models.target_company_input import TargetCompanyInput





T = TypeVar("T", bound="SpvCreateInput")



@_attrs_define
class SpvCreateInput:
    """ 
        Attributes:
            name (str):  Example: Acme Series A SPV.
            target_company (TargetCompanyInput):
            terms (SpvTerms): Investment terms for an SPV.
            settings (SpvSettings | Unset):
            metadata (SpvCreateInputMetadata | Unset): Arbitrary partner-defined key-value pairs echoed back on the SPV.
                Example: {'partner_reference': 'acme-series-a-2025', 'internal_notes': 'Introduced via Demo Day'}.
     """

    name: str
    target_company: TargetCompanyInput
    terms: SpvTerms
    settings: SpvSettings | Unset = UNSET
    metadata: SpvCreateInputMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.spv_create_input_metadata import SpvCreateInputMetadata # noqa: PLC0415
        from ..models.spv_settings import SpvSettings # noqa: PLC0415
        from ..models.spv_terms import SpvTerms # noqa: PLC0415
        from ..models.target_company_input import TargetCompanyInput # noqa: PLC0415
        name = self.name

        target_company = self.target_company.to_dict()

        terms = self.terms.to_dict()

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "target_company": target_company,
            "terms": terms,
        })
        if settings is not UNSET:
            field_dict["settings"] = settings
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spv_create_input_metadata import SpvCreateInputMetadata # noqa: PLC0415
        from ..models.spv_settings import SpvSettings # noqa: PLC0415
        from ..models.spv_terms import SpvTerms # noqa: PLC0415
        from ..models.target_company_input import TargetCompanyInput # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        target_company = TargetCompanyInput.from_dict(d.pop("target_company"))




        terms = SpvTerms.from_dict(d.pop("terms"))




        _settings = d.pop("settings", UNSET)
        settings: SpvSettings | Unset
        if isinstance(_settings,  Unset):
            settings = UNSET
        else:
            settings = SpvSettings.from_dict(_settings)




        _metadata = d.pop("metadata", UNSET)
        metadata: SpvCreateInputMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SpvCreateInputMetadata.from_dict(_metadata)




        spv_create_input = cls(
            name=name,
            target_company=target_company,
            terms=terms,
            settings=settings,
            metadata=metadata,
        )


        spv_create_input.additional_properties = d
        return spv_create_input

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
