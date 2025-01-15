# Employment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_calendar_id** | **str** | Xero unique identifier for the payroll calendar of the employee | 
**start_date** | **date** | Start date of the employment (YYYY-MM-DD) | 
**employee_number** | **str** | The employment number of the employee | 
**ni_category** | **str** | The NI Category of the employee | 

## Example

```python
from xero_python.models.employment import Employment

# TODO update the JSON string below
json = "{}"
# create an instance of Employment from a JSON string
employment_instance = Employment.from_json(json)
# print the JSON string representation of the object
print Employment.to_json()

# convert the object into a dict
employment_dict = employment_instance.to_dict()
# create an instance of Employment from a dict
employment_from_dict = Employment.from_dict(employment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


