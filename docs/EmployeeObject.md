# EmployeeObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**employee** | [**Employee**](Employee.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_object import EmployeeObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeObject from a JSON string
employee_object_instance = EmployeeObject.from_json(json)
# print the JSON string representation of the object
print EmployeeObject.to_json()

# convert the object into a dict
employee_object_dict = employee_object_instance.to_dict()
# create an instance of EmployeeObject from a dict
employee_object_from_dict = EmployeeObject.from_dict(employee_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


