from xero.models import BaseModel


class WorkingWeek(BaseModel):
    openapi_types = {
        "monday": "float",
        "tuesday": "float",
        "wednesday": "float",
        "thursday": "float",
        "friday": "float",
        "saturday": "float",
        "sunday": "float",
    }
    attribute_map = {
        "monday": "monday",
        "tuesday": "tuesday",
        "wednesday": "wednesday",
        "thursday": "thursday",
        "friday": "friday",
        "saturday": "saturday",
        "sunday": "sunday",
    }

    def __init__(
        self,
        monday=None,
        tuesday=None,
        wednesday=None,
        thursday=None,
        friday=None,
        saturday=None,
        sunday=None,
    ):
        self._monday = None
        self._tuesday = None
        self._wednesday = None
        self._thursday = None
        self._friday = None
        self._saturday = None
        self._sunday = None
        self.discriminator = None
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday

    @property
    def monday(self):
        return self._monday

    @monday.setter
    def monday(self, monday):
        if monday is None:
            raise ValueError("Invalid value for `monday`, must not be `None`")
        self._monday = monday

    @property
    def tuesday(self):
        return self._tuesday

    @tuesday.setter
    def tuesday(self, tuesday):
        if tuesday is None:
            raise ValueError("Invalid value for `tuesday`, must not be `None`")
        self._tuesday = tuesday

    @property
    def wednesday(self):
        return self._wednesday

    @wednesday.setter
    def wednesday(self, wednesday):
        if wednesday is None:
            raise ValueError("Invalid value for `wednesday`, must not be `None`")
        self._wednesday = wednesday

    @property
    def thursday(self):
        return self._thursday

    @thursday.setter
    def thursday(self, thursday):
        if thursday is None:
            raise ValueError("Invalid value for `thursday`, must not be `None`")
        self._thursday = thursday

    @property
    def friday(self):
        return self._friday

    @friday.setter
    def friday(self, friday):
        if friday is None:
            raise ValueError("Invalid value for `friday`, must not be `None`")
        self._friday = friday

    @property
    def saturday(self):
        return self._saturday

    @saturday.setter
    def saturday(self, saturday):
        if saturday is None:
            raise ValueError("Invalid value for `saturday`, must not be `None`")
        self._saturday = saturday

    @property
    def sunday(self):
        return self._sunday

    @sunday.setter
    def sunday(self, sunday):
        if sunday is None:
            raise ValueError("Invalid value for `sunday`, must not be `None`")
        self._sunday = sunday
