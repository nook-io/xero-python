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
from datetime import date
from typing import Optional, Union

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator


class LeavePeriod2(BaseModel):
    """
    LeavePeriod2
    """

    period_start_date: Optional[date] = Field(
        default=None, alias="periodStartDate", description="The Pay Period Start Date (YYYY-MM-DD)"
    )
    period_end_date: Optional[date] = Field(
        default=None, alias="periodEndDate", description="The Pay Period End Date (YYYY-MM-DD)"
    )
    number_of_units: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="numberOfUnits", description="The Number of Units for the leave"
    )
    period_status: Optional[StrictStr] = Field(default=None, alias="periodStatus", description="Period Status")
    __properties = ["periodStartDate", "periodEndDate", "numberOfUnits", "periodStatus"]

    @validator("period_status")
    def period_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("Approved", "Completed"):
            raise ValueError("must be one of enum values ('Approved', 'Completed')")
        return value

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
    def from_json(cls, json_str: str) -> LeavePeriod2:
        """Create an instance of LeavePeriod2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LeavePeriod2:
        """Create an instance of LeavePeriod2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LeavePeriod2.parse_obj(obj)

        _obj = LeavePeriod2.parse_obj(
            {
                "period_start_date": obj.get("periodStartDate"),
                "period_end_date": obj.get("periodEndDate"),
                "number_of_units": obj.get("numberOfUnits"),
                "period_status": obj.get("periodStatus"),
            }
        )
        return _obj
