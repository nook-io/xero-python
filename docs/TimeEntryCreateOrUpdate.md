# TimeEntryCreateOrUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The xero user identifier of the person logging the time. | 
**task_id** | **str** | Identifier of the task that time entry is logged against. | 
**date_utc** | **datetime** | Date time entry is logged on. UTC Date Time in ISO-8601 format. | 
**duration** | **int** | Number of minutes to be logged. Duration is between 1 and 59940 inclusively. | 
**description** | **str** | An optional description of the time entry, will be set to null if not provided during update. | [optional] 

## Example

```python
from xero_python.models.time_entry_create_or_update import TimeEntryCreateOrUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntryCreateOrUpdate from a JSON string
time_entry_create_or_update_instance = TimeEntryCreateOrUpdate.from_json(json)
# print the JSON string representation of the object
print TimeEntryCreateOrUpdate.to_json()

# convert the object into a dict
time_entry_create_or_update_dict = time_entry_create_or_update_instance.to_dict()
# create an instance of TimeEntryCreateOrUpdate from a dict
time_entry_create_or_update_from_dict = TimeEntryCreateOrUpdate.from_dict(time_entry_create_or_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


