# BankTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_bank_account** | [**Account**](Account.md) |  | 
**to_bank_account** | [**Account**](Account.md) |  | 
**amount** | **float** | amount of the transaction | 
**var_date** | **str** | The date of the Transfer YYYY-MM-DD | [optional] 
**bank_transfer_id** | **str** | The identifier of the Bank Transfer | [optional] [readonly] 
**currency_rate** | **float** | The currency rate | [optional] [readonly] 
**from_bank_transaction_id** | **str** | The Bank Transaction ID for the source account | [optional] [readonly] 
**to_bank_transaction_id** | **str** | The Bank Transaction ID for the destination account | [optional] [readonly] 
**from_is_reconciled** | **bool** | The Bank Transaction boolean to show if it is reconciled for the source account | [optional] [default to False]
**to_is_reconciled** | **bool** | The Bank Transaction boolean to show if it is reconciled for the destination account | [optional] [default to False]
**reference** | **str** | Reference for the transactions. | [optional] 
**has_attachments** | **bool** | Boolean to indicate if a Bank Transfer has an attachment | [optional] [readonly] [default to False]
**created_date_utc** | **str** | UTC timestamp of creation date of bank transfer | [optional] [readonly] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

## Example

```python
from xero_python.models.bank_transfer import BankTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransfer from a JSON string
bank_transfer_instance = BankTransfer.from_json(json)
# print the JSON string representation of the object
print BankTransfer.to_json()

# convert the object into a dict
bank_transfer_dict = bank_transfer_instance.to_dict()
# create an instance of BankTransfer from a dict
bank_transfer_from_dict = BankTransfer.from_dict(bank_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


