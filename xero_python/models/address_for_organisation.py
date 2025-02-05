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

from pydantic import BaseModel, Field, StrictStr, constr, validator


class AddressForOrganisation(BaseModel):
    """
    AddressForOrganisation
    """

    address_type: Optional[StrictStr] = Field(
        default=None, alias="AddressType", description="define the type of address"
    )
    address_line1: Optional[constr(strict=True, max_length=500)] = Field(
        default=None, alias="AddressLine1", description="max length = 500"
    )
    address_line2: Optional[constr(strict=True, max_length=500)] = Field(
        default=None, alias="AddressLine2", description="max length = 500"
    )
    address_line3: Optional[constr(strict=True, max_length=500)] = Field(
        default=None, alias="AddressLine3", description="max length = 500"
    )
    address_line4: Optional[constr(strict=True, max_length=500)] = Field(
        default=None, alias="AddressLine4", description="max length = 500"
    )
    city: Optional[constr(strict=True, max_length=255)] = Field(
        default=None, alias="City", description="max length = 255"
    )
    region: Optional[constr(strict=True, max_length=255)] = Field(
        default=None, alias="Region", description="max length = 255"
    )
    postal_code: Optional[constr(strict=True, max_length=50)] = Field(
        default=None, alias="PostalCode", description="max length = 50"
    )
    country: Optional[constr(strict=True, max_length=50)] = Field(
        default=None, alias="Country", description="max length = 50, [A-Z], [a-z] only"
    )
    attention_to: Optional[constr(strict=True, max_length=255)] = Field(
        default=None, alias="AttentionTo", description="max length = 255"
    )
    __properties = [
        "AddressType",
        "AddressLine1",
        "AddressLine2",
        "AddressLine3",
        "AddressLine4",
        "City",
        "Region",
        "PostalCode",
        "Country",
        "AttentionTo",
    ]

    @validator("address_type")
    def address_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("POBOX", "STREET", "DELIVERY"):
            raise ValueError("must be one of enum values ('POBOX', 'STREET', 'DELIVERY')")
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
    def from_json(cls, json_str: str) -> AddressForOrganisation:
        """Create an instance of AddressForOrganisation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddressForOrganisation:
        """Create an instance of AddressForOrganisation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddressForOrganisation.parse_obj(obj)

        _obj = AddressForOrganisation.parse_obj(
            {
                "address_type": obj.get("AddressType"),
                "address_line1": obj.get("AddressLine1"),
                "address_line2": obj.get("AddressLine2"),
                "address_line3": obj.get("AddressLine3"),
                "address_line4": obj.get("AddressLine4"),
                "city": obj.get("City"),
                "region": obj.get("Region"),
                "postal_code": obj.get("PostalCode"),
                "country": obj.get("Country"),
                "attention_to": obj.get("AttentionTo"),
            }
        )
        return _obj
