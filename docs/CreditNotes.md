# CreditNotes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination1**](Pagination1.md) |  | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**credit_notes** | [**List[CreditNote]**](CreditNote.md) |  | [optional] 

## Example

```python
from xero_python.models.credit_notes import CreditNotes

# TODO update the JSON string below
json = "{}"
# create an instance of CreditNotes from a JSON string
credit_notes_instance = CreditNotes.from_json(json)
# print the JSON string representation of the object
print CreditNotes.to_json()

# convert the object into a dict
credit_notes_dict = credit_notes_instance.to_dict()
# create an instance of CreditNotes from a dict
credit_notes_from_dict = CreditNotes.from_dict(credit_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


