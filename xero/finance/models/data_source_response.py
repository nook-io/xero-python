from xero.models import BaseModel


class DataSourceResponse(BaseModel):
    openapi_types = {
        "direct_bank_feed": "float",
        "indirect_bank_feed": "float",
        "file_upload": "float",
        "manual": "float",
        "direct_bank_feed_pos": "float",
        "indirect_bank_feed_pos": "float",
        "file_upload_pos": "float",
        "manual_pos": "float",
        "direct_bank_feed_neg": "float",
        "indirect_bank_feed_neg": "float",
        "file_upload_neg": "float",
        "manual_neg": "float",
        "other_pos": "float",
        "other_neg": "float",
        "other": "float",
    }
    attribute_map = {
        "direct_bank_feed": "directBankFeed",
        "indirect_bank_feed": "indirectBankFeed",
        "file_upload": "fileUpload",
        "manual": "manual",
        "direct_bank_feed_pos": "directBankFeedPos",
        "indirect_bank_feed_pos": "indirectBankFeedPos",
        "file_upload_pos": "fileUploadPos",
        "manual_pos": "manualPos",
        "direct_bank_feed_neg": "directBankFeedNeg",
        "indirect_bank_feed_neg": "indirectBankFeedNeg",
        "file_upload_neg": "fileUploadNeg",
        "manual_neg": "manualNeg",
        "other_pos": "otherPos",
        "other_neg": "otherNeg",
        "other": "other",
    }

    def __init__(
        self,
        direct_bank_feed=None,
        indirect_bank_feed=None,
        file_upload=None,
        manual=None,
        direct_bank_feed_pos=None,
        indirect_bank_feed_pos=None,
        file_upload_pos=None,
        manual_pos=None,
        direct_bank_feed_neg=None,
        indirect_bank_feed_neg=None,
        file_upload_neg=None,
        manual_neg=None,
        other_pos=None,
        other_neg=None,
        other=None,
    ):
        self._direct_bank_feed = None
        self._indirect_bank_feed = None
        self._file_upload = None
        self._manual = None
        self._direct_bank_feed_pos = None
        self._indirect_bank_feed_pos = None
        self._file_upload_pos = None
        self._manual_pos = None
        self._direct_bank_feed_neg = None
        self._indirect_bank_feed_neg = None
        self._file_upload_neg = None
        self._manual_neg = None
        self._other_pos = None
        self._other_neg = None
        self._other = None
        self.discriminator = None
        if direct_bank_feed is not None:
            self.direct_bank_feed = direct_bank_feed
        if indirect_bank_feed is not None:
            self.indirect_bank_feed = indirect_bank_feed
        if file_upload is not None:
            self.file_upload = file_upload
        if manual is not None:
            self.manual = manual
        if direct_bank_feed_pos is not None:
            self.direct_bank_feed_pos = direct_bank_feed_pos
        if indirect_bank_feed_pos is not None:
            self.indirect_bank_feed_pos = indirect_bank_feed_pos
        if file_upload_pos is not None:
            self.file_upload_pos = file_upload_pos
        if manual_pos is not None:
            self.manual_pos = manual_pos
        if direct_bank_feed_neg is not None:
            self.direct_bank_feed_neg = direct_bank_feed_neg
        if indirect_bank_feed_neg is not None:
            self.indirect_bank_feed_neg = indirect_bank_feed_neg
        if file_upload_neg is not None:
            self.file_upload_neg = file_upload_neg
        if manual_neg is not None:
            self.manual_neg = manual_neg
        if other_pos is not None:
            self.other_pos = other_pos
        if other_neg is not None:
            self.other_neg = other_neg
        if other is not None:
            self.other = other

    @property
    def direct_bank_feed(self):
        return self._direct_bank_feed

    @direct_bank_feed.setter
    def direct_bank_feed(self, direct_bank_feed):
        self._direct_bank_feed = direct_bank_feed

    @property
    def indirect_bank_feed(self):
        return self._indirect_bank_feed

    @indirect_bank_feed.setter
    def indirect_bank_feed(self, indirect_bank_feed):
        self._indirect_bank_feed = indirect_bank_feed

    @property
    def file_upload(self):
        return self._file_upload

    @file_upload.setter
    def file_upload(self, file_upload):
        self._file_upload = file_upload

    @property
    def manual(self):
        return self._manual

    @manual.setter
    def manual(self, manual):
        self._manual = manual

    @property
    def direct_bank_feed_pos(self):
        return self._direct_bank_feed_pos

    @direct_bank_feed_pos.setter
    def direct_bank_feed_pos(self, direct_bank_feed_pos):
        self._direct_bank_feed_pos = direct_bank_feed_pos

    @property
    def indirect_bank_feed_pos(self):
        return self._indirect_bank_feed_pos

    @indirect_bank_feed_pos.setter
    def indirect_bank_feed_pos(self, indirect_bank_feed_pos):
        self._indirect_bank_feed_pos = indirect_bank_feed_pos

    @property
    def file_upload_pos(self):
        return self._file_upload_pos

    @file_upload_pos.setter
    def file_upload_pos(self, file_upload_pos):
        self._file_upload_pos = file_upload_pos

    @property
    def manual_pos(self):
        return self._manual_pos

    @manual_pos.setter
    def manual_pos(self, manual_pos):
        self._manual_pos = manual_pos

    @property
    def direct_bank_feed_neg(self):
        return self._direct_bank_feed_neg

    @direct_bank_feed_neg.setter
    def direct_bank_feed_neg(self, direct_bank_feed_neg):
        self._direct_bank_feed_neg = direct_bank_feed_neg

    @property
    def indirect_bank_feed_neg(self):
        return self._indirect_bank_feed_neg

    @indirect_bank_feed_neg.setter
    def indirect_bank_feed_neg(self, indirect_bank_feed_neg):
        self._indirect_bank_feed_neg = indirect_bank_feed_neg

    @property
    def file_upload_neg(self):
        return self._file_upload_neg

    @file_upload_neg.setter
    def file_upload_neg(self, file_upload_neg):
        self._file_upload_neg = file_upload_neg

    @property
    def manual_neg(self):
        return self._manual_neg

    @manual_neg.setter
    def manual_neg(self, manual_neg):
        self._manual_neg = manual_neg

    @property
    def other_pos(self):
        return self._other_pos

    @other_pos.setter
    def other_pos(self, other_pos):
        self._other_pos = other_pos

    @property
    def other_neg(self):
        return self._other_neg

    @other_neg.setter
    def other_neg(self, other_neg):
        self._other_neg = other_neg

    @property
    def other(self):
        return self._other

    @other.setter
    def other(self, other):
        self._other = other
