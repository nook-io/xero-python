from xero.models import BaseModel


class ContactDetail(BaseModel):
    openapi_types = {
        "contact_id": "str",
        "name": "str",
        "total": "float",
        "total_detail": "ContactTotalDetail",
        "total_other": "ContactTotalOther",
        "account_codes": "list[str]",
    }
    attribute_map = {
        "contact_id": "contactId",
        "name": "name",
        "total": "total",
        "total_detail": "totalDetail",
        "total_other": "totalOther",
        "account_codes": "accountCodes",
    }

    def __init__(
        self,
        contact_id=None,
        name=None,
        total=None,
        total_detail=None,
        total_other=None,
        account_codes=None,
    ):
        self._contact_id = None
        self._name = None
        self._total = None
        self._total_detail = None
        self._total_other = None
        self._account_codes = None
        self.discriminator = None
        if contact_id is not None:
            self.contact_id = contact_id
        if name is not None:
            self.name = name
        if total is not None:
            self.total = total
        if total_detail is not None:
            self.total_detail = total_detail
        if total_other is not None:
            self.total_other = total_other
        if account_codes is not None:
            self.account_codes = account_codes

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

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
    def account_codes(self):
        return self._account_codes

    @account_codes.setter
    def account_codes(self, account_codes):
        self._account_codes = account_codes
