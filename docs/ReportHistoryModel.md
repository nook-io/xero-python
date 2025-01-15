# ReportHistoryModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_name** | **str** | Report code or report title | [optional] 
**report_date_text** | **str** | The date or date range of the report | [optional] 
**published_date_utc** | **datetime** | The system date time that the report was published | [optional] 

## Example

```python
from xero_python.models.report_history_model import ReportHistoryModel

# TODO update the JSON string below
json = "{}"
# create an instance of ReportHistoryModel from a JSON string
report_history_model_instance = ReportHistoryModel.from_json(json)
# print the JSON string representation of the object
print ReportHistoryModel.to_json()

# convert the object into a dict
report_history_model_dict = report_history_model_instance.to_dict()
# create an instance of ReportHistoryModel from a dict
report_history_model_from_dict = ReportHistoryModel.from_dict(report_history_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


