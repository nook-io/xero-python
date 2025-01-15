# PayRunCalendarObject1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**pay_run_calendar** | [**PayRunCalendar1**](PayRunCalendar1.md) |  | [optional] 

## Example

```python
from xero_python.models.pay_run_calendar_object1 import PayRunCalendarObject1

# TODO update the JSON string below
json = "{}"
# create an instance of PayRunCalendarObject1 from a JSON string
pay_run_calendar_object1_instance = PayRunCalendarObject1.from_json(json)
# print the JSON string representation of the object
print PayRunCalendarObject1.to_json()

# convert the object into a dict
pay_run_calendar_object1_dict = pay_run_calendar_object1_instance.to_dict()
# create an instance of PayRunCalendarObject1 from a dict
pay_run_calendar_object1_from_dict = PayRunCalendarObject1.from_dict(pay_run_calendar_object1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


