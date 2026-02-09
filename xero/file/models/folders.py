from xero.models import BaseModel


class Folders(BaseModel):
    openapi_types = {"folders": "list[Folder]"}
    attribute_map = {"folders": "Folders"}

    def __init__(self, folders=None):
        self._folders = None
        self.discriminator = None
        if folders is not None:
            self.folders = folders

    @property
    def folders(self):
        return self._folders

    @folders.setter
    def folders(self, folders):
        self._folders = folders
