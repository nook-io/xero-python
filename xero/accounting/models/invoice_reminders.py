from xero.models import BaseModel


class InvoiceReminders(BaseModel):
    openapi_types = {"invoice_reminders": "list[InvoiceReminder]"}
    attribute_map = {"invoice_reminders": "InvoiceReminders"}

    def __init__(self, invoice_reminders=None):
        self._invoice_reminders = None
        self.discriminator = None
        if invoice_reminders is not None:
            self.invoice_reminders = invoice_reminders

    @property
    def invoice_reminders(self):
        return self._invoice_reminders

    @invoice_reminders.setter
    def invoice_reminders(self, invoice_reminders):
        self._invoice_reminders = invoice_reminders
