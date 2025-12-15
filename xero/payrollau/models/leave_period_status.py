from enum import Enum


class LeavePeriodStatus(Enum):
    SCHEDULED = "SCHEDULED"
    PROCESSED = "PROCESSED"
    REQUESTED = "REQUESTED"
    REJECTED = "REJECTED"
