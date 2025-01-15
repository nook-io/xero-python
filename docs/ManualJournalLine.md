# ManualJournalLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_amount** | **float** | total for line. Debits are positive, credits are negative value | [optional] 
**account_code** | **str** | See Accounts | [optional] 
**account_id** | **str** | See Accounts | [optional] 
**description** | **str** | Description for journal line | [optional] 
**tax_type** | **str** | The tax type from TaxRates | [optional] 
**tracking** | [**List[TrackingCategory]**](TrackingCategory.md) | Optional Tracking Category – see Tracking. Any JournalLine can have a maximum of 2 &lt;TrackingCategory&gt; elements. | [optional] 
**tax_amount** | **float** | The calculated tax amount based on the TaxType and LineAmount | [optional] 
**is_blank** | **bool** | is the line blank | [optional] 

## Example

```python
from xero_python.models.manual_journal_line import ManualJournalLine

# TODO update the JSON string below
json = "{}"
# create an instance of ManualJournalLine from a JSON string
manual_journal_line_instance = ManualJournalLine.from_json(json)
# print the JSON string representation of the object
print ManualJournalLine.to_json()

# convert the object into a dict
manual_journal_line_dict = manual_journal_line_instance.to_dict()
# create an instance of ManualJournalLine from a dict
manual_journal_line_from_dict = ManualJournalLine.from_dict(manual_journal_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


