from xero.models import BaseModel


class OnlineInvoice(BaseModel):
    openapi_types = {"online_invoice_url": "str"}
    attribute_map = {"online_invoice_url": "OnlineInvoiceUrl"}

    def __init__(self, online_invoice_url=None):
        self._online_invoice_url = None
        self.discriminator = None
        if online_invoice_url is not None:
            self.online_invoice_url = online_invoice_url

    @property
    def online_invoice_url(self):
        return self._online_invoice_url

    @online_invoice_url.setter
    def online_invoice_url(self, online_invoice_url):
        self._online_invoice_url = online_invoice_url
