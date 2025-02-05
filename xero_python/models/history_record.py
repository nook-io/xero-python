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

from pydantic import BaseModel, Field, StrictStr


class HistoryRecord(BaseModel):
    """
    HistoryRecord
    """

    details: Optional[StrictStr] = Field(default=None, alias="Details", description="details")
    changes: Optional[StrictStr] = Field(default=None, alias="Changes", description="Name of branding theme")
    user: Optional[StrictStr] = Field(default=None, alias="User", description="has a value of 0")
    date_utc: Optional[StrictStr] = Field(
        default=None, alias="DateUTC", description="UTC timestamp of creation date of branding theme"
    )
    __properties = ["Details", "Changes", "User", "DateUTC"]

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
    def from_json(cls, json_str: str) -> HistoryRecord:
        """Create an instance of HistoryRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={"date_utc"}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HistoryRecord:
        """Create an instance of HistoryRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HistoryRecord.parse_obj(obj)

        _obj = HistoryRecord.parse_obj(
            {
                "details": obj.get("Details"),
                "changes": obj.get("Changes"),
                "user": obj.get("User"),
                "date_utc": obj.get("DateUTC"),
            }
        )
        return _obj
