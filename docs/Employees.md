# Employees


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**employees** | [**List[Employee]**](Employee.md) |  | [optional] 

## Example

```python
from xero_python.models.employees import Employees

# TODO update the JSON string below
json = "{}"
# create an instance of Employees from a JSON string
employees_instance = Employees.from_json(json)
# print the JSON string representation of the object
print Employees.to_json()

# convert the object into a dict
employees_dict = employees_instance.to_dict()
# create an instance of Employees from a dict
employees_from_dict = Employees.from_dict(employees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


