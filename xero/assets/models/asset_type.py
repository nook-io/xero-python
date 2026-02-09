from xero.models import BaseModel


class AssetType(BaseModel):
    openapi_types = {
        "asset_type_id": "str",
        "asset_type_name": "str",
        "fixed_asset_account_id": "str",
        "depreciation_expense_account_id": "str",
        "accumulated_depreciation_account_id": "str",
        "book_depreciation_setting": "BookDepreciationSetting",
        "locks": "int",
    }
    attribute_map = {
        "asset_type_id": "assetTypeId",
        "asset_type_name": "assetTypeName",
        "fixed_asset_account_id": "fixedAssetAccountId",
        "depreciation_expense_account_id": "depreciationExpenseAccountId",
        "accumulated_depreciation_account_id": "accumulatedDepreciationAccountId",
        "book_depreciation_setting": "bookDepreciationSetting",
        "locks": "locks",
    }

    def __init__(
        self,
        asset_type_id=None,
        asset_type_name=None,
        fixed_asset_account_id=None,
        depreciation_expense_account_id=None,
        accumulated_depreciation_account_id=None,
        book_depreciation_setting=None,
        locks=None,
    ):
        self._asset_type_id = None
        self._asset_type_name = None
        self._fixed_asset_account_id = None
        self._depreciation_expense_account_id = None
        self._accumulated_depreciation_account_id = None
        self._book_depreciation_setting = None
        self._locks = None
        self.discriminator = None
        if asset_type_id is not None:
            self.asset_type_id = asset_type_id
        self.asset_type_name = asset_type_name
        if fixed_asset_account_id is not None:
            self.fixed_asset_account_id = fixed_asset_account_id
        if depreciation_expense_account_id is not None:
            self.depreciation_expense_account_id = depreciation_expense_account_id
        if accumulated_depreciation_account_id is not None:
            self.accumulated_depreciation_account_id = (
                accumulated_depreciation_account_id
            )
        self.book_depreciation_setting = book_depreciation_setting
        if locks is not None:
            self.locks = locks

    @property
    def asset_type_id(self):
        return self._asset_type_id

    @asset_type_id.setter
    def asset_type_id(self, asset_type_id):
        self._asset_type_id = asset_type_id

    @property
    def asset_type_name(self):
        return self._asset_type_name

    @asset_type_name.setter
    def asset_type_name(self, asset_type_name):
        if asset_type_name is None:
            raise ValueError("Invalid value for `asset_type_name`, must not be `None`")
        self._asset_type_name = asset_type_name

    @property
    def fixed_asset_account_id(self):
        return self._fixed_asset_account_id

    @fixed_asset_account_id.setter
    def fixed_asset_account_id(self, fixed_asset_account_id):
        self._fixed_asset_account_id = fixed_asset_account_id

    @property
    def depreciation_expense_account_id(self):
        return self._depreciation_expense_account_id

    @depreciation_expense_account_id.setter
    def depreciation_expense_account_id(self, depreciation_expense_account_id):
        self._depreciation_expense_account_id = depreciation_expense_account_id

    @property
    def accumulated_depreciation_account_id(self):
        return self._accumulated_depreciation_account_id

    @accumulated_depreciation_account_id.setter
    def accumulated_depreciation_account_id(self, accumulated_depreciation_account_id):
        self._accumulated_depreciation_account_id = accumulated_depreciation_account_id

    @property
    def book_depreciation_setting(self):
        return self._book_depreciation_setting

    @book_depreciation_setting.setter
    def book_depreciation_setting(self, book_depreciation_setting):
        if book_depreciation_setting is None:
            raise ValueError(
                "Invalid value for `book_depreciation_setting`, must not be `None`"
            )
        self._book_depreciation_setting = book_depreciation_setting

    @property
    def locks(self):
        return self._locks

    @locks.setter
    def locks(self, locks):
        self._locks = locks
