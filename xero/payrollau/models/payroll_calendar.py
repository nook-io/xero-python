from xero.models import BaseModel


class PayrollCalendar(BaseModel):
    openapi_types = {
        "name": "str",
        "calendar_type": "CalendarType",
        "start_date": "date[ms-format]",
        "payment_date": "date[ms-format]",
        "payroll_calendar_id": "str",
        "updated_date_utc": "datetime[ms-format]",
        "reference_date": "date[ms-format]",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "name": "Name",
        "calendar_type": "CalendarType",
        "start_date": "StartDate",
        "payment_date": "PaymentDate",
        "payroll_calendar_id": "PayrollCalendarID",
        "updated_date_utc": "UpdatedDateUTC",
        "reference_date": "ReferenceDate",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        name=None,
        calendar_type=None,
        start_date=None,
        payment_date=None,
        payroll_calendar_id=None,
        updated_date_utc=None,
        reference_date=None,
        validation_errors=None,
    ):
        self._name = None
        self._calendar_type = None
        self._start_date = None
        self._payment_date = None
        self._payroll_calendar_id = None
        self._updated_date_utc = None
        self._reference_date = None
        self._validation_errors = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if calendar_type is not None:
            self.calendar_type = calendar_type
        if start_date is not None:
            self.start_date = start_date
        if payment_date is not None:
            self.payment_date = payment_date
        if payroll_calendar_id is not None:
            self.payroll_calendar_id = payroll_calendar_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if reference_date is not None:
            self.reference_date = reference_date
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def calendar_type(self):
        return self._calendar_type

    @calendar_type.setter
    def calendar_type(self, calendar_type):
        self._calendar_type = calendar_type

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        self._payment_date = payment_date

    @property
    def payroll_calendar_id(self):
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        self._payroll_calendar_id = payroll_calendar_id

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def reference_date(self):
        return self._reference_date

    @reference_date.setter
    def reference_date(self, reference_date):
        self._reference_date = reference_date

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
