from xero.models import BaseModel


class CISOrgSettings(BaseModel):
    openapi_types = {"cis_settings": "list[CISOrgSetting]"}
    attribute_map = {"cis_settings": "CISSettings"}

    def __init__(self, cis_settings=None):
        self._cis_settings = None
        self.discriminator = None
        if cis_settings is not None:
            self.cis_settings = cis_settings

    @property
    def cis_settings(self):
        return self._cis_settings

    @cis_settings.setter
    def cis_settings(self, cis_settings):
        self._cis_settings = cis_settings
