from xero.models import BaseModel


class CourtOrderLine(BaseModel):
    openapi_types = {"court_order_type_id": "str", "amount": "float"}
    attribute_map = {"court_order_type_id": "courtOrderTypeID", "amount": "amount"}

    def __init__(self, court_order_type_id=None, amount=None):
        self._court_order_type_id = None
        self._amount = None
        self.discriminator = None
        if court_order_type_id is not None:
            self.court_order_type_id = court_order_type_id
        if amount is not None:
            self.amount = amount

    @property
    def court_order_type_id(self):
        return self._court_order_type_id

    @court_order_type_id.setter
    def court_order_type_id(self, court_order_type_id):
        self._court_order_type_id = court_order_type_id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount
