from xero.models import BaseModel


class TaxRates(BaseModel):
    openapi_types = {"tax_rates": "list[TaxRate]"}
    attribute_map = {"tax_rates": "TaxRates"}

    def __init__(self, tax_rates=None):
        self._tax_rates = None
        self.discriminator = None
        if tax_rates is not None:
            self.tax_rates = tax_rates

    @property
    def tax_rates(self):
        return self._tax_rates

    @tax_rates.setter
    def tax_rates(self, tax_rates):
        self._tax_rates = tax_rates
