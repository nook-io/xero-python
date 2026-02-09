from xero.models import BaseModel


class BrandingTheme(BaseModel):
    openapi_types = {
        "branding_theme_id": "str",
        "name": "str",
        "logo_url": "str",
        "type": "str",
        "sort_order": "int",
        "created_date_utc": "datetime[ms-format]",
    }
    attribute_map = {
        "branding_theme_id": "BrandingThemeID",
        "name": "Name",
        "logo_url": "LogoUrl",
        "type": "Type",
        "sort_order": "SortOrder",
        "created_date_utc": "CreatedDateUTC",
    }

    def __init__(
        self,
        branding_theme_id=None,
        name=None,
        logo_url=None,
        type=None,
        sort_order=None,
        created_date_utc=None,
    ):
        self._branding_theme_id = None
        self._name = None
        self._logo_url = None
        self._type = None
        self._sort_order = None
        self._created_date_utc = None
        self.discriminator = None
        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if name is not None:
            self.name = name
        if logo_url is not None:
            self.logo_url = logo_url
        if type is not None:
            self.type = type
        if sort_order is not None:
            self.sort_order = sort_order
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc

    @property
    def branding_theme_id(self):
        return self._branding_theme_id

    @branding_theme_id.setter
    def branding_theme_id(self, branding_theme_id):
        self._branding_theme_id = branding_theme_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        self._logo_url = logo_url

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_values = ["INVOICE", "None"]
        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(
                        type, allowed_values
                    )
                )
        self._type = type

    @property
    def sort_order(self):
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        self._sort_order = sort_order

    @property
    def created_date_utc(self):
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        self._created_date_utc = created_date_utc
