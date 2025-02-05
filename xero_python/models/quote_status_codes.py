"""
merged spec

merged spec

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import json
import re  # noqa: F401

from aenum import Enum


class QuoteStatusCodes(str, Enum):
    """
    The status of the quote.
    """

    """
    allowed enum values
    """
    DRAFT = "DRAFT"
    SENT = "SENT"
    DECLINED = "DECLINED"
    ACCEPTED = "ACCEPTED"
    INVOICED = "INVOICED"
    DELETED = "DELETED"

    @classmethod
    def from_json(cls, json_str: str) -> "QuoteStatusCodes":
        """Create an instance of QuoteStatusCodes from a JSON string"""
        return QuoteStatusCodes(json.loads(json_str))
