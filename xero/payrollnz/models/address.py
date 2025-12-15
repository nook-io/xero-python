from xero.models import BaseModel


class Address(BaseModel):
    openapi_types = {
        "address_line1": "str",
        "address_line2": "str",
        "city": "str",
        "suburb": "str",
        "post_code": "str",
        "country_name": "str",
    }
    attribute_map = {
        "address_line1": "addressLine1",
        "address_line2": "addressLine2",
        "city": "city",
        "suburb": "suburb",
        "post_code": "postCode",
        "country_name": "countryName",
    }

    def __init__(
        self,
        address_line1=None,
        address_line2=None,
        city=None,
        suburb=None,
        post_code=None,
        country_name=None,
    ):
        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._suburb = None
        self._post_code = None
        self._country_name = None
        self.discriminator = None
        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        self.city = city
        if suburb is not None:
            self.suburb = suburb
        self.post_code = post_code
        if country_name is not None:
            self.country_name = country_name

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
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")
        self._city = city

    @property
    def suburb(self):
        return self._suburb

    @suburb.setter
    def suburb(self, suburb):
        self._suburb = suburb

    @property
    def post_code(self):
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        if post_code is None:
            raise ValueError("Invalid value for `post_code`, must not be `None`")
        self._post_code = post_code

    @property
    def country_name(self):
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        self._country_name = country_name
