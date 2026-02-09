from xero.models import BaseModel


class SuperFundProduct(BaseModel):
    openapi_types = {"abn": "str", "usi": "str", "spin": "str", "product_name": "str"}
    attribute_map = {
        "abn": "ABN",
        "usi": "USI",
        "spin": "SPIN",
        "product_name": "ProductName",
    }

    def __init__(self, abn=None, usi=None, spin=None, product_name=None):
        self._abn = None
        self._usi = None
        self._spin = None
        self._product_name = None
        self.discriminator = None
        if abn is not None:
            self.abn = abn
        if usi is not None:
            self.usi = usi
        if spin is not None:
            self.spin = spin
        if product_name is not None:
            self.product_name = product_name

    @property
    def abn(self):
        return self._abn

    @abn.setter
    def abn(self, abn):
        self._abn = abn

    @property
    def usi(self):
        return self._usi

    @usi.setter
    def usi(self, usi):
        self._usi = usi

    @property
    def spin(self):
        return self._spin

    @spin.setter
    def spin(self, spin):
        self._spin = spin

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        self._product_name = product_name
