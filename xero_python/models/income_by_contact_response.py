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

from pydantic import BaseModel, Field, StrictFloat, StrictInt, conlist

from xero_python.models.contact_detail import ContactDetail
from xero_python.models.manual_journal_total import ManualJournalTotal
from xero_python.models.total_detail import TotalDetail
from xero_python.models.total_other import TotalOther


class IncomeByContactResponse(BaseModel):
    """
    IncomeByContactResponse
    """

    start_date: Optional[date] = Field(default=None, alias="startDate", description="Start date of the report")
    end_date: Optional[date] = Field(default=None, alias="endDate", description="End date of the report")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total value")
    total_detail: Optional[TotalDetail] = Field(default=None, alias="totalDetail")
    total_other: Optional[TotalOther] = Field(default=None, alias="totalOther")
    contacts: Optional[conlist(ContactDetail)] = None
    manual_journals: Optional[ManualJournalTotal] = Field(default=None, alias="manualJournals")
    __properties = ["startDate", "endDate", "total", "totalDetail", "totalOther", "contacts", "manualJournals"]

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
    def from_json(cls, json_str: str) -> IncomeByContactResponse:
        """Create an instance of IncomeByContactResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of total_detail
        if self.total_detail:
            _dict["totalDetail"] = self.total_detail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_other
        if self.total_other:
            _dict["totalOther"] = self.total_other.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in contacts (list)
        _items = []
        if self.contacts:
            for _item in self.contacts:
                if _item:
                    _items.append(_item.to_dict())
            _dict["contacts"] = _items
        # override the default output from pydantic by calling `to_dict()` of manual_journals
        if self.manual_journals:
            _dict["manualJournals"] = self.manual_journals.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IncomeByContactResponse:
        """Create an instance of IncomeByContactResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IncomeByContactResponse.parse_obj(obj)

        _obj = IncomeByContactResponse.parse_obj(
            {
                "start_date": obj.get("startDate"),
                "end_date": obj.get("endDate"),
                "total": obj.get("total"),
                "total_detail": TotalDetail.from_dict(obj.get("totalDetail"))
                if obj.get("totalDetail") is not None
                else None,
                "total_other": TotalOther.from_dict(obj.get("totalOther"))
                if obj.get("totalOther") is not None
                else None,
                "contacts": [ContactDetail.from_dict(_item) for _item in obj.get("contacts")]
                if obj.get("contacts") is not None
                else None,
                "manual_journals": ManualJournalTotal.from_dict(obj.get("manualJournals"))
                if obj.get("manualJournals") is not None
                else None,
            }
        )
        return _obj
