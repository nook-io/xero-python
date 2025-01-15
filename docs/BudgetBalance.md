# BudgetBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** | Period the amount applies to (e.g. “2019-08”) | [optional] 
**amount** | **float** | LineItem Quantity | [optional] 
**unit_amount** | **float** | Budgeted amount | [optional] 
**notes** | **str** | Any footnotes associated with this balance | [optional] 

## Example

```python
from xero_python.models.budget_balance import BudgetBalance

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetBalance from a JSON string
budget_balance_instance = BudgetBalance.from_json(json)
# print the JSON string representation of the object
print BudgetBalance.to_json()

# convert the object into a dict
budget_balance_dict = budget_balance_instance.to_dict()
# create an instance of BudgetBalance from a dict
budget_balance_from_dict = BudgetBalance.from_dict(budget_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


