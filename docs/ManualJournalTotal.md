# ManualJournalTotal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | Total value of manual journals. | [optional] 

## Example

```python
from xero_python.models.manual_journal_total import ManualJournalTotal

# TODO update the JSON string below
json = "{}"
# create an instance of ManualJournalTotal from a JSON string
manual_journal_total_instance = ManualJournalTotal.from_json(json)
# print the JSON string representation of the object
print ManualJournalTotal.to_json()

# convert the object into a dict
manual_journal_total_dict = manual_journal_total_instance.to_dict()
# create an instance of ManualJournalTotal from a dict
manual_journal_total_from_dict = ManualJournalTotal.from_dict(manual_journal_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


