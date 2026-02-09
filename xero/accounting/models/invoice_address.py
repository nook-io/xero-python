from xero.models import BaseModel


class InvoiceAddress(BaseModel):
    openapi_types = {
        "invoice_address_type": "str",
        "address_line1": "str",
        "address_line2": "str",
        "address_line3": "str",
        "address_line4": "str",
        "city": "str",
        "region": "str",
        "postal_code": "str",
        "country": "str",
    }
    attribute_map = {
        "invoice_address_type": "InvoiceAddressType",
        "address_line1": "AddressLine1",
        "address_line2": "AddressLine2",
        "address_line3": "AddressLine3",
        "address_line4": "AddressLine4",
        "city": "City",
        "region": "Region",
        "postal_code": "PostalCode",
        "country": "Country",
    }

    def __init__(
        self,
        invoice_address_type=None,
        address_line1=None,
        address_line2=None,
        address_line3=None,
        address_line4=None,
        city=None,
        region=None,
        postal_code=None,
        country=None,
    ):
        self._invoice_address_type = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_line3 = None
        self._address_line4 = None
        self._city = None
        self._region = None
        self._postal_code = None
        self._country = None
        self.discriminator = None
        if invoice_address_type is not None:
            self.invoice_address_type = invoice_address_type
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

    @property
    def invoice_address_type(self):
        return self._invoice_address_type

    @invoice_address_type.setter
    def invoice_address_type(self, invoice_address_type):
        allowed_values = ["FROM", "TO", "None"]
        if invoice_address_type:
            if invoice_address_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `invoice_address_type` ({0}), must be one of {1}".format(
                        invoice_address_type, allowed_values
                    )
                )
        self._invoice_address_type = invoice_address_type

    @property
    def address_line1(self):
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        self._address_line1 = address_line1

    @property
    def address_line2(self):
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        self._address_line2 = address_line2

    @property
    def address_line3(self):
        return self._address_line3

    @address_line3.setter
    def address_line3(self, address_line3):
        self._address_line3 = address_line3

    @property
    def address_line4(self):
        return self._address_line4

    @address_line4.setter
    def address_line4(self, address_line4):
        self._address_line4 = address_line4

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
