# ReportWithRow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** | ID of the Report | [optional] 
**report_name** | **str** | Name of the report | [optional] 
**report_title** | **str** | Title of the report | [optional] 
**report_type** | **str** | The type of report (BalanceSheet,ProfitLoss, etc) | [optional] 
**report_titles** | **List[str]** | Report titles array (3 to 4 strings with the report name, orgnisation name and time frame of report) | [optional] 
**report_date** | **str** | Date of report | [optional] 
**rows** | [**List[ReportRows]**](ReportRows.md) |  | [optional] 
**updated_date_utc** | **str** | Updated Date | [optional] [readonly] 
**fields** | [**List[ReportFields]**](ReportFields.md) |  | [optional] 

## Example

```python
from xero_python.models.report_with_row import ReportWithRow

# TODO update the JSON string below
json = "{}"
# create an instance of ReportWithRow from a JSON string
report_with_row_instance = ReportWithRow.from_json(json)
# print the JSON string representation of the object
print ReportWithRow.to_json()

# convert the object into a dict
report_with_row_dict = report_with_row_instance.to_dict()
# create an instance of ReportWithRow from a dict
report_with_row_from_dict = ReportWithRow.from_dict(report_with_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


