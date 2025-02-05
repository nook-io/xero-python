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

from pydantic import BaseModel, Field, conlist

from xero_python.models.contact_group import ContactGroup


class ContactGroups(BaseModel):
    """
    ContactGroups
    """

    contact_groups: Optional[conlist(ContactGroup)] = Field(default=None, alias="ContactGroups")
    __properties = ["ContactGroups"]

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
    def from_json(cls, json_str: str) -> ContactGroups:
        """Create an instance of ContactGroups from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in contact_groups (list)
        _items = []
        if self.contact_groups:
            for _item in self.contact_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict["ContactGroups"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContactGroups:
        """Create an instance of ContactGroups from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContactGroups.parse_obj(obj)

        _obj = ContactGroups.parse_obj(
            {
                "contact_groups": [ContactGroup.from_dict(_item) for _item in obj.get("ContactGroups")]
                if obj.get("ContactGroups") is not None
                else None
            }
        )
        return _obj
