from xero.models import BaseModel


class Asset(BaseModel):
    openapi_types = {
        "asset_id": "str",
        "asset_name": "str",
        "asset_type_id": "str",
        "asset_number": "str",
        "purchase_date": "date",
        "purchase_price": "float",
        "disposal_date": "date",
        "disposal_price": "float",
        "asset_status": "AssetStatus",
        "warranty_expiry_date": "str",
        "serial_number": "str",
        "book_depreciation_setting": "BookDepreciationSetting",
        "book_depreciation_detail": "BookDepreciationDetail",
        "can_rollback": "bool",
        "accounting_book_value": "float",
        "is_delete_enabled_for_date": "bool",
    }
    attribute_map = {
        "asset_id": "assetId",
        "asset_name": "assetName",
        "asset_type_id": "assetTypeId",
        "asset_number": "assetNumber",
        "purchase_date": "purchaseDate",
        "purchase_price": "purchasePrice",
        "disposal_date": "disposalDate",
        "disposal_price": "disposalPrice",
        "asset_status": "assetStatus",
        "warranty_expiry_date": "warrantyExpiryDate",
        "serial_number": "serialNumber",
        "book_depreciation_setting": "bookDepreciationSetting",
        "book_depreciation_detail": "bookDepreciationDetail",
        "can_rollback": "canRollback",
        "accounting_book_value": "accountingBookValue",
        "is_delete_enabled_for_date": "isDeleteEnabledForDate",
    }

    def __init__(
        self,
        asset_id=None,
        asset_name=None,
        asset_type_id=None,
        asset_number=None,
        purchase_date=None,
        purchase_price=None,
        disposal_date=None,
        disposal_price=None,
        asset_status=None,
        warranty_expiry_date=None,
        serial_number=None,
        book_depreciation_setting=None,
        book_depreciation_detail=None,
        can_rollback=None,
        accounting_book_value=None,
        is_delete_enabled_for_date=None,
    ):
        self._asset_id = None
        self._asset_name = None
        self._asset_type_id = None
        self._asset_number = None
        self._purchase_date = None
        self._purchase_price = None
        self._disposal_date = None
        self._disposal_price = None
        self._asset_status = None
        self._warranty_expiry_date = None
        self._serial_number = None
        self._book_depreciation_setting = None
        self._book_depreciation_detail = None
        self._can_rollback = None
        self._accounting_book_value = None
        self._is_delete_enabled_for_date = None
        self.discriminator = None
        if asset_id is not None:
            self.asset_id = asset_id
        self.asset_name = asset_name
        if asset_type_id is not None:
            self.asset_type_id = asset_type_id
        if asset_number is not None:
            self.asset_number = asset_number
        if purchase_date is not None:
            self.purchase_date = purchase_date
        if purchase_price is not None:
            self.purchase_price = purchase_price
        if disposal_date is not None:
            self.disposal_date = disposal_date
        if disposal_price is not None:
            self.disposal_price = disposal_price
        if asset_status is not None:
            self.asset_status = asset_status
        if warranty_expiry_date is not None:
            self.warranty_expiry_date = warranty_expiry_date
        if serial_number is not None:
            self.serial_number = serial_number
        if book_depreciation_setting is not None:
            self.book_depreciation_setting = book_depreciation_setting
        if book_depreciation_detail is not None:
            self.book_depreciation_detail = book_depreciation_detail
        if can_rollback is not None:
            self.can_rollback = can_rollback
        if accounting_book_value is not None:
            self.accounting_book_value = accounting_book_value
        if is_delete_enabled_for_date is not None:
            self.is_delete_enabled_for_date = is_delete_enabled_for_date

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        self._asset_id = asset_id

    @property
    def asset_name(self):
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        if asset_name is None:
            raise ValueError("Invalid value for `asset_name`, must not be `None`")
        self._asset_name = asset_name

    @property
    def asset_type_id(self):
        return self._asset_type_id

    @asset_type_id.setter
    def asset_type_id(self, asset_type_id):
        self._asset_type_id = asset_type_id

    @property
    def asset_number(self):
        return self._asset_number

    @asset_number.setter
    def asset_number(self, asset_number):
        self._asset_number = asset_number

    @property
    def purchase_date(self):
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, purchase_date):
        self._purchase_date = purchase_date

    @property
    def purchase_price(self):
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price):
        self._purchase_price = purchase_price

    @property
    def disposal_date(self):
        return self._disposal_date

    @disposal_date.setter
    def disposal_date(self, disposal_date):
        self._disposal_date = disposal_date

    @property
    def disposal_price(self):
        return self._disposal_price

    @disposal_price.setter
    def disposal_price(self, disposal_price):
        self._disposal_price = disposal_price

    @property
    def asset_status(self):
        return self._asset_status

    @asset_status.setter
    def asset_status(self, asset_status):
        self._asset_status = asset_status

    @property
    def warranty_expiry_date(self):
        return self._warranty_expiry_date

    @warranty_expiry_date.setter
    def warranty_expiry_date(self, warranty_expiry_date):
        self._warranty_expiry_date = warranty_expiry_date

    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        self._serial_number = serial_number

    @property
    def book_depreciation_setting(self):
        return self._book_depreciation_setting

    @book_depreciation_setting.setter
    def book_depreciation_setting(self, book_depreciation_setting):
        self._book_depreciation_setting = book_depreciation_setting

    @property
    def book_depreciation_detail(self):
        return self._book_depreciation_detail

    @book_depreciation_detail.setter
    def book_depreciation_detail(self, book_depreciation_detail):
        self._book_depreciation_detail = book_depreciation_detail

    @property
    def can_rollback(self):
        return self._can_rollback

    @can_rollback.setter
    def can_rollback(self, can_rollback):
        self._can_rollback = can_rollback

    @property
    def accounting_book_value(self):
        return self._accounting_book_value

    @accounting_book_value.setter
    def accounting_book_value(self, accounting_book_value):
        self._accounting_book_value = accounting_book_value

    @property
    def is_delete_enabled_for_date(self):
        return self._is_delete_enabled_for_date

    @is_delete_enabled_for_date.setter
    def is_delete_enabled_for_date(self, is_delete_enabled_for_date):
        self._is_delete_enabled_for_date = is_delete_enabled_for_date
