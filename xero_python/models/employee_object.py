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

from pydantic import BaseModel

from xero_python.models.employee import Employee
from xero_python.models.pagination import Pagination
from xero_python.models.problem import Problem


class EmployeeObject(BaseModel):
    """
    EmployeeObject
    """

    pagination: Optional[Pagination] = None
    employee: Optional[Employee] = None
    problem: Optional[Problem] = None
    __properties = ["pagination", "employee", "problem"]

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
    def from_json(cls, json_str: str) -> EmployeeObject:
        """Create an instance of EmployeeObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict["pagination"] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of employee
        if self.employee:
            _dict["employee"] = self.employee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of problem
        if self.problem:
            _dict["problem"] = self.problem.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EmployeeObject:
        """Create an instance of EmployeeObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EmployeeObject.parse_obj(obj)

        _obj = EmployeeObject.parse_obj(
            {
                "pagination": Pagination.from_dict(obj.get("pagination"))
                if obj.get("pagination") is not None
                else None,
                "employee": Employee.from_dict(obj.get("employee")) if obj.get("employee") is not None else None,
                "problem": Problem.from_dict(obj.get("problem")) if obj.get("problem") is not None else None,
            }
        )
        return _obj
