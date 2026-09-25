from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.exemption_family import ExemptionFamily
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Exemption")



@_attrs_define
class Exemption:
    """ The offering's SEC exemption, in market vocabulary.

        Attributes:
            family (ExemptionFamily | Unset): `other` appears only on a company's past rounds, for a reported round under an
                exemption outside this list (e.g. Section 4(a)(2)).
                `reg_cf` — Regulation Crowdfunding: open to all investors, with per-investor annual
                limits set by the SEC; amounts and investor counts are public. `reg_d` — Regulation D
                private placement: `506c` is open to verified accredited investors only and may be
                advertised; `506b` is by invitation and never publicly listed. `reg_a`, `reg_s` and
                `ecsp` exist in the data but are not filterable on `/explore`.
                 Example: reg_cf.
            subtype (None | str | Unset): Sub-type/flavor — `506b` or `506c` for the `reg_d` family, otherwise null.
            label (str | Unset): Human-readable label in normal market language. Example: Reg CF.
     """

    family: ExemptionFamily | Unset = UNSET
    subtype: None | str | Unset = UNSET
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        family: str | Unset = UNSET
        if not isinstance(self.family, Unset):
            family = self.family.value


        subtype: None | str | Unset
        if isinstance(self.subtype, Unset):
            subtype = UNSET
        else:
            subtype = self.subtype

        label = self.label


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if family is not UNSET:
            field_dict["family"] = family
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _family = d.pop("family", UNSET)
        family: ExemptionFamily | Unset
        if isinstance(_family,  Unset):
            family = UNSET
        else:
            family = ExemptionFamily(_family)




        def _parse_subtype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subtype = _parse_subtype(d.pop("subtype", UNSET))


        label = d.pop("label", UNSET)

        exemption = cls(
            family=family,
            subtype=subtype,
            label=label,
        )


        exemption.additional_properties = d
        return exemption

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
