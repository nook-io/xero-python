# EmployeePayTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | Unique identifier for the employee | [optional] 
**earning_templates** | [**List[EarningsTemplate]**](EarningsTemplate.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_pay_template import EmployeePayTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeePayTemplate from a JSON string
employee_pay_template_instance = EmployeePayTemplate.from_json(json)
# print the JSON string representation of the object
print EmployeePayTemplate.to_json()

# convert the object into a dict
employee_pay_template_dict = employee_pay_template_instance.to_dict()
# create an instance of EmployeePayTemplate from a dict
employee_pay_template_from_dict = EmployeePayTemplate.from_dict(employee_pay_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


