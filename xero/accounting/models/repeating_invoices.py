from xero.models import BaseModel


class RepeatingInvoices(BaseModel):
    openapi_types = {"repeating_invoices": "list[RepeatingInvoice]"}
    attribute_map = {"repeating_invoices": "RepeatingInvoices"}

    def __init__(self, repeating_invoices=None):
        self._repeating_invoices = None
        self.discriminator = None
        if repeating_invoices is not None:
            self.repeating_invoices = repeating_invoices

    @property
    def repeating_invoices(self):
        return self._repeating_invoices

    @repeating_invoices.setter
    def repeating_invoices(self, repeating_invoices):
        self._repeating_invoices = repeating_invoices
