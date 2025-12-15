from xero.models import BaseModel


class EmployeeWorkingPattern(BaseModel):
    openapi_types = {"payee_working_pattern_id": "str", "effective_from": "date"}
    attribute_map = {
        "payee_working_pattern_id": "payeeWorkingPatternID",
        "effective_from": "effectiveFrom",
    }

    def __init__(self, payee_working_pattern_id=None, effective_from=None):
        self._payee_working_pattern_id = None
        self._effective_from = None
        self.discriminator = None
        self.payee_working_pattern_id = payee_working_pattern_id
        self.effective_from = effective_from

    @property
    def payee_working_pattern_id(self):
        return self._payee_working_pattern_id

    @payee_working_pattern_id.setter
    def payee_working_pattern_id(self, payee_working_pattern_id):
        if payee_working_pattern_id is None:
            raise ValueError(
                "Invalid value for `payee_working_pattern_id`, must not be `None`"
            )
        self._payee_working_pattern_id = payee_working_pattern_id

    @property
    def effective_from(self):
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        if effective_from is None:
            raise ValueError("Invalid value for `effective_from`, must not be `None`")
        self._effective_from = effective_from
