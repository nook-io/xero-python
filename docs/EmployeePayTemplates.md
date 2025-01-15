# EmployeePayTemplates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**earning_templates** | [**List[EarningsTemplate]**](EarningsTemplate.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_pay_templates import EmployeePayTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeePayTemplates from a JSON string
employee_pay_templates_instance = EmployeePayTemplates.from_json(json)
# print the JSON string representation of the object
print EmployeePayTemplates.to_json()

# convert the object into a dict
employee_pay_templates_dict = employee_pay_templates_instance.to_dict()
# create an instance of EmployeePayTemplates from a dict
employee_pay_templates_from_dict = EmployeePayTemplates.from_dict(employee_pay_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


