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

from pydantic import BaseModel, Field, StrictFloat, StrictInt

from xero_python.models.data_source_response import DataSourceResponse


class StatementLinesResponse(BaseModel):
    """
    StatementLinesResponse
    """

    unreconciled_amount_pos: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="unreconciledAmountPos",
        description="Sum of the amounts of all statement lines where both the reconciled flag is set to FALSE, and the amount is positive.",
    )
    unreconciled_amount_neg: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="unreconciledAmountNeg",
        description="Sum of the amounts of all statement lines where both the reconciled flag is set to FALSE, and the amount is negative.",
    )
    unreconciled_lines: Optional[StrictInt] = Field(
        default=None,
        alias="unreconciledLines",
        description="Count of all statement lines where the reconciled flag is set to FALSE.",
    )
    avg_days_unreconciled_pos: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="avgDaysUnreconciledPos",
        description="Sum-product of age of statement line in days multiplied by transaction amount, divided by the sum of transaction amount - in for those statement lines in which the reconciled flag is set to FALSE, and the amount is positive. Provides an indication of the age of unreconciled transactions.",
    )
    avg_days_unreconciled_neg: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="avgDaysUnreconciledNeg",
        description="Sum-product of age of statement line in days multiplied by transaction amount, divided by the sum of transaction amount - in for those statement lines in which the reconciled flag is set to FALSE, and the amount is negative. Provides an indication of the age of unreconciled transactions.",
    )
    earliest_unreconciled_transaction: Optional[date] = Field(
        default=None,
        alias="earliestUnreconciledTransaction",
        description="UTC Date which is the earliest transaction date of a statement line for which the reconciled flag is set to FALSE.  This date is represented in ISO 8601 format.",
    )
    latest_unreconciled_transaction: Optional[date] = Field(
        default=None,
        alias="latestUnreconciledTransaction",
        description="UTC Date which is the latest transaction date of a statement line for which the reconciled flag is set to FALSE.  This date is represented in ISO 8601 format.",
    )
    deleted_amount: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="deletedAmount",
        description="Sum of the amounts of all deleted statement lines.  Transactions may be deleted due to duplication or otherwise.",
    )
    total_amount: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="totalAmount",
        description="Sum of the amounts of all statement lines.  This is used as a metric of comparison to the unreconciled figures above.",
    )
    data_source: Optional[DataSourceResponse] = Field(default=None, alias="dataSource")
    earliest_reconciled_transaction: Optional[date] = Field(
        default=None,
        alias="earliestReconciledTransaction",
        description="UTC Date which is the earliest transaction date of a statement line for which the reconciled flag is set to TRUE.  This date is represented in ISO 8601 format.",
    )
    latest_reconciled_transaction: Optional[date] = Field(
        default=None,
        alias="latestReconciledTransaction",
        description="UTC Date which is the latest transaction date of a statement line for which the reconciled flag is set to TRUE.  This date is represented in ISO 8601 format.",
    )
    reconciled_amount_pos: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="reconciledAmountPos",
        description="Sum of the amounts of all statement lines where both the reconciled flag is set to TRUE, and the amount is positive.",
    )
    reconciled_amount_neg: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="reconciledAmountNeg",
        description="Sum of the amounts of all statement lines where both the reconciled flag is set to TRUE, and the amount is negative.",
    )
    reconciled_lines: Optional[StrictInt] = Field(
        default=None,
        alias="reconciledLines",
        description="Count of all statement lines where the reconciled flag is set to TRUE",
    )
    total_amount_pos: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="totalAmountPos",
        description="Sum of the amounts of all statement lines where the amount is positive",
    )
    total_amount_neg: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="totalAmountNeg",
        description="Sum of the amounts of all statement lines where the amount is negative.",
    )
    __properties = [
        "unreconciledAmountPos",
        "unreconciledAmountNeg",
        "unreconciledLines",
        "avgDaysUnreconciledPos",
        "avgDaysUnreconciledNeg",
        "earliestUnreconciledTransaction",
        "latestUnreconciledTransaction",
        "deletedAmount",
        "totalAmount",
        "dataSource",
        "earliestReconciledTransaction",
        "latestReconciledTransaction",
        "reconciledAmountPos",
        "reconciledAmountNeg",
        "reconciledLines",
        "totalAmountPos",
        "totalAmountNeg",
    ]

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
    def from_json(cls, json_str: str) -> StatementLinesResponse:
        """Create an instance of StatementLinesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data_source
        if self.data_source:
            _dict["dataSource"] = self.data_source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StatementLinesResponse:
        """Create an instance of StatementLinesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StatementLinesResponse.parse_obj(obj)

        _obj = StatementLinesResponse.parse_obj(
            {
                "unreconciled_amount_pos": obj.get("unreconciledAmountPos"),
                "unreconciled_amount_neg": obj.get("unreconciledAmountNeg"),
                "unreconciled_lines": obj.get("unreconciledLines"),
                "avg_days_unreconciled_pos": obj.get("avgDaysUnreconciledPos"),
                "avg_days_unreconciled_neg": obj.get("avgDaysUnreconciledNeg"),
                "earliest_unreconciled_transaction": obj.get("earliestUnreconciledTransaction"),
                "latest_unreconciled_transaction": obj.get("latestUnreconciledTransaction"),
                "deleted_amount": obj.get("deletedAmount"),
                "total_amount": obj.get("totalAmount"),
                "data_source": DataSourceResponse.from_dict(obj.get("dataSource"))
                if obj.get("dataSource") is not None
                else None,
                "earliest_reconciled_transaction": obj.get("earliestReconciledTransaction"),
                "latest_reconciled_transaction": obj.get("latestReconciledTransaction"),
                "reconciled_amount_pos": obj.get("reconciledAmountPos"),
                "reconciled_amount_neg": obj.get("reconciledAmountNeg"),
                "reconciled_lines": obj.get("reconciledLines"),
                "total_amount_pos": obj.get("totalAmountPos"),
                "total_amount_neg": obj.get("totalAmountNeg"),
            }
        )
        return _obj
