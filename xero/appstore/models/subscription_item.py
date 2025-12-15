from xero.models import BaseModel


class SubscriptionItem(BaseModel):
    openapi_types = {
        "end_date": "datetime",
        "id": "str",
        "price": "Price",
        "product": "Product",
        "quantity": "int",
        "start_date": "datetime",
        "status": "str",
        "test_mode": "bool",
    }
    attribute_map = {
        "end_date": "endDate",
        "id": "id",
        "price": "price",
        "product": "product",
        "quantity": "quantity",
        "start_date": "startDate",
        "status": "status",
        "test_mode": "testMode",
    }

    def __init__(
        self,
        end_date=None,
        id=None,
        price=None,
        product=None,
        quantity=None,
        start_date=None,
        status=None,
        test_mode=None,
    ):
        self._end_date = None
        self._id = None
        self._price = None
        self._product = None
        self._quantity = None
        self._start_date = None
        self._status = None
        self._test_mode = None
        self.discriminator = None
        if end_date is not None:
            self.end_date = end_date
        self.id = id
        self.price = price
        self.product = product
        if quantity is not None:
            self.quantity = quantity
        self.start_date = start_date
        self.status = status
        if test_mode is not None:
            self.test_mode = test_mode

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        self._id = id

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")
        self._price = price

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        if product is None:
            raise ValueError("Invalid value for `product`, must not be `None`")
        self._product = product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")
        self._start_date = start_date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        allowed_values = [
            "ACTIVE",
            "CANCELED",
            "PENDING_ACTIVATION",
            "None",
        ]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def test_mode(self):
        return self._test_mode

    @test_mode.setter
    def test_mode(self, test_mode):
        self._test_mode = test_mode
