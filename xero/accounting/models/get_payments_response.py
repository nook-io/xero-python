from xero.models import BaseModel


class GetPaymentsResponse(BaseModel):
    openapi_types = {
        "id": "str",
        "status": "str",
        "provider_name": "str",
        "date_time_utc": "str",
        "page_info": "PageInfo",
        "payments": "list[Payment]",
    }
    attribute_map = {
        "id": "Id",
        "status": "Status",
        "provider_name": "ProviderName",
        "date_time_utc": "DateTimeUTC",
        "page_info": "PageInfo",
        "payments": "Payments",
    }

    def __init__(
        self,
        id=None,
        status=None,
        provider_name=None,
        date_time_utc=None,
        page_info=None,
        payments=None,
    ):
        self._id = None
        self._status = None
        self._provider_name = None
        self._date_time_utc = None
        self._page_info = None
        self._payments = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if provider_name is not None:
            self.provider_name = provider_name
        if date_time_utc is not None:
            self.date_time_utc = date_time_utc
        if page_info is not None:
            self.page_info = page_info
        if payments is not None:
            self.payments = payments

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def provider_name(self):
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        self._provider_name = provider_name

    @property
    def date_time_utc(self):
        return self._date_time_utc

    @date_time_utc.setter
    def date_time_utc(self, date_time_utc):
        self._date_time_utc = date_time_utc

    @property
    def page_info(self):
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        self._page_info = page_info

    @property
    def payments(self):
        return self._payments

    @payments.setter
    def payments(self, payments):
        self._payments = payments
