# TimeEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_entry_id** | **str** | Identifier of the time entry. | [optional] 
**user_id** | **str** | The xero user identifier of the person who logged time. | [optional] 
**project_id** | **str** | Identifier of the project, that the task (which the time entry is logged against) belongs to. | [optional] 
**task_id** | **str** | Identifier of the task that time entry is logged against. | [optional] 
**date_utc** | **datetime** | The date time that time entry is logged on. UTC Date Time in ISO-8601 format. | [optional] 
**date_entered_utc** | **datetime** | The date time that time entry is created. UTC Date Time in ISO-8601 format. By default it is set to server time. | [optional] 
**duration** | **int** | The duration of logged minutes. | [optional] 
**description** | **str** | A description of the time entry. | [optional] 
**status** | **str** | Status of the time entry. By default a time entry is created with status of &#x60;ACTIVE&#x60;. A &#x60;LOCKED&#x60; state indicates that the time entry is currently changing state (for example being invoiced). Updates are not allowed when in this state. It will have a status of INVOICED once it is invoiced. | [optional] 

## Example

```python
from xero_python.models.time_entry import TimeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntry from a JSON string
time_entry_instance = TimeEntry.from_json(json)
# print the JSON string representation of the object
print TimeEntry.to_json()

# convert the object into a dict
time_entry_dict = time_entry_instance.to_dict()
# create an instance of TimeEntry from a dict
time_entry_from_dict = TimeEntry.from_dict(time_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


