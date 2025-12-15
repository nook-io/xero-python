from xero.models import BaseModel


class Journal(BaseModel):
    openapi_types = {
        "journal_id": "str",
        "journal_date": "date[ms-format]",
        "journal_number": "int",
        "created_date_utc": "datetime[ms-format]",
        "reference": "str",
        "source_id": "str",
        "source_type": "str",
        "journal_lines": "list[JournalLine]",
    }
    attribute_map = {
        "journal_id": "JournalID",
        "journal_date": "JournalDate",
        "journal_number": "JournalNumber",
        "created_date_utc": "CreatedDateUTC",
        "reference": "Reference",
        "source_id": "SourceID",
        "source_type": "SourceType",
        "journal_lines": "JournalLines",
    }

    def __init__(
        self,
        journal_id=None,
        journal_date=None,
        journal_number=None,
        created_date_utc=None,
        reference=None,
        source_id=None,
        source_type=None,
        journal_lines=None,
    ):
        self._journal_id = None
        self._journal_date = None
        self._journal_number = None
        self._created_date_utc = None
        self._reference = None
        self._source_id = None
        self._source_type = None
        self._journal_lines = None
        self.discriminator = None
        if journal_id is not None:
            self.journal_id = journal_id
        if journal_date is not None:
            self.journal_date = journal_date
        if journal_number is not None:
            self.journal_number = journal_number
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc
        if reference is not None:
            self.reference = reference
        if source_id is not None:
            self.source_id = source_id
        if source_type is not None:
            self.source_type = source_type
        if journal_lines is not None:
            self.journal_lines = journal_lines

    @property
    def journal_id(self):
        return self._journal_id

    @journal_id.setter
    def journal_id(self, journal_id):
        self._journal_id = journal_id

    @property
    def journal_date(self):
        return self._journal_date

    @journal_date.setter
    def journal_date(self, journal_date):
        self._journal_date = journal_date

    @property
    def journal_number(self):
        return self._journal_number

    @journal_number.setter
    def journal_number(self, journal_number):
        self._journal_number = journal_number

    @property
    def created_date_utc(self):
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        self._created_date_utc = created_date_utc

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        self._source_id = source_id

    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        allowed_values = [
            "ACCREC",
            "ACCPAY",
            "ACCRECCREDIT",
            "ACCPAYCREDIT",
            "ACCRECPAYMENT",
            "ACCPAYPAYMENT",
            "ARCREDITPAYMENT",
            "APCREDITPAYMENT",
            "CASHREC",
            "CASHPAID",
            "TRANSFER",
            "ARPREPAYMENT",
            "APPREPAYMENT",
            "AROVERPAYMENT",
            "APOVERPAYMENT",
            "EXPCLAIM",
            "EXPPAYMENT",
            "MANJOURNAL",
            "PAYSLIP",
            "WAGEPAYABLE",
            "INTEGRATEDPAYROLLPE",
            "INTEGRATEDPAYROLLPT",
            "EXTERNALSPENDMONEY",
            "INTEGRATEDPAYROLLPTPAYMENT",
            "INTEGRATEDPAYROLLCN",
            "None",
        ]
        if source_type:
            if source_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `source_type` ({0}), must be one of {1}".format(
                        source_type, allowed_values
                    )
                )
        self._source_type = source_type

    @property
    def journal_lines(self):
        return self._journal_lines

    @journal_lines.setter
    def journal_lines(self, journal_lines):
        self._journal_lines = journal_lines
