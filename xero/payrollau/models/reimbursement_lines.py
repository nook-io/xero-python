from xero.models import BaseModel


class ReimbursementLines(BaseModel):
    openapi_types = {"reimbursement_lines": "list[ReimbursementLine]"}
    attribute_map = {"reimbursement_lines": "ReimbursementLines"}

    def __init__(self, reimbursement_lines=None):
        self._reimbursement_lines = None
        self.discriminator = None
        if reimbursement_lines is not None:
            self.reimbursement_lines = reimbursement_lines

    @property
    def reimbursement_lines(self):
        return self._reimbursement_lines

    @reimbursement_lines.setter
    def reimbursement_lines(self, reimbursement_lines):
        self._reimbursement_lines = reimbursement_lines
