# ReportAttribute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from xero_python.models.report_attribute import ReportAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ReportAttribute from a JSON string
report_attribute_instance = ReportAttribute.from_json(json)
# print the JSON string representation of the object
print ReportAttribute.to_json()

# convert the object into a dict
report_attribute_dict = report_attribute_instance.to_dict()
# create an instance of ReportAttribute from a dict
report_attribute_from_dict = ReportAttribute.from_dict(report_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


