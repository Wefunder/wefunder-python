from enum import StrEnum

class CreateWebhookEndpointBodyEventsItem(StrEnum):
    INVESTMENT_AMOUNT_CHANGED = "investment.amount_changed"
    INVESTMENT_CANCELED = "investment.canceled"
    INVESTMENT_CHANGED = "investment.changed"
    INVESTMENT_CONVERTED = "investment.converted"
    INVESTMENT_CREATED = "investment.created"
    INVESTMENT_EXECUTED = "investment.executed"
    INVESTMENT_REINSTATED = "investment.reinstated"
    INVESTMENT_SESSION_CANCELED = "investment_session.canceled"
    INVESTMENT_SESSION_COMPLETED = "investment_session.completed"
    INVESTMENT_SESSION_CREATED = "investment_session.created"
    INVESTMENT_SESSION_EXPIRED = "investment_session.expired"
    INVESTMENT_SESSION_STARTED = "investment_session.started"
    OFFERING_CANCELED = "offering.canceled"
    OFFERING_CLOSED = "offering.closed"
    OFFERING_CLOSING = "offering.closing"
    OFFERING_OPENED = "offering.opened"
    SYNDICATE_MEMBER_APPLIED = "syndicate_member.applied"
    SYNDICATE_MEMBER_APPROVED = "syndicate_member.approved"
    SYNDICATE_MEMBER_INVITED = "syndicate_member.invited"
    SYNDICATE_MEMBER_JOINED = "syndicate_member.joined"
    SYNDICATE_MEMBER_REINVITED = "syndicate_member.reinvited"

    def __str__(self) -> str:
        return str(self.value)
