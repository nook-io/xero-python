from xero.models import BaseModel


class Phone(BaseModel):
    openapi_types = {
        "phone_type": "str",
        "phone_number": "str",
        "phone_area_code": "str",
        "phone_country_code": "str",
    }
    attribute_map = {
        "phone_type": "PhoneType",
        "phone_number": "PhoneNumber",
        "phone_area_code": "PhoneAreaCode",
        "phone_country_code": "PhoneCountryCode",
    }

    def __init__(
        self,
        phone_type=None,
        phone_number=None,
        phone_area_code=None,
        phone_country_code=None,
    ):
        self._phone_type = None
        self._phone_number = None
        self._phone_area_code = None
        self._phone_country_code = None
        self.discriminator = None
        if phone_type is not None:
            self.phone_type = phone_type
        if phone_number is not None:
            self.phone_number = phone_number
        if phone_area_code is not None:
            self.phone_area_code = phone_area_code
        if phone_country_code is not None:
            self.phone_country_code = phone_country_code

    @property
    def phone_type(self):
        return self._phone_type

    @phone_type.setter
    def phone_type(self, phone_type):
        allowed_values = [
            "DEFAULT",
            "DDI",
            "MOBILE",
            "FAX",
            "OFFICE",
            "None",
        ]
        if phone_type:
            if phone_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `phone_type` ({0}), must be one of {1}".format(
                        phone_type, allowed_values
                    )
                )
        self._phone_type = phone_type

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if phone_number is not None and len(phone_number) > 50:
            raise ValueError(
                "Invalid value for `phone_number`, "
                "length must be less than or equal to `50`"
            )
        self._phone_number = phone_number

    @property
    def phone_area_code(self):
        return self._phone_area_code

    @phone_area_code.setter
    def phone_area_code(self, phone_area_code):
        if phone_area_code is not None and len(phone_area_code) > 10:
            raise ValueError(
                "Invalid value for `phone_area_code`, "
                "length must be less than or equal to `10`"
            )
        self._phone_area_code = phone_area_code

    @property
    def phone_country_code(self):
        return self._phone_country_code

    @phone_country_code.setter
    def phone_country_code(self, phone_country_code):
        if phone_country_code is not None and len(phone_country_code) > 20:
            raise ValueError(
                "Invalid value for `phone_country_code`, "
                "length must be less than or equal to `20`"
            )
        self._phone_country_code = phone_country_code
