from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.company_attributes_location import CompanyAttributesLocation
  from ..models.company_totals import CompanyTotals
  from ..models.current_raise import CurrentRaise
  from ..models.past_round import PastRound
  from ..models.wefunder_round import WefunderRound





T = TypeVar("T", bound="CompanyAttributes")



@_attrs_define
class CompanyAttributes:
    """ 
        Attributes:
            name (str | Unset):
            tagline (None | str | Unset):
            url (None | str | Unset): The company's Wefunder page.
            logo_url (None | str | Unset):
            card_image_url (None | str | Unset):
            location (CompanyAttributesLocation | Unset):
            raising (bool | Unset): True when the round the page shows this viewer is live (accepting investments or
                reservations). False for a funded company, or one with no round the viewer may see.
            current_raise (CurrentRaise | None | Unset): The live round the page shows, or null when `raising` is false. A
                funded company still has its history in `wefunder_rounds` and the page's ticker in `totals`.
            past_rounds (list[PastRound] | Unset): The prior rounds the company page's ticker folds in (its own accounting;
                see `totals.profile_*`). Not the company's full Wefunder history — that is `wefunder_rounds`.
            wefunder_rounds (list[WefunderRound] | Unset): Every round this company has run on Wefunder that the viewer may
                see, live and closed, newest first, each with its own metric. Independent of what the page's ticker chooses to
                include.
            totals (CompanyTotals | Unset):
     """

    name: str | Unset = UNSET
    tagline: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    card_image_url: None | str | Unset = UNSET
    location: CompanyAttributesLocation | Unset = UNSET
    raising: bool | Unset = UNSET
    current_raise: CurrentRaise | None | Unset = UNSET
    past_rounds: list[PastRound] | Unset = UNSET
    wefunder_rounds: list[WefunderRound] | Unset = UNSET
    totals: CompanyTotals | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_attributes_location import CompanyAttributesLocation # noqa: PLC0415
        from ..models.company_totals import CompanyTotals # noqa: PLC0415
        from ..models.current_raise import CurrentRaise # noqa: PLC0415
        from ..models.past_round import PastRound # noqa: PLC0415
        from ..models.wefunder_round import WefunderRound # noqa: PLC0415
        name = self.name

        tagline: None | str | Unset
        if isinstance(self.tagline, Unset):
            tagline = UNSET
        else:
            tagline = self.tagline

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        card_image_url: None | str | Unset
        if isinstance(self.card_image_url, Unset):
            card_image_url = UNSET
        else:
            card_image_url = self.card_image_url

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        raising = self.raising

        current_raise: dict[str, Any] | None | Unset
        if isinstance(self.current_raise, Unset):
            current_raise = UNSET
        elif isinstance(self.current_raise, CurrentRaise):
            current_raise = self.current_raise.to_dict()
        else:
            current_raise = self.current_raise

        past_rounds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.past_rounds, Unset):
            past_rounds = []
            for past_rounds_item_data in self.past_rounds:
                past_rounds_item = past_rounds_item_data.to_dict()
                past_rounds.append(past_rounds_item)



        wefunder_rounds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wefunder_rounds, Unset):
            wefunder_rounds = []
            for wefunder_rounds_item_data in self.wefunder_rounds:
                wefunder_rounds_item = wefunder_rounds_item_data.to_dict()
                wefunder_rounds.append(wefunder_rounds_item)



        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if url is not UNSET:
            field_dict["url"] = url
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if card_image_url is not UNSET:
            field_dict["card_image_url"] = card_image_url
        if location is not UNSET:
            field_dict["location"] = location
        if raising is not UNSET:
            field_dict["raising"] = raising
        if current_raise is not UNSET:
            field_dict["current_raise"] = current_raise
        if past_rounds is not UNSET:
            field_dict["past_rounds"] = past_rounds
        if wefunder_rounds is not UNSET:
            field_dict["wefunder_rounds"] = wefunder_rounds
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_attributes_location import CompanyAttributesLocation # noqa: PLC0415
        from ..models.company_totals import CompanyTotals # noqa: PLC0415
        from ..models.current_raise import CurrentRaise # noqa: PLC0415
        from ..models.past_round import PastRound # noqa: PLC0415
        from ..models.wefunder_round import WefunderRound # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_tagline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tagline = _parse_tagline(d.pop("tagline", UNSET))


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))


        def _parse_card_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_image_url = _parse_card_image_url(d.pop("card_image_url", UNSET))


        _location = d.pop("location", UNSET)
        location: CompanyAttributesLocation | Unset
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = CompanyAttributesLocation.from_dict(_location)




        raising = d.pop("raising", UNSET)

        def _parse_current_raise(data: object) -> CurrentRaise | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_raise_type_1 = CurrentRaise.from_dict(data)



                return current_raise_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CurrentRaise | None | Unset, data)

        current_raise = _parse_current_raise(d.pop("current_raise", UNSET))


        _past_rounds = d.pop("past_rounds", UNSET)
        past_rounds: list[PastRound] | Unset = UNSET
        if _past_rounds is not UNSET:
            past_rounds = []
            for past_rounds_item_data in _past_rounds:
                past_rounds_item = PastRound.from_dict(past_rounds_item_data)



                past_rounds.append(past_rounds_item)


        _wefunder_rounds = d.pop("wefunder_rounds", UNSET)
        wefunder_rounds: list[WefunderRound] | Unset = UNSET
        if _wefunder_rounds is not UNSET:
            wefunder_rounds = []
            for wefunder_rounds_item_data in _wefunder_rounds:
                wefunder_rounds_item = WefunderRound.from_dict(wefunder_rounds_item_data)



                wefunder_rounds.append(wefunder_rounds_item)


        _totals = d.pop("totals", UNSET)
        totals: CompanyTotals | Unset
        if isinstance(_totals,  Unset):
            totals = UNSET
        else:
            totals = CompanyTotals.from_dict(_totals)




        company_attributes = cls(
            name=name,
            tagline=tagline,
            url=url,
            logo_url=logo_url,
            card_image_url=card_image_url,
            location=location,
            raising=raising,
            current_raise=current_raise,
            past_rounds=past_rounds,
            wefunder_rounds=wefunder_rounds,
            totals=totals,
        )


        company_attributes.additional_properties = d
        return company_attributes

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
