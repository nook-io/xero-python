"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Optional

from pydantic import BaseModel, Field

from xero_python.models.earnings_rate import EarningsRate
from xero_python.models.pagination import Pagination
from xero_python.models.problem import Problem


class EarningsRateObject(BaseModel):
    """
    EarningsRateObject
    """

    pagination: Optional[Pagination] = None
    problem: Optional[Problem] = None
    earnings_rate: Optional[EarningsRate] = Field(default=None, alias="earningsRate")
    __properties = ["pagination", "problem", "earningsRate"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EarningsRateObject:
        """Create an instance of EarningsRateObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict["pagination"] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of problem
        if self.problem:
            _dict["problem"] = self.problem.to_dict()
        # override the default output from pydantic by calling `to_dict()` of earnings_rate
        if self.earnings_rate:
            _dict["earningsRate"] = self.earnings_rate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EarningsRateObject:
        """Create an instance of EarningsRateObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EarningsRateObject.parse_obj(obj)

        _obj = EarningsRateObject.parse_obj(
            {
                "pagination": Pagination.from_dict(obj.get("pagination"))
                if obj.get("pagination") is not None
                else None,
                "problem": Problem.from_dict(obj.get("problem")) if obj.get("problem") is not None else None,
                "earnings_rate": EarningsRate.from_dict(obj.get("earningsRate"))
                if obj.get("earningsRate") is not None
                else None,
            }
        )
        return _obj
