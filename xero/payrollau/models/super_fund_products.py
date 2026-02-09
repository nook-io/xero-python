from xero.models import BaseModel


class SuperFundProducts(BaseModel):
    openapi_types = {"super_fund_products": "list[SuperFundProduct]"}
    attribute_map = {"super_fund_products": "SuperFundProducts"}

    def __init__(self, super_fund_products=None):
        self._super_fund_products = None
        self.discriminator = None
        if super_fund_products is not None:
            self.super_fund_products = super_fund_products

    @property
    def super_fund_products(self):
        return self._super_fund_products

    @super_fund_products.setter
    def super_fund_products(self, super_fund_products):
        self._super_fund_products = super_fund_products
