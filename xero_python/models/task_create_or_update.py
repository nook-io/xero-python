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
from typing import Optional, Union

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr

from xero_python.models.amount import Amount


class TaskCreateOrUpdate(BaseModel):
    """
    TaskCreateOrUpdate
    """

    name: constr(strict=True) = Field(default=..., description="Name of the task. Max length 100 characters.")
    rate: Union[StrictFloat, StrictInt] = Field(...)
    charge_type: StrictStr = Field(default=..., alias="chargeType")
    estimate_minutes: Optional[StrictInt] = Field(
        default=None, alias="estimateMinutes", description="An estimated time to perform the task"
    )
    __properties = ["name", "rate", "chargeType", "estimateMinutes"]

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
    def from_json(cls, json_str: str) -> TaskCreateOrUpdate:
        """Create an instance of TaskCreateOrUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of rate
        if self.rate:
            _dict["rate"] = self.rate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskCreateOrUpdate:
        """Create an instance of TaskCreateOrUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskCreateOrUpdate.parse_obj(obj)

        _obj = TaskCreateOrUpdate.parse_obj(
            {
                "name": obj.get("name"),
                "rate": Amount.from_dict(obj.get("rate")) if obj.get("rate") is not None else None,
                "charge_type": obj.get("chargeType"),
                "estimate_minutes": obj.get("estimateMinutes"),
            }
        )
        return _obj
