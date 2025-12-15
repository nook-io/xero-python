from xero.models import BaseModel


class EmployeeTax(BaseModel):
    openapi_types = {
        "ird_number": "str",
        "tax_code": "TaxCode",
        "special_tax_rate_percentage": "float",
        "has_special_student_loan_rate": "bool",
        "special_student_loan_rate_percentage": "float",
        "is_eligible_for_kiwi_saver": "bool",
        "esct_rate_percentage": "float",
        "kiwi_saver_contributions": "str",
        "kiwi_saver_employee_contribution_rate_percentage": "float",
        "kiwi_saver_employer_contribution_rate_percentage": "float",
        "kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage": "float",
        "kiwi_saver_opt_out_date": "date",
        "kiwi_saver_contribution_holiday_end_date": "date",
        "has_student_loan_balance": "bool",
        "student_loan_balance": "float",
        "student_loan_as_at": "date",
    }
    attribute_map = {
        "ird_number": "irdNumber",
        "tax_code": "taxCode",
        "special_tax_rate_percentage": "specialTaxRatePercentage",
        "has_special_student_loan_rate": "hasSpecialStudentLoanRate",
        "special_student_loan_rate_percentage": "specialStudentLoanRatePercentage",
        "is_eligible_for_kiwi_saver": "isEligibleForKiwiSaver",
        "esct_rate_percentage": "esctRatePercentage",
        "kiwi_saver_contributions": "kiwiSaverContributions",
        "kiwi_saver_employee_contribution_rate_percentage": "kiwiSaverEmployeeContributionRatePercentage",
        "kiwi_saver_employer_contribution_rate_percentage": "kiwiSaverEmployerContributionRatePercentage",
        "kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage": "kiwiSaverEmployerSalarySacrificeContributionRatePercentage",
        "kiwi_saver_opt_out_date": "kiwiSaverOptOutDate",
        "kiwi_saver_contribution_holiday_end_date": "kiwiSaverContributionHolidayEndDate",
        "has_student_loan_balance": "hasStudentLoanBalance",
        "student_loan_balance": "studentLoanBalance",
        "student_loan_as_at": "studentLoanAsAt",
    }

    def __init__(
        self,
        ird_number=None,
        tax_code=None,
        special_tax_rate_percentage=None,
        has_special_student_loan_rate=None,
        special_student_loan_rate_percentage=None,
        is_eligible_for_kiwi_saver=None,
        esct_rate_percentage=None,
        kiwi_saver_contributions=None,
        kiwi_saver_employee_contribution_rate_percentage=None,
        kiwi_saver_employer_contribution_rate_percentage=None,
        kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage=None,
        kiwi_saver_opt_out_date=None,
        kiwi_saver_contribution_holiday_end_date=None,
        has_student_loan_balance=None,
        student_loan_balance=None,
        student_loan_as_at=None,
    ):
        self._ird_number = None
        self._tax_code = None
        self._special_tax_rate_percentage = None
        self._has_special_student_loan_rate = None
        self._special_student_loan_rate_percentage = None
        self._is_eligible_for_kiwi_saver = None
        self._esct_rate_percentage = None
        self._kiwi_saver_contributions = None
        self._kiwi_saver_employee_contribution_rate_percentage = None
        self._kiwi_saver_employer_contribution_rate_percentage = None
        self._kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage = None
        self._kiwi_saver_opt_out_date = None
        self._kiwi_saver_contribution_holiday_end_date = None
        self._has_student_loan_balance = None
        self._student_loan_balance = None
        self._student_loan_as_at = None
        self.discriminator = None
        if ird_number is not None:
            self.ird_number = ird_number
        if tax_code is not None:
            self.tax_code = tax_code
        if special_tax_rate_percentage is not None:
            self.special_tax_rate_percentage = special_tax_rate_percentage
        if has_special_student_loan_rate is not None:
            self.has_special_student_loan_rate = has_special_student_loan_rate
        if special_student_loan_rate_percentage is not None:
            self.special_student_loan_rate_percentage = (
                special_student_loan_rate_percentage
            )
        if is_eligible_for_kiwi_saver is not None:
            self.is_eligible_for_kiwi_saver = is_eligible_for_kiwi_saver
        if esct_rate_percentage is not None:
            self.esct_rate_percentage = esct_rate_percentage
        if kiwi_saver_contributions is not None:
            self.kiwi_saver_contributions = kiwi_saver_contributions
        if kiwi_saver_employee_contribution_rate_percentage is not None:
            self.kiwi_saver_employee_contribution_rate_percentage = (
                kiwi_saver_employee_contribution_rate_percentage
            )
        if kiwi_saver_employer_contribution_rate_percentage is not None:
            self.kiwi_saver_employer_contribution_rate_percentage = (
                kiwi_saver_employer_contribution_rate_percentage
            )
        if (
            kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage
            is not None
        ):
            self.kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage = (
                kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage
            )
        if kiwi_saver_opt_out_date is not None:
            self.kiwi_saver_opt_out_date = kiwi_saver_opt_out_date
        if kiwi_saver_contribution_holiday_end_date is not None:
            self.kiwi_saver_contribution_holiday_end_date = (
                kiwi_saver_contribution_holiday_end_date
            )
        if has_student_loan_balance is not None:
            self.has_student_loan_balance = has_student_loan_balance
        if student_loan_balance is not None:
            self.student_loan_balance = student_loan_balance
        if student_loan_as_at is not None:
            self.student_loan_as_at = student_loan_as_at

    @property
    def ird_number(self):
        return self._ird_number

    @ird_number.setter
    def ird_number(self, ird_number):
        self._ird_number = ird_number

    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, tax_code):
        self._tax_code = tax_code

    @property
    def special_tax_rate_percentage(self):
        return self._special_tax_rate_percentage

    @special_tax_rate_percentage.setter
    def special_tax_rate_percentage(self, special_tax_rate_percentage):
        self._special_tax_rate_percentage = special_tax_rate_percentage

    @property
    def has_special_student_loan_rate(self):
        return self._has_special_student_loan_rate

    @has_special_student_loan_rate.setter
    def has_special_student_loan_rate(self, has_special_student_loan_rate):
        self._has_special_student_loan_rate = has_special_student_loan_rate

    @property
    def special_student_loan_rate_percentage(self):
        return self._special_student_loan_rate_percentage

    @special_student_loan_rate_percentage.setter
    def special_student_loan_rate_percentage(
        self, special_student_loan_rate_percentage
    ):
        self._special_student_loan_rate_percentage = (
            special_student_loan_rate_percentage
        )

    @property
    def is_eligible_for_kiwi_saver(self):
        return self._is_eligible_for_kiwi_saver

    @is_eligible_for_kiwi_saver.setter
    def is_eligible_for_kiwi_saver(self, is_eligible_for_kiwi_saver):
        self._is_eligible_for_kiwi_saver = is_eligible_for_kiwi_saver

    @property
    def esct_rate_percentage(self):
        return self._esct_rate_percentage

    @esct_rate_percentage.setter
    def esct_rate_percentage(self, esct_rate_percentage):
        self._esct_rate_percentage = esct_rate_percentage

    @property
    def kiwi_saver_contributions(self):
        return self._kiwi_saver_contributions

    @kiwi_saver_contributions.setter
    def kiwi_saver_contributions(self, kiwi_saver_contributions):
        allowed_values = [
            "MakeContributions",
            "OptOut",
            "OnAContributionsHoliday",
            "OnASavingsSuspension",
            "NotCurrentlyAKiwiSaverMember",
            "None",
        ]
        if kiwi_saver_contributions:
            if kiwi_saver_contributions not in allowed_values:
                raise ValueError(
                    "Invalid value for `kiwi_saver_contributions` ({0}), must be one of {1}".format(
                        kiwi_saver_contributions, allowed_values
                    )
                )
        self._kiwi_saver_contributions = kiwi_saver_contributions

    @property
    def kiwi_saver_employee_contribution_rate_percentage(self):
        return self._kiwi_saver_employee_contribution_rate_percentage

    @kiwi_saver_employee_contribution_rate_percentage.setter
    def kiwi_saver_employee_contribution_rate_percentage(
        self, kiwi_saver_employee_contribution_rate_percentage
    ):
        self._kiwi_saver_employee_contribution_rate_percentage = (
            kiwi_saver_employee_contribution_rate_percentage
        )

    @property
    def kiwi_saver_employer_contribution_rate_percentage(self):
        return self._kiwi_saver_employer_contribution_rate_percentage

    @kiwi_saver_employer_contribution_rate_percentage.setter
    def kiwi_saver_employer_contribution_rate_percentage(
        self, kiwi_saver_employer_contribution_rate_percentage
    ):
        self._kiwi_saver_employer_contribution_rate_percentage = (
            kiwi_saver_employer_contribution_rate_percentage
        )

    @property
    def kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage(self):
        return self._kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage

    @kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage.setter
    def kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage(
        self, kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage
    ):
        self._kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage = (
            kiwi_saver_employer_salary_sacrifice_contribution_rate_percentage
        )

    @property
    def kiwi_saver_opt_out_date(self):
        return self._kiwi_saver_opt_out_date

    @kiwi_saver_opt_out_date.setter
    def kiwi_saver_opt_out_date(self, kiwi_saver_opt_out_date):
        self._kiwi_saver_opt_out_date = kiwi_saver_opt_out_date

    @property
    def kiwi_saver_contribution_holiday_end_date(self):
        return self._kiwi_saver_contribution_holiday_end_date

    @kiwi_saver_contribution_holiday_end_date.setter
    def kiwi_saver_contribution_holiday_end_date(
        self, kiwi_saver_contribution_holiday_end_date
    ):
        self._kiwi_saver_contribution_holiday_end_date = (
            kiwi_saver_contribution_holiday_end_date
        )

    @property
    def has_student_loan_balance(self):
        return self._has_student_loan_balance

    @has_student_loan_balance.setter
    def has_student_loan_balance(self, has_student_loan_balance):
        self._has_student_loan_balance = has_student_loan_balance

    @property
    def student_loan_balance(self):
        return self._student_loan_balance

    @student_loan_balance.setter
    def student_loan_balance(self, student_loan_balance):
        self._student_loan_balance = student_loan_balance

    @property
    def student_loan_as_at(self):
        return self._student_loan_as_at

    @student_loan_as_at.setter
    def student_loan_as_at(self, student_loan_as_at):
        self._student_loan_as_at = student_loan_as_at
