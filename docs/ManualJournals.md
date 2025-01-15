# ManualJournals


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination1**](Pagination1.md) |  | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**manual_journals** | [**List[ManualJournal]**](ManualJournal.md) |  | [optional] 

## Example

```python
from xero_python.models.manual_journals import ManualJournals

# TODO update the JSON string below
json = "{}"
# create an instance of ManualJournals from a JSON string
manual_journals_instance = ManualJournals.from_json(json)
# print the JSON string representation of the object
print ManualJournals.to_json()

# convert the object into a dict
manual_journals_dict = manual_journals_instance.to_dict()
# create an instance of ManualJournals from a dict
manual_journals_from_dict = ManualJournals.from_dict(manual_journals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


