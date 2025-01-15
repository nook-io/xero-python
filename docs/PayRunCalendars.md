# PayRunCalendars


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**pay_run_calendars** | [**List[PayRunCalendar1]**](PayRunCalendar1.md) |  | [optional] 

## Example

```python
from xero_python.models.pay_run_calendars import PayRunCalendars

# TODO update the JSON string below
json = "{}"
# create an instance of PayRunCalendars from a JSON string
pay_run_calendars_instance = PayRunCalendars.from_json(json)
# print the JSON string representation of the object
print PayRunCalendars.to_json()

# convert the object into a dict
pay_run_calendars_dict = pay_run_calendars_instance.to_dict()
# create an instance of PayRunCalendars from a dict
pay_run_calendars_from_dict = PayRunCalendars.from_dict(pay_run_calendars_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


