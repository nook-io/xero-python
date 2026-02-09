from xero.models import BaseModel


class UsageRecord(BaseModel):
    openapi_types = {
        "quantity": "int",
        "subscription_id": "str",
        "subscription_item_id": "str",
        "test_mode": "bool",
        "recorded_at": "datetime",
        "usage_record_id": "str",
        "price_per_unit": "float",
        "product_id": "str",
    }
    attribute_map = {
        "quantity": "quantity",
        "subscription_id": "subscriptionId",
        "subscription_item_id": "subscriptionItemId",
        "test_mode": "testMode",
        "recorded_at": "recordedAt",
        "usage_record_id": "usageRecordId",
        "price_per_unit": "pricePerUnit",
        "product_id": "productId",
    }

    def __init__(
        self,
        quantity=None,
        subscription_id=None,
        subscription_item_id=None,
        test_mode=None,
        recorded_at=None,
        usage_record_id=None,
        price_per_unit=None,
        product_id=None,
    ):
        self._quantity = None
        self._subscription_id = None
        self._subscription_item_id = None
        self._test_mode = None
        self._recorded_at = None
        self._usage_record_id = None
        self._price_per_unit = None
        self._product_id = None
        self.discriminator = None
        self.quantity = quantity
        self.subscription_id = subscription_id
        self.subscription_item_id = subscription_item_id
        self.test_mode = test_mode
        self.recorded_at = recorded_at
        self.usage_record_id = usage_record_id
        self.price_per_unit = price_per_unit
        self.product_id = product_id

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")
        self._quantity = quantity

    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        if subscription_id is None:
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")
        self._subscription_id = subscription_id

    @property
    def subscription_item_id(self):
        return self._subscription_item_id

    @subscription_item_id.setter
    def subscription_item_id(self, subscription_item_id):
        if subscription_item_id is None:
            raise ValueError(
                "Invalid value for `subscription_item_id`, must not be `None`"
            )
        self._subscription_item_id = subscription_item_id

    @property
    def test_mode(self):
        return self._test_mode

    @test_mode.setter
    def test_mode(self, test_mode):
        if test_mode is None:
            raise ValueError("Invalid value for `test_mode`, must not be `None`")
        self._test_mode = test_mode

    @property
    def recorded_at(self):
        return self._recorded_at

    @recorded_at.setter
    def recorded_at(self, recorded_at):
        if recorded_at is None:
            raise ValueError("Invalid value for `recorded_at`, must not be `None`")
        self._recorded_at = recorded_at

    @property
    def usage_record_id(self):
        return self._usage_record_id

    @usage_record_id.setter
    def usage_record_id(self, usage_record_id):
        if usage_record_id is None:
            raise ValueError("Invalid value for `usage_record_id`, must not be `None`")
        self._usage_record_id = usage_record_id

    @property
    def price_per_unit(self):
        return self._price_per_unit

    @price_per_unit.setter
    def price_per_unit(self, price_per_unit):
        if price_per_unit is None:
            raise ValueError("Invalid value for `price_per_unit`, must not be `None`")
        self._price_per_unit = price_per_unit

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")
        self._product_id = product_id
