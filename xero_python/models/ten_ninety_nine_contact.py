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
from typing import Optional, Union

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator


class TenNinetyNineContact(BaseModel):
    """
    TenNinetyNineContact
    """

    box1: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Box1", description="Box 1 on 1099 Form")
    box2: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Box2", description="Box 2 on 1099 Form")
    box3: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Box3", description="Box 3 on 1099 Form")
    box4: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Box4", description="Box 4 on 1099 Form")
    box5: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Box5", description="Box 5 on 1099 Form")
    box6: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Box6", description="Box 6 on 1099 Form")
    box7: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Box7", description="Box 7 on 1099 Form")
    box8: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Box8", description="Box 8 on 1099 Form")
    box9: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Box9", description="Box 9 on 1099 Form")
    box10: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="Box10", description="Box 10 on 1099 Form"
    )
    box11: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="Box11", description="Box 11 on 1099 Form"
    )
    box13: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="Box13", description="Box 13 on 1099 Form"
    )
    box14: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="Box14", description="Box 14 on 1099 Form"
    )
    name: Optional[StrictStr] = Field(default=None, alias="Name", description="Contact name on 1099 Form")
    federal_tax_id_type: Optional[StrictStr] = Field(
        default=None, alias="FederalTaxIDType", description="Contact Fed Tax ID type"
    )
    city: Optional[StrictStr] = Field(default=None, alias="City", description="Contact city on 1099 Form")
    zip: Optional[StrictStr] = Field(default=None, alias="Zip", description="Contact zip on 1099 Form")
    state: Optional[StrictStr] = Field(default=None, alias="State", description="Contact State on 1099 Form")
    email: Optional[StrictStr] = Field(default=None, alias="Email", description="Contact email on 1099 Form")
    street_address: Optional[StrictStr] = Field(
        default=None, alias="StreetAddress", description="Contact address on 1099 Form"
    )
    tax_id: Optional[StrictStr] = Field(default=None, alias="TaxID", description="Contact tax id on 1099 Form")
    contact_id: Optional[StrictStr] = Field(default=None, alias="ContactId", description="Contact contact id")
    legal_name: Optional[StrictStr] = Field(default=None, alias="LegalName", description="Contact legal name")
    business_name: Optional[StrictStr] = Field(default=None, alias="BusinessName", description="Contact business name")
    federal_tax_classification: Optional[StrictStr] = Field(
        default=None, alias="FederalTaxClassification", description="Contact federal tax classification"
    )
    __properties = [
        "Box1",
        "Box2",
        "Box3",
        "Box4",
        "Box5",
        "Box6",
        "Box7",
        "Box8",
        "Box9",
        "Box10",
        "Box11",
        "Box13",
        "Box14",
        "Name",
        "FederalTaxIDType",
        "City",
        "Zip",
        "State",
        "Email",
        "StreetAddress",
        "TaxID",
        "ContactId",
        "LegalName",
        "BusinessName",
        "FederalTaxClassification",
    ]

    @validator("federal_tax_classification")
    def federal_tax_classification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("SOLE_PROPRIETOR", "PARTNERSHIP", "TRUST_OR_ESTATE", "NONPROFIT", "C_CORP", "S_CORP", "OTHER"):
            raise ValueError(
                "must be one of enum values ('SOLE_PROPRIETOR', 'PARTNERSHIP', 'TRUST_OR_ESTATE', 'NONPROFIT', 'C_CORP', 'S_CORP', 'OTHER')"
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
    def from_json(cls, json_str: str) -> TenNinetyNineContact:
        """Create an instance of TenNinetyNineContact from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TenNinetyNineContact:
        """Create an instance of TenNinetyNineContact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TenNinetyNineContact.parse_obj(obj)

        _obj = TenNinetyNineContact.parse_obj(
            {
                "box1": obj.get("Box1"),
                "box2": obj.get("Box2"),
                "box3": obj.get("Box3"),
                "box4": obj.get("Box4"),
                "box5": obj.get("Box5"),
                "box6": obj.get("Box6"),
                "box7": obj.get("Box7"),
                "box8": obj.get("Box8"),
                "box9": obj.get("Box9"),
                "box10": obj.get("Box10"),
                "box11": obj.get("Box11"),
                "box13": obj.get("Box13"),
                "box14": obj.get("Box14"),
                "name": obj.get("Name"),
                "federal_tax_id_type": obj.get("FederalTaxIDType"),
                "city": obj.get("City"),
                "zip": obj.get("Zip"),
                "state": obj.get("State"),
                "email": obj.get("Email"),
                "street_address": obj.get("StreetAddress"),
                "tax_id": obj.get("TaxID"),
                "contact_id": obj.get("ContactId"),
                "legal_name": obj.get("LegalName"),
                "business_name": obj.get("BusinessName"),
                "federal_tax_classification": obj.get("FederalTaxClassification"),
            }
        )
        return _obj
