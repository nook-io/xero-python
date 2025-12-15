from xero.models import BaseModel


class BookDepreciationDetail(BaseModel):
    openapi_types = {
        "current_capital_gain": "float",
        "current_gain_loss": "float",
        "depreciation_start_date": "date",
        "cost_limit": "float",
        "residual_value": "float",
        "prior_accum_depreciation_amount": "float",
        "current_accum_depreciation_amount": "float",
    }
    attribute_map = {
        "current_capital_gain": "currentCapitalGain",
        "current_gain_loss": "currentGainLoss",
        "depreciation_start_date": "depreciationStartDate",
        "cost_limit": "costLimit",
        "residual_value": "residualValue",
        "prior_accum_depreciation_amount": "priorAccumDepreciationAmount",
        "current_accum_depreciation_amount": "currentAccumDepreciationAmount",
    }

    def __init__(
        self,
        current_capital_gain=None,
        current_gain_loss=None,
        depreciation_start_date=None,
        cost_limit=None,
        residual_value=None,
        prior_accum_depreciation_amount=None,
        current_accum_depreciation_amount=None,
    ):
        self._current_capital_gain = None
        self._current_gain_loss = None
        self._depreciation_start_date = None
        self._cost_limit = None
        self._residual_value = None
        self._prior_accum_depreciation_amount = None
        self._current_accum_depreciation_amount = None
        self.discriminator = None
        if current_capital_gain is not None:
            self.current_capital_gain = current_capital_gain
        if current_gain_loss is not None:
            self.current_gain_loss = current_gain_loss
        if depreciation_start_date is not None:
            self.depreciation_start_date = depreciation_start_date
        if cost_limit is not None:
            self.cost_limit = cost_limit
        if residual_value is not None:
            self.residual_value = residual_value
        if prior_accum_depreciation_amount is not None:
            self.prior_accum_depreciation_amount = prior_accum_depreciation_amount
        if current_accum_depreciation_amount is not None:
            self.current_accum_depreciation_amount = current_accum_depreciation_amount

    @property
    def current_capital_gain(self):
        return self._current_capital_gain

    @current_capital_gain.setter
    def current_capital_gain(self, current_capital_gain):
        self._current_capital_gain = current_capital_gain

    @property
    def current_gain_loss(self):
        return self._current_gain_loss

    @current_gain_loss.setter
    def current_gain_loss(self, current_gain_loss):
        self._current_gain_loss = current_gain_loss

    @property
    def depreciation_start_date(self):
        return self._depreciation_start_date

    @depreciation_start_date.setter
    def depreciation_start_date(self, depreciation_start_date):
        self._depreciation_start_date = depreciation_start_date

    @property
    def cost_limit(self):
        return self._cost_limit

    @cost_limit.setter
    def cost_limit(self, cost_limit):
        self._cost_limit = cost_limit

    @property
    def residual_value(self):
        return self._residual_value

    @residual_value.setter
    def residual_value(self, residual_value):
        self._residual_value = residual_value

    @property
    def prior_accum_depreciation_amount(self):
        return self._prior_accum_depreciation_amount

    @prior_accum_depreciation_amount.setter
    def prior_accum_depreciation_amount(self, prior_accum_depreciation_amount):
        self._prior_accum_depreciation_amount = prior_accum_depreciation_amount

    @property
    def current_accum_depreciation_amount(self):
        return self._current_accum_depreciation_amount

    @current_accum_depreciation_amount.setter
    def current_accum_depreciation_amount(self, current_accum_depreciation_amount):
        self._current_accum_depreciation_amount = current_accum_depreciation_amount
