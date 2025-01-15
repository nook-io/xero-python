# PayrollCalendars


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_calendars** | [**List[PayrollCalendar]**](PayrollCalendar.md) |  | [optional] 

## Example

```python
from xero_python.models.payroll_calendars import PayrollCalendars

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollCalendars from a JSON string
payroll_calendars_instance = PayrollCalendars.from_json(json)
# print the JSON string representation of the object
print PayrollCalendars.to_json()

# convert the object into a dict
payroll_calendars_dict = payroll_calendars_instance.to_dict()
# create an instance of PayrollCalendars from a dict
payroll_calendars_from_dict = PayrollCalendars.from_dict(payroll_calendars_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


