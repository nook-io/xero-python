# PayRunCalendarObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**pay_run_calendar** | [**PayRunCalendar**](PayRunCalendar.md) |  | [optional] 

## Example

```python
from xero_python.models.pay_run_calendar_object import PayRunCalendarObject

# TODO update the JSON string below
json = "{}"
# create an instance of PayRunCalendarObject from a JSON string
pay_run_calendar_object_instance = PayRunCalendarObject.from_json(json)
# print the JSON string representation of the object
print PayRunCalendarObject.to_json()

# convert the object into a dict
pay_run_calendar_object_dict = pay_run_calendar_object_instance.to_dict()
# create an instance of PayRunCalendarObject from a dict
pay_run_calendar_object_from_dict = PayRunCalendarObject.from_dict(pay_run_calendar_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


