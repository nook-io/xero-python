from xero.models import BaseModel


class TrackingOptions(BaseModel):
    openapi_types = {"options": "list[TrackingOption]"}
    attribute_map = {"options": "Options"}

    def __init__(self, options=None):
        self._options = None
        self.discriminator = None
        if options is not None:
            self.options = options

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, options):
        self._options = options
