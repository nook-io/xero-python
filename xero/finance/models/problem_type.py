from enum import Enum


class ProblemType(Enum):
    NOTSET = "NotSet"
    BANK_ACCOUNT_NOT_FOUND = "bank-account-not-found"
    INTERNAL_ERROR = "internal-error"
    INVALID_APPLICATION = "invalid-application"
    INVALID_REQUEST = "invalid-request"
    ORGANISATION_NOT_FOUND = "organisation-not-found"
    ORGANISATION_OFFLINE = "organisation-offline"
    REQUEST_TIMEOUT = "request-timeout"
    SERVICE_UNAVAILABLE = "service-unavailable"
    UNAUTHORIZED = "unauthorized"
    RATE_LIMIT_ERROR = "rate-limit-error"
