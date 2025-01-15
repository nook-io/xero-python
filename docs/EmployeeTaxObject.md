# EmployeeTaxObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**employee_tax** | [**EmployeeTax**](EmployeeTax.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_tax_object import EmployeeTaxObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeTaxObject from a JSON string
employee_tax_object_instance = EmployeeTaxObject.from_json(json)
# print the JSON string representation of the object
print EmployeeTaxObject.to_json()

# convert the object into a dict
employee_tax_object_dict = employee_tax_object_instance.to_dict()
# create an instance of EmployeeTaxObject from a dict
employee_tax_object_from_dict = EmployeeTaxObject.from_dict(employee_tax_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


