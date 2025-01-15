# ReportFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from xero_python.models.report_fields import ReportFields

# TODO update the JSON string below
json = "{}"
# create an instance of ReportFields from a JSON string
report_fields_instance = ReportFields.from_json(json)
# print the JSON string representation of the object
print ReportFields.to_json()

# convert the object into a dict
report_fields_dict = report_fields_instance.to_dict()
# create an instance of ReportFields from a dict
report_fields_from_dict = ReportFields.from_dict(report_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


