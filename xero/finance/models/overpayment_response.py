from xero.models import BaseModel


class OverpaymentResponse(BaseModel):
    openapi_types = {
        "overpayment_id": "str",
        "contact": "ContactResponse",
        "total": "float",
        "line_items": "list[LineItemResponse]",
    }
    attribute_map = {
        "overpayment_id": "overpaymentId",
        "contact": "contact",
        "total": "total",
        "line_items": "lineItems",
    }

    def __init__(self, overpayment_id=None, contact=None, total=None, line_items=None):
        self._overpayment_id = None
        self._contact = None
        self._total = None
        self._line_items = None
        self.discriminator = None
        if overpayment_id is not None:
            self.overpayment_id = overpayment_id
        if contact is not None:
            self.contact = contact
        if total is not None:
            self.total = total
        if line_items is not None:
            self.line_items = line_items

    @property
    def overpayment_id(self):
        return self._overpayment_id

    @overpayment_id.setter
    def overpayment_id(self, overpayment_id):
        self._overpayment_id = overpayment_id

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
