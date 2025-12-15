from xero.models import BaseModel


class EmployeeTax(BaseModel):
    openapi_types = {
        "starter_type": "str",
        "starter_declaration": "str",
        "tax_code": "str",
        "w1_m1": "bool",
        "previous_taxable_pay": "float",
        "previous_tax_paid": "float",
        "student_loan_deduction": "str",
        "has_post_graduate_loans": "bool",
        "is_director": "bool",
        "directorship_start_date": "date",
        "nic_calculation_method": "str",
    }
    attribute_map = {
        "starter_type": "starterType",
        "starter_declaration": "starterDeclaration",
        "tax_code": "taxCode",
        "w1_m1": "w1M1",
        "previous_taxable_pay": "previousTaxablePay",
        "previous_tax_paid": "previousTaxPaid",
        "student_loan_deduction": "studentLoanDeduction",
        "has_post_graduate_loans": "hasPostGraduateLoans",
        "is_director": "isDirector",
        "directorship_start_date": "directorshipStartDate",
        "nic_calculation_method": "nicCalculationMethod",
    }

    def __init__(
        self,
        starter_type=None,
        starter_declaration=None,
        tax_code=None,
        w1_m1=None,
        previous_taxable_pay=None,
        previous_tax_paid=None,
        student_loan_deduction=None,
        has_post_graduate_loans=None,
        is_director=None,
        directorship_start_date=None,
        nic_calculation_method=None,
    ):
        self._starter_type = None
        self._starter_declaration = None
        self._tax_code = None
        self._w1_m1 = None
        self._previous_taxable_pay = None
        self._previous_tax_paid = None
        self._student_loan_deduction = None
        self._has_post_graduate_loans = None
        self._is_director = None
        self._directorship_start_date = None
        self._nic_calculation_method = None
        self.discriminator = None
        if starter_type is not None:
            self.starter_type = starter_type
        if starter_declaration is not None:
            self.starter_declaration = starter_declaration
        if tax_code is not None:
            self.tax_code = tax_code
        if w1_m1 is not None:
            self.w1_m1 = w1_m1
        if previous_taxable_pay is not None:
            self.previous_taxable_pay = previous_taxable_pay
        if previous_tax_paid is not None:
            self.previous_tax_paid = previous_tax_paid
        if student_loan_deduction is not None:
            self.student_loan_deduction = student_loan_deduction
        if has_post_graduate_loans is not None:
            self.has_post_graduate_loans = has_post_graduate_loans
        if is_director is not None:
            self.is_director = is_director
        if directorship_start_date is not None:
            self.directorship_start_date = directorship_start_date
        if nic_calculation_method is not None:
            self.nic_calculation_method = nic_calculation_method

    @property
    def starter_type(self):
        return self._starter_type

    @starter_type.setter
    def starter_type(self, starter_type):
        self._starter_type = starter_type

    @property
    def starter_declaration(self):
        return self._starter_declaration

    @starter_declaration.setter
    def starter_declaration(self, starter_declaration):
        self._starter_declaration = starter_declaration

    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, tax_code):
        self._tax_code = tax_code

    @property
    def w1_m1(self):
        return self._w1_m1

    @w1_m1.setter
    def w1_m1(self, w1_m1):
        self._w1_m1 = w1_m1

    @property
    def previous_taxable_pay(self):
        return self._previous_taxable_pay

    @previous_taxable_pay.setter
    def previous_taxable_pay(self, previous_taxable_pay):
        self._previous_taxable_pay = previous_taxable_pay

    @property
    def previous_tax_paid(self):
        return self._previous_tax_paid

    @previous_tax_paid.setter
    def previous_tax_paid(self, previous_tax_paid):
        self._previous_tax_paid = previous_tax_paid

    @property
    def student_loan_deduction(self):
        return self._student_loan_deduction

    @student_loan_deduction.setter
    def student_loan_deduction(self, student_loan_deduction):
        self._student_loan_deduction = student_loan_deduction

    @property
    def has_post_graduate_loans(self):
        return self._has_post_graduate_loans

    @has_post_graduate_loans.setter
    def has_post_graduate_loans(self, has_post_graduate_loans):
        self._has_post_graduate_loans = has_post_graduate_loans

    @property
    def is_director(self):
        return self._is_director

    @is_director.setter
    def is_director(self, is_director):
        self._is_director = is_director

    @property
    def directorship_start_date(self):
        return self._directorship_start_date

    @directorship_start_date.setter
    def directorship_start_date(self, directorship_start_date):
        self._directorship_start_date = directorship_start_date

    @property
    def nic_calculation_method(self):
        return self._nic_calculation_method

    @nic_calculation_method.setter
    def nic_calculation_method(self, nic_calculation_method):
        self._nic_calculation_method = nic_calculation_method
