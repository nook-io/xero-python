# ReportCell


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**attributes** | [**List[ReportAttribute]**](ReportAttribute.md) |  | [optional] 

## Example

```python
from xero_python.models.report_cell import ReportCell

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCell from a JSON string
report_cell_instance = ReportCell.from_json(json)
# print the JSON string representation of the object
print ReportCell.to_json()

# convert the object into a dict
report_cell_dict = report_cell_instance.to_dict()
# create an instance of ReportCell from a dict
report_cell_from_dict = ReportCell.from_dict(report_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


