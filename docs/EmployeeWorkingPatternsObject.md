# EmployeeWorkingPatternsObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**payee_working_patterns** | [**List[EmployeeWorkingPattern]**](EmployeeWorkingPattern.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_working_patterns_object import EmployeeWorkingPatternsObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeWorkingPatternsObject from a JSON string
employee_working_patterns_object_instance = EmployeeWorkingPatternsObject.from_json(json)
# print the JSON string representation of the object
print EmployeeWorkingPatternsObject.to_json()

# convert the object into a dict
employee_working_patterns_object_dict = employee_working_patterns_object_instance.to_dict()
# create an instance of EmployeeWorkingPatternsObject from a dict
employee_working_patterns_object_from_dict = EmployeeWorkingPatternsObject.from_dict(employee_working_patterns_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


