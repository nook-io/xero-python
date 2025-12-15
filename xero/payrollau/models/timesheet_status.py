from enum import Enum


class TimesheetStatus(Enum):
    DRAFT = "DRAFT"
    PROCESSED = "PROCESSED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    REQUESTED = "REQUESTED"
