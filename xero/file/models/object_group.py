from enum import Enum


class ObjectGroup(Enum):
    ACCOUNT = "Account"
    BANKTRANSACTION = "BankTransaction"
    CONTACT = "Contact"
    CREDITNOTE = "CreditNote"
    INVOICE = "Invoice"
    ITEM = "Item"
    MANUALJOURNAL = "ManualJournal"
    OVERPAYMENT = "Overpayment"
    PAYMENT = "Payment"
    PREPAYMENT = "Prepayment"
    QUOTE = "Quote"
    RECEIPT = "Receipt"
