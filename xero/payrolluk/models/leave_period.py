from xero.models import BaseModel


class LeavePeriod(BaseModel):
    openapi_types = {
        "period_start_date": "date",
        "period_end_date": "date",
        "number_of_units": "float",
        "period_status": "str",
    }
    attribute_map = {
        "period_start_date": "periodStartDate",
        "period_end_date": "periodEndDate",
        "number_of_units": "numberOfUnits",
        "period_status": "periodStatus",
    }

    def __init__(
        self,
        period_start_date=None,
        period_end_date=None,
        number_of_units=None,
        period_status=None,
    ):
        self._period_start_date = None
        self._period_end_date = None
        self._number_of_units = None
        self._period_status = None
        self.discriminator = None
        if period_start_date is not None:
            self.period_start_date = period_start_date
        if period_end_date is not None:
            self.period_end_date = period_end_date
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if period_status is not None:
            self.period_status = period_status

    @property
    def period_start_date(self):
        return self._period_start_date

    @period_start_date.setter
    def period_start_date(self, period_start_date):
        self._period_start_date = period_start_date

    @property
    def period_end_date(self):
        return self._period_end_date

    @period_end_date.setter
    def period_end_date(self, period_end_date):
        self._period_end_date = period_end_date

    @property
    def number_of_units(self):
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        self._number_of_units = number_of_units

    @property
    def period_status(self):
        return self._period_status

    @period_status.setter
    def period_status(self, period_status):
        allowed_values = ["Approved", "Completed", "None"]
        if period_status:
            if period_status not in allowed_values:
                raise ValueError(
                    "Invalid value for `period_status` ({0}), must be one of {1}".format(
                        period_status, allowed_values
                    )
                )
        self._period_status = period_status
