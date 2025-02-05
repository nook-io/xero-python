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


class PaymentTermType(str, Enum):
    """
    PaymentTermType
    """

    """
    allowed enum values
    """
    DAYSAFTERBILLDATE = "DAYSAFTERBILLDATE"
    DAYSAFTERBILLMONTH = "DAYSAFTERBILLMONTH"
    OFCURRENTMONTH = "OFCURRENTMONTH"
    OFFOLLOWINGMONTH = "OFFOLLOWINGMONTH"

    @classmethod
    def from_json(cls, json_str: str) -> "PaymentTermType":
        """Create an instance of PaymentTermType from a JSON string"""
        return PaymentTermType(json.loads(json_str))
