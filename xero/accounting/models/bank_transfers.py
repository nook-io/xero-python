from xero.models import BaseModel


class BankTransfers(BaseModel):
    openapi_types = {"bank_transfers": "list[BankTransfer]"}
    attribute_map = {"bank_transfers": "BankTransfers"}

    def __init__(self, bank_transfers=None):
        self._bank_transfers = None
        self.discriminator = None
        if bank_transfers is not None:
            self.bank_transfers = bank_transfers

    @property
    def bank_transfers(self):
        return self._bank_transfers

    @bank_transfers.setter
    def bank_transfers(self, bank_transfers):
        self._bank_transfers = bank_transfers
