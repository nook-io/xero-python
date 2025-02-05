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

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator


class EmployeeStatutorySickLeave(BaseModel):
    """
    EmployeeStatutorySickLeave
    """

    statutory_leave_id: Optional[StrictStr] = Field(
        default=None, alias="statutoryLeaveID", description="The unique identifier (guid) of a statutory leave"
    )
    employee_id: StrictStr = Field(
        default=..., alias="employeeID", description="The unique identifier (guid) of the employee"
    )
    leave_type_id: StrictStr = Field(
        default=...,
        alias="leaveTypeID",
        description='The unique identifier (guid) of the "Statutory Sick Leave (non-pensionable)" pay item',
    )
    start_date: date = Field(default=..., alias="startDate", description="The date when the leave starts")
    end_date: date = Field(default=..., alias="endDate", description="The date when the leave ends")
    type: Optional[StrictStr] = Field(default=None, description="the type of statutory leave")
    status: Optional[StrictStr] = Field(default=None, description="the type of statutory leave")
    work_pattern: conlist(StrictStr) = Field(
        default=...,
        alias="workPattern",
        description="The days of the work week the employee is scheduled to work at the time the leave is taken",
    )
    is_pregnancy_related: StrictBool = Field(
        default=..., alias="isPregnancyRelated", description="Whether the sick leave was pregnancy related"
    )
    sufficient_notice: StrictBool = Field(
        default=...,
        alias="sufficientNotice",
        description="Whether the employee provided sufficient notice and documentation as required by the employer supporting the sick leave request",
    )
    is_entitled: Optional[StrictBool] = Field(
        default=None, alias="isEntitled", description="Whether the leave was entitled to receive payment"
    )
    entitlement_weeks_requested: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="entitlementWeeksRequested", description="The amount of requested time (in weeks)"
    )
    entitlement_weeks_qualified: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="entitlementWeeksQualified",
        description="The amount of statutory sick leave time off (in weeks) that is available to take at the time the leave was requested",
    )
    entitlement_weeks_remaining: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="entitlementWeeksRemaining",
        description="A calculated amount of time (in weeks) that remains for the statutory sick leave period",
    )
    overlaps_with_other_leave: Optional[StrictBool] = Field(
        default=None,
        alias="overlapsWithOtherLeave",
        description="Whether another leave (Paternity, Shared Parental specifically) occurs during the requested leave's period. While this is allowed it could affect payment amounts",
    )
    entitlement_failure_reasons: Optional[conlist(StrictStr)] = Field(
        default=None,
        alias="entitlementFailureReasons",
        description='If the leave requested was considered "not entitled", the reasons why are listed here.',
    )
    __properties = [
        "statutoryLeaveID",
        "employeeID",
        "leaveTypeID",
        "startDate",
        "endDate",
        "type",
        "status",
        "workPattern",
        "isPregnancyRelated",
        "sufficientNotice",
        "isEntitled",
        "entitlementWeeksRequested",
        "entitlementWeeksQualified",
        "entitlementWeeksRemaining",
        "overlapsWithOtherLeave",
        "entitlementFailureReasons",
    ]

    @validator("entitlement_failure_reasons")
    def entitlement_failure_reasons_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in (
                "UnableToCalculateAwe",
                "AweLowerThanLel",
                "NotQualifiedInPreviousPiw",
                "ExceededMaximumEntitlementWeeksOfSsp",
                "ExceededMaximumDurationOfPiw",
                "SufficientNoticeNotGiven",
            ):
                raise ValueError(
                    "each list item must be one of ('UnableToCalculateAwe', 'AweLowerThanLel', 'NotQualifiedInPreviousPiw', 'ExceededMaximumEntitlementWeeksOfSsp', 'ExceededMaximumDurationOfPiw', 'SufficientNoticeNotGiven')"
                )
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
    def from_json(cls, json_str: str) -> EmployeeStatutorySickLeave:
        """Create an instance of EmployeeStatutorySickLeave from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EmployeeStatutorySickLeave:
        """Create an instance of EmployeeStatutorySickLeave from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EmployeeStatutorySickLeave.parse_obj(obj)

        _obj = EmployeeStatutorySickLeave.parse_obj(
            {
                "statutory_leave_id": obj.get("statutoryLeaveID"),
                "employee_id": obj.get("employeeID"),
                "leave_type_id": obj.get("leaveTypeID"),
                "start_date": obj.get("startDate"),
                "end_date": obj.get("endDate"),
                "type": obj.get("type"),
                "status": obj.get("status"),
                "work_pattern": obj.get("workPattern"),
                "is_pregnancy_related": obj.get("isPregnancyRelated"),
                "sufficient_notice": obj.get("sufficientNotice"),
                "is_entitled": obj.get("isEntitled"),
                "entitlement_weeks_requested": obj.get("entitlementWeeksRequested"),
                "entitlement_weeks_qualified": obj.get("entitlementWeeksQualified"),
                "entitlement_weeks_remaining": obj.get("entitlementWeeksRemaining"),
                "overlaps_with_other_leave": obj.get("overlapsWithOtherLeave"),
                "entitlement_failure_reasons": obj.get("entitlementFailureReasons"),
            }
        )
        return _obj
