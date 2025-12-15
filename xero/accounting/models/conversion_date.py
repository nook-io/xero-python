from xero.models import BaseModel


class ConversionDate(BaseModel):
    openapi_types = {"month": "int", "year": "int"}
    attribute_map = {"month": "Month", "year": "Year"}

    def __init__(self, month=None, year=None):
        self._month = None
        self._year = None
        self.discriminator = None
        if month is not None:
            self.month = month
        if year is not None:
            self.year = year

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        self._month = month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year
