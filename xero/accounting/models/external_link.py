from xero.models import BaseModel


class ExternalLink(BaseModel):
    openapi_types = {"link_type": "str", "url": "str", "description": "str"}
    attribute_map = {
        "link_type": "LinkType",
        "url": "Url",
        "description": "Description",
    }

    def __init__(self, link_type=None, url=None, description=None):
        self._link_type = None
        self._url = None
        self._description = None
        self.discriminator = None
        if link_type is not None:
            self.link_type = link_type
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description

    @property
    def link_type(self):
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        allowed_values = [
            "Facebook",
            "GooglePlus",
            "LinkedIn",
            "Twitter",
            "Website",
            "None",
        ]
        if link_type:
            if link_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `link_type` ({0}), must be one of {1}".format(
                        link_type, allowed_values
                    )
                )
        self._link_type = link_type

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description
