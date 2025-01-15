# CashBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opening_cash_balance** | **float** | Opening balance of cash and cash equivalents | [optional] 
**closing_cash_balance** | **float** | Closing balance of cash and cash equivalents | [optional] 
**net_cash_movement** | **float** | Net movement of cash and cash equivalents for the period | [optional] [readonly] 

## Example

```python
from xero_python.models.cash_balance import CashBalance

# TODO update the JSON string below
json = "{}"
# create an instance of CashBalance from a JSON string
cash_balance_instance = CashBalance.from_json(json)
# print the JSON string representation of the object
print CashBalance.to_json()

# convert the object into a dict
cash_balance_dict = cash_balance_instance.to_dict()
# create an instance of CashBalance from a dict
cash_balance_from_dict = CashBalance.from_dict(cash_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


