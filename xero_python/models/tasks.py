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

from pydantic import BaseModel, conlist

from xero_python.models.pagination2 import Pagination2
from xero_python.models.task import Task


class Tasks(BaseModel):
    """
    Tasks
    """

    pagination: Optional[Pagination2] = None
    items: Optional[conlist(Task)] = None
    __properties = ["pagination", "items"]

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
    def from_json(cls, json_str: str) -> Tasks:
        """Create an instance of Tasks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict["pagination"] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict["items"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Tasks:
        """Create an instance of Tasks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Tasks.parse_obj(obj)

        _obj = Tasks.parse_obj(
            {
                "pagination": Pagination2.from_dict(obj.get("pagination"))
                if obj.get("pagination") is not None
                else None,
                "items": [Task.from_dict(_item) for _item in obj.get("items")]
                if obj.get("items") is not None
                else None,
            }
        )
        return _obj
