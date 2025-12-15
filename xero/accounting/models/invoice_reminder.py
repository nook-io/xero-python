from xero.models import BaseModel


class InvoiceReminder(BaseModel):
    openapi_types = {"enabled": "bool"}
    attribute_map = {"enabled": "Enabled"}

    def __init__(self, enabled=None):
        self._enabled = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        self._enabled = enabled
