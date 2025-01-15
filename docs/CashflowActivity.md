# CashflowActivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the cashflow activity type. It will be either Operating Activities, Investing Activities or Financing Activities | [optional] 
**total** | **float** | Total value of the activity type | [optional] 
**cashflow_types** | [**List[CashflowType]**](CashflowType.md) |  | [optional] 

## Example

```python
from xero_python.models.cashflow_activity import CashflowActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowActivity from a JSON string
cashflow_activity_instance = CashflowActivity.from_json(json)
# print the JSON string representation of the object
print CashflowActivity.to_json()

# convert the object into a dict
cashflow_activity_dict = cashflow_activity_instance.to_dict()
# create an instance of CashflowActivity from a dict
cashflow_activity_from_dict = CashflowActivity.from_dict(cashflow_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


