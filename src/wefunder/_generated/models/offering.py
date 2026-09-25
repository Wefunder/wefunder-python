from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offering_attributes import OfferingAttributes
    from ..models.offering_warnings_item import OfferingWarningsItem


T = TypeVar("T", bound="Offering")


@_attrs_define
class Offering:
    """A public offering (a fundraise), addressed by its id (`ofr_...`). Returned by the
    Explore endpoints. Monetary fields are USD decimal strings — parse them as decimals, not
    floats.

        Attributes:
            id (str | Unset): The offering's stable id. Example: ofr_yw3OhusvpfJP4Pk3wRYV1F2R.
            type_ (str | Unset):  Example: offering.
            attributes (OfferingAttributes | Unset):
            company (None | str | Unset): The parent company's id (`co_...`). Resolve it with `GET /companies/{id}`.
                Example: co_8Kd0aB3xQ9k2vF8mNp1zT5wY.
            warnings (list[OfferingWarningsItem] | Unset): Context for reading this offering's numbers correctly. Empty for
                most offerings.
                `concurrent_rounds`: the company has other open rounds (e.g. a Reg D round alongside
                this one), so the company's Wefunder page shows a combined total larger than
                `amount_raised`. `prior_rounds`: the company completed earlier rounds on Wefunder, so
                `amount_raised` is not its lifetime total. Not part of the `etag`.
            etag (str | Unset): Content digest of this offering's public payload (`attributes`), for client-side change
                detection when polling. `warnings` are not included.
                 Example: a1b2c3d4e5f6.
    """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    attributes: OfferingAttributes | Unset = UNSET
    company: None | str | Unset = UNSET
    warnings: list[OfferingWarningsItem] | Unset = UNSET
    etag: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        etag = self.etag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if company is not UNSET:
            field_dict["company"] = company
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if etag is not UNSET:
            field_dict["etag"] = etag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_attributes import OfferingAttributes  # noqa: PLC0415
        from ..models.offering_warnings_item import OfferingWarningsItem  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: OfferingAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = OfferingAttributes.from_dict(_attributes)

        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))

        _warnings = d.pop("warnings", UNSET)
        warnings: list[OfferingWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = OfferingWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        etag = d.pop("etag", UNSET)

        offering = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            company=company,
            warnings=warnings,
            etag=etag,
        )

        offering.additional_properties = d
        return offering

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
