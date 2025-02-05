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

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, constr

from xero_python.models.purchase import Purchase
from xero_python.models.validation_error import ValidationError


class Item(BaseModel):
    """
    Item
    """

    code: constr(strict=True, max_length=30) = Field(
        default=..., alias="Code", description="User defined item code (max length = 30)"
    )
    inventory_asset_account_code: Optional[StrictStr] = Field(
        default=None,
        alias="InventoryAssetAccountCode",
        description="The inventory asset account for the item. The account must be of type INVENTORY. The  COGSAccountCode in PurchaseDetails is also required to create a tracked item",
    )
    name: Optional[constr(strict=True, max_length=50)] = Field(
        default=None, alias="Name", description="The name of the item (max length = 50)"
    )
    is_sold: Optional[StrictBool] = Field(
        default=None,
        alias="IsSold",
        description="Boolean value, defaults to true. When IsSold is true the item will be available on sales transactions in the Xero UI. If IsSold is updated to false then Description and SalesDetails values will be nulled.",
    )
    is_purchased: Optional[StrictBool] = Field(
        default=None,
        alias="IsPurchased",
        description="Boolean value, defaults to true. When IsPurchased is true the item is available for purchase transactions in the Xero UI. If IsPurchased is updated to false then PurchaseDescription and PurchaseDetails values will be nulled.",
    )
    description: Optional[constr(strict=True, max_length=4000)] = Field(
        default=None, alias="Description", description="The sales description of the item (max length = 4000)"
    )
    purchase_description: Optional[constr(strict=True, max_length=4000)] = Field(
        default=None,
        alias="PurchaseDescription",
        description="The purchase description of the item (max length = 4000)",
    )
    purchase_details: Optional[Purchase] = Field(default=None, alias="PurchaseDetails")
    sales_details: Optional[Purchase] = Field(default=None, alias="SalesDetails")
    is_tracked_as_inventory: Optional[StrictBool] = Field(
        default=None,
        alias="IsTrackedAsInventory",
        description="True for items that are tracked as inventory. An item will be tracked as inventory if the InventoryAssetAccountCode and COGSAccountCode are set.",
    )
    total_cost_pool: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        alias="TotalCostPool",
        description="The value of the item on hand. Calculated using average cost accounting.",
    )
    quantity_on_hand: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="QuantityOnHand", description="The quantity of the item on hand"
    )
    updated_date_utc: Optional[StrictStr] = Field(
        default=None, alias="UpdatedDateUTC", description="Last modified date in UTC format"
    )
    item_id: Optional[StrictStr] = Field(default=None, alias="ItemID", description="The Xero identifier for an Item")
    status_attribute_string: Optional[StrictStr] = Field(
        default=None, alias="StatusAttributeString", description="Status of object"
    )
    validation_errors: Optional[conlist(ValidationError)] = Field(
        default=None, alias="ValidationErrors", description="Displays array of validation error messages from the API"
    )
    __properties = [
        "Code",
        "InventoryAssetAccountCode",
        "Name",
        "IsSold",
        "IsPurchased",
        "Description",
        "PurchaseDescription",
        "PurchaseDetails",
        "SalesDetails",
        "IsTrackedAsInventory",
        "TotalCostPool",
        "QuantityOnHand",
        "UpdatedDateUTC",
        "ItemID",
        "StatusAttributeString",
        "ValidationErrors",
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
    def from_json(cls, json_str: str) -> Item:
        """Create an instance of Item from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={"updated_date_utc"}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of purchase_details
        if self.purchase_details:
            _dict["PurchaseDetails"] = self.purchase_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sales_details
        if self.sales_details:
            _dict["SalesDetails"] = self.sales_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in validation_errors (list)
        _items = []
        if self.validation_errors:
            for _item in self.validation_errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict["ValidationErrors"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Item:
        """Create an instance of Item from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Item.parse_obj(obj)

        _obj = Item.parse_obj(
            {
                "code": obj.get("Code"),
                "inventory_asset_account_code": obj.get("InventoryAssetAccountCode"),
                "name": obj.get("Name"),
                "is_sold": obj.get("IsSold"),
                "is_purchased": obj.get("IsPurchased"),
                "description": obj.get("Description"),
                "purchase_description": obj.get("PurchaseDescription"),
                "purchase_details": Purchase.from_dict(obj.get("PurchaseDetails"))
                if obj.get("PurchaseDetails") is not None
                else None,
                "sales_details": Purchase.from_dict(obj.get("SalesDetails"))
                if obj.get("SalesDetails") is not None
                else None,
                "is_tracked_as_inventory": obj.get("IsTrackedAsInventory"),
                "total_cost_pool": obj.get("TotalCostPool"),
                "quantity_on_hand": obj.get("QuantityOnHand"),
                "updated_date_utc": obj.get("UpdatedDateUTC"),
                "item_id": obj.get("ItemID"),
                "status_attribute_string": obj.get("StatusAttributeString"),
                "validation_errors": [ValidationError.from_dict(_item) for _item in obj.get("ValidationErrors")]
                if obj.get("ValidationErrors") is not None
                else None,
            }
        )
        return _obj
