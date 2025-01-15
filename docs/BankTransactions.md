# BankTransactions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination1**](Pagination1.md) |  | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**bank_transactions** | [**List[BankTransaction]**](BankTransaction.md) |  | [optional] 

## Example

```python
from xero_python.models.bank_transactions import BankTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactions from a JSON string
bank_transactions_instance = BankTransactions.from_json(json)
# print the JSON string representation of the object
print BankTransactions.to_json()

# convert the object into a dict
bank_transactions_dict = bank_transactions_instance.to_dict()
# create an instance of BankTransactions from a dict
bank_transactions_from_dict = BankTransactions.from_dict(bank_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


