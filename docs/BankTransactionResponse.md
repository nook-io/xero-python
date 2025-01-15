# BankTransactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_transaction_id** | **str** | Xero Identifier of transaction | [optional] 
**batch_payment_id** | **str** | Xero Identifier of batch payment. Present if the transaction is part of a batch. | [optional] 
**contact** | [**ContactResponse**](ContactResponse.md) |  | [optional] 
**var_date** | **date** | Date of transaction - YYYY-MM-DD | [optional] 
**amount** | **float** | Amount of transaction | [optional] 
**line_items** | [**List[LineItemResponse]**](LineItemResponse.md) | The LineItems element can contain any number of individual LineItem sub-elements. Not included in summary mode | [optional] 

## Example

```python
from xero_python.models.bank_transaction_response import BankTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionResponse from a JSON string
bank_transaction_response_instance = BankTransactionResponse.from_json(json)
# print the JSON string representation of the object
print BankTransactionResponse.to_json()

# convert the object into a dict
bank_transaction_response_dict = bank_transaction_response_instance.to_dict()
# create an instance of BankTransactionResponse from a dict
bank_transaction_response_from_dict = BankTransactionResponse.from_dict(bank_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


