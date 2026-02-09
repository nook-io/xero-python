from xero.models import BaseModel


class HistoryRecords(BaseModel):
    openapi_types = {"history_records": "list[HistoryRecord]"}
    attribute_map = {"history_records": "HistoryRecords"}

    def __init__(self, history_records=None):
        self._history_records = None
        self.discriminator = None
        if history_records is not None:
            self.history_records = history_records

    @property
    def history_records(self):
        return self._history_records

    @history_records.setter
    def history_records(self, history_records):
        self._history_records = history_records
