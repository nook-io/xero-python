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

from pydantic import BaseModel, Field, StrictInt, conlist

from xero_python.models.file_object import FileObject


class Files(BaseModel):
    """
    Files
    """

    total_count: Optional[StrictInt] = Field(default=None, alias="TotalCount")
    page: Optional[StrictInt] = Field(default=None, alias="Page")
    per_page: Optional[StrictInt] = Field(default=None, alias="PerPage")
    items: Optional[conlist(FileObject)] = Field(default=None, alias="Items")
    __properties = ["TotalCount", "Page", "PerPage", "Items"]

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
    def from_json(cls, json_str: str) -> Files:
        """Create an instance of Files from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict["Items"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Files:
        """Create an instance of Files from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Files.parse_obj(obj)

        _obj = Files.parse_obj(
            {
                "total_count": obj.get("TotalCount"),
                "page": obj.get("Page"),
                "per_page": obj.get("PerPage"),
                "items": [FileObject.from_dict(_item) for _item in obj.get("Items")]
                if obj.get("Items") is not None
                else None,
            }
        )
        return _obj
