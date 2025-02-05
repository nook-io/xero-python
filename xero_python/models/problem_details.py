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
from typing import Any, Optional

from pydantic import BaseModel, StrictInt, StrictStr


class ProblemDetails(BaseModel):
    """
    ProblemDetails
    """

    detail: Optional[StrictStr] = None
    extensions: Optional[dict[str, Any]] = None
    instance: Optional[StrictStr] = None
    status: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    __properties = ["detail", "extensions", "instance", "status", "title", "type"]

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
    def from_json(cls, json_str: str) -> ProblemDetails:
        """Create an instance of ProblemDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProblemDetails:
        """Create an instance of ProblemDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProblemDetails.parse_obj(obj)

        _obj = ProblemDetails.parse_obj(
            {
                "detail": obj.get("detail"),
                "extensions": obj.get("extensions"),
                "instance": obj.get("instance"),
                "status": obj.get("status"),
                "title": obj.get("title"),
                "type": obj.get("type"),
            }
        )
        return _obj
