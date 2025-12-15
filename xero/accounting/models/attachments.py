from xero.models import BaseModel


class Attachments(BaseModel):
    openapi_types = {"attachments": "list[Attachment]"}
    attribute_map = {"attachments": "Attachments"}

    def __init__(self, attachments=None):
        self._attachments = None
        self.discriminator = None
        if attachments is not None:
            self.attachments = attachments

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        self._attachments = attachments
