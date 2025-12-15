from xero.models import BaseModel


class BrandingThemes(BaseModel):
    openapi_types = {"branding_themes": "list[BrandingTheme]"}
    attribute_map = {"branding_themes": "BrandingThemes"}

    def __init__(self, branding_themes=None):
        self._branding_themes = None
        self.discriminator = None
        if branding_themes is not None:
            self.branding_themes = branding_themes

    @property
    def branding_themes(self):
        return self._branding_themes

    @branding_themes.setter
    def branding_themes(self, branding_themes):
        self._branding_themes = branding_themes
