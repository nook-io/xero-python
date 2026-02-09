from xero.models import BaseModel


class Account(BaseModel):
    openapi_types = {
        "code": "str",
        "name": "str",
        "account_id": "str",
        "type": "AccountType",
        "bank_account_number": "str",
        "status": "str",
        "description": "str",
        "bank_account_type": "str",
        "currency_code": "CurrencyCode",
        "tax_type": "str",
        "enable_payments_to_account": "bool",
        "show_in_expense_claims": "bool",
        "_class": "str",
        "system_account": "str",
        "reporting_code": "str",
        "reporting_code_name": "str",
        "has_attachments": "bool",
        "updated_date_utc": "datetime[ms-format]",
        "add_to_watchlist": "bool",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "code": "Code",
        "name": "Name",
        "account_id": "AccountID",
        "type": "Type",
        "bank_account_number": "BankAccountNumber",
        "status": "Status",
        "description": "Description",
        "bank_account_type": "BankAccountType",
        "currency_code": "CurrencyCode",
        "tax_type": "TaxType",
        "enable_payments_to_account": "EnablePaymentsToAccount",
        "show_in_expense_claims": "ShowInExpenseClaims",
        "_class": "Class",
        "system_account": "SystemAccount",
        "reporting_code": "ReportingCode",
        "reporting_code_name": "ReportingCodeName",
        "has_attachments": "HasAttachments",
        "updated_date_utc": "UpdatedDateUTC",
        "add_to_watchlist": "AddToWatchlist",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        code=None,
        name=None,
        account_id=None,
        type=None,
        bank_account_number=None,
        status=None,
        description=None,
        bank_account_type=None,
        currency_code=None,
        tax_type=None,
        enable_payments_to_account=None,
        show_in_expense_claims=None,
        _class=None,
        system_account=None,
        reporting_code=None,
        reporting_code_name=None,
        has_attachments=False,
        updated_date_utc=None,
        add_to_watchlist=None,
        validation_errors=None,
    ):
        self._code = None
        self._name = None
        self._account_id = None
        self._type = None
        self._bank_account_number = None
        self._status = None
        self._description = None
        self._bank_account_type = None
        self._currency_code = None
        self._tax_type = None
        self._enable_payments_to_account = None
        self._show_in_expense_claims = None
        self.__class = None
        self._system_account = None
        self._reporting_code = None
        self._reporting_code_name = None
        self._has_attachments = None
        self._updated_date_utc = None
        self._add_to_watchlist = None
        self._validation_errors = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if account_id is not None:
            self.account_id = account_id
        if type is not None:
            self.type = type
        if bank_account_number is not None:
            self.bank_account_number = bank_account_number
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if bank_account_type is not None:
            self.bank_account_type = bank_account_type
        if currency_code is not None:
            self.currency_code = currency_code
        if tax_type is not None:
            self.tax_type = tax_type
        if enable_payments_to_account is not None:
            self.enable_payments_to_account = enable_payments_to_account
        if show_in_expense_claims is not None:
            self.show_in_expense_claims = show_in_expense_claims
        if _class is not None:
            self._class = _class
        if system_account is not None:
            self.system_account = system_account
        if reporting_code is not None:
            self.reporting_code = reporting_code
        if reporting_code_name is not None:
            self.reporting_code_name = reporting_code_name
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if add_to_watchlist is not None:
            self.add_to_watchlist = add_to_watchlist
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 150:
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `150`"
            )
        self._name = name

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def bank_account_number(self):
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        self._bank_account_number = bank_account_number

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = ["ACTIVE", "ARCHIVED", "DELETED", "None"]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def bank_account_type(self):
        return self._bank_account_type

    @bank_account_type.setter
    def bank_account_type(self, bank_account_type):
        allowed_values = [
            "BANK",
            "CREDITCARD",
            "PAYPAL",
            "NONE",
            "",
            "None",
        ]
        if bank_account_type:
            if bank_account_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `bank_account_type` ({0}), must be one of {1}".format(
                        bank_account_type, allowed_values
                    )
                )
        self._bank_account_type = bank_account_type

    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        self._currency_code = currency_code

    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        self._tax_type = tax_type

    @property
    def enable_payments_to_account(self):
        return self._enable_payments_to_account

    @enable_payments_to_account.setter
    def enable_payments_to_account(self, enable_payments_to_account):
        self._enable_payments_to_account = enable_payments_to_account

    @property
    def show_in_expense_claims(self):
        return self._show_in_expense_claims

    @show_in_expense_claims.setter
    def show_in_expense_claims(self, show_in_expense_claims):
        self._show_in_expense_claims = show_in_expense_claims

    @property
    def _class(self):
        return self.__class

    @_class.setter
    def _class(self, _class):
        allowed_values = [
            "ASSET",
            "EQUITY",
            "EXPENSE",
            "LIABILITY",
            "REVENUE",
            "None",
        ]
        if _class:
            if _class not in allowed_values:
                raise ValueError(
                    "Invalid value for `_class` ({0}), must be one of {1}".format(
                        _class, allowed_values
                    )
                )
        self.__class = _class

    @property
    def system_account(self):
        return self._system_account

    @system_account.setter
    def system_account(self, system_account):
        allowed_values = [
            "DEBTORS",
            "CREDITORS",
            "BANKCURRENCYGAIN",
            "GST",
            "GSTONIMPORTS",
            "HISTORICAL",
            "REALISEDCURRENCYGAIN",
            "RETAINEDEARNINGS",
            "ROUNDING",
            "TRACKINGTRANSFERS",
            "UNPAIDEXPCLM",
            "UNREALISEDCURRENCYGAIN",
            "WAGEPAYABLES",
            "CISASSETS",
            "CISASSET",
            "CISLABOUR",
            "CISLABOUREXPENSE",
            "CISLABOURINCOME",
            "CISLIABILITY",
            "CISMATERIALS",
            "",
            "None",
        ]
        if system_account:
            if system_account not in allowed_values:
                raise ValueError(
                    "Invalid value for `system_account` ({0}), must be one of {1}".format(
                        system_account, allowed_values
                    )
                )
        self._system_account = system_account

    @property
    def reporting_code(self):
        return self._reporting_code

    @reporting_code.setter
    def reporting_code(self, reporting_code):
        self._reporting_code = reporting_code

    @property
    def reporting_code_name(self):
        return self._reporting_code_name

    @reporting_code_name.setter
    def reporting_code_name(self, reporting_code_name):
        self._reporting_code_name = reporting_code_name

    @property
    def has_attachments(self):
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        self._has_attachments = has_attachments

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def add_to_watchlist(self):
        return self._add_to_watchlist

    @add_to_watchlist.setter
    def add_to_watchlist(self, add_to_watchlist):
        self._add_to_watchlist = add_to_watchlist

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
