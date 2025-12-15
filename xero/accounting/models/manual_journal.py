from xero.models import BaseModel


class ManualJournal(BaseModel):
    openapi_types = {
        "narration": "str",
        "journal_lines": "list[ManualJournalLine]",
        "date": "date[ms-format]",
        "line_amount_types": "LineAmountTypes",
        "status": "str",
        "url": "str",
        "show_on_cash_basis_reports": "bool",
        "has_attachments": "bool",
        "updated_date_utc": "datetime[ms-format]",
        "manual_journal_id": "str",
        "status_attribute_string": "str",
        "warnings": "list[ValidationError]",
        "validation_errors": "list[ValidationError]",
        "attachments": "list[Attachment]",
    }
    attribute_map = {
        "narration": "Narration",
        "journal_lines": "JournalLines",
        "date": "Date",
        "line_amount_types": "LineAmountTypes",
        "status": "Status",
        "url": "Url",
        "show_on_cash_basis_reports": "ShowOnCashBasisReports",
        "has_attachments": "HasAttachments",
        "updated_date_utc": "UpdatedDateUTC",
        "manual_journal_id": "ManualJournalID",
        "status_attribute_string": "StatusAttributeString",
        "warnings": "Warnings",
        "validation_errors": "ValidationErrors",
        "attachments": "Attachments",
    }

    def __init__(
        self,
        narration=None,
        journal_lines=None,
        date=None,
        line_amount_types=None,
        status=None,
        url=None,
        show_on_cash_basis_reports=None,
        has_attachments=False,
        updated_date_utc=None,
        manual_journal_id=None,
        status_attribute_string=None,
        warnings=None,
        validation_errors=None,
        attachments=None,
    ):
        self._narration = None
        self._journal_lines = None
        self._date = None
        self._line_amount_types = None
        self._status = None
        self._url = None
        self._show_on_cash_basis_reports = None
        self._has_attachments = None
        self._updated_date_utc = None
        self._manual_journal_id = None
        self._status_attribute_string = None
        self._warnings = None
        self._validation_errors = None
        self._attachments = None
        self.discriminator = None
        self.narration = narration
        if journal_lines is not None:
            self.journal_lines = journal_lines
        if date is not None:
            self.date = date
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url
        if show_on_cash_basis_reports is not None:
            self.show_on_cash_basis_reports = show_on_cash_basis_reports
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if manual_journal_id is not None:
            self.manual_journal_id = manual_journal_id
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if warnings is not None:
            self.warnings = warnings
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if attachments is not None:
            self.attachments = attachments

    @property
    def narration(self):
        return self._narration

    @narration.setter
    def narration(self, narration):
        if narration is None:
            raise ValueError("Invalid value for `narration`, must not be `None`")
        self._narration = narration

    @property
    def journal_lines(self):
        return self._journal_lines

    @journal_lines.setter
    def journal_lines(self, journal_lines):
        self._journal_lines = journal_lines

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def line_amount_types(self):
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        self._line_amount_types = line_amount_types

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = [
            "DRAFT",
            "POSTED",
            "DELETED",
            "VOIDED",
            "ARCHIVED",
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
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def show_on_cash_basis_reports(self):
        return self._show_on_cash_basis_reports

    @show_on_cash_basis_reports.setter
    def show_on_cash_basis_reports(self, show_on_cash_basis_reports):
        self._show_on_cash_basis_reports = show_on_cash_basis_reports

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
    def manual_journal_id(self):
        return self._manual_journal_id

    @manual_journal_id.setter
    def manual_journal_id(self, manual_journal_id):
        self._manual_journal_id = manual_journal_id

    @property
    def status_attribute_string(self):
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        self._status_attribute_string = status_attribute_string

    @property
    def warnings(self):
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        self._warnings = warnings

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        self._attachments = attachments
