# Schedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **int** | Integer used with the unit e.g. 1 (every 1 week), 2 (every 2 months) | [optional] 
**unit** | **str** | One of the following - WEEKLY or MONTHLY | [optional] 
**due_date** | **int** | Integer used with due date type e.g 20 (of following month), 31 (of current month) | [optional] 
**due_date_type** | **str** | the payment terms | [optional] 
**start_date** | **str** | Date the first invoice of the current version of the repeating schedule was generated (changes when repeating invoice is edited) | [optional] 
**next_scheduled_date** | **str** | The calendar date of the next invoice in the schedule to be generated | [optional] 
**end_date** | **str** | Invoice end date – only returned if the template has an end date set | [optional] 

## Example

```python
from xero_python.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print Schedule.to_json()

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_from_dict = Schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


