from xero.models import BaseModel


class Quote(BaseModel):
    openapi_types = {
        "quote_id": "str",
        "quote_number": "str",
        "reference": "str",
        "terms": "str",
        "contact": "Contact",
        "line_items": "list[LineItem]",
        "date": "date[ms-format]",
        "date_string": "str",
        "expiry_date": "date[ms-format]",
        "expiry_date_string": "str",
        "status": "QuoteStatusCodes",
        "currency_code": "CurrencyCode",
        "currency_rate": "float",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "total_discount": "float",
        "title": "str",
        "summary": "str",
        "branding_theme_id": "str",
        "updated_date_utc": "datetime[ms-format]",
        "line_amount_types": "QuoteLineAmountTypes",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
    }
    attribute_map = {
        "quote_id": "QuoteID",
        "quote_number": "QuoteNumber",
        "reference": "Reference",
        "terms": "Terms",
        "contact": "Contact",
        "line_items": "LineItems",
        "date": "Date",
        "date_string": "DateString",
        "expiry_date": "ExpiryDate",
        "expiry_date_string": "ExpiryDateString",
        "status": "Status",
        "currency_code": "CurrencyCode",
        "currency_rate": "CurrencyRate",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "total_discount": "TotalDiscount",
        "title": "Title",
        "summary": "Summary",
        "branding_theme_id": "BrandingThemeID",
        "updated_date_utc": "UpdatedDateUTC",
        "line_amount_types": "LineAmountTypes",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        quote_id=None,
        quote_number=None,
        reference=None,
        terms=None,
        contact=None,
        line_items=None,
        date=None,
        date_string=None,
        expiry_date=None,
        expiry_date_string=None,
        status=None,
        currency_code=None,
        currency_rate=None,
        sub_total=None,
        total_tax=None,
        total=None,
        total_discount=None,
        title=None,
        summary=None,
        branding_theme_id=None,
        updated_date_utc=None,
        line_amount_types=None,
        status_attribute_string=None,
        validation_errors=None,
    ):
        self._quote_id = None
        self._quote_number = None
        self._reference = None
        self._terms = None
        self._contact = None
        self._line_items = None
        self._date = None
        self._date_string = None
        self._expiry_date = None
        self._expiry_date_string = None
        self._status = None
        self._currency_code = None
        self._currency_rate = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._total_discount = None
        self._title = None
        self._summary = None
        self._branding_theme_id = None
        self._updated_date_utc = None
        self._line_amount_types = None
        self._status_attribute_string = None
        self._validation_errors = None
        self.discriminator = None
        if quote_id is not None:
            self.quote_id = quote_id
        if quote_number is not None:
            self.quote_number = quote_number
        if reference is not None:
            self.reference = reference
        if terms is not None:
            self.terms = terms
        if contact is not None:
            self.contact = contact
        if line_items is not None:
            self.line_items = line_items
        if date is not None:
            self.date = date
        if date_string is not None:
            self.date_string = date_string
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if expiry_date_string is not None:
            self.expiry_date_string = expiry_date_string
        if status is not None:
            self.status = status
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if total_discount is not None:
            self.total_discount = total_discount
        if title is not None:
            self.title = title
        if summary is not None:
            self.summary = summary
        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def quote_id(self):
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        self._quote_id = quote_id

    @property
    def quote_number(self):
        return self._quote_number

    @quote_number.setter
    def quote_number(self, quote_number):
        if quote_number is not None and len(quote_number) > 255:
            raise ValueError(
                "Invalid value for `quote_number`, "
                "length must be less than or equal to `255`"
            )
        self._quote_number = quote_number

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if reference is not None and len(reference) > 4000:
            raise ValueError(
                "Invalid value for `reference`, "
                "length must be less than or equal to `4000`"
            )
        self._reference = reference

    @property
    def terms(self):
        return self._terms

    @terms.setter
    def terms(self, terms):
        if terms is not None and len(terms) > 4000:
            raise ValueError(
                "Invalid value for `terms`, length must be less than or equal to `4000`"
            )
        self._terms = terms

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    @property
    def line_items(self):
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        self._line_items = line_items

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def date_string(self):
        return self._date_string

    @date_string.setter
    def date_string(self, date_string):
        self._date_string = date_string

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        self._expiry_date = expiry_date

    @property
    def expiry_date_string(self):
        return self._expiry_date_string

    @expiry_date_string.setter
    def expiry_date_string(self, expiry_date_string):
        self._expiry_date_string = expiry_date_string

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        self._currency_code = currency_code

    @property
    def currency_rate(self):
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        self._currency_rate = currency_rate

    @property
    def sub_total(self):
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        self._sub_total = sub_total

    @property
    def total_tax(self):
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        self._total_tax = total_tax

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def total_discount(self):
        return self._total_discount

    @total_discount.setter
    def total_discount(self, total_discount):
        self._total_discount = total_discount

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title is not None and len(title) > 100:
            raise ValueError(
                "Invalid value for `title`, length must be less than or equal to `100`"
            )
        self._title = title

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, summary):
        if summary is not None and len(summary) > 3000:
            raise ValueError(
                "Invalid value for `summary`, "
                "length must be less than or equal to `3000`"
            )
        self._summary = summary

    @property
    def branding_theme_id(self):
        return self._branding_theme_id

    @branding_theme_id.setter
    def branding_theme_id(self, branding_theme_id):
        self._branding_theme_id = branding_theme_id

    @property
    def updated_date_utc(self):
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        self._updated_date_utc = updated_date_utc

    @property
    def line_amount_types(self):
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        self._line_amount_types = line_amount_types

    @property
    def status_attribute_string(self):
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        self._validation_errors = validation_errors
