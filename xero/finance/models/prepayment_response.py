from xero.models import BaseModel


class PrepaymentResponse(BaseModel):
    openapi_types = {
        "prepayment_id": "str",
        "contact": "ContactResponse",
        "total": "float",
        "line_items": "list[LineItemResponse]",
    }
    attribute_map = {
        "prepayment_id": "prepaymentId",
        "contact": "contact",
        "total": "total",
        "line_items": "lineItems",
    }

    def __init__(self, prepayment_id=None, contact=None, total=None, line_items=None):
        self._prepayment_id = None
        self._contact = None
        self._total = None
        self._line_items = None
        self.discriminator = None
        if prepayment_id is not None:
            self.prepayment_id = prepayment_id
        if contact is not None:
            self.contact = contact
        if total is not None:
            self.total = total
        if line_items is not None:
            self.line_items = line_items

    @property
    def prepayment_id(self):
        return self._prepayment_id

    @prepayment_id.setter
    def prepayment_id(self, prepayment_id):
        self._prepayment_id = prepayment_id

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def line_items(self):
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        self._line_items = line_items
