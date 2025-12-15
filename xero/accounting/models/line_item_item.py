from xero.models import BaseModel


class LineItemItem(BaseModel):
    openapi_types = {"code": "str", "name": "str", "item_id": "str"}
    attribute_map = {"code": "Code", "name": "Name", "item_id": "ItemID"}

    def __init__(self, code=None, name=None, item_id=None):
        self._code = None
        self._name = None
        self._item_id = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if item_id is not None:
            self.item_id = item_id

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if code is not None and len(code) > 30:
            raise ValueError(
                "Invalid value for `code`, length must be less than or equal to `30`"
            )
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None and len(name) > 50:
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `50`"
            )
        self._name = name

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        self._item_id = item_id
