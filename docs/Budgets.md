# Budgets


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budgets** | [**List[Budget]**](Budget.md) |  | [optional] 

## Example

```python
from xero_python.models.budgets import Budgets

# TODO update the JSON string below
json = "{}"
# create an instance of Budgets from a JSON string
budgets_instance = Budgets.from_json(json)
# print the JSON string representation of the object
print Budgets.to_json()

# convert the object into a dict
budgets_dict = budgets_instance.to_dict()
# create an instance of Budgets from a dict
budgets_from_dict = Budgets.from_dict(budgets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


