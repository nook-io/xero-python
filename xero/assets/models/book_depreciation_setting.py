from xero.models import BaseModel


class BookDepreciationSetting(BaseModel):
    openapi_types = {
        "depreciation_method": "str",
        "averaging_method": "str",
        "depreciation_rate": "float",
        "effective_life_years": "int",
        "depreciation_calculation_method": "str",
        "depreciable_object_id": "str",
        "depreciable_object_type": "str",
        "book_effective_date_of_change_id": "str",
    }
    attribute_map = {
        "depreciation_method": "depreciationMethod",
        "averaging_method": "averagingMethod",
        "depreciation_rate": "depreciationRate",
        "effective_life_years": "effectiveLifeYears",
        "depreciation_calculation_method": "depreciationCalculationMethod",
        "depreciable_object_id": "depreciableObjectId",
        "depreciable_object_type": "depreciableObjectType",
        "book_effective_date_of_change_id": "bookEffectiveDateOfChangeId",
    }

    def __init__(
        self,
        depreciation_method=None,
        averaging_method=None,
        depreciation_rate=None,
        effective_life_years=None,
        depreciation_calculation_method=None,
        depreciable_object_id=None,
        depreciable_object_type=None,
        book_effective_date_of_change_id=None,
    ):
        self._depreciation_method = None
        self._averaging_method = None
        self._depreciation_rate = None
        self._effective_life_years = None
        self._depreciation_calculation_method = None
        self._depreciable_object_id = None
        self._depreciable_object_type = None
        self._book_effective_date_of_change_id = None
        self.discriminator = None
        if depreciation_method is not None:
            self.depreciation_method = depreciation_method
        if averaging_method is not None:
            self.averaging_method = averaging_method
        if depreciation_rate is not None:
            self.depreciation_rate = depreciation_rate
        if effective_life_years is not None:
            self.effective_life_years = effective_life_years
        if depreciation_calculation_method is not None:
            self.depreciation_calculation_method = depreciation_calculation_method
        if depreciable_object_id is not None:
            self.depreciable_object_id = depreciable_object_id
        if depreciable_object_type is not None:
            self.depreciable_object_type = depreciable_object_type
        if book_effective_date_of_change_id is not None:
            self.book_effective_date_of_change_id = book_effective_date_of_change_id

    @property
    def depreciation_method(self):
        return self._depreciation_method

    @depreciation_method.setter
    def depreciation_method(self, depreciation_method):
        allowed_values = [
            "NoDepreciation",
            "StraightLine",
            "DiminishingValue100",
            "DiminishingValue150",
            "DiminishingValue200",
            "FullDepreciation",
            "None",
        ]
        if depreciation_method:
            if depreciation_method not in allowed_values:
                raise ValueError(
                    "Invalid value for `depreciation_method` ({0}), must be one of {1}".format(
                        depreciation_method, allowed_values
                    )
                )
        self._depreciation_method = depreciation_method

    @property
    def averaging_method(self):
        return self._averaging_method

    @averaging_method.setter
    def averaging_method(self, averaging_method):
        allowed_values = ["FullMonth", "ActualDays", "None"]
        if averaging_method:
            if averaging_method not in allowed_values:
                raise ValueError(
                    "Invalid value for `averaging_method` ({0}), must be one of {1}".format(
                        averaging_method, allowed_values
                    )
                )
        self._averaging_method = averaging_method

    @property
    def depreciation_rate(self):
        return self._depreciation_rate

    @depreciation_rate.setter
    def depreciation_rate(self, depreciation_rate):
        self._depreciation_rate = depreciation_rate

    @property
    def effective_life_years(self):
        return self._effective_life_years

    @effective_life_years.setter
    def effective_life_years(self, effective_life_years):
        self._effective_life_years = effective_life_years

    @property
    def depreciation_calculation_method(self):
        return self._depreciation_calculation_method

    @depreciation_calculation_method.setter
    def depreciation_calculation_method(self, depreciation_calculation_method):
        allowed_values = ["Rate", "Life", "None", "None"]
        if depreciation_calculation_method:
            if depreciation_calculation_method not in allowed_values:
                raise ValueError(
                    "Invalid value for `depreciation_calculation_method` ({0}), must be one of {1}".format(
                        depreciation_calculation_method, allowed_values
                    )
                )
        self._depreciation_calculation_method = depreciation_calculation_method

    @property
    def depreciable_object_id(self):
        return self._depreciable_object_id

    @depreciable_object_id.setter
    def depreciable_object_id(self, depreciable_object_id):
        self._depreciable_object_id = depreciable_object_id

    @property
    def depreciable_object_type(self):
        return self._depreciable_object_type

    @depreciable_object_type.setter
    def depreciable_object_type(self, depreciable_object_type):
        self._depreciable_object_type = depreciable_object_type

    @property
    def book_effective_date_of_change_id(self):
        return self._book_effective_date_of_change_id

    @book_effective_date_of_change_id.setter
    def book_effective_date_of_change_id(self, book_effective_date_of_change_id):
        self._book_effective_date_of_change_id = book_effective_date_of_change_id
