from xero.models import BaseModel


class SuperannuationLine(BaseModel):
    openapi_types = {
        "super_membership_id": "str",
        "contribution_type": "SuperannuationContributionType",
        "calculation_type": "SuperannuationCalculationType",
        "minimum_monthly_earnings": "float",
        "expense_account_code": "str",
        "liability_account_code": "str",
        "payment_date_for_this_period": "date[ms-format]",
        "percentage": "float",
        "amount": "float",
    }
    attribute_map = {
        "super_membership_id": "SuperMembershipID",
        "contribution_type": "ContributionType",
        "calculation_type": "CalculationType",
        "minimum_monthly_earnings": "MinimumMonthlyEarnings",
        "expense_account_code": "ExpenseAccountCode",
        "liability_account_code": "LiabilityAccountCode",
        "payment_date_for_this_period": "PaymentDateForThisPeriod",
        "percentage": "Percentage",
        "amount": "Amount",
    }

    def __init__(
        self,
        super_membership_id=None,
        contribution_type=None,
        calculation_type=None,
        minimum_monthly_earnings=None,
        expense_account_code=None,
        liability_account_code=None,
        payment_date_for_this_period=None,
        percentage=None,
        amount=None,
    ):
        self._super_membership_id = None
        self._contribution_type = None
        self._calculation_type = None
        self._minimum_monthly_earnings = None
        self._expense_account_code = None
        self._liability_account_code = None
        self._payment_date_for_this_period = None
        self._percentage = None
        self._amount = None
        self.discriminator = None
        if super_membership_id is not None:
            self.super_membership_id = super_membership_id
        if contribution_type is not None:
            self.contribution_type = contribution_type
        if calculation_type is not None:
            self.calculation_type = calculation_type
        if minimum_monthly_earnings is not None:
            self.minimum_monthly_earnings = minimum_monthly_earnings
        if expense_account_code is not None:
            self.expense_account_code = expense_account_code
        if liability_account_code is not None:
            self.liability_account_code = liability_account_code
        if payment_date_for_this_period is not None:
            self.payment_date_for_this_period = payment_date_for_this_period
        if percentage is not None:
            self.percentage = percentage
        if amount is not None:
            self.amount = amount

    @property
    def super_membership_id(self):
        return self._super_membership_id

    @super_membership_id.setter
    def super_membership_id(self, super_membership_id):
        self._super_membership_id = super_membership_id

    @property
    def contribution_type(self):
        return self._contribution_type

    @contribution_type.setter
    def contribution_type(self, contribution_type):
        self._contribution_type = contribution_type

    @property
    def calculation_type(self):
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        self._calculation_type = calculation_type

    @property
    def minimum_monthly_earnings(self):
        return self._minimum_monthly_earnings

    @minimum_monthly_earnings.setter
    def minimum_monthly_earnings(self, minimum_monthly_earnings):
        self._minimum_monthly_earnings = minimum_monthly_earnings

    @property
    def expense_account_code(self):
        return self._expense_account_code

    @expense_account_code.setter
    def expense_account_code(self, expense_account_code):
        self._expense_account_code = expense_account_code

    @property
    def liability_account_code(self):
        return self._liability_account_code

    @liability_account_code.setter
    def liability_account_code(self, liability_account_code):
        self._liability_account_code = liability_account_code

    @property
    def payment_date_for_this_period(self):
        return self._payment_date_for_this_period

    @payment_date_for_this_period.setter
    def payment_date_for_this_period(self, payment_date_for_this_period):
        self._payment_date_for_this_period = payment_date_for_this_period

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        self._percentage = percentage

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount
