from enum import StrEnum


class GetCompanyDisclosuresSectionsItem(StrEnum):
    BUSINESS = "business"
    CAPITAL_STRUCTURE = "capital_structure"
    CURRENT_POSITION = "current_position"
    DIRECTORS = "directors"
    FINANCIAL_CONDITION = "financial_condition"
    FINANCIAL_STATEMENTS = "financial_statements"
    FINANCIAL_STATEMENT_DOCUMENTS = "financial_statement_documents"
    INVESTMENT_DOCUMENTS = "investment_documents"
    OFFICERS = "officers"
    OUTSTANDING_DEBTS = "outstanding_debts"
    OUTSTANDING_NOTES = "outstanding_notes"
    PRIOR_OFFERINGS = "prior_offerings"
    RATIOS = "ratios"
    RELATED_PARTIES = "related_parties"
    RISKS = "risks"
    USE_OF_FUNDS = "use_of_funds"
    VOTING_POWER = "voting_power"

    def __str__(self) -> str:
        return str(self.value)
