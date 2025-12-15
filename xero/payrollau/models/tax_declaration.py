from xero.models import BaseModel


class TaxDeclaration(BaseModel):
    openapi_types = {
        "employee_id": "str",
        "employment_basis": "EmploymentBasis",
        "tfn_exemption_type": "TFNExemptionType",
        "tax_file_number": "str",
        "abn": "str",
        "australian_resident_for_tax_purposes": "bool",
        "residency_status": "ResidencyStatus",
        "tax_scale_type": "TaxScaleType",
        "work_condition": "WorkCondition",
        "senior_marital_status": "SeniorMaritalStatus",
        "tax_free_threshold_claimed": "bool",
        "tax_offset_estimated_amount": "float",
        "has_help_debt": "bool",
        "has_sfss_debt": "bool",
        "has_trade_support_loan_debt": "bool",
        "upward_variation_tax_withholding_amount": "float",
        "eligible_to_receive_leave_loading": "bool",
        "approved_withholding_variation_percentage": "float",
        "has_student_startup_loan": "bool",
        "has_loan_or_student_debt": "bool",
        "updated_date_utc": "datetime[ms-format]",
    }
    attribute_map = {
        "employee_id": "EmployeeID",
        "employment_basis": "EmploymentBasis",
        "tfn_exemption_type": "TFNExemptionType",
        "tax_file_number": "TaxFileNumber",
        "abn": "ABN",
        "australian_resident_for_tax_purposes": "AustralianResidentForTaxPurposes",
        "residency_status": "ResidencyStatus",
        "tax_scale_type": "TaxScaleType",
        "work_condition": "WorkCondition",
        "senior_marital_status": "SeniorMaritalStatus",
        "tax_free_threshold_claimed": "TaxFreeThresholdClaimed",
        "tax_offset_estimated_amount": "TaxOffsetEstimatedAmount",
        "has_help_debt": "HasHELPDebt",
        "has_sfss_debt": "HasSFSSDebt",
        "has_trade_support_loan_debt": "HasTradeSupportLoanDebt",
        "upward_variation_tax_withholding_amount": "UpwardVariationTaxWithholdingAmount",
        "eligible_to_receive_leave_loading": "EligibleToReceiveLeaveLoading",
        "approved_withholding_variation_percentage": "ApprovedWithholdingVariationPercentage",
        "has_student_startup_loan": "HasStudentStartupLoan",
        "has_loan_or_student_debt": "HasLoanOrStudentDebt",
        "updated_date_utc": "UpdatedDateUTC",
    }

    def __init__(
        self,
        employee_id=None,
        employment_basis=None,
        tfn_exemption_type=None,
        tax_file_number=None,
        abn=None,
        australian_resident_for_tax_purposes=None,
        residency_status=None,
        tax_scale_type=None,
        work_condition=None,
        senior_marital_status=None,
        tax_free_threshold_claimed=None,
        tax_offset_estimated_amount=None,
        has_help_debt=None,
        has_sfss_debt=None,
        has_trade_support_loan_debt=None,
        upward_variation_tax_withholding_amount=None,
        eligible_to_receive_leave_loading=None,
        approved_withholding_variation_percentage=None,
        has_student_startup_loan=None,
        has_loan_or_student_debt=None,
        updated_date_utc=None,
    ):
        self._employee_id = None
        self._employment_basis = None
        self._tfn_exemption_type = None
        self._tax_file_number = None
        self._abn = None
        self._australian_resident_for_tax_purposes = None
        self._residency_status = None
        self._tax_scale_type = None
        self._work_condition = None
        self._senior_marital_status = None
        self._tax_free_threshold_claimed = None
        self._tax_offset_estimated_amount = None
        self._has_help_debt = None
        self._has_sfss_debt = None
        self._has_trade_support_loan_debt = None
        self._upward_variation_tax_withholding_amount = None
        self._eligible_to_receive_leave_loading = None
        self._approved_withholding_variation_percentage = None
        self._has_student_startup_loan = None
        self._has_loan_or_student_debt = None
        self._updated_date_utc = None
        self.discriminator = None
        if employee_id is not None:
            self.employee_id = employee_id
        if employment_basis is not None:
            self.employment_basis = employment_basis
        if tfn_exemption_type is not None:
            self.tfn_exemption_type = tfn_exemption_type
        if tax_file_number is not None:
            self.tax_file_number = tax_file_number
        if abn is not None:
            self.abn = abn
        if australian_resident_for_tax_purposes is not None:
            self.australian_resident_for_tax_purposes = (
                australian_resident_for_tax_purposes
            )
        if residency_status is not None:
            self.residency_status = residency_status
        if tax_scale_type is not None:
            self.tax_scale_type = tax_scale_type
        if work_condition is not None:
            self.work_condition = work_condition
        if senior_marital_status is not None:
            self.senior_marital_status = senior_marital_status
        if tax_free_threshold_claimed is not None:
            self.tax_free_threshold_claimed = tax_free_threshold_claimed
        if tax_offset_estimated_amount is not None:
            self.tax_offset_estimated_amount = tax_offset_estimated_amount
        if has_help_debt is not None:
            self.has_help_debt = has_help_debt
        if has_sfss_debt is not None:
            self.has_sfss_debt = has_sfss_debt
        if has_trade_support_loan_debt is not None:
            self.has_trade_support_loan_debt = has_trade_support_loan_debt
        if upward_variation_tax_withholding_amount is not None:
            self.upward_variation_tax_withholding_amount = (
                upward_variation_tax_withholding_amount
            )
        if eligible_to_receive_leave_loading is not None:
            self.eligible_to_receive_leave_loading = eligible_to_receive_leave_loading
        if approved_withholding_variation_percentage is not None:
            self.approved_withholding_variation_percentage = (
                approved_withholding_variation_percentage
            )
        if has_student_startup_loan is not None:
            self.has_student_startup_loan = has_student_startup_loan
        if has_loan_or_student_debt is not None:
            self.has_loan_or_student_debt = has_loan_or_student_debt
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def employment_basis(self):
        return self._employment_basis

    @employment_basis.setter
    def employment_basis(self, employment_basis):
        self._employment_basis = employment_basis

    @property
    def tfn_exemption_type(self):
        return self._tfn_exemption_type

    @tfn_exemption_type.setter
    def tfn_exemption_type(self, tfn_exemption_type):
        self._tfn_exemption_type = tfn_exemption_type

    @property
    def tax_file_number(self):
        return self._tax_file_number

    @tax_file_number.setter
    def tax_file_number(self, tax_file_number):
        self._tax_file_number = tax_file_number

    @property
    def abn(self):
        return self._abn

    @abn.setter
    def abn(self, abn):
        self._abn = abn

    @property
    def australian_resident_for_tax_purposes(self):
        return self._australian_resident_for_tax_purposes

    @australian_resident_for_tax_purposes.setter
    def australian_resident_for_tax_purposes(
        self, australian_resident_for_tax_purposes
    ):
        self._australian_resident_for_tax_purposes = (
            australian_resident_for_tax_purposes
        )

    @property
    def residency_status(self):
        return self._residency_status

    @residency_status.setter
    def residency_status(self, residency_status):
        self._residency_status = residency_status

    @property
    def tax_scale_type(self):
        return self._tax_scale_type

    @tax_scale_type.setter
    def tax_scale_type(self, tax_scale_type):
        self._tax_scale_type = tax_scale_type

    @property
    def work_condition(self):
        return self._work_condition

    @work_condition.setter
    def work_condition(self, work_condition):
        self._work_condition = work_condition

    @property
    def senior_marital_status(self):
        return self._senior_marital_status

    @senior_marital_status.setter
    def senior_marital_status(self, senior_marital_status):
        self._senior_marital_status = senior_marital_status

    @property
    def tax_free_threshold_claimed(self):
        return self._tax_free_threshold_claimed

    @tax_free_threshold_claimed.setter
    def tax_free_threshold_claimed(self, tax_free_threshold_claimed):
        self._tax_free_threshold_claimed = tax_free_threshold_claimed

    @property
    def tax_offset_estimated_amount(self):
        return self._tax_offset_estimated_amount

    @tax_offset_estimated_amount.setter
    def tax_offset_estimated_amount(self, tax_offset_estimated_amount):
        self._tax_offset_estimated_amount = tax_offset_estimated_amount

    @property
    def has_help_debt(self):
        return self._has_help_debt

    @has_help_debt.setter
    def has_help_debt(self, has_help_debt):
        self._has_help_debt = has_help_debt

    @property
    def has_sfss_debt(self):
        return self._has_sfss_debt

    @has_sfss_debt.setter
    def has_sfss_debt(self, has_sfss_debt):
        self._has_sfss_debt = has_sfss_debt

    @property
    def has_trade_support_loan_debt(self):
        return self._has_trade_support_loan_debt

    @has_trade_support_loan_debt.setter
    def has_trade_support_loan_debt(self, has_trade_support_loan_debt):
        self._has_trade_support_loan_debt = has_trade_support_loan_debt

    @property
    def upward_variation_tax_withholding_amount(self):
        return self._upward_variation_tax_withholding_amount

    @upward_variation_tax_withholding_amount.setter
    def upward_variation_tax_withholding_amount(
        self, upward_variation_tax_withholding_amount
    ):
        self._upward_variation_tax_withholding_amount = (
            upward_variation_tax_withholding_amount
        )

    @property
    def eligible_to_receive_leave_loading(self):
        return self._eligible_to_receive_leave_loading

    @eligible_to_receive_leave_loading.setter
    def eligible_to_receive_leave_loading(self, eligible_to_receive_leave_loading):
        self._eligible_to_receive_leave_loading = eligible_to_receive_leave_loading

    @property
    def approved_withholding_variation_percentage(self):
        return self._approved_withholding_variation_percentage

    @approved_withholding_variation_percentage.setter
    def approved_withholding_variation_percentage(
        self, approved_withholding_variation_percentage
    ):
        self._approved_withholding_variation_percentage = (
            approved_withholding_variation_percentage
        )

    @property
    def has_student_startup_loan(self):
        return self._has_student_startup_loan

    @has_student_startup_loan.setter
    def has_student_startup_loan(self, has_student_startup_loan):
        self._has_student_startup_loan = has_student_startup_loan

    @property
    def has_loan_or_student_debt(self):
        return self._has_loan_or_student_debt

    @has_loan_or_student_debt.setter
    def has_loan_or_student_debt(self, has_loan_or_student_debt):
        self._has_loan_or_student_debt = has_loan_or_student_debt

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc
