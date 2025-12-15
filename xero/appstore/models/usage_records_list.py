from xero.models import BaseModel


class UsageRecordsList(BaseModel):
    openapi_types = {"usage_records": "list[UsageRecord]"}
    attribute_map = {"usage_records": "usageRecords"}

    def __init__(self, usage_records=None):
        self._usage_records = None
        self.discriminator = None
        self.usage_records = usage_records

    @property
    def usage_records(self):
        return self._usage_records

    @usage_records.setter
    def usage_records(self, usage_records):
        if usage_records is None:
            raise ValueError("Invalid value for `usage_records`, must not be `None`")
        self._usage_records = usage_records
