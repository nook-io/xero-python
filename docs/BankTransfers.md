# BankTransfers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_transfers** | [**List[BankTransfer]**](BankTransfer.md) |  | [optional] 

## Example

```python
from xero_python.models.bank_transfers import BankTransfers

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransfers from a JSON string
bank_transfers_instance = BankTransfers.from_json(json)
# print the JSON string representation of the object
print BankTransfers.to_json()

# convert the object into a dict
bank_transfers_dict = bank_transfers_instance.to_dict()
# create an instance of BankTransfers from a dict
bank_transfers_from_dict = BankTransfers.from_dict(bank_transfers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


