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
from datetime import date, datetime
from typing import Optional, Union

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr


class CurrentStatementResponse(BaseModel):
    """
    CurrentStatementResponse
    """

    start_date: Optional[date] = Field(
        default=None,
        alias="startDate",
        description="Looking at the most recent bank statement, this field indicates the first date which transactions on this statement pertain to. This date is represented in ISO 8601 format.",
    )
    end_date: Optional[date] = Field(
        default=None,
        alias="endDate",
        description="Looking at the most recent bank statement, this field indicates the last date which transactions on this statement pertain to. This date is represented in ISO 8601 format.",
    )
    start_balance: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="startBalance",
        description="Looking at the most recent bank statement, this field indicates the balance before the transactions on the statement are applied (note, this is not always populated by the bank in every single instance (~10%)).",
    )
    end_balance: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="endBalance",
        description="Looking at the most recent bank statement, this field indicates the balance after the transactions on the statement are applied (note, this is not always populated by the bank in every single instance (~10%)).",
    )
    imported_date_time_utc: Optional[datetime] = Field(
        default=None,
        alias="importedDateTimeUtc",
        description="Looking at the most recent bank statement, this field indicates when the document was imported into Xero.  This date is represented in ISO 8601 format.",
    )
    import_source_type: Optional[StrictStr] = Field(
        default=None,
        alias="importSourceType",
        description="Looking at the most recent bank statement, this field indicates the source of the data (direct bank feed, indirect bank feed, file upload, or manual keying).",
    )
    __properties = ["startDate", "endDate", "startBalance", "endBalance", "importedDateTimeUtc", "importSourceType"]

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
    def from_json(cls, json_str: str) -> CurrentStatementResponse:
        """Create an instance of CurrentStatementResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CurrentStatementResponse:
        """Create an instance of CurrentStatementResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CurrentStatementResponse.parse_obj(obj)

        _obj = CurrentStatementResponse.parse_obj(
            {
                "start_date": obj.get("startDate"),
                "end_date": obj.get("endDate"),
                "start_balance": obj.get("startBalance"),
                "end_balance": obj.get("endBalance"),
                "imported_date_time_utc": obj.get("importedDateTimeUtc"),
                "import_source_type": obj.get("importSourceType"),
            }
        )
        return _obj
