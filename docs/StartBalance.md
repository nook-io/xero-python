# StartBalance

The starting balance of the statement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | decimal(19,4) unsigned Opening/closing balance amount. | [optional] 
**credit_debit_indicator** | [**CreditDebitIndicator**](CreditDebitIndicator.md) |  | [optional] 

## Example

```python
from xero_python.models.start_balance import StartBalance

# TODO update the JSON string below
json = "{}"
# create an instance of StartBalance from a JSON string
start_balance_instance = StartBalance.from_json(json)
# print the JSON string representation of the object
print StartBalance.to_json()

# convert the object into a dict
start_balance_dict = start_balance_instance.to_dict()
# create an instance of StartBalance from a dict
start_balance_from_dict = StartBalance.from_dict(start_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


