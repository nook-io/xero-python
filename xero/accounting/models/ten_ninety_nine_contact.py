from xero.models import BaseModel


class TenNinetyNineContact(BaseModel):
    openapi_types = {
        "box1": "float",
        "box2": "float",
        "box3": "float",
        "box4": "float",
        "box5": "float",
        "box6": "float",
        "box7": "float",
        "box8": "float",
        "box9": "float",
        "box10": "float",
        "box11": "float",
        "box13": "float",
        "box14": "float",
        "name": "str",
        "federal_tax_id_type": "str",
        "city": "str",
        "zip": "str",
        "state": "str",
        "email": "str",
        "street_address": "str",
        "tax_id": "str",
        "contact_id": "str",
        "legal_name": "str",
        "business_name": "str",
        "federal_tax_classification": "str",
    }
    attribute_map = {
        "box1": "Box1",
        "box2": "Box2",
        "box3": "Box3",
        "box4": "Box4",
        "box5": "Box5",
        "box6": "Box6",
        "box7": "Box7",
        "box8": "Box8",
        "box9": "Box9",
        "box10": "Box10",
        "box11": "Box11",
        "box13": "Box13",
        "box14": "Box14",
        "name": "Name",
        "federal_tax_id_type": "FederalTaxIDType",
        "city": "City",
        "zip": "Zip",
        "state": "State",
        "email": "Email",
        "street_address": "StreetAddress",
        "tax_id": "TaxID",
        "contact_id": "ContactId",
        "legal_name": "LegalName",
        "business_name": "BusinessName",
        "federal_tax_classification": "FederalTaxClassification",
    }

    def __init__(
        self,
        box1=None,
        box2=None,
        box3=None,
        box4=None,
        box5=None,
        box6=None,
        box7=None,
        box8=None,
        box9=None,
        box10=None,
        box11=None,
        box13=None,
        box14=None,
        name=None,
        federal_tax_id_type=None,
        city=None,
        zip=None,
        state=None,
        email=None,
        street_address=None,
        tax_id=None,
        contact_id=None,
        legal_name=None,
        business_name=None,
        federal_tax_classification=None,
    ):
        self._box1 = None
        self._box2 = None
        self._box3 = None
        self._box4 = None
        self._box5 = None
        self._box6 = None
        self._box7 = None
        self._box8 = None
        self._box9 = None
        self._box10 = None
        self._box11 = None
        self._box13 = None
        self._box14 = None
        self._name = None
        self._federal_tax_id_type = None
        self._city = None
        self._zip = None
        self._state = None
        self._email = None
        self._street_address = None
        self._tax_id = None
        self._contact_id = None
        self._legal_name = None
        self._business_name = None
        self._federal_tax_classification = None
        self.discriminator = None
        if box1 is not None:
            self.box1 = box1
        if box2 is not None:
            self.box2 = box2
        if box3 is not None:
            self.box3 = box3
        if box4 is not None:
            self.box4 = box4
        if box5 is not None:
            self.box5 = box5
        if box6 is not None:
            self.box6 = box6
        if box7 is not None:
            self.box7 = box7
        if box8 is not None:
            self.box8 = box8
        if box9 is not None:
            self.box9 = box9
        if box10 is not None:
            self.box10 = box10
        if box11 is not None:
            self.box11 = box11
        if box13 is not None:
            self.box13 = box13
        if box14 is not None:
            self.box14 = box14
        if name is not None:
            self.name = name
        if federal_tax_id_type is not None:
            self.federal_tax_id_type = federal_tax_id_type
        if city is not None:
            self.city = city
        if zip is not None:
            self.zip = zip
        if state is not None:
            self.state = state
        if email is not None:
            self.email = email
        if street_address is not None:
            self.street_address = street_address
        if tax_id is not None:
            self.tax_id = tax_id
        if contact_id is not None:
            self.contact_id = contact_id
        if legal_name is not None:
            self.legal_name = legal_name
        if business_name is not None:
            self.business_name = business_name
        if federal_tax_classification is not None:
            self.federal_tax_classification = federal_tax_classification

    @property
    def box1(self):
        return self._box1

    @box1.setter
    def box1(self, box1):
        self._box1 = box1

    @property
    def box2(self):
        return self._box2

    @box2.setter
    def box2(self, box2):
        self._box2 = box2

    @property
    def box3(self):
        return self._box3

    @box3.setter
    def box3(self, box3):
        self._box3 = box3

    @property
    def box4(self):
        return self._box4

    @box4.setter
    def box4(self, box4):
        self._box4 = box4

    @property
    def box5(self):
        return self._box5

    @box5.setter
    def box5(self, box5):
        self._box5 = box5

    @property
    def box6(self):
        return self._box6

    @box6.setter
    def box6(self, box6):
        self._box6 = box6

    @property
    def box7(self):
        return self._box7

    @box7.setter
    def box7(self, box7):
        self._box7 = box7

    @property
    def box8(self):
        return self._box8

    @box8.setter
    def box8(self, box8):
        self._box8 = box8

    @property
    def box9(self):
        return self._box9

    @box9.setter
    def box9(self, box9):
        self._box9 = box9

    @property
    def box10(self):
        return self._box10

    @box10.setter
    def box10(self, box10):
        self._box10 = box10

    @property
    def box11(self):
        return self._box11

    @box11.setter
    def box11(self, box11):
        self._box11 = box11

    @property
    def box13(self):
        return self._box13

    @box13.setter
    def box13(self, box13):
        self._box13 = box13

    @property
    def box14(self):
        return self._box14

    @box14.setter
    def box14(self, box14):
        self._box14 = box14

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def federal_tax_id_type(self):
        return self._federal_tax_id_type

    @federal_tax_id_type.setter
    def federal_tax_id_type(self, federal_tax_id_type):
        self._federal_tax_id_type = federal_tax_id_type

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def zip(self):
        return self._zip

    @zip.setter
    def zip(self, zip):
        self._zip = zip

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def street_address(self):
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        self._street_address = street_address

    @property
    def tax_id(self):
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        self._tax_id = tax_id

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        self._legal_name = legal_name

    @property
    def business_name(self):
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        self._business_name = business_name

    @property
    def federal_tax_classification(self):
        return self._federal_tax_classification

    @federal_tax_classification.setter
    def federal_tax_classification(self, federal_tax_classification):
        allowed_values = [
            "SOLE_PROPRIETOR",
            "PARTNERSHIP",
            "TRUST_OR_ESTATE",
            "NONPROFIT",
            "C_CORP",
            "S_CORP",
            "OTHER",
            "None",
        ]
        if federal_tax_classification:
            if federal_tax_classification not in allowed_values:
                raise ValueError(
                    "Invalid value for `federal_tax_classification` ({0}), must be one of {1}".format(
                        federal_tax_classification, allowed_values
                    )
                )
        self._federal_tax_classification = federal_tax_classification
