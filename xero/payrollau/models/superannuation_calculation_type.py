from enum import Enum


class SuperannuationCalculationType(Enum):
    FIXEDAMOUNT = "FIXEDAMOUNT"
    PERCENTAGEOFEARNINGS = "PERCENTAGEOFEARNINGS"
    STATUTORY = "STATUTORY"
