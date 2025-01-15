# Budget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_id** | **str** | Xero identifier | [optional] 
**type** | **str** | Type of Budget. OVERALL or TRACKING | [optional] 
**description** | **str** | The Budget description | [optional] 
**updated_date_utc** | **str** | UTC timestamp of last update to budget | [optional] [readonly] 
**budget_lines** | [**List[BudgetLine]**](BudgetLine.md) |  | [optional] 
**tracking** | [**List[TrackingCategory]**](TrackingCategory.md) |  | [optional] 

## Example

```python
from xero_python.models.budget import Budget

# TODO update the JSON string below
json = "{}"
# create an instance of Budget from a JSON string
budget_instance = Budget.from_json(json)
# print the JSON string representation of the object
print Budget.to_json()

# convert the object into a dict
budget_dict = budget_instance.to_dict()
# create an instance of Budget from a dict
budget_from_dict = Budget.from_dict(budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


