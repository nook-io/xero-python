from xero.models import BaseModel


class AccountUsage(BaseModel):
    openapi_types = {
        "month": "str",
        "account_id": "str",
        "currency_code": "str",
        "total_received": "float",
        "count_received": "int",
        "total_paid": "float",
        "count_paid": "int",
        "total_manual_journal": "float",
        "count_manual_journal": "int",
        "account_name": "str",
        "reporting_code": "str",
        "reporting_code_name": "str",
        "report_code_updated_date_utc": "datetime",
    }
    attribute_map = {
        "month": "month",
        "account_id": "accountId",
        "currency_code": "currencyCode",
        "total_received": "totalReceived",
        "count_received": "countReceived",
        "total_paid": "totalPaid",
        "count_paid": "countPaid",
        "total_manual_journal": "totalManualJournal",
        "count_manual_journal": "countManualJournal",
        "account_name": "accountName",
        "reporting_code": "reportingCode",
        "reporting_code_name": "reportingCodeName",
        "report_code_updated_date_utc": "reportCodeUpdatedDateUtc",
    }

    def __init__(
        self,
        month=None,
        account_id=None,
        currency_code=None,
        total_received=None,
        count_received=None,
        total_paid=None,
        count_paid=None,
        total_manual_journal=None,
        count_manual_journal=None,
        account_name=None,
        reporting_code=None,
        reporting_code_name=None,
        report_code_updated_date_utc=None,
    ):
        self._month = None
        self._account_id = None
        self._currency_code = None
        self._total_received = None
        self._count_received = None
        self._total_paid = None
        self._count_paid = None
        self._total_manual_journal = None
        self._count_manual_journal = None
        self._account_name = None
        self._reporting_code = None
        self._reporting_code_name = None
        self._report_code_updated_date_utc = None
        self.discriminator = None
        if month is not None:
            self.month = month
        if account_id is not None:
            self.account_id = account_id
        if currency_code is not None:
            self.currency_code = currency_code
        if total_received is not None:
            self.total_received = total_received
        if count_received is not None:
            self.count_received = count_received
        if total_paid is not None:
            self.total_paid = total_paid
        if count_paid is not None:
            self.count_paid = count_paid
        if total_manual_journal is not None:
            self.total_manual_journal = total_manual_journal
        if count_manual_journal is not None:
            self.count_manual_journal = count_manual_journal
        if account_name is not None:
            self.account_name = account_name
        if reporting_code is not None:
            self.reporting_code = reporting_code
        if reporting_code_name is not None:
            self.reporting_code_name = reporting_code_name
        if report_code_updated_date_utc is not None:
            self.report_code_updated_date_utc = report_code_updated_date_utc

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        self._month = month

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        self._currency_code = currency_code

    @property
    def total_received(self):
        return self._total_received

    @total_received.setter
    def total_received(self, total_received):
        self._total_received = total_received

    @property
    def count_received(self):
        return self._count_received

    @count_received.setter
    def count_received(self, count_received):
        self._count_received = count_received

    @property
    def total_paid(self):
        return self._total_paid

    @total_paid.setter
    def total_paid(self, total_paid):
        self._total_paid = total_paid

    @property
    def count_paid(self):
        return self._count_paid

    @count_paid.setter
    def count_paid(self, count_paid):
        self._count_paid = count_paid

    @property
    def total_manual_journal(self):
        return self._total_manual_journal

    @total_manual_journal.setter
    def total_manual_journal(self, total_manual_journal):
        self._total_manual_journal = total_manual_journal

    @property
    def count_manual_journal(self):
        return self._count_manual_journal

    @count_manual_journal.setter
    def count_manual_journal(self, count_manual_journal):
        self._count_manual_journal = count_manual_journal

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        self._account_name = account_name

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
    def report_code_updated_date_utc(self):
        return self._report_code_updated_date_utc

    @report_code_updated_date_utc.setter
    def report_code_updated_date_utc(self, report_code_updated_date_utc):
        self._report_code_updated_date_utc = report_code_updated_date_utc
