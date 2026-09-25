from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.company_disclosures_attributes_business import CompanyDisclosuresAttributesBusiness
  from ..models.company_disclosures_attributes_capital_structure_type_0_item import CompanyDisclosuresAttributesCapitalStructureType0Item
  from ..models.company_disclosures_attributes_current_position import CompanyDisclosuresAttributesCurrentPosition
  from ..models.company_disclosures_attributes_filing import CompanyDisclosuresAttributesFiling
  from ..models.company_disclosures_attributes_financial_statements import CompanyDisclosuresAttributesFinancialStatements
  from ..models.company_disclosures_attributes_outstanding_debts_type_0 import CompanyDisclosuresAttributesOutstandingDebtsType0
  from ..models.company_disclosures_attributes_outstanding_notes_type_0_item import CompanyDisclosuresAttributesOutstandingNotesType0Item
  from ..models.company_disclosures_attributes_prior_offerings_type_0_item import CompanyDisclosuresAttributesPriorOfferingsType0Item
  from ..models.company_disclosures_attributes_ratios_type_0 import CompanyDisclosuresAttributesRatiosType0
  from ..models.company_disclosures_attributes_related_parties_type_0 import CompanyDisclosuresAttributesRelatedPartiesType0
  from ..models.company_disclosures_attributes_use_of_funds_type_0_item import CompanyDisclosuresAttributesUseOfFundsType0Item
  from ..models.company_disclosures_attributes_voting_power_type_0_item import CompanyDisclosuresAttributesVotingPowerType0Item
  from ..models.disclosure_document import DisclosureDocument
  from ..models.disclosure_person import DisclosurePerson





T = TypeVar("T", bound="CompanyDisclosuresAttributes")



