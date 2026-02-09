from xero.models import BaseModel


class AddressForOrganisation(BaseModel):
    openapi_types = {
        "address_type": "str",
        "address_line1": "str",
        "address_line2": "str",
        "address_line3": "str",
        "address_line4": "str",
        "city": "str",
        "region": "str",
        "postal_code": "str",
        "country": "str",
        "attention_to": "str",
    }
    attribute_map = {
        "address_type": "AddressType",
        "address_line1": "AddressLine1",
        "address_line2": "AddressLine2",
        "address_line3": "AddressLine3",
        "address_line4": "AddressLine4",
        "city": "City",
        "region": "Region",
        "postal_code": "PostalCode",
        "country": "Country",
        "attention_to": "AttentionTo",
    }

    def __init__(
        self,
        address_type=None,
        address_line1=None,
        address_line2=None,
        address_line3=None,
        address_line4=None,
        city=None,
        region=None,
        postal_code=None,
        country=None,
        attention_to=None,
    ):
        self._address_type = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_line3 = None
        self._address_line4 = None
        self._city = None
        self._region = None
        self._postal_code = None
        self._country = None
        self._attention_to = None
        self.discriminator = None
        if address_type is not None:
            self.address_type = address_type
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_line3 is not None:
            self.address_line3 = address_line3
        if address_line4 is not None:
            self.address_line4 = address_line4
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if attention_to is not None:
            self.attention_to = attention_to

    @property
    def address_type(self):
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        allowed_values = ["POBOX", "STREET", "DELIVERY", "None"]
        if address_type:
            if address_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `address_type` ({0}), must be one of {1}".format(
                        address_type, allowed_values
                    )
                )
        self._address_type = address_type

    @property
    def address_line1(self):
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        if address_line1 is not None and len(address_line1) > 500:
            raise ValueError(
                "Invalid value for `address_line1`, "
                "length must be less than or equal to `500`"
            )
        self._address_line1 = address_line1

    @property
    def address_line2(self):
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        if address_line2 is not None and len(address_line2) > 500:
            raise ValueError(
                "Invalid value for `address_line2`, "
                "length must be less than or equal to `500`"
            )
        self._address_line2 = address_line2

    @property
    def address_line3(self):
        return self._address_line3

    @address_line3.setter
    def address_line3(self, address_line3):
        if address_line3 is not None and len(address_line3) > 500:
            raise ValueError(
                "Invalid value for `address_line3`, "
                "length must be less than or equal to `500`"
            )
        self._address_line3 = address_line3

    @property
    def address_line4(self):
        return self._address_line4

    @address_line4.setter
    def address_line4(self, address_line4):
        if address_line4 is not None and len(address_line4) > 500:
            raise ValueError(
                "Invalid value for `address_line4`, "
                "length must be less than or equal to `500`"
            )
        self._address_line4 = address_line4

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if city is not None and len(city) > 255:
            raise ValueError(
                "Invalid value for `city`, length must be less than or equal to `255`"
            )
        self._city = city

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region is not None and len(region) > 255:
            raise ValueError(
                "Invalid value for `region`, length must be less than or equal to `255`"
            )
        self._region = region

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        if postal_code is not None and len(postal_code) > 50:
            raise ValueError(
                "Invalid value for `postal_code`, "
                "length must be less than or equal to `50`"
            )
        self._postal_code = postal_code

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        if country is not None and len(country) > 50:
            raise ValueError(
                "Invalid value for `country`, length must be less than or equal to `50`"
            )
        self._country = country

    @property
    def attention_to(self):
        return self._attention_to

    @attention_to.setter
    def attention_to(self, attention_to):
        if attention_to is not None and len(attention_to) > 255:
            raise ValueError(
                "Invalid value for `attention_to`, "
                "length must be less than or equal to `255`"
            )
        self._attention_to = attention_to
