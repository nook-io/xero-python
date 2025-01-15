# ManualJournal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**narration** | **str** | Description of journal being posted | 
**journal_lines** | [**List[ManualJournalLine]**](ManualJournalLine.md) | See JournalLines | [optional] 
**var_date** | **str** | Date journal was posted – YYYY-MM-DD | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**status** | **str** | See Manual Journal Status Codes | [optional] 
**url** | **str** | Url link to a source document – shown as “Go to [appName]” in the Xero app | [optional] 
**show_on_cash_basis_reports** | **bool** | Boolean – default is true if not specified | [optional] 
**has_attachments** | **bool** | Boolean to indicate if a manual journal has an attachment | [optional] [readonly] [default to False]
**updated_date_utc** | **str** | Last modified date UTC format | [optional] [readonly] 
**manual_journal_id** | **str** | The Xero identifier for a Manual Journal | [optional] 
**status_attribute_string** | **str** | A string to indicate if a invoice status | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**attachments** | [**List[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 

## Example

```python
from xero_python.models.manual_journal import ManualJournal

# TODO update the JSON string below
json = "{}"
# create an instance of ManualJournal from a JSON string
manual_journal_instance = ManualJournal.from_json(json)
# print the JSON string representation of the object
print ManualJournal.to_json()

# convert the object into a dict
manual_journal_dict = manual_journal_instance.to_dict()
# create an instance of ManualJournal from a dict
manual_journal_from_dict = ManualJournal.from_dict(manual_journal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


