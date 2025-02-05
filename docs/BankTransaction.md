# BankTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | See Bank Transaction Types | 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**line_items** | [**List[LineItem]**](LineItem.md) | See LineItems | 
**bank_account** | [**Account**](Account.md) |  | 
**is_reconciled** | **bool** | Boolean to show if transaction is reconciled | [optional] 
**var_date** | **str** | Date of transaction – YYYY-MM-DD | [optional] 
**reference** | **str** | Reference for the transaction. Only supported for SPEND and RECEIVE transactions. | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**currency_rate** | **float** | Exchange rate to base currency when money is spent or received. e.g.0.7500 Only used for bank transactions in non base currency. If this isn’t specified for non base currency accounts then either the user-defined rate (preference) or the XE.com day rate will be used. Setting currency is only supported on overpayments. | [optional] 
**url** | **str** | URL link to a source document – shown as “Go to App Name” | [optional] 
**status** | **str** | See Bank Transaction Status Codes | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**sub_total** | **float** | Total of bank transaction excluding taxes | [optional] 
**total_tax** | **float** | Total tax on bank transaction | [optional] 
**total** | **float** | Total of bank transaction tax inclusive | [optional] 
**bank_transaction_id** | **str** | Xero generated unique identifier for bank transaction | [optional] 
**prepayment_id** | **str** | Xero generated unique identifier for a Prepayment. This will be returned on BankTransactions with a Type of SPEND-PREPAYMENT or RECEIVE-PREPAYMENT | [optional] [readonly] 
**overpayment_id** | **str** | Xero generated unique identifier for an Overpayment. This will be returned on BankTransactions with a Type of SPEND-OVERPAYMENT or RECEIVE-OVERPAYMENT | [optional] [readonly] 
**updated_date_utc** | **str** | Last modified date UTC format | [optional] [readonly] 
**has_attachments** | **bool** | Boolean to indicate if a bank transaction has an attachment | [optional] [readonly] [default to False]
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

## Example

```python
from xero_python.models.bank_transaction import BankTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransaction from a JSON string
bank_transaction_instance = BankTransaction.from_json(json)
# print the JSON string representation of the object
print BankTransaction.to_json()

# convert the object into a dict
bank_transaction_dict = bank_transaction_instance.to_dict()
# create an instance of BankTransaction from a dict
bank_transaction_from_dict = BankTransaction.from_dict(bank_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


