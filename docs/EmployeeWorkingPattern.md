# EmployeeWorkingPattern


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_working_pattern_id** | **str** | The Xero identifier for for Employee working pattern | 
**effective_from** | **date** | The effective date of the corresponding salary and wages | 

## Example

```python
from xero_python.models.employee_working_pattern import EmployeeWorkingPattern

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeWorkingPattern from a JSON string
employee_working_pattern_instance = EmployeeWorkingPattern.from_json(json)
# print the JSON string representation of the object
print EmployeeWorkingPattern.to_json()

# convert the object into a dict
employee_working_pattern_dict = employee_working_pattern_instance.to_dict()
# create an instance of EmployeeWorkingPattern from a dict
employee_working_pattern_from_dict = EmployeeWorkingPattern.from_dict(employee_working_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


