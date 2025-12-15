from xero.models import BaseModel


class Setting(BaseModel):
    openapi_types = {
        "asset_number_prefix": "str",
        "asset_number_sequence": "str",
        "asset_start_date": "date",
        "last_depreciation_date": "date",
        "default_gain_on_disposal_account_id": "str",
        "default_loss_on_disposal_account_id": "str",
        "default_capital_gain_on_disposal_account_id": "str",
        "opt_in_for_tax": "bool",
    }
    attribute_map = {
        "asset_number_prefix": "assetNumberPrefix",
        "asset_number_sequence": "assetNumberSequence",
        "asset_start_date": "assetStartDate",
        "last_depreciation_date": "lastDepreciationDate",
        "default_gain_on_disposal_account_id": "defaultGainOnDisposalAccountId",
        "default_loss_on_disposal_account_id": "defaultLossOnDisposalAccountId",
        "default_capital_gain_on_disposal_account_id": "defaultCapitalGainOnDisposalAccountId",
        "opt_in_for_tax": "optInForTax",
    }

    def __init__(
        self,
        asset_number_prefix=None,
        asset_number_sequence=None,
        asset_start_date=None,
        last_depreciation_date=None,
        default_gain_on_disposal_account_id=None,
        default_loss_on_disposal_account_id=None,
        default_capital_gain_on_disposal_account_id=None,
        opt_in_for_tax=None,
    ):
        self._asset_number_prefix = None
        self._asset_number_sequence = None
        self._asset_start_date = None
        self._last_depreciation_date = None
        self._default_gain_on_disposal_account_id = None
        self._default_loss_on_disposal_account_id = None
        self._default_capital_gain_on_disposal_account_id = None
        self._opt_in_for_tax = None
        self.discriminator = None
        if asset_number_prefix is not None:
            self.asset_number_prefix = asset_number_prefix
        if asset_number_sequence is not None:
            self.asset_number_sequence = asset_number_sequence
        if asset_start_date is not None:
            self.asset_start_date = asset_start_date
        if last_depreciation_date is not None:
            self.last_depreciation_date = last_depreciation_date
        if default_gain_on_disposal_account_id is not None:
            self.default_gain_on_disposal_account_id = (
                default_gain_on_disposal_account_id
            )
        if default_loss_on_disposal_account_id is not None:
            self.default_loss_on_disposal_account_id = (
                default_loss_on_disposal_account_id
            )
        if default_capital_gain_on_disposal_account_id is not None:
            self.default_capital_gain_on_disposal_account_id = (
                default_capital_gain_on_disposal_account_id
            )
        if opt_in_for_tax is not None:
            self.opt_in_for_tax = opt_in_for_tax

    @property
    def asset_number_prefix(self):
        return self._asset_number_prefix

    @asset_number_prefix.setter
    def asset_number_prefix(self, asset_number_prefix):
        self._asset_number_prefix = asset_number_prefix

    @property
    def asset_number_sequence(self):
        return self._asset_number_sequence

    @asset_number_sequence.setter
    def asset_number_sequence(self, asset_number_sequence):
        self._asset_number_sequence = asset_number_sequence

    @property
    def asset_start_date(self):
        return self._asset_start_date

    @asset_start_date.setter
    def asset_start_date(self, asset_start_date):
        self._asset_start_date = asset_start_date

    @property
    def last_depreciation_date(self):
        return self._last_depreciation_date

    @last_depreciation_date.setter
    def last_depreciation_date(self, last_depreciation_date):
        self._last_depreciation_date = last_depreciation_date

    @property
    def default_gain_on_disposal_account_id(self):
        return self._default_gain_on_disposal_account_id

    @default_gain_on_disposal_account_id.setter
    def default_gain_on_disposal_account_id(self, default_gain_on_disposal_account_id):
        self._default_gain_on_disposal_account_id = default_gain_on_disposal_account_id

    @property
    def default_loss_on_disposal_account_id(self):
        return self._default_loss_on_disposal_account_id

    @default_loss_on_disposal_account_id.setter
    def default_loss_on_disposal_account_id(self, default_loss_on_disposal_account_id):
        self._default_loss_on_disposal_account_id = default_loss_on_disposal_account_id

    @property
    def default_capital_gain_on_disposal_account_id(self):
        return self._default_capital_gain_on_disposal_account_id

    @default_capital_gain_on_disposal_account_id.setter
    def default_capital_gain_on_disposal_account_id(
        self, default_capital_gain_on_disposal_account_id
    ):
        self._default_capital_gain_on_disposal_account_id = (
            default_capital_gain_on_disposal_account_id
        )

    @property
    def opt_in_for_tax(self):
        return self._opt_in_for_tax

    @opt_in_for_tax.setter
    def opt_in_for_tax(self, opt_in_for_tax):
        self._opt_in_for_tax = opt_in_for_tax
