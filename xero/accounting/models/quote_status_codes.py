from enum import Enum


class QuoteStatusCodes(Enum):
    DRAFT = "DRAFT"
    SENT = "SENT"
    DECLINED = "DECLINED"
    ACCEPTED = "ACCEPTED"
    INVOICED = "INVOICED"
    DELETED = "DELETED"
