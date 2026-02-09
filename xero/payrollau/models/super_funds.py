from xero.models import BaseModel


class SuperFunds(BaseModel):
    openapi_types = {"super_funds": "list[SuperFund]"}
    attribute_map = {"super_funds": "SuperFunds"}

    def __init__(self, super_funds=None):
        self._super_funds = None
        self.discriminator = None
        if super_funds is not None:
            self.super_funds = super_funds

    @property
    def super_funds(self):
        return self._super_funds

    @super_funds.setter
    def super_funds(self, super_funds):
        self._super_funds = super_funds
