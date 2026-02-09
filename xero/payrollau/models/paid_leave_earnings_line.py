from xero.models import BaseModel


class PaidLeaveEarningsLine(BaseModel):
    openapi_types = {
        "leave_type_id": "str",
        "amount": "float",
        "sgc_applied_leave_loading_amount": "float",
        "sgc_exempted_leave_loading_amount": "float",
        "reset_stp_categorisation": "bool",
    }
    attribute_map = {
        "leave_type_id": "LeaveTypeID",
        "amount": "Amount",
        "sgc_applied_leave_loading_amount": "SGCAppliedLeaveLoadingAmount",
        "sgc_exempted_leave_loading_amount": "SGCExemptedLeaveLoadingAmount",
        "reset_stp_categorisation": "ResetSTPCategorisation",
    }

    def __init__(
        self,
        leave_type_id=None,
        amount=None,
        sgc_applied_leave_loading_amount=None,
        sgc_exempted_leave_loading_amount=None,
        reset_stp_categorisation=None,
    ):
        self._leave_type_id = None
        self._amount = None
        self._sgc_applied_leave_loading_amount = None
        self._sgc_exempted_leave_loading_amount = None
        self._reset_stp_categorisation = None
        self.discriminator = None
        self.leave_type_id = leave_type_id
        self.amount = amount
        if sgc_applied_leave_loading_amount is not None:
            self.sgc_applied_leave_loading_amount = sgc_applied_leave_loading_amount
        if sgc_exempted_leave_loading_amount is not None:
            self.sgc_exempted_leave_loading_amount = sgc_exempted_leave_loading_amount
        if reset_stp_categorisation is not None:
            self.reset_stp_categorisation = reset_stp_categorisation

    @property
    def leave_type_id(self):
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        if leave_type_id is None:
            raise ValueError("Invalid value for `leave_type_id`, must not be `None`")
        self._leave_type_id = leave_type_id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")
        self._amount = amount

    @property
    def sgc_applied_leave_loading_amount(self):
        return self._sgc_applied_leave_loading_amount

    @sgc_applied_leave_loading_amount.setter
    def sgc_applied_leave_loading_amount(self, sgc_applied_leave_loading_amount):
        self._sgc_applied_leave_loading_amount = sgc_applied_leave_loading_amount

    @property
    def sgc_exempted_leave_loading_amount(self):
        return self._sgc_exempted_leave_loading_amount

    @sgc_exempted_leave_loading_amount.setter
    def sgc_exempted_leave_loading_amount(self, sgc_exempted_leave_loading_amount):
        self._sgc_exempted_leave_loading_amount = sgc_exempted_leave_loading_amount

    @property
    def reset_stp_categorisation(self):
        return self._reset_stp_categorisation

    @reset_stp_categorisation.setter
    def reset_stp_categorisation(self, reset_stp_categorisation):
        self._reset_stp_categorisation = reset_stp_categorisation
