# ImportSummary

A summary of the import from setup endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**ImportSummaryAccounts**](ImportSummaryAccounts.md) |  | [optional] 
**organisation** | [**ImportSummaryOrganisation**](ImportSummaryOrganisation.md) |  | [optional] 

## Example

```python
from xero_python.models.import_summary import ImportSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ImportSummary from a JSON string
import_summary_instance = ImportSummary.from_json(json)
# print the JSON string representation of the object
print ImportSummary.to_json()

# convert the object into a dict
import_summary_dict = import_summary_instance.to_dict()
# create an instance of ImportSummary from a dict
import_summary_from_dict = ImportSummary.from_dict(import_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


