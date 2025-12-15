from xero.models import BaseModel


class PracticeResponse(BaseModel):
    openapi_types = {
        "xero_partner_since": "int",
        "tier": "str",
        "location": "str",
        "organisation_count": "int",
        "staff_certified": "bool",
    }
    attribute_map = {
        "xero_partner_since": "xeroPartnerSince",
        "tier": "tier",
        "location": "location",
        "organisation_count": "organisationCount",
        "staff_certified": "staffCertified",
    }

    def __init__(
        self,
        xero_partner_since=None,
        tier=None,
        location=None,
        organisation_count=None,
        staff_certified=None,
    ):
        self._xero_partner_since = None
        self._tier = None
        self._location = None
        self._organisation_count = None
        self._staff_certified = None
        self.discriminator = None
        if xero_partner_since is not None:
            self.xero_partner_since = xero_partner_since
        if tier is not None:
            self.tier = tier
        if location is not None:
            self.location = location
        if organisation_count is not None:
            self.organisation_count = organisation_count
        if staff_certified is not None:
            self.staff_certified = staff_certified

    @property
    def xero_partner_since(self):
        return self._xero_partner_since

    @xero_partner_since.setter
    def xero_partner_since(self, xero_partner_since):
        self._xero_partner_since = xero_partner_since

    @property
    def tier(self):
        return self._tier

    @tier.setter
    def tier(self, tier):
        self._tier = tier

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def organisation_count(self):
        return self._organisation_count

    @organisation_count.setter
    def organisation_count(self, organisation_count):
        self._organisation_count = organisation_count

    @property
    def staff_certified(self):
        return self._staff_certified

    @staff_certified.setter
    def staff_certified(self, staff_certified):
        self._staff_certified = staff_certified
