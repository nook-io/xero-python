# BudgetLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | See Accounts | [optional] 
**account_code** | **str** | See Accounts | [optional] 
**budget_balances** | [**List[BudgetBalance]**](BudgetBalance.md) |  | [optional] 

## Example

```python
from xero_python.models.budget_line import BudgetLine

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetLine from a JSON string
budget_line_instance = BudgetLine.from_json(json)
# print the JSON string representation of the object
print BudgetLine.to_json()

# convert the object into a dict
budget_line_dict = budget_line_instance.to_dict()
# create an instance of BudgetLine from a dict
budget_line_from_dict = BudgetLine.from_dict(budget_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


