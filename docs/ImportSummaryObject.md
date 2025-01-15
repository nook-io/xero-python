# ImportSummaryObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_summary** | [**ImportSummary**](ImportSummary.md) |  | [optional] 

## Example

```python
from xero_python.models.import_summary_object import ImportSummaryObject

# TODO update the JSON string below
json = "{}"
# create an instance of ImportSummaryObject from a JSON string
import_summary_object_instance = ImportSummaryObject.from_json(json)
# print the JSON string representation of the object
print ImportSummaryObject.to_json()

# convert the object into a dict
import_summary_object_dict = import_summary_object_instance.to_dict()
# create an instance of ImportSummaryObject from a dict
import_summary_object_from_dict = ImportSummaryObject.from_dict(import_summary_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


