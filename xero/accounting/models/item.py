from xero.models import BaseModel


class Item(BaseModel):
    openapi_types = {
        "code": "str",
        "inventory_asset_account_code": "str",
        "name": "str",
        "is_sold": "bool",
        "is_purchased": "bool",
        "description": "str",
        "purchase_description": "str",
        "purchase_details": "Purchase",
        "sales_details": "Purchase",
        "is_tracked_as_inventory": "bool",
        "total_cost_pool": "float",
        "quantity_on_hand": "float",
        "updated_date_utc": "datetime[ms-format]",
        "item_id": "str",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "code": "Code",
        "inventory_asset_account_code": "InventoryAssetAccountCode",
        "name": "Name",
        "is_sold": "IsSold",
        "is_purchased": "IsPurchased",
        "description": "Description",
        "purchase_description": "PurchaseDescription",
        "purchase_details": "PurchaseDetails",
        "sales_details": "SalesDetails",
        "is_tracked_as_inventory": "IsTrackedAsInventory",
        "total_cost_pool": "TotalCostPool",
        "quantity_on_hand": "QuantityOnHand",
        "updated_date_utc": "UpdatedDateUTC",
        "item_id": "ItemID",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        code=None,
        inventory_asset_account_code=None,
        name=None,
        is_sold=None,
        is_purchased=None,
        description=None,
        purchase_description=None,
        purchase_details=None,
        sales_details=None,
        is_tracked_as_inventory=None,
        total_cost_pool=None,
        quantity_on_hand=None,
        updated_date_utc=None,
        item_id=None,
        status_attribute_string=None,
        validation_errors=None,
    ):
        self._code = None
        self._inventory_asset_account_code = None
        self._name = None
        self._is_sold = None
        self._is_purchased = None
        self._description = None
        self._purchase_description = None
        self._purchase_details = None
        self._sales_details = None
        self._is_tracked_as_inventory = None
        self._total_cost_pool = None
        self._quantity_on_hand = None
        self._updated_date_utc = None
        self._item_id = None
        self._status_attribute_string = None
        self._validation_errors = None
        self.discriminator = None
        self.code = code
        if inventory_asset_account_code is not None:
            self.inventory_asset_account_code = inventory_asset_account_code
        if name is not None:
            self.name = name
        if is_sold is not None:
            self.is_sold = is_sold
        if is_purchased is not None:
            self.is_purchased = is_purchased
        if description is not None:
            self.description = description
        if purchase_description is not None:
            self.purchase_description = purchase_description
        if purchase_details is not None:
            self.purchase_details = purchase_details
        if sales_details is not None:
            self.sales_details = sales_details
        if is_tracked_as_inventory is not None:
            self.is_tracked_as_inventory = is_tracked_as_inventory
        if total_cost_pool is not None:
            self.total_cost_pool = total_cost_pool
        if quantity_on_hand is not None:
            self.quantity_on_hand = quantity_on_hand
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if item_id is not None:
            self.item_id = item_id
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")
        if code is not None and len(code) > 30:
            raise ValueError(
                "Invalid value for `code`, length must be less than or equal to `30`"
            )
        self._code = code

    @property
    def inventory_asset_account_code(self):
        return self._inventory_asset_account_code

    @inventory_asset_account_code.setter
    def inventory_asset_account_code(self, inventory_asset_account_code):
        self._inventory_asset_account_code = inventory_asset_account_code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 50:
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `50`"
            )
        self._name = name

    @property
    def is_sold(self):
        return self._is_sold

    @is_sold.setter
    def is_sold(self, is_sold):
        self._is_sold = is_sold

    @property
    def is_purchased(self):
        return self._is_purchased

    @is_purchased.setter
    def is_purchased(self, is_purchased):
        self._is_purchased = is_purchased

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if description is not None and len(description) > 4000:
            raise ValueError(
                "Invalid value for `description`, "
                "length must be less than or equal to `4000`"
            )
        self._description = description

    @property
    def purchase_description(self):
        return self._purchase_description

    @purchase_description.setter
    def purchase_description(self, purchase_description):
        if purchase_description is not None and len(purchase_description) > 4000:
            raise ValueError(
                "Invalid value for `purchase_description`, "
                "length must be less than or equal to `4000`"
            )
        self._purchase_description = purchase_description

    @property
    def purchase_details(self):
        return self._purchase_details

    @purchase_details.setter
    def purchase_details(self, purchase_details):
        self._purchase_details = purchase_details

    @property
    def sales_details(self):
        return self._sales_details

    @sales_details.setter
    def sales_details(self, sales_details):
        self._sales_details = sales_details

    @property
    def is_tracked_as_inventory(self):
        return self._is_tracked_as_inventory

    @is_tracked_as_inventory.setter
    def is_tracked_as_inventory(self, is_tracked_as_inventory):
        self._is_tracked_as_inventory = is_tracked_as_inventory

    @property
    def total_cost_pool(self):
        return self._total_cost_pool

    @total_cost_pool.setter
    def total_cost_pool(self, total_cost_pool):
        self._total_cost_pool = total_cost_pool

    @property
    def quantity_on_hand(self):
        return self._quantity_on_hand

    @quantity_on_hand.setter
    def quantity_on_hand(self, quantity_on_hand):
        self._quantity_on_hand = quantity_on_hand

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        self._item_id = item_id

    @property
    def status_attribute_string(self):
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
