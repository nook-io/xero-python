from xero.models import BaseModel


class CISSetting(BaseModel):
    openapi_types = {"cis_enabled": "bool", "rate": "float"}
    attribute_map = {"cis_enabled": "CISEnabled", "rate": "Rate"}

    def __init__(self, cis_enabled=None, rate=None):
        self._cis_enabled = None
        self._rate = None
        self.discriminator = None
        if cis_enabled is not None:
            self.cis_enabled = cis_enabled
        if rate is not None:
            self.rate = rate

    @property
    def cis_enabled(self):
        return self._cis_enabled

    @cis_enabled.setter
    def cis_enabled(self, cis_enabled):
        self._cis_enabled = cis_enabled

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        self._rate = rate
