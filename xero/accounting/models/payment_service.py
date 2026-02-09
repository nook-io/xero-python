from xero.models import BaseModel


class PaymentService(BaseModel):
    openapi_types = {
        "payment_service_id": "str",
        "payment_service_name": "str",
        "payment_service_url": "str",
        "pay_now_text": "str",
        "payment_service_type": "str",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "payment_service_id": "PaymentServiceID",
        "payment_service_name": "PaymentServiceName",
        "payment_service_url": "PaymentServiceUrl",
        "pay_now_text": "PayNowText",
        "payment_service_type": "PaymentServiceType",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        payment_service_id=None,
        payment_service_name=None,
        payment_service_url=None,
        pay_now_text=None,
        payment_service_type=None,
        validation_errors=None,
    ):
        self._payment_service_id = None
        self._payment_service_name = None
        self._payment_service_url = None
        self._pay_now_text = None
        self._payment_service_type = None
        self._validation_errors = None
        self.discriminator = None
        if payment_service_id is not None:
            self.payment_service_id = payment_service_id
        if payment_service_name is not None:
            self.payment_service_name = payment_service_name
        if payment_service_url is not None:
            self.payment_service_url = payment_service_url
        if pay_now_text is not None:
            self.pay_now_text = pay_now_text
        if payment_service_type is not None:
            self.payment_service_type = payment_service_type
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def payment_service_id(self):
        return self._payment_service_id

    @payment_service_id.setter
    def payment_service_id(self, payment_service_id):
        self._payment_service_id = payment_service_id

    @property
    def payment_service_name(self):
        return self._payment_service_name

    @payment_service_name.setter
    def payment_service_name(self, payment_service_name):
        self._payment_service_name = payment_service_name

    @property
    def payment_service_url(self):
        return self._payment_service_url

    @payment_service_url.setter
    def payment_service_url(self, payment_service_url):
        self._payment_service_url = payment_service_url

    @property
    def pay_now_text(self):
        return self._pay_now_text

    @pay_now_text.setter
    def pay_now_text(self, pay_now_text):
        self._pay_now_text = pay_now_text

    @property
    def payment_service_type(self):
        return self._payment_service_type

    @payment_service_type.setter
    def payment_service_type(self, payment_service_type):
        self._payment_service_type = payment_service_type

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
