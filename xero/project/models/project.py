from xero.models import BaseModel


class Project(BaseModel):
    openapi_types = {
        "project_id": "str",
        "contact_id": "str",
        "name": "str",
        "currency_code": "CurrencyCode",
        "minutes_logged": "int",
        "total_task_amount": "Amount",
        "total_expense_amount": "Amount",
        "estimate_amount": "Amount",
        "minutes_to_be_invoiced": "int",
        "task_amount_to_be_invoiced": "Amount",
        "task_amount_invoiced": "Amount",
        "expense_amount_to_be_invoiced": "Amount",
        "expense_amount_invoiced": "Amount",
        "project_amount_invoiced": "Amount",
        "deposit": "Amount",
        "deposit_applied": "Amount",
        "credit_note_amount": "Amount",
        "deadline_utc": "datetime",
        "total_invoiced": "Amount",
        "total_to_be_invoiced": "Amount",
        "estimate": "Amount",
        "status": "ProjectStatus",
    }
    attribute_map = {
        "project_id": "projectId",
        "contact_id": "contactId",
        "name": "name",
        "currency_code": "currencyCode",
        "minutes_logged": "minutesLogged",
        "total_task_amount": "totalTaskAmount",
        "total_expense_amount": "totalExpenseAmount",
        "estimate_amount": "estimateAmount",
        "minutes_to_be_invoiced": "minutesToBeInvoiced",
        "task_amount_to_be_invoiced": "taskAmountToBeInvoiced",
        "task_amount_invoiced": "taskAmountInvoiced",
        "expense_amount_to_be_invoiced": "expenseAmountToBeInvoiced",
        "expense_amount_invoiced": "expenseAmountInvoiced",
        "project_amount_invoiced": "projectAmountInvoiced",
        "deposit": "deposit",
        "deposit_applied": "depositApplied",
        "credit_note_amount": "creditNoteAmount",
        "deadline_utc": "deadlineUtc",
        "total_invoiced": "totalInvoiced",
        "total_to_be_invoiced": "totalToBeInvoiced",
        "estimate": "estimate",
        "status": "status",
    }

    def __init__(
        self,
        project_id=None,
        contact_id=None,
        name=None,
        currency_code=None,
        minutes_logged=None,
        total_task_amount=None,
        total_expense_amount=None,
        estimate_amount=None,
        minutes_to_be_invoiced=None,
        task_amount_to_be_invoiced=None,
        task_amount_invoiced=None,
        expense_amount_to_be_invoiced=None,
        expense_amount_invoiced=None,
        project_amount_invoiced=None,
        deposit=None,
        deposit_applied=None,
        credit_note_amount=None,
        deadline_utc=None,
        total_invoiced=None,
        total_to_be_invoiced=None,
        estimate=None,
        status=None,
    ):
        self._project_id = None
        self._contact_id = None
        self._name = None
        self._currency_code = None
        self._minutes_logged = None
        self._total_task_amount = None
        self._total_expense_amount = None
        self._estimate_amount = None
        self._minutes_to_be_invoiced = None
        self._task_amount_to_be_invoiced = None
        self._task_amount_invoiced = None
        self._expense_amount_to_be_invoiced = None
        self._expense_amount_invoiced = None
        self._project_amount_invoiced = None
        self._deposit = None
        self._deposit_applied = None
        self._credit_note_amount = None
        self._deadline_utc = None
        self._total_invoiced = None
        self._total_to_be_invoiced = None
        self._estimate = None
        self._status = None
        self.discriminator = None
        if project_id is not None:
            self.project_id = project_id
        if contact_id is not None:
            self.contact_id = contact_id
        self.name = name
        if currency_code is not None:
            self.currency_code = currency_code
        if minutes_logged is not None:
            self.minutes_logged = minutes_logged
        if total_task_amount is not None:
            self.total_task_amount = total_task_amount
        if total_expense_amount is not None:
            self.total_expense_amount = total_expense_amount
        if estimate_amount is not None:
            self.estimate_amount = estimate_amount
        if minutes_to_be_invoiced is not None:
            self.minutes_to_be_invoiced = minutes_to_be_invoiced
        if task_amount_to_be_invoiced is not None:
            self.task_amount_to_be_invoiced = task_amount_to_be_invoiced
        if task_amount_invoiced is not None:
            self.task_amount_invoiced = task_amount_invoiced
        if expense_amount_to_be_invoiced is not None:
            self.expense_amount_to_be_invoiced = expense_amount_to_be_invoiced
        if expense_amount_invoiced is not None:
            self.expense_amount_invoiced = expense_amount_invoiced
        if project_amount_invoiced is not None:
            self.project_amount_invoiced = project_amount_invoiced
        if deposit is not None:
            self.deposit = deposit
        if deposit_applied is not None:
            self.deposit_applied = deposit_applied
        if credit_note_amount is not None:
            self.credit_note_amount = credit_note_amount
        if deadline_utc is not None:
            self.deadline_utc = deadline_utc
        if total_invoiced is not None:
            self.total_invoiced = total_invoiced
        if total_to_be_invoiced is not None:
            self.total_to_be_invoiced = total_to_be_invoiced
        if estimate is not None:
            self.estimate = estimate
        if status is not None:
            self.status = status

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        self._project_id = project_id

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
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        self._currency_code = currency_code

    @property
    def minutes_logged(self):
        return self._minutes_logged

    @minutes_logged.setter
    def minutes_logged(self, minutes_logged):
        self._minutes_logged = minutes_logged

    @property
    def total_task_amount(self):
        return self._total_task_amount

    @total_task_amount.setter
    def total_task_amount(self, total_task_amount):
        self._total_task_amount = total_task_amount

    @property
    def total_expense_amount(self):
        return self._total_expense_amount

    @total_expense_amount.setter
    def total_expense_amount(self, total_expense_amount):
        self._total_expense_amount = total_expense_amount

    @property
    def estimate_amount(self):
        return self._estimate_amount

    @estimate_amount.setter
    def estimate_amount(self, estimate_amount):
        self._estimate_amount = estimate_amount

    @property
    def minutes_to_be_invoiced(self):
        return self._minutes_to_be_invoiced

    @minutes_to_be_invoiced.setter
    def minutes_to_be_invoiced(self, minutes_to_be_invoiced):
        self._minutes_to_be_invoiced = minutes_to_be_invoiced

    @property
    def task_amount_to_be_invoiced(self):
        return self._task_amount_to_be_invoiced

    @task_amount_to_be_invoiced.setter
    def task_amount_to_be_invoiced(self, task_amount_to_be_invoiced):
        self._task_amount_to_be_invoiced = task_amount_to_be_invoiced

    @property
    def task_amount_invoiced(self):
        return self._task_amount_invoiced

    @task_amount_invoiced.setter
    def task_amount_invoiced(self, task_amount_invoiced):
        self._task_amount_invoiced = task_amount_invoiced

    @property
    def expense_amount_to_be_invoiced(self):
        return self._expense_amount_to_be_invoiced

    @expense_amount_to_be_invoiced.setter
    def expense_amount_to_be_invoiced(self, expense_amount_to_be_invoiced):
        self._expense_amount_to_be_invoiced = expense_amount_to_be_invoiced

    @property
    def expense_amount_invoiced(self):
        return self._expense_amount_invoiced

    @expense_amount_invoiced.setter
    def expense_amount_invoiced(self, expense_amount_invoiced):
        self._expense_amount_invoiced = expense_amount_invoiced

    @property
    def project_amount_invoiced(self):
        return self._project_amount_invoiced

    @project_amount_invoiced.setter
    def project_amount_invoiced(self, project_amount_invoiced):
        self._project_amount_invoiced = project_amount_invoiced

    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, deposit):
        self._deposit = deposit

    @property
    def deposit_applied(self):
        return self._deposit_applied

    @deposit_applied.setter
    def deposit_applied(self, deposit_applied):
        self._deposit_applied = deposit_applied

    @property
    def credit_note_amount(self):
        return self._credit_note_amount

    @credit_note_amount.setter
    def credit_note_amount(self, credit_note_amount):
        self._credit_note_amount = credit_note_amount

    @property
    def deadline_utc(self):
        return self._deadline_utc

    @deadline_utc.setter
    def deadline_utc(self, deadline_utc):
        self._deadline_utc = deadline_utc

    @property
    def total_invoiced(self):
        return self._total_invoiced

    @total_invoiced.setter
    def total_invoiced(self, total_invoiced):
        self._total_invoiced = total_invoiced

    @property
    def total_to_be_invoiced(self):
        return self._total_to_be_invoiced

    @total_to_be_invoiced.setter
    def total_to_be_invoiced(self, total_to_be_invoiced):
        self._total_to_be_invoiced = total_to_be_invoiced

    @property
    def estimate(self):
        return self._estimate

    @estimate.setter
    def estimate(self, estimate):
        self._estimate = estimate

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
