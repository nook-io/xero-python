from xero.models import BaseModel


class Schedule(BaseModel):
    openapi_types = {
        "period": "int",
        "unit": "str",
        "due_date": "int",
        "due_date_type": "str",
        "start_date": "date[ms-format]",
        "next_scheduled_date": "date[ms-format]",
        "end_date": "date[ms-format]",
    }
    attribute_map = {
        "period": "Period",
        "unit": "Unit",
        "due_date": "DueDate",
        "due_date_type": "DueDateType",
        "start_date": "StartDate",
        "next_scheduled_date": "NextScheduledDate",
        "end_date": "EndDate",
    }

    def __init__(
        self,
        period=None,
        unit=None,
        due_date=None,
        due_date_type=None,
        start_date=None,
        next_scheduled_date=None,
        end_date=None,
    ):
        self._period = None
        self._unit = None
        self._due_date = None
        self._due_date_type = None
        self._start_date = None
        self._next_scheduled_date = None
        self._end_date = None
        self.discriminator = None
        if period is not None:
            self.period = period
        if unit is not None:
            self.unit = unit
        if due_date is not None:
            self.due_date = due_date
        if due_date_type is not None:
            self.due_date_type = due_date_type
        if start_date is not None:
            self.start_date = start_date
        if next_scheduled_date is not None:
            self.next_scheduled_date = next_scheduled_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, period):
        self._period = period

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, unit):
        allowed_values = ["WEEKLY", "MONTHLY", "None"]
        if unit:
            if unit not in allowed_values:
                raise ValueError(
                    "Invalid value for `unit` ({0}), must be one of {1}".format(
                        unit, allowed_values
                    )
                )
        self._unit = unit

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        self._due_date = due_date

    @property
    def due_date_type(self):
        return self._due_date_type

    @due_date_type.setter
    def due_date_type(self, due_date_type):
        allowed_values = [
            "DAYSAFTERBILLDATE",
            "DAYSAFTERBILLMONTH",
            "DAYSAFTERINVOICEDATE",
            "DAYSAFTERINVOICEMONTH",
            "OFCURRENTMONTH",
            "OFFOLLOWINGMONTH",
            "None",
        ]
        if due_date_type:
            if due_date_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `due_date_type` ({0}), must be one of {1}".format(
                        due_date_type, allowed_values
                    )
                )
        self._due_date_type = due_date_type

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def next_scheduled_date(self):
        return self._next_scheduled_date

    @next_scheduled_date.setter
    def next_scheduled_date(self, next_scheduled_date):
        self._next_scheduled_date = next_scheduled_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date
