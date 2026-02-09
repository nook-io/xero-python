from xero.models import BaseModel


class LinkedTransaction(BaseModel):
    openapi_types = {
        "source_transaction_id": "str",
        "source_line_item_id": "str",
        "contact_id": "str",
        "target_transaction_id": "str",
        "target_line_item_id": "str",
        "linked_transaction_id": "str",
        "status": "str",
        "type": "str",
        "updated_date_utc": "datetime[ms-format]",
        "source_transaction_type_code": "str",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "source_transaction_id": "SourceTransactionID",
        "source_line_item_id": "SourceLineItemID",
        "contact_id": "ContactID",
        "target_transaction_id": "TargetTransactionID",
        "target_line_item_id": "TargetLineItemID",
        "linked_transaction_id": "LinkedTransactionID",
        "status": "Status",
        "type": "Type",
        "updated_date_utc": "UpdatedDateUTC",
        "source_transaction_type_code": "SourceTransactionTypeCode",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        source_transaction_id=None,
        source_line_item_id=None,
        contact_id=None,
        target_transaction_id=None,
        target_line_item_id=None,
        linked_transaction_id=None,
        status=None,
        type=None,
        updated_date_utc=None,
        source_transaction_type_code=None,
        validation_errors=None,
    ):
        self._source_transaction_id = None
        self._source_line_item_id = None
        self._contact_id = None
        self._target_transaction_id = None
        self._target_line_item_id = None
        self._linked_transaction_id = None
        self._status = None
        self._type = None
        self._updated_date_utc = None
        self._source_transaction_type_code = None
        self._validation_errors = None
        self.discriminator = None
        if source_transaction_id is not None:
            self.source_transaction_id = source_transaction_id
        if source_line_item_id is not None:
            self.source_line_item_id = source_line_item_id
        if contact_id is not None:
            self.contact_id = contact_id
        if target_transaction_id is not None:
            self.target_transaction_id = target_transaction_id
        if target_line_item_id is not None:
            self.target_line_item_id = target_line_item_id
        if linked_transaction_id is not None:
            self.linked_transaction_id = linked_transaction_id
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if source_transaction_type_code is not None:
            self.source_transaction_type_code = source_transaction_type_code
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def source_transaction_id(self):
        return self._source_transaction_id

    @source_transaction_id.setter
    def source_transaction_id(self, source_transaction_id):
        self._source_transaction_id = source_transaction_id

    @property
    def source_line_item_id(self):
        return self._source_line_item_id

    @source_line_item_id.setter
    def source_line_item_id(self, source_line_item_id):
        self._source_line_item_id = source_line_item_id

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def target_transaction_id(self):
        return self._target_transaction_id

    @target_transaction_id.setter
    def target_transaction_id(self, target_transaction_id):
        self._target_transaction_id = target_transaction_id

    @property
    def target_line_item_id(self):
        return self._target_line_item_id

    @target_line_item_id.setter
    def target_line_item_id(self, target_line_item_id):
        self._target_line_item_id = target_line_item_id

    @property
    def linked_transaction_id(self):
        return self._linked_transaction_id

    @linked_transaction_id.setter
    def linked_transaction_id(self, linked_transaction_id):
        self._linked_transaction_id = linked_transaction_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        allowed_values = [
            "APPROVED",
            "DRAFT",
            "ONDRAFT",
            "BILLED",
            "VOIDED",
            "None",
        ]
        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(
                        status, allowed_values
                    )
                )
        self._status = status

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_values = ["BILLABLEEXPENSE", "None"]
        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(
                        type, allowed_values
                    )
                )
        self._type = type

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def source_transaction_type_code(self):
        return self._source_transaction_type_code

    @source_transaction_type_code.setter
    def source_transaction_type_code(self, source_transaction_type_code):
        allowed_values = ["ACCPAY", "SPEND", "None"]
        if source_transaction_type_code:
            if source_transaction_type_code not in allowed_values:
                raise ValueError(
                    "Invalid value for `source_transaction_type_code` ({0}), must be one of {1}".format(
                        source_transaction_type_code, allowed_values
                    )
                )
        self._source_transaction_type_code = source_transaction_type_code

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
