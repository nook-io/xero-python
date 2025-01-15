# CashflowType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the activity | [optional] 
**total** | **float** | Total value of the activity | [optional] 
**accounts** | [**List[CashflowAccount]**](CashflowAccount.md) | List of the accounts in this activity | [optional] 

## Example

```python
from xero_python.models.cashflow_type import CashflowType

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowType from a JSON string
cashflow_type_instance = CashflowType.from_json(json)
# print the JSON string representation of the object
print CashflowType.to_json()

# convert the object into a dict
cashflow_type_dict = cashflow_type_instance.to_dict()
# create an instance of CashflowType from a dict
cashflow_type_from_dict = CashflowType.from_dict(cashflow_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


