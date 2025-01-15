# EmployeeWorkingPatternWithWorkingWeeksRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **date** | The effective date of the corresponding salary and wages | 
**working_weeks** | [**List[WorkingWeek]**](WorkingWeek.md) |  | 

## Example

```python
from xero_python.models.employee_working_pattern_with_working_weeks_request import EmployeeWorkingPatternWithWorkingWeeksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeWorkingPatternWithWorkingWeeksRequest from a JSON string
employee_working_pattern_with_working_weeks_request_instance = EmployeeWorkingPatternWithWorkingWeeksRequest.from_json(json)
# print the JSON string representation of the object
print EmployeeWorkingPatternWithWorkingWeeksRequest.to_json()

# convert the object into a dict
employee_working_pattern_with_working_weeks_request_dict = employee_working_pattern_with_working_weeks_request_instance.to_dict()
# create an instance of EmployeeWorkingPatternWithWorkingWeeksRequest from a dict
employee_working_pattern_with_working_weeks_request_from_dict = EmployeeWorkingPatternWithWorkingWeeksRequest.from_dict(employee_working_pattern_with_working_weeks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


