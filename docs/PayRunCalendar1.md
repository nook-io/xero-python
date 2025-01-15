# PayRunCalendar1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_calendar_id** | **str** | Xero unique identifier for the payroll calendar | [optional] 
**name** | **str** | Name of the calendar | 
**calendar_type** | **str** | Type of the calendar | 
**period_start_date** | **date** | Period start date of the calendar | 
**period_end_date** | **date** | Period end date of the calendar | [optional] 
**payment_date** | **date** | Payment date of the calendar | 
**updated_date_utc** | **datetime** | UTC timestamp of the last update to the pay run calendar | [optional] 

## Example

```python
from xero_python.models.pay_run_calendar1 import PayRunCalendar1

# TODO update the JSON string below
json = "{}"
# create an instance of PayRunCalendar1 from a JSON string
pay_run_calendar1_instance = PayRunCalendar1.from_json(json)
# print the JSON string representation of the object
print PayRunCalendar1.to_json()

# convert the object into a dict
pay_run_calendar1_dict = pay_run_calendar1_instance.to_dict()
# create an instance of PayRunCalendar1 from a dict
pay_run_calendar1_from_dict = PayRunCalendar1.from_dict(pay_run_calendar1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


