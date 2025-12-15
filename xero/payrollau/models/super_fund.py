from xero.models import BaseModel


class SuperFund(BaseModel):
    openapi_types = {
        "super_fund_id": "str",
        "type": "SuperFundType",
        "name": "str",
        "abn": "str",
        "bsb": "str",
        "account_number": "str",
        "account_name": "str",
        "electronic_service_address": "str",
        "employer_number": "str",
        "spin": "str",
        "usi": "str",
        "updated_date_utc": "datetime[ms-format]",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "super_fund_id": "SuperFundID",
        "type": "Type",
        "name": "Name",
        "abn": "ABN",
        "bsb": "BSB",
        "account_number": "AccountNumber",
        "account_name": "AccountName",
        "electronic_service_address": "ElectronicServiceAddress",
        "employer_number": "EmployerNumber",
        "spin": "SPIN",
        "usi": "USI",
        "updated_date_utc": "UpdatedDateUTC",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        super_fund_id=None,
        type=None,
        name=None,
        abn=None,
        bsb=None,
        account_number=None,
        account_name=None,
        electronic_service_address=None,
        employer_number=None,
        spin=None,
        usi=None,
        updated_date_utc=None,
        validation_errors=None,
    ):
        self._super_fund_id = None
        self._type = None
        self._name = None
        self._abn = None
        self._bsb = None
        self._account_number = None
        self._account_name = None
        self._electronic_service_address = None
        self._employer_number = None
        self._spin = None
        self._usi = None
        self._updated_date_utc = None
        self._validation_errors = None
        self.discriminator = None
        if super_fund_id is not None:
            self.super_fund_id = super_fund_id
        self.type = type
        if name is not None:
            self.name = name
        if abn is not None:
            self.abn = abn
        if bsb is not None:
            self.bsb = bsb
        if account_number is not None:
            self.account_number = account_number
        if account_name is not None:
            self.account_name = account_name
        if electronic_service_address is not None:
            self.electronic_service_address = electronic_service_address
        if employer_number is not None:
            self.employer_number = employer_number
        if spin is not None:
            self.spin = spin
        if usi is not None:
            self.usi = usi
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def super_fund_id(self):
        return self._super_fund_id

    @super_fund_id.setter
    def super_fund_id(self, super_fund_id):
        self._super_fund_id = super_fund_id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        self._type = type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def abn(self):
        return self._abn

    @abn.setter
    def abn(self, abn):
        self._abn = abn

    @property
    def bsb(self):
        return self._bsb

    @bsb.setter
    def bsb(self, bsb):
        self._bsb = bsb

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        self._account_number = account_number

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        self._account_name = account_name

    @property
    def electronic_service_address(self):
        return self._electronic_service_address

    @electronic_service_address.setter
    def electronic_service_address(self, electronic_service_address):
        self._electronic_service_address = electronic_service_address

    @property
    def employer_number(self):
        return self._employer_number

    @employer_number.setter
    def employer_number(self, employer_number):
        self._employer_number = employer_number

    @property
    def spin(self):
        return self._spin

    @spin.setter
    def spin(self, spin):
        self._spin = spin

    @property
    def usi(self):
        return self._usi

    @usi.setter
    def usi(self, usi):
        self._usi = usi

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
