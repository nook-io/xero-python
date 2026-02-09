from xero.models import BaseModel


class Allocations(BaseModel):
    openapi_types = {"allocations": "list[Allocation]"}
    attribute_map = {"allocations": "Allocations"}

    def __init__(self, allocations=None):
        self._allocations = None
        self.discriminator = None
        if allocations is not None:
            self.allocations = allocations

    @property
    def allocations(self):
        return self._allocations

    @allocations.setter
    def allocations(self, allocations):
        self._allocations = allocations
