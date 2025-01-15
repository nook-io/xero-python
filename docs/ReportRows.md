# ReportRows


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_type** | [**RowType**](RowType.md) |  | [optional] 
**title** | **str** |  | [optional] 
**cells** | [**List[ReportCell]**](ReportCell.md) |  | [optional] 
**rows** | [**List[ReportRow]**](ReportRow.md) |  | [optional] 

## Example

```python
from xero_python.models.report_rows import ReportRows

# TODO update the JSON string below
json = "{}"
# create an instance of ReportRows from a JSON string
report_rows_instance = ReportRows.from_json(json)
# print the JSON string representation of the object
print ReportRows.to_json()

# convert the object into a dict
report_rows_dict = report_rows_instance.to_dict()
# create an instance of ReportRows from a dict
report_rows_from_dict = ReportRows.from_dict(report_rows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


