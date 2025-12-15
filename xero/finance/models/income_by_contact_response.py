from xero.models import BaseModel


class IncomeByContactResponse(BaseModel):
    openapi_types = {
        "start_date": "date",
        "end_date": "date",
        "total": "float",
        "total_detail": "TotalDetail",
        "total_other": "TotalOther",
        "contacts": "list[ContactDetail]",
        "manual_journals": "ManualJournalTotal",
    }
    attribute_map = {
        "start_date": "startDate",
        "end_date": "endDate",
        "total": "total",
        "total_detail": "totalDetail",
        "total_other": "totalOther",
        "contacts": "contacts",
        "manual_journals": "manualJournals",
    }

    def __init__(
        self,
        start_date=None,
        end_date=None,
        total=None,
        total_detail=None,
        total_other=None,
        contacts=None,
        manual_journals=None,
    ):
        self._start_date = None
        self._end_date = None
        self._total = None
        self._total_detail = None
        self._total_other = None
        self._contacts = None
        self._manual_journals = None
        self.discriminator = None
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if total is not None:
            self.total = total
        if total_detail is not None:
            self.total_detail = total_detail
        if total_other is not None:
            self.total_other = total_other
        if contacts is not None:
            self.contacts = contacts
        if manual_journals is not None:
            self.manual_journals = manual_journals

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def total_detail(self):
        return self._total_detail

    @total_detail.setter
    def total_detail(self, total_detail):
        self._total_detail = total_detail

    @property
    def total_other(self):
        return self._total_other

    @total_other.setter
    def total_other(self, total_other):
        self._total_other = total_other

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        self._contacts = contacts

    @property
    def manual_journals(self):
        return self._manual_journals

    @manual_journals.setter
    def manual_journals(self, manual_journals):
        self._manual_journals = manual_journals
