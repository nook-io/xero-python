# Journal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journal_id** | **str** | Xero identifier | [optional] 
**journal_date** | **str** | Date the journal was posted | [optional] 
**journal_number** | **int** | Xero generated journal number | [optional] 
**created_date_utc** | **str** | Created date UTC format | [optional] [readonly] 
**reference** | **str** | reference field for additional indetifying information | [optional] 
**source_id** | **str** | The identifier for the source transaction (e.g. InvoiceID) | [optional] 
**source_type** | **str** | The journal source type. The type of transaction that created the journal | [optional] 
**journal_lines** | [**List[JournalLine]**](JournalLine.md) | See JournalLines | [optional] 

## Example

```python
from xero_python.models.journal import Journal

# TODO update the JSON string below
json = "{}"
# create an instance of Journal from a JSON string
journal_instance = Journal.from_json(json)
# print the JSON string representation of the object
print Journal.to_json()

# convert the object into a dict
journal_dict = journal_instance.to_dict()
# create an instance of Journal from a dict
journal_from_dict = Journal.from_dict(journal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


