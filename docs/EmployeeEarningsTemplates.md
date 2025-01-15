# EmployeeEarningsTemplates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**earning_templates** | [**List[EarningsTemplate]**](EarningsTemplate.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_earnings_templates import EmployeeEarningsTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeEarningsTemplates from a JSON string
employee_earnings_templates_instance = EmployeeEarningsTemplates.from_json(json)
# print the JSON string representation of the object
print EmployeeEarningsTemplates.to_json()

# convert the object into a dict
employee_earnings_templates_dict = employee_earnings_templates_instance.to_dict()
# create an instance of EmployeeEarningsTemplates from a dict
employee_earnings_templates_from_dict = EmployeeEarningsTemplates.from_dict(employee_earnings_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


