from xero.models import BaseModel


class ExpenseClaim(BaseModel):
    openapi_types = {
        "expense_claim_id": "str",
        "status": "str",
        "payments": "list[Payment]",
        "user": "User",
        "receipts": "list[Receipt]",
        "updated_date_utc": "datetime[ms-format]",
        "total": "float",
        "amount_due": "float",
        "amount_paid": "float",
        "payment_due_date": "date[ms-format]",
        "reporting_date": "date[ms-format]",
        "receipt_id": "str",
    }
    attribute_map = {
        "expense_claim_id": "ExpenseClaimID",
        "status": "Status",
        "payments": "Payments",
        "user": "User",
        "receipts": "Receipts",
        "updated_date_utc": "UpdatedDateUTC",
        "total": "Total",
        "amount_due": "AmountDue",
        "amount_paid": "AmountPaid",
        "payment_due_date": "PaymentDueDate",
        "reporting_date": "ReportingDate",
        "receipt_id": "ReceiptID",
    }

    def __init__(
        self,
        expense_claim_id=None,
        status=None,
        payments=None,
        user=None,
        receipts=None,
        updated_date_utc=None,
        total=None,
        amount_due=None,
        amount_paid=None,
        payment_due_date=None,
        reporting_date=None,
        receipt_id=None,
    ):
        self._expense_claim_id = None
        self._status = None
        self._payments = None
        self._user = None
        self._receipts = None
        self._updated_date_utc = None
        self._total = None
        self._amount_due = None
        self._amount_paid = None
        self._payment_due_date = None
        self._reporting_date = None
        self._receipt_id = None
        self.discriminator = None
        if expense_claim_id is not None:
            self.expense_claim_id = expense_claim_id
        if status is not None:
            self.status = status
        if payments is not None:
            self.payments = payments
        if user is not None:
            self.user = user
        if receipts is not None:
            self.receipts = receipts
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if total is not None:
            self.total = total
        if amount_due is not None:
            self.amount_due = amount_due
        if amount_paid is not None:
            self.amount_paid = amount_paid
        if payment_due_date is not None:
            self.payment_due_date = payment_due_date
        if reporting_date is not None:
            self.reporting_date = reporting_date
        if receipt_id is not None:
            self.receipt_id = receipt_id

    @property
    def expense_claim_id(self):
        return self._expense_claim_id

    @expense_claim_id.setter
    def expense_claim_id(self, expense_claim_id):
        self._expense_claim_id = expense_claim_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = [
            "SUBMITTED",
            "AUTHORISED",
            "PAID",
            "VOIDED",
            "DELETED",
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
    def payments(self):
        return self._payments

    @payments.setter
    def payments(self, payments):
        self._payments = payments

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def receipts(self):
        return self._receipts

    @receipts.setter
    def receipts(self, receipts):
        self._receipts = receipts

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def amount_due(self):
        return self._amount_due

    @amount_due.setter
    def amount_due(self, amount_due):
        self._amount_due = amount_due

    @property
    def amount_paid(self):
        return self._amount_paid

    @amount_paid.setter
    def amount_paid(self, amount_paid):
        self._amount_paid = amount_paid

    @property
    def payment_due_date(self):
        return self._payment_due_date

    @payment_due_date.setter
    def payment_due_date(self, payment_due_date):
        self._payment_due_date = payment_due_date

    @property
    def reporting_date(self):
        return self._reporting_date

    @reporting_date.setter
    def reporting_date(self, reporting_date):
        self._reporting_date = reporting_date

    @property
    def receipt_id(self):
        return self._receipt_id

    @receipt_id.setter
    def receipt_id(self, receipt_id):
        self._receipt_id = receipt_id
