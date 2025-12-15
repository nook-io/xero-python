from xero.models import BaseModel


class PaymentServices(BaseModel):
    openapi_types = {"payment_services": "list[PaymentService]"}
    attribute_map = {"payment_services": "PaymentServices"}

    def __init__(self, payment_services=None):
        self._payment_services = None
        self.discriminator = None
        if payment_services is not None:
            self.payment_services = payment_services

    @property
    def payment_services(self):
        return self._payment_services

    @payment_services.setter
    def payment_services(self, payment_services):
        self._payment_services = payment_services
