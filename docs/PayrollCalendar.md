# PayrollCalendar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Payroll Calendar | [optional] 
**calendar_type** | [**CalendarType1**](CalendarType1.md) |  | [optional] 
**start_date** | **str** | The start date of the upcoming pay period. The end date will be calculated based upon this date, and the calendar type selected (YYYY-MM-DD) | [optional] 
**payment_date** | **str** | The date on which employees will be paid for the upcoming pay period (YYYY-MM-DD) | [optional] 
**payroll_calendar_id** | **str** | Xero identifier | [optional] 
**updated_date_utc** | **str** | Last modified timestamp | [optional] [readonly] 
**reference_date** | **str** | Reference Date (YYYY-MM-DD) | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

## Example

```python
from xero_python.models.payroll_calendar import PayrollCalendar

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollCalendar from a JSON string
payroll_calendar_instance = PayrollCalendar.from_json(json)
# print the JSON string representation of the object
print PayrollCalendar.to_json()

# convert the object into a dict
payroll_calendar_dict = payroll_calendar_instance.to_dict()
# create an instance of PayrollCalendar from a dict
payroll_calendar_from_dict = PayrollCalendar.from_dict(payroll_calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


