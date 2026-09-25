from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.portfolio_security_owner_type_0_kind import PortfolioSecurityOwnerType0Kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="PortfolioSecurityOwnerType0")


@_attrs_define
class PortfolioSecurityOwnerType0:
    """The legal owner of this stake — `{"kind": "individual"}` for
    personally-held stakes, `{"kind": "entity", "name": "..."}` for stakes
    held through the investor's own entity (IRA, LLC). Present on the
    investor endpoint only.

        Attributes:
            kind (PortfolioSecurityOwnerType0Kind | Unset):
            name (str | Unset):
    """

    kind: PortfolioSecurityOwnerType0Kind | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: PortfolioSecurityOwnerType0Kind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = PortfolioSecurityOwnerType0Kind(_kind)

        name = d.pop("name", UNSET)

        portfolio_security_owner_type_0 = cls(
            kind=kind,
            name=name,
        )

        portfolio_security_owner_type_0.additional_properties = d
        return portfolio_security_owner_type_0

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
