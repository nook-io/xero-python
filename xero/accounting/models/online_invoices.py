from xero.models import BaseModel


class OnlineInvoices(BaseModel):
    openapi_types = {"online_invoices": "list[OnlineInvoice]"}
    attribute_map = {"online_invoices": "OnlineInvoices"}

    def __init__(self, online_invoices=None):
        self._online_invoices = None
        self.discriminator = None
        if online_invoices is not None:
            self.online_invoices = online_invoices

    @property
    def online_invoices(self):
        return self._online_invoices

    @online_invoices.setter
    def online_invoices(self, online_invoices):
        self._online_invoices = online_invoices
