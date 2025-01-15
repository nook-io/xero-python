# EmployeeWorkingPatternWithWorkingWeeks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_working_pattern_id** | **str** | The Xero identifier for for Employee working pattern | 
**effective_from** | **date** | The effective date of the corresponding salary and wages | 
**working_weeks** | [**List[WorkingWeek]**](WorkingWeek.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_working_pattern_with_working_weeks import EmployeeWorkingPatternWithWorkingWeeks

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeWorkingPatternWithWorkingWeeks from a JSON string
employee_working_pattern_with_working_weeks_instance = EmployeeWorkingPatternWithWorkingWeeks.from_json(json)
# print the JSON string representation of the object
print EmployeeWorkingPatternWithWorkingWeeks.to_json()

# convert the object into a dict
employee_working_pattern_with_working_weeks_dict = employee_working_pattern_with_working_weeks_instance.to_dict()
# create an instance of EmployeeWorkingPatternWithWorkingWeeks from a dict
employee_working_pattern_with_working_weeks_from_dict = EmployeeWorkingPatternWithWorkingWeeks.from_dict(employee_working_pattern_with_working_weeks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


