from xero.models import BaseModel


class UserResponse(BaseModel):
    openapi_types = {
        "user_id": "str",
        "user_created_date_utc": "datetime",
        "last_login_date_utc": "datetime",
        "is_external_partner": "bool",
        "has_accountant_role": "bool",
        "month_period": "str",
        "number_of_logins": "int",
        "number_of_documents_created": "int",
        "net_value_documents_created": "float",
        "absolute_value_documents_created": "float",
        "attached_practices": "list[PracticeResponse]",
        "history_records": "list[HistoryRecordResponse]",
    }
    attribute_map = {
        "user_id": "userId",
        "user_created_date_utc": "userCreatedDateUtc",
        "last_login_date_utc": "lastLoginDateUtc",
        "is_external_partner": "isExternalPartner",
        "has_accountant_role": "hasAccountantRole",
        "month_period": "monthPeriod",
        "number_of_logins": "numberOfLogins",
        "number_of_documents_created": "numberOfDocumentsCreated",
        "net_value_documents_created": "netValueDocumentsCreated",
        "absolute_value_documents_created": "absoluteValueDocumentsCreated",
        "attached_practices": "attachedPractices",
        "history_records": "historyRecords",
    }

    def __init__(
        self,
        user_id=None,
        user_created_date_utc=None,
        last_login_date_utc=None,
        is_external_partner=None,
        has_accountant_role=None,
        month_period=None,
        number_of_logins=None,
        number_of_documents_created=None,
        net_value_documents_created=None,
        absolute_value_documents_created=None,
        attached_practices=None,
        history_records=None,
    ):
        self._user_id = None
        self._user_created_date_utc = None
        self._last_login_date_utc = None
        self._is_external_partner = None
        self._has_accountant_role = None
        self._month_period = None
        self._number_of_logins = None
        self._number_of_documents_created = None
        self._net_value_documents_created = None
        self._absolute_value_documents_created = None
        self._attached_practices = None
        self._history_records = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if user_created_date_utc is not None:
            self.user_created_date_utc = user_created_date_utc
        if last_login_date_utc is not None:
            self.last_login_date_utc = last_login_date_utc
        if is_external_partner is not None:
            self.is_external_partner = is_external_partner
        if has_accountant_role is not None:
            self.has_accountant_role = has_accountant_role
        if month_period is not None:
            self.month_period = month_period
        if number_of_logins is not None:
            self.number_of_logins = number_of_logins
        if number_of_documents_created is not None:
            self.number_of_documents_created = number_of_documents_created
        if net_value_documents_created is not None:
            self.net_value_documents_created = net_value_documents_created
        if absolute_value_documents_created is not None:
            self.absolute_value_documents_created = absolute_value_documents_created
        if attached_practices is not None:
            self.attached_practices = attached_practices
        if history_records is not None:
            self.history_records = history_records

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def user_created_date_utc(self):
        return self._user_created_date_utc

    @user_created_date_utc.setter
    def user_created_date_utc(self, user_created_date_utc):
        self._user_created_date_utc = user_created_date_utc

    @property
    def last_login_date_utc(self):
        return self._last_login_date_utc

    @last_login_date_utc.setter
    def last_login_date_utc(self, last_login_date_utc):
        self._last_login_date_utc = last_login_date_utc

    @property
    def is_external_partner(self):
        return self._is_external_partner

    @is_external_partner.setter
    def is_external_partner(self, is_external_partner):
        self._is_external_partner = is_external_partner

    @property
    def has_accountant_role(self):
        return self._has_accountant_role

    @has_accountant_role.setter
    def has_accountant_role(self, has_accountant_role):
        self._has_accountant_role = has_accountant_role

    @property
    def month_period(self):
        return self._month_period

    @month_period.setter
    def month_period(self, month_period):
        self._month_period = month_period

    @property
    def number_of_logins(self):
        return self._number_of_logins

    @number_of_logins.setter
    def number_of_logins(self, number_of_logins):
        self._number_of_logins = number_of_logins

    @property
    def number_of_documents_created(self):
        return self._number_of_documents_created

    @number_of_documents_created.setter
    def number_of_documents_created(self, number_of_documents_created):
        self._number_of_documents_created = number_of_documents_created

    @property
    def net_value_documents_created(self):
        return self._net_value_documents_created

    @net_value_documents_created.setter
    def net_value_documents_created(self, net_value_documents_created):
        self._net_value_documents_created = net_value_documents_created

    @property
    def absolute_value_documents_created(self):
        return self._absolute_value_documents_created

    @absolute_value_documents_created.setter
    def absolute_value_documents_created(self, absolute_value_documents_created):
        self._absolute_value_documents_created = absolute_value_documents_created

    @property
    def attached_practices(self):
        return self._attached_practices

    @attached_practices.setter
    def attached_practices(self, attached_practices):
        self._attached_practices = attached_practices

    @property
    def history_records(self):
        return self._history_records

    @history_records.setter
    def history_records(self, history_records):
        self._history_records = history_records
