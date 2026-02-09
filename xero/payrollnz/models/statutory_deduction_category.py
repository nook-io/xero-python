from enum import Enum


class StatutoryDeductionCategory(Enum):
    PRIORITYORDER = "PriorityOrder"
    NONPRIORITYORDER = "NonPriorityOrder"
    TABLEBASED = "TableBased"
    CHILDSUPPORT = "ChildSupport"
    COURTFINES = "CourtFines"
    INLANDREVENUEARREARS = "InlandRevenueArrears"
    MSDREPAYMENTS = "MsdRepayments"
    STUDENTLOAN = "StudentLoan"
    ADDITIONALSTUDENTLOAN = "AdditionalStudentLoan"
    VOLUNTARYSTUDENTLOAN = "VoluntaryStudentLoan"
    KIWISAVER = "KiwiSaver"
