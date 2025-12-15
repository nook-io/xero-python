from xero.models import BaseModel


class ImportSummaryOrganisation(BaseModel):
    openapi_types = {"present": "bool"}
    attribute_map = {"present": "Present"}

    def __init__(self, present=None):
        self._present = None
        self.discriminator = None
        if present is not None:
            self.present = present

    @property
    def present(self):
        return self._present

    @present.setter
    def present(self, present):
        self._present = present
