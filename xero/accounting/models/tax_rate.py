from xero.models import BaseModel


class TaxRate(BaseModel):
    openapi_types = {
        "name": "str",
        "tax_type": "str",
        "tax_components": "list[TaxComponent]",
        "status": "str",
        "report_tax_type": "str",
        "can_apply_to_assets": "bool",
        "can_apply_to_equity": "bool",
        "can_apply_to_expenses": "bool",
        "can_apply_to_liabilities": "bool",
        "can_apply_to_revenue": "bool",
        "display_tax_rate": "float",
        "effective_rate": "float",
    }
    attribute_map = {
        "name": "Name",
        "tax_type": "TaxType",
        "tax_components": "TaxComponents",
        "status": "Status",
        "report_tax_type": "ReportTaxType",
        "can_apply_to_assets": "CanApplyToAssets",
        "can_apply_to_equity": "CanApplyToEquity",
        "can_apply_to_expenses": "CanApplyToExpenses",
        "can_apply_to_liabilities": "CanApplyToLiabilities",
        "can_apply_to_revenue": "CanApplyToRevenue",
        "display_tax_rate": "DisplayTaxRate",
        "effective_rate": "EffectiveRate",
    }

    def __init__(
        self,
        name=None,
        tax_type=None,
        tax_components=None,
        status=None,
        report_tax_type=None,
        can_apply_to_assets=None,
        can_apply_to_equity=None,
        can_apply_to_expenses=None,
        can_apply_to_liabilities=None,
        can_apply_to_revenue=None,
        display_tax_rate=None,
        effective_rate=None,
    ):
        self._name = None
        self._tax_type = None
        self._tax_components = None
        self._status = None
        self._report_tax_type = None
        self._can_apply_to_assets = None
        self._can_apply_to_equity = None
        self._can_apply_to_expenses = None
        self._can_apply_to_liabilities = None
        self._can_apply_to_revenue = None
        self._display_tax_rate = None
        self._effective_rate = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if tax_type is not None:
            self.tax_type = tax_type
        if tax_components is not None:
            self.tax_components = tax_components
        if status is not None:
            self.status = status
        if report_tax_type is not None:
            self.report_tax_type = report_tax_type
        if can_apply_to_assets is not None:
            self.can_apply_to_assets = can_apply_to_assets
        if can_apply_to_equity is not None:
            self.can_apply_to_equity = can_apply_to_equity
        if can_apply_to_expenses is not None:
            self.can_apply_to_expenses = can_apply_to_expenses
        if can_apply_to_liabilities is not None:
            self.can_apply_to_liabilities = can_apply_to_liabilities
        if can_apply_to_revenue is not None:
            self.can_apply_to_revenue = can_apply_to_revenue
        if display_tax_rate is not None:
            self.display_tax_rate = display_tax_rate
        if effective_rate is not None:
            self.effective_rate = effective_rate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        self._tax_type = tax_type

    @property
    def tax_components(self):
        return self._tax_components

    @tax_components.setter
    def tax_components(self, tax_components):
        self._tax_components = tax_components

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = [
            "ACTIVE",
            "DELETED",
            "ARCHIVED",
            "PENDING",
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
    def report_tax_type(self):
        return self._report_tax_type

    @report_tax_type.setter
    def report_tax_type(self, report_tax_type):
        allowed_values = [
            "AVALARA",
            "BASEXCLUDED",
            "CAPITALSALESOUTPUT",
            "CAPITALEXPENSESINPUT",
            "ECOUTPUT",
            "ECOUTPUTSERVICES",
            "ECINPUT",
            "ECACQUISITIONS",
            "EXEMPTEXPENSES",
            "EXEMPTINPUT",
            "EXEMPTOUTPUT",
            "GSTONIMPORTS",
            "INPUT",
            "INPUTTAXED",
            "MOSSSALES",
            "NONE",
            "NONEOUTPUT",
            "OUTPUT",
            "PURCHASESINPUT",
            "SALESOUTPUT",
            "EXEMPTCAPITAL",
            "EXEMPTEXPORT",
            "CAPITALEXINPUT",
            "GSTONCAPIMPORTS",
            "GSTONCAPITALIMPORTS",
            "REVERSECHARGES",
            "PAYMENTS",
            "INVOICE",
            "CASH",
            "ACCRUAL",
            "FLATRATECASH",
            "FLATRATEACCRUAL",
            "ACCRUALS",
            "TXCA",
            "SRCAS",
            "DSOUTPUT",
            "BLINPUT2",
            "EPINPUT",
            "IMINPUT2",
            "MEINPUT",
            "IGDSINPUT2",
            "ESN33OUTPUT",
            "OPINPUT",
            "OSOUTPUT",
            "TXN33INPUT",
            "TXESSINPUT",
            "TXREINPUT",
            "TXPETINPUT",
            "NRINPUT",
            "ES33OUTPUT",
            "ZERORATEDINPUT",
            "ZERORATEDOUTPUT",
            "DRCHARGESUPPLY",
            "DRCHARGE",
            "CAPINPUT",
            "CAPIMPORTS",
            "IMINPUT",
            "INPUT2",
            "CIUINPUT",
            "SRINPUT",
            "OUTPUT2",
            "SROUTPUT",
            "CAPOUTPUT",
            "SROUTPUT2",
            "CIUOUTPUT",
            "ZROUTPUT",
            "ZREXPORT",
            "ACC28PLUS",
            "ACCUPTO28",
            "OTHEROUTPUT",
            "SHOUTPUT",
            "ZRINPUT",
            "BADDEBT",
            "OTHERINPUT",
            "BADDEBTRELIEF",
            "IGDSINPUT3",
            "SROVR",
            "TOURISTREFUND",
            "TXRCN33",
            "TXRCRE",
            "TXRCESS",
            "TXRCTS",
            "CAPEXINPUT",
            "UNDEFINED",
            "CAPEXOUTPUT",
            "ZEROEXPOUTPUT",
            "GOODSIMPORT",
            "NONEINPUT",
            "NOTREPORTED",
            "SROVRRS",
            "SROVRLVG",
            "SRLVG",
            "IM",
            "IMESS",
            "IMN33",
            "IMRE",
            "BADDEBTRECOVERY",
            "USSALESTAX",
            "BLINPUT3",
            "None",
        ]
        if report_tax_type:
            if report_tax_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `report_tax_type` ({0}), must be one of {1}".format(
                        report_tax_type, allowed_values
                    )
                )
        self._report_tax_type = report_tax_type

    @property
    def can_apply_to_assets(self):
        return self._can_apply_to_assets

    @can_apply_to_assets.setter
    def can_apply_to_assets(self, can_apply_to_assets):
        self._can_apply_to_assets = can_apply_to_assets

    @property
    def can_apply_to_equity(self):
        return self._can_apply_to_equity

    @can_apply_to_equity.setter
    def can_apply_to_equity(self, can_apply_to_equity):
        self._can_apply_to_equity = can_apply_to_equity

    @property
    def can_apply_to_expenses(self):
        return self._can_apply_to_expenses

    @can_apply_to_expenses.setter
    def can_apply_to_expenses(self, can_apply_to_expenses):
        self._can_apply_to_expenses = can_apply_to_expenses

    @property
    def can_apply_to_liabilities(self):
        return self._can_apply_to_liabilities

    @can_apply_to_liabilities.setter
    def can_apply_to_liabilities(self, can_apply_to_liabilities):
        self._can_apply_to_liabilities = can_apply_to_liabilities

    @property
    def can_apply_to_revenue(self):
        return self._can_apply_to_revenue

    @can_apply_to_revenue.setter
    def can_apply_to_revenue(self, can_apply_to_revenue):
        self._can_apply_to_revenue = can_apply_to_revenue

    @property
    def display_tax_rate(self):
        return self._display_tax_rate

    @display_tax_rate.setter
    def display_tax_rate(self, display_tax_rate):
        self._display_tax_rate = display_tax_rate

    @property
    def effective_rate(self):
        return self._effective_rate

    @effective_rate.setter
    def effective_rate(self, effective_rate):
        self._effective_rate = effective_rate
