from xero.models import BaseModel


class TaxBreakdownComponent(BaseModel):
    openapi_types = {
        "tax_component_id": "str",
        "type": "str",
        "name": "str",
        "tax_percentage": "float",
        "tax_amount": "float",
        "taxable_amount": "float",
        "non_taxable_amount": "float",
        "exempt_amount": "float",
        "state_assigned_no": "str",
        "jurisdiction_region": "str",
    }
    attribute_map = {
        "tax_component_id": "TaxComponentId",
        "type": "Type",
        "name": "Name",
        "tax_percentage": "TaxPercentage",
        "tax_amount": "TaxAmount",
        "taxable_amount": "TaxableAmount",
        "non_taxable_amount": "NonTaxableAmount",
        "exempt_amount": "ExemptAmount",
        "state_assigned_no": "StateAssignedNo",
        "jurisdiction_region": "JurisdictionRegion",
    }

    def __init__(
        self,
        tax_component_id=None,
        type=None,
        name=None,
        tax_percentage=None,
        tax_amount=None,
        taxable_amount=None,
        non_taxable_amount=None,
        exempt_amount=None,
        state_assigned_no=None,
        jurisdiction_region=None,
    ):
        self._tax_component_id = None
        self._type = None
        self._name = None
        self._tax_percentage = None
        self._tax_amount = None
        self._taxable_amount = None
        self._non_taxable_amount = None
        self._exempt_amount = None
        self._state_assigned_no = None
        self._jurisdiction_region = None
        self.discriminator = None
        if tax_component_id is not None:
            self.tax_component_id = tax_component_id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if tax_percentage is not None:
            self.tax_percentage = tax_percentage
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if taxable_amount is not None:
            self.taxable_amount = taxable_amount
        if non_taxable_amount is not None:
            self.non_taxable_amount = non_taxable_amount
        if exempt_amount is not None:
            self.exempt_amount = exempt_amount
        if state_assigned_no is not None:
            self.state_assigned_no = state_assigned_no
        if jurisdiction_region is not None:
            self.jurisdiction_region = jurisdiction_region

    @property
    def tax_component_id(self):
        return self._tax_component_id

    @tax_component_id.setter
    def tax_component_id(self, tax_component_id):
        self._tax_component_id = tax_component_id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_values = [
            "SYSGST/USCOUNTRY",
            "SYSGST/USSTATE",
            "SYSGST/USCOUNTY",
            "SYSGST/USCITY",
            "SYSGST/USSPECIAL",
            "None",
        ]
        if type:
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}".format(
                        type, allowed_values
                    )
                )
        self._type = type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tax_percentage(self):
        return self._tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, tax_percentage):
        self._tax_percentage = tax_percentage

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        self._tax_amount = tax_amount

    @property
    def taxable_amount(self):
        return self._taxable_amount

    @taxable_amount.setter
    def taxable_amount(self, taxable_amount):
        self._taxable_amount = taxable_amount

    @property
    def non_taxable_amount(self):
        return self._non_taxable_amount

    @non_taxable_amount.setter
    def non_taxable_amount(self, non_taxable_amount):
        self._non_taxable_amount = non_taxable_amount

    @property
    def exempt_amount(self):
        return self._exempt_amount

    @exempt_amount.setter
    def exempt_amount(self, exempt_amount):
        self._exempt_amount = exempt_amount

    @property
    def state_assigned_no(self):
        return self._state_assigned_no

    @state_assigned_no.setter
    def state_assigned_no(self, state_assigned_no):
        self._state_assigned_no = state_assigned_no

    @property
    def jurisdiction_region(self):
        return self._jurisdiction_region

    @jurisdiction_region.setter
    def jurisdiction_region(self, jurisdiction_region):
        self._jurisdiction_region = jurisdiction_region
