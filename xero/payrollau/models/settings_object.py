from xero.models import BaseModel


class SettingsObject(BaseModel):
    openapi_types = {"settings": "Settings"}
    attribute_map = {"settings": "Settings"}

    def __init__(self, settings=None):
        self._settings = None
        self.discriminator = None
        if settings is not None:
            self.settings = settings

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, settings):
        self._settings = settings
