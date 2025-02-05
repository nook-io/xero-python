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


class EmploymentTerminationPaymentType(str, Enum):
    """
    EmploymentTerminationPaymentType
    """

    """
    allowed enum values
    """
    O = "O"
    R = "R"

    @classmethod
    def from_json(cls, json_str: str) -> "EmploymentTerminationPaymentType":
        """Create an instance of EmploymentTerminationPaymentType from a JSON string"""
        return EmploymentTerminationPaymentType(json.loads(json_str))
