from xero.models import BaseModel


class TaxLine(BaseModel):
    openapi_types = {
        "payslip_tax_line_id": "str",
        "amount": "float",
        "tax_type_name": "str",
        "description": "str",
        "manual_tax_type": "ManualTaxType",
        "liability_account": "str",
    }
    attribute_map = {
        "payslip_tax_line_id": "PayslipTaxLineID",
        "amount": "Amount",
        "tax_type_name": "TaxTypeName",
        "description": "Description",
        "manual_tax_type": "ManualTaxType",
        "liability_account": "LiabilityAccount",
    }

    def __init__(
        self,
        payslip_tax_line_id=None,
        amount=None,
        tax_type_name=None,
        description=None,
        manual_tax_type=None,
        liability_account=None,
    ):
        self._payslip_tax_line_id = None
        self._amount = None
        self._tax_type_name = None
        self._description = None
        self._manual_tax_type = None
        self._liability_account = None
        self.discriminator = None
        if payslip_tax_line_id is not None:
            self.payslip_tax_line_id = payslip_tax_line_id
        if amount is not None:
            self.amount = amount
        if tax_type_name is not None:
            self.tax_type_name = tax_type_name
        if description is not None:
            self.description = description
        if manual_tax_type is not None:
            self.manual_tax_type = manual_tax_type
        if liability_account is not None:
            self.liability_account = liability_account

    @property
    def payslip_tax_line_id(self):
        return self._payslip_tax_line_id

    @payslip_tax_line_id.setter
    def payslip_tax_line_id(self, payslip_tax_line_id):
        self._payslip_tax_line_id = payslip_tax_line_id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def tax_type_name(self):
        return self._tax_type_name

    @tax_type_name.setter
    def tax_type_name(self, tax_type_name):
        self._tax_type_name = tax_type_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def manual_tax_type(self):
        return self._manual_tax_type

    @manual_tax_type.setter
    def manual_tax_type(self, manual_tax_type):
        self._manual_tax_type = manual_tax_type

    @property
    def liability_account(self):
        return self._liability_account

    @liability_account.setter
    def liability_account(self, liability_account):
        self._liability_account = liability_account
