from xero.models import BaseModel


class HomeAddress(BaseModel):
    openapi_types = {
        "address_line1": "str",
        "address_line2": "str",
        "city": "str",
        "region": "State",
        "postal_code": "str",
        "country": "str",
    }
    attribute_map = {
        "address_line1": "AddressLine1",
        "address_line2": "AddressLine2",
        "city": "City",
        "region": "Region",
        "postal_code": "PostalCode",
        "country": "Country",
    }

    def __init__(
        self,
        address_line1=None,
        address_line2=None,
        city=None,
        region=None,
        postal_code=None,
        country=None,
    ):
        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._region = None
        self._postal_code = None
        self._country = None
        self.discriminator = None
        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country

    @property
    def address_line1(self):
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        if address_line1 is None:
            raise ValueError("Invalid value for `address_line1`, must not be `None`")
        self._address_line1 = address_line1

    @property
    def address_line2(self):
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        self._address_line2 = address_line2

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        self._region = region

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = postal_code

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country
