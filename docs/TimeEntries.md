# TimeEntries


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination2**](Pagination2.md) |  | [optional] 
**items** | [**List[TimeEntry]**](TimeEntry.md) |  | [optional] 

## Example

```python
from xero_python.models.time_entries import TimeEntries

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntries from a JSON string
time_entries_instance = TimeEntries.from_json(json)
# print the JSON string representation of the object
print TimeEntries.to_json()

# convert the object into a dict
time_entries_dict = time_entries_instance.to_dict()
# create an instance of TimeEntries from a dict
time_entries_from_dict = TimeEntries.from_dict(time_entries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


