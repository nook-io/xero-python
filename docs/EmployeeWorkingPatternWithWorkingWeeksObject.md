# EmployeeWorkingPatternWithWorkingWeeksObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**payee_working_pattern** | [**EmployeeWorkingPatternWithWorkingWeeks**](EmployeeWorkingPatternWithWorkingWeeks.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_working_pattern_with_working_weeks_object import EmployeeWorkingPatternWithWorkingWeeksObject

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeWorkingPatternWithWorkingWeeksObject from a JSON string
employee_working_pattern_with_working_weeks_object_instance = EmployeeWorkingPatternWithWorkingWeeksObject.from_json(json)
# print the JSON string representation of the object
print EmployeeWorkingPatternWithWorkingWeeksObject.to_json()

# convert the object into a dict
employee_working_pattern_with_working_weeks_object_dict = employee_working_pattern_with_working_weeks_object_instance.to_dict()
# create an instance of EmployeeWorkingPatternWithWorkingWeeksObject from a dict
employee_working_pattern_with_working_weeks_object_from_dict = EmployeeWorkingPatternWithWorkingWeeksObject.from_dict(employee_working_pattern_with_working_weeks_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


