# JournalLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journal_line_id** | **str** | Xero identifier for Journal | [optional] 
**account_id** | **str** | See Accounts | [optional] 
**account_code** | **str** | See Accounts | [optional] 
**account_type** | [**AccountType**](AccountType.md) |  | [optional] 
**account_name** | **str** | See AccountCodes | [optional] 
**description** | **str** | The description from the source transaction line item. Only returned if populated. | [optional] 
**net_amount** | **float** | Net amount of journal line. This will be a positive value for a debit and negative for a credit | [optional] 
**gross_amount** | **float** | Gross amount of journal line (NetAmount + TaxAmount). | [optional] 
**tax_amount** | **float** | Total tax on a journal line | [optional] [readonly] 
**tax_type** | **str** | The tax type from taxRates | [optional] 
**tax_name** | **str** | see TaxRates | [optional] 
**tracking_categories** | [**List[TrackingCategory]**](TrackingCategory.md) | Optional Tracking Category – see Tracking. Any JournalLine can have a maximum of 2 &lt;TrackingCategory&gt; elements. | [optional] 

## Example

```python
from xero_python.models.journal_line import JournalLine

# TODO update the JSON string below
json = "{}"
# create an instance of JournalLine from a JSON string
journal_line_instance = JournalLine.from_json(json)
# print the JSON string representation of the object
print JournalLine.to_json()

# convert the object into a dict
journal_line_dict = journal_line_instance.to_dict()
# create an instance of JournalLine from a dict
journal_line_from_dict = JournalLine.from_dict(journal_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