@_attrs_define
class CompanyDisclosuresAttributes:
    """ 
        Attributes:
            offering_id (str | Unset): The round whose Form C this is (`ofr_...`).
            filing (CompanyDisclosuresAttributesFiling | Unset):
            business (CompanyDisclosuresAttributesBusiness | Unset):
            financial_statements (CompanyDisclosuresAttributesFinancialStatements | Unset): One column per fiscal year on
                file; a year with no figures is omitted.
            ratios (CompanyDisclosuresAttributesRatiosType0 | None | Unset): The page's at-a-glance ratios for the most
                recent fiscal year, percentages as decimal strings; null where the page shows N/A, or the whole block null when
                hidden for this company.
            current_position (CompanyDisclosuresAttributesCurrentPosition | Unset): The founder's own disclosure of where
                the company stands today, each field when supplied.
            financial_condition (None | str | Unset): The issuer's financial-condition narrative, plain text.
            financial_statement_documents (list[DisclosureDocument] | Unset):
            investment_documents (list[DisclosureDocument] | Unset): The contracts an investor signs (the page's "Investment
                Terms").
            risks (list[str] | Unset): The issuer's risk factors, in the page's order, plain text.
            use_of_funds (list[CompanyDisclosuresAttributesUseOfFundsType0Item] | None | Unset): How the company says it
                will use the money at each amount raised.
            directors (list[DisclosurePerson] | None | Unset):
            officers (list[DisclosurePerson] | None | Unset):
            voting_power (list[CompanyDisclosuresAttributesVotingPowerType0Item] | None | Unset): Holders of 20% or more of
                voting power, as disclosed.
            capital_structure (list[CompanyDisclosuresAttributesCapitalStructureType0Item] | None | Unset):
            prior_offerings (list[CompanyDisclosuresAttributesPriorOfferingsType0Item] | None | Unset): Exempt offerings in
                the prior three years, as disclosed.
            outstanding_notes (list[CompanyDisclosuresAttributesOutstandingNotesType0Item] | None | Unset):
            outstanding_debts (CompanyDisclosuresAttributesOutstandingDebtsType0 | None | Unset):
            related_parties (CompanyDisclosuresAttributesRelatedPartiesType0 | None | Unset):
     """

    offering_id: str | Unset = UNSET
    filing: CompanyDisclosuresAttributesFiling | Unset = UNSET
    business: CompanyDisclosuresAttributesBusiness | Unset = UNSET
    financial_statements: CompanyDisclosuresAttributesFinancialStatements | Unset = UNSET
    ratios: CompanyDisclosuresAttributesRatiosType0 | None | Unset = UNSET
    current_position: CompanyDisclosuresAttributesCurrentPosition | Unset = UNSET
    financial_condition: None | str | Unset = UNSET
    financial_statement_documents: list[DisclosureDocument] | Unset = UNSET
    investment_documents: list[DisclosureDocument] | Unset = UNSET
    risks: list[str] | Unset = UNSET
    use_of_funds: list[CompanyDisclosuresAttributesUseOfFundsType0Item] | None | Unset = UNSET
    directors: list[DisclosurePerson] | None | Unset = UNSET
    officers: list[DisclosurePerson] | None | Unset = UNSET
    voting_power: list[CompanyDisclosuresAttributesVotingPowerType0Item] | None | Unset = UNSET
    capital_structure: list[CompanyDisclosuresAttributesCapitalStructureType0Item] | None | Unset = UNSET
    prior_offerings: list[CompanyDisclosuresAttributesPriorOfferingsType0Item] | None | Unset = UNSET
    outstanding_notes: list[CompanyDisclosuresAttributesOutstandingNotesType0Item] | None | Unset = UNSET
    outstanding_debts: CompanyDisclosuresAttributesOutstandingDebtsType0 | None | Unset = UNSET
    related_parties: CompanyDisclosuresAttributesRelatedPartiesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_disclosures_attributes_business import CompanyDisclosuresAttributesBusiness # noqa: PLC0415
        from ..models.company_disclosures_attributes_capital_structure_type_0_item import CompanyDisclosuresAttributesCapitalStructureType0Item # noqa: PLC0415
        from ..models.company_disclosures_attributes_current_position import CompanyDisclosuresAttributesCurrentPosition # noqa: PLC0415
        from ..models.company_disclosures_attributes_filing import CompanyDisclosuresAttributesFiling # noqa: PLC0415
        from ..models.company_disclosures_attributes_financial_statements import CompanyDisclosuresAttributesFinancialStatements # noqa: PLC0415
        from ..models.company_disclosures_attributes_outstanding_debts_type_0 import CompanyDisclosuresAttributesOutstandingDebtsType0 # noqa: PLC0415
        from ..models.company_disclosures_attributes_outstanding_notes_type_0_item import CompanyDisclosuresAttributesOutstandingNotesType0Item # noqa: PLC0415
        from ..models.company_disclosures_attributes_prior_offerings_type_0_item import CompanyDisclosuresAttributesPriorOfferingsType0Item # noqa: PLC0415
        from ..models.company_disclosures_attributes_ratios_type_0 import CompanyDisclosuresAttributesRatiosType0 # noqa: PLC0415
        from ..models.company_disclosures_attributes_related_parties_type_0 import CompanyDisclosuresAttributesRelatedPartiesType0 # noqa: PLC0415
        from ..models.company_disclosures_attributes_use_of_funds_type_0_item import CompanyDisclosuresAttributesUseOfFundsType0Item # noqa: PLC0415
        from ..models.company_disclosures_attributes_voting_power_type_0_item import CompanyDisclosuresAttributesVotingPowerType0Item # noqa: PLC0415
        from ..models.disclosure_document import DisclosureDocument # noqa: PLC0415
        from ..models.disclosure_person import DisclosurePerson # noqa: PLC0415
        offering_id = self.offering_id

        filing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filing, Unset):
            filing = self.filing.to_dict()

        business: dict[str, Any] | Unset = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

        financial_statements: dict[str, Any] | Unset = UNSET
        if not isinstance(self.financial_statements, Unset):
            financial_statements = self.financial_statements.to_dict()

        ratios: dict[str, Any] | None | Unset
        if isinstance(self.ratios, Unset):
            ratios = UNSET
        elif isinstance(self.ratios, CompanyDisclosuresAttributesRatiosType0):
            ratios = self.ratios.to_dict()
        else:
            ratios = self.ratios

        current_position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_position, Unset):
            current_position = self.current_position.to_dict()

        financial_condition: None | str | Unset
        if isinstance(self.financial_condition, Unset):
            financial_condition = UNSET
        else:
            financial_condition = self.financial_condition

        financial_statement_documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.financial_statement_documents, Unset):
            financial_statement_documents = []
            for financial_statement_documents_item_data in self.financial_statement_documents:
                financial_statement_documents_item = financial_statement_documents_item_data.to_dict()
                financial_statement_documents.append(financial_statement_documents_item)



        investment_documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.investment_documents, Unset):
            investment_documents = []
            for investment_documents_item_data in self.investment_documents:
                investment_documents_item = investment_documents_item_data.to_dict()
                investment_documents.append(investment_documents_item)



        risks: list[str] | Unset = UNSET
        if not isinstance(self.risks, Unset):
            risks = self.risks



        use_of_funds: list[dict[str, Any]] | None | Unset
        if isinstance(self.use_of_funds, Unset):
            use_of_funds = UNSET
        elif isinstance(self.use_of_funds, list):
            use_of_funds = []
            for use_of_funds_type_0_item_data in self.use_of_funds:
                use_of_funds_type_0_item = use_of_funds_type_0_item_data.to_dict()
                use_of_funds.append(use_of_funds_type_0_item)


        else:
            use_of_funds = self.use_of_funds

        directors: list[dict[str, Any]] | None | Unset
        if isinstance(self.directors, Unset):
            directors = UNSET
        elif isinstance(self.directors, list):
            directors = []
            for directors_type_0_item_data in self.directors:
                directors_type_0_item = directors_type_0_item_data.to_dict()
                directors.append(directors_type_0_item)


        else:
            directors = self.directors

        officers: list[dict[str, Any]] | None | Unset
        if isinstance(self.officers, Unset):
            officers = UNSET
        elif isinstance(self.officers, list):
            officers = []
            for officers_type_0_item_data in self.officers:
                officers_type_0_item = officers_type_0_item_data.to_dict()
                officers.append(officers_type_0_item)


        else:
            officers = self.officers

        voting_power: list[dict[str, Any]] | None | Unset
        if isinstance(self.voting_power, Unset):
            voting_power = UNSET
        elif isinstance(self.voting_power, list):
            voting_power = []
            for voting_power_type_0_item_data in self.voting_power:
                voting_power_type_0_item = voting_power_type_0_item_data.to_dict()
                voting_power.append(voting_power_type_0_item)


        else:
            voting_power = self.voting_power

        capital_structure: list[dict[str, Any]] | None | Unset
        if isinstance(self.capital_structure, Unset):
            capital_structure = UNSET
        elif isinstance(self.capital_structure, list):
            capital_structure = []
            for capital_structure_type_0_item_data in self.capital_structure:
                capital_structure_type_0_item = capital_structure_type_0_item_data.to_dict()
                capital_structure.append(capital_structure_type_0_item)


        else:
            capital_structure = self.capital_structure

        prior_offerings: list[dict[str, Any]] | None | Unset
        if isinstance(self.prior_offerings, Unset):
            prior_offerings = UNSET
        elif isinstance(self.prior_offerings, list):
            prior_offerings = []
            for prior_offerings_type_0_item_data in self.prior_offerings:
                prior_offerings_type_0_item = prior_offerings_type_0_item_data.to_dict()
                prior_offerings.append(prior_offerings_type_0_item)


        else:
            prior_offerings = self.prior_offerings

        outstanding_notes: list[dict[str, Any]] | None | Unset
        if isinstance(self.outstanding_notes, Unset):
            outstanding_notes = UNSET
        elif isinstance(self.outstanding_notes, list):
            outstanding_notes = []
            for outstanding_notes_type_0_item_data in self.outstanding_notes:
                outstanding_notes_type_0_item = outstanding_notes_type_0_item_data.to_dict()
                outstanding_notes.append(outstanding_notes_type_0_item)


        else:
            outstanding_notes = self.outstanding_notes

        outstanding_debts: dict[str, Any] | None | Unset
        if isinstance(self.outstanding_debts, Unset):
            outstanding_debts = UNSET
        elif isinstance(self.outstanding_debts, CompanyDisclosuresAttributesOutstandingDebtsType0):
            outstanding_debts = self.outstanding_debts.to_dict()
        else:
            outstanding_debts = self.outstanding_debts

        related_parties: dict[str, Any] | None | Unset
        if isinstance(self.related_parties, Unset):
            related_parties = UNSET
        elif isinstance(self.related_parties, CompanyDisclosuresAttributesRelatedPartiesType0):
            related_parties = self.related_parties.to_dict()
        else:
            related_parties = self.related_parties


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if offering_id is not UNSET:
            field_dict["offering_id"] = offering_id
        if filing is not UNSET:
            field_dict["filing"] = filing
        if business is not UNSET:
            field_dict["business"] = business
        if financial_statements is not UNSET:
            field_dict["financial_statements"] = financial_statements
        if ratios is not UNSET:
            field_dict["ratios"] = ratios
        if current_position is not UNSET:
            field_dict["current_position"] = current_position
        if financial_condition is not UNSET:
            field_dict["financial_condition"] = financial_condition
        if financial_statement_documents is not UNSET:
            field_dict["financial_statement_documents"] = financial_statement_documents
        if investment_documents is not UNSET:
            field_dict["investment_documents"] = investment_documents
        if risks is not UNSET:
            field_dict["risks"] = risks
        if use_of_funds is not UNSET:
            field_dict["use_of_funds"] = use_of_funds
        if directors is not UNSET:
            field_dict["directors"] = directors
        if officers is not UNSET:
            field_dict["officers"] = officers
        if voting_power is not UNSET:
            field_dict["voting_power"] = voting_power
        if capital_structure is not UNSET:
            field_dict["capital_structure"] = capital_structure
        if prior_offerings is not UNSET:
            field_dict["prior_offerings"] = prior_offerings
        if outstanding_notes is not UNSET:
            field_dict["outstanding_notes"] = outstanding_notes
        if outstanding_debts is not UNSET:
            field_dict["outstanding_debts"] = outstanding_debts
        if related_parties is not UNSET:
            field_dict["related_parties"] = related_parties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_disclosures_attributes_business import CompanyDisclosuresAttributesBusiness # noqa: PLC0415
        from ..models.company_disclosures_attributes_capital_structure_type_0_item import CompanyDisclosuresAttributesCapitalStructureType0Item # noqa: PLC0415
        from ..models.company_disclosures_attributes_current_position import CompanyDisclosuresAttributesCurrentPosition # noqa: PLC0415
        from ..models.company_disclosures_attributes_filing import CompanyDisclosuresAttributesFiling # noqa: PLC0415
        from ..models.company_disclosures_attributes_financial_statements import CompanyDisclosuresAttributesFinancialStatements # noqa: PLC0415
        from ..models.company_disclosures_attributes_outstanding_debts_type_0 import CompanyDisclosuresAttributesOutstandingDebtsType0 # noqa: PLC0415
        from ..models.company_disclosures_attributes_outstanding_notes_type_0_item import CompanyDisclosuresAttributesOutstandingNotesType0Item # noqa: PLC0415
        from ..models.company_disclosures_attributes_prior_offerings_type_0_item import CompanyDisclosuresAttributesPriorOfferingsType0Item # noqa: PLC0415
        from ..models.company_disclosures_attributes_ratios_type_0 import CompanyDisclosuresAttributesRatiosType0 # noqa: PLC0415
        from ..models.company_disclosures_attributes_related_parties_type_0 import CompanyDisclosuresAttributesRelatedPartiesType0 # noqa: PLC0415
        from ..models.company_disclosures_attributes_use_of_funds_type_0_item import CompanyDisclosuresAttributesUseOfFundsType0Item # noqa: PLC0415
        from ..models.company_disclosures_attributes_voting_power_type_0_item import CompanyDisclosuresAttributesVotingPowerType0Item # noqa: PLC0415
        from ..models.disclosure_document import DisclosureDocument # noqa: PLC0415
        from ..models.disclosure_person import DisclosurePerson # noqa: PLC0415
        d = dict(src_dict)
        offering_id = d.pop("offering_id", UNSET)

        _filing = d.pop("filing", UNSET)
        filing: CompanyDisclosuresAttributesFiling | Unset
        if isinstance(_filing,  Unset):
            filing = UNSET
        else:
            filing = CompanyDisclosuresAttributesFiling.from_dict(_filing)




        _business = d.pop("business", UNSET)
        business: CompanyDisclosuresAttributesBusiness | Unset
        if isinstance(_business,  Unset):
            business = UNSET
        else:
            business = CompanyDisclosuresAttributesBusiness.from_dict(_business)




        _financial_statements = d.pop("financial_statements", UNSET)
        financial_statements: CompanyDisclosuresAttributesFinancialStatements | Unset
        if isinstance(_financial_statements,  Unset):
            financial_statements = UNSET
        else:
            financial_statements = CompanyDisclosuresAttributesFinancialStatements.from_dict(_financial_statements)




        def _parse_ratios(data: object) -> CompanyDisclosuresAttributesRatiosType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ratios_type_0 = CompanyDisclosuresAttributesRatiosType0.from_dict(data)



                return ratios_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyDisclosuresAttributesRatiosType0 | None | Unset, data)

        ratios = _parse_ratios(d.pop("ratios", UNSET))


        _current_position = d.pop("current_position", UNSET)
        current_position: CompanyDisclosuresAttributesCurrentPosition | Unset
        if isinstance(_current_position,  Unset):
            current_position = UNSET
        else:
            current_position = CompanyDisclosuresAttributesCurrentPosition.from_dict(_current_position)




        def _parse_financial_condition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        financial_condition = _parse_financial_condition(d.pop("financial_condition", UNSET))


        _financial_statement_documents = d.pop("financial_statement_documents", UNSET)
        financial_statement_documents: list[DisclosureDocument] | Unset = UNSET
        if _financial_statement_documents is not UNSET:
            financial_statement_documents = []
            for financial_statement_documents_item_data in _financial_statement_documents:
                financial_statement_documents_item = DisclosureDocument.from_dict(financial_statement_documents_item_data)



                financial_statement_documents.append(financial_statement_documents_item)


        _investment_documents = d.pop("investment_documents", UNSET)
        investment_documents: list[DisclosureDocument] | Unset = UNSET
        if _investment_documents is not UNSET:
            investment_documents = []
            for investment_documents_item_data in _investment_documents:
                investment_documents_item = DisclosureDocument.from_dict(investment_documents_item_data)



                investment_documents.append(investment_documents_item)


        risks = cast(list[str], d.pop("risks", UNSET))


        def _parse_use_of_funds(data: object) -> list[CompanyDisclosuresAttributesUseOfFundsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                use_of_funds_type_0 = []
                _use_of_funds_type_0 = data
                for use_of_funds_type_0_item_data in (_use_of_funds_type_0):
                    use_of_funds_type_0_item = CompanyDisclosuresAttributesUseOfFundsType0Item.from_dict(use_of_funds_type_0_item_data)



                    use_of_funds_type_0.append(use_of_funds_type_0_item)

                return use_of_funds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyDisclosuresAttributesUseOfFundsType0Item] | None | Unset, data)

        use_of_funds = _parse_use_of_funds(d.pop("use_of_funds", UNSET))


        def _parse_directors(data: object) -> list[DisclosurePerson] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                directors_type_0 = []
                _directors_type_0 = data
                for directors_type_0_item_data in (_directors_type_0):
                    directors_type_0_item = DisclosurePerson.from_dict(directors_type_0_item_data)



                    directors_type_0.append(directors_type_0_item)

                return directors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DisclosurePerson] | None | Unset, data)

        directors = _parse_directors(d.pop("directors", UNSET))


        def _parse_officers(data: object) -> list[DisclosurePerson] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                officers_type_0 = []
                _officers_type_0 = data
                for officers_type_0_item_data in (_officers_type_0):
                    officers_type_0_item = DisclosurePerson.from_dict(officers_type_0_item_data)



                    officers_type_0.append(officers_type_0_item)

                return officers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DisclosurePerson] | None | Unset, data)

        officers = _parse_officers(d.pop("officers", UNSET))


        def _parse_voting_power(data: object) -> list[CompanyDisclosuresAttributesVotingPowerType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                voting_power_type_0 = []
                _voting_power_type_0 = data
                for voting_power_type_0_item_data in (_voting_power_type_0):
                    voting_power_type_0_item = CompanyDisclosuresAttributesVotingPowerType0Item.from_dict(voting_power_type_0_item_data)



                    voting_power_type_0.append(voting_power_type_0_item)

                return voting_power_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyDisclosuresAttributesVotingPowerType0Item] | None | Unset, data)

        voting_power = _parse_voting_power(d.pop("voting_power", UNSET))


        def _parse_capital_structure(data: object) -> list[CompanyDisclosuresAttributesCapitalStructureType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                capital_structure_type_0 = []
                _capital_structure_type_0 = data
                for capital_structure_type_0_item_data in (_capital_structure_type_0):
                    capital_structure_type_0_item = CompanyDisclosuresAttributesCapitalStructureType0Item.from_dict(capital_structure_type_0_item_data)



                    capital_structure_type_0.append(capital_structure_type_0_item)

                return capital_structure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyDisclosuresAttributesCapitalStructureType0Item] | None | Unset, data)

        capital_structure = _parse_capital_structure(d.pop("capital_structure", UNSET))


        def _parse_prior_offerings(data: object) -> list[CompanyDisclosuresAttributesPriorOfferingsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prior_offerings_type_0 = []
                _prior_offerings_type_0 = data
                for prior_offerings_type_0_item_data in (_prior_offerings_type_0):
                    prior_offerings_type_0_item = CompanyDisclosuresAttributesPriorOfferingsType0Item.from_dict(prior_offerings_type_0_item_data)



                    prior_offerings_type_0.append(prior_offerings_type_0_item)

                return prior_offerings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyDisclosuresAttributesPriorOfferingsType0Item] | None | Unset, data)

        prior_offerings = _parse_prior_offerings(d.pop("prior_offerings", UNSET))


        def _parse_outstanding_notes(data: object) -> list[CompanyDisclosuresAttributesOutstandingNotesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                outstanding_notes_type_0 = []
                _outstanding_notes_type_0 = data
                for outstanding_notes_type_0_item_data in (_outstanding_notes_type_0):
                    outstanding_notes_type_0_item = CompanyDisclosuresAttributesOutstandingNotesType0Item.from_dict(outstanding_notes_type_0_item_data)



                    outstanding_notes_type_0.append(outstanding_notes_type_0_item)

                return outstanding_notes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyDisclosuresAttributesOutstandingNotesType0Item] | None | Unset, data)

        outstanding_notes = _parse_outstanding_notes(d.pop("outstanding_notes", UNSET))


        def _parse_outstanding_debts(data: object) -> CompanyDisclosuresAttributesOutstandingDebtsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                outstanding_debts_type_0 = CompanyDisclosuresAttributesOutstandingDebtsType0.from_dict(data)



                return outstanding_debts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyDisclosuresAttributesOutstandingDebtsType0 | None | Unset, data)

        outstanding_debts = _parse_outstanding_debts(d.pop("outstanding_debts", UNSET))


        def _parse_related_parties(data: object) -> CompanyDisclosuresAttributesRelatedPartiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                related_parties_type_0 = CompanyDisclosuresAttributesRelatedPartiesType0.from_dict(data)



                return related_parties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyDisclosuresAttributesRelatedPartiesType0 | None | Unset, data)

        related_parties = _parse_related_parties(d.pop("related_parties", UNSET))


        company_disclosures_attributes = cls(
            offering_id=offering_id,
            filing=filing,
            business=business,
            financial_statements=financial_statements,
            ratios=ratios,
            current_position=current_position,
            financial_condition=financial_condition,
            financial_statement_documents=financial_statement_documents,
            investment_documents=investment_documents,
            risks=risks,
            use_of_funds=use_of_funds,
            directors=directors,
            officers=officers,
            voting_power=voting_power,
            capital_structure=capital_structure,
            prior_offerings=prior_offerings,
            outstanding_notes=outstanding_notes,
            outstanding_debts=outstanding_debts,
            related_parties=related_parties,
        )


        company_disclosures_attributes.additional_properties = d
        return company_disclosures_attributes

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
