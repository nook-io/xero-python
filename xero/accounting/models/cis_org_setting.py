from xero.models import BaseModel


class CISOrgSetting(BaseModel):
    openapi_types = {
        "cis_contractor_enabled": "bool",
        "cis_sub_contractor_enabled": "bool",
        "rate": "float",
    }
    attribute_map = {
        "cis_contractor_enabled": "CISContractorEnabled",
        "cis_sub_contractor_enabled": "CISSubContractorEnabled",
        "rate": "Rate",
    }

    def __init__(
        self, cis_contractor_enabled=None, cis_sub_contractor_enabled=None, rate=None
    ):
        self._cis_contractor_enabled = None
        self._cis_sub_contractor_enabled = None
        self._rate = None
        self.discriminator = None
        if cis_contractor_enabled is not None:
            self.cis_contractor_enabled = cis_contractor_enabled
        if cis_sub_contractor_enabled is not None:
            self.cis_sub_contractor_enabled = cis_sub_contractor_enabled
        if rate is not None:
            self.rate = rate

    @property
    def cis_contractor_enabled(self):
        return self._cis_contractor_enabled

    @cis_contractor_enabled.setter
    def cis_contractor_enabled(self, cis_contractor_enabled):
        self._cis_contractor_enabled = cis_contractor_enabled

    @property
    def cis_sub_contractor_enabled(self):
        return self._cis_sub_contractor_enabled

    @cis_sub_contractor_enabled.setter
    def cis_sub_contractor_enabled(self, cis_sub_contractor_enabled):
        self._cis_sub_contractor_enabled = cis_sub_contractor_enabled

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        self._rate = rate
