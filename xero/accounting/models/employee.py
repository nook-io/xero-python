from xero.models import BaseModel


class Employee(BaseModel):
    openapi_types = {
        "employee_id": "str",
        "status": "str",
        "first_name": "str",
        "last_name": "str",
        "external_link": "ExternalLink",
        "updated_date_utc": "datetime[ms-format]",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "employee_id": "EmployeeID",
        "status": "Status",
        "first_name": "FirstName",
        "last_name": "LastName",
        "external_link": "ExternalLink",
        "updated_date_utc": "UpdatedDateUTC",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        employee_id=None,
        status=None,
        first_name=None,
        last_name=None,
        external_link=None,
        updated_date_utc=None,
        status_attribute_string=None,
        validation_errors=None,
    ):
        self._employee_id = None
        self._status = None
        self._first_name = None
        self._last_name = None
        self._external_link = None
        self._updated_date_utc = None
        self._status_attribute_string = None
        self._validation_errors = None
        self.discriminator = None
        if employee_id is not None:
            self.employee_id = employee_id
        if status is not None:
            self.status = status
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if external_link is not None:
            self.external_link = external_link
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = [
            "ACTIVE",
            "ARCHIVED",
            "GDPRREQUEST",
            "DELETED",
            "None",
        ]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name is not None and len(first_name) > 255:
            raise ValueError(
                "Invalid value for `first_name`, "
                "length must be less than or equal to `255`"
            )
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name is not None and len(last_name) > 255:
            raise ValueError(
                "Invalid value for `last_name`, "
                "length must be less than or equal to `255`"
            )
        self._last_name = last_name

    @property
    def external_link(self):
        return self._external_link

    @external_link.setter
    def external_link(self, external_link):
        self._external_link = external_link

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def status_attribute_string(self):
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
