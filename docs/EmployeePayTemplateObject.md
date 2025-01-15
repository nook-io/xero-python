# EmployeePayTemplateObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**pay_template** | [**EmployeePayTemplate**](EmployeePayTemplate.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_pay_template_object import EmployeePayTemplateObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeePayTemplateObject from a JSON string
employee_pay_template_object_instance = EmployeePayTemplateObject.from_json(json)
# print the JSON string representation of the object
print EmployeePayTemplateObject.to_json()

# convert the object into a dict
employee_pay_template_object_dict = employee_pay_template_object_instance.to_dict()
# create an instance of EmployeePayTemplateObject from a dict
employee_pay_template_object_from_dict = EmployeePayTemplateObject.from_dict(employee_pay_template_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


