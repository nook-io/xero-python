from xero.models import BaseModel


class InvoiceResponse(BaseModel):
    openapi_types = {
        "invoice_id": "str",
        "contact": "ContactResponse",
        "total": "float",
        "line_items": "list[LineItemResponse]",
    }
    attribute_map = {
        "invoice_id": "invoiceId",
        "contact": "contact",
        "total": "total",
        "line_items": "lineItems",
    }

    def __init__(self, invoice_id=None, contact=None, total=None, line_items=None):
        self._invoice_id = None
        self._contact = None
        self._total = None
        self._line_items = None
        self.discriminator = None
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if contact is not None:
            self.contact = contact
        if total is not None:
            self.total = total
        if line_items is not None:
            self.line_items = line_items

    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        self._invoice_id = invoice_id

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
