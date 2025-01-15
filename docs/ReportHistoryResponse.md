# ReportHistoryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organisation_id** | **str** | The requested Organisation to which the data pertains | [optional] 
**end_date** | **date** | The end date of the report | [optional] 
**reports** | [**List[ReportHistoryModel]**](ReportHistoryModel.md) |  | [optional] 

## Example

```python
from xero_python.models.report_history_response import ReportHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportHistoryResponse from a JSON string
report_history_response_instance = ReportHistoryResponse.from_json(json)
# print the JSON string representation of the object
print ReportHistoryResponse.to_json()

# convert the object into a dict
report_history_response_dict = report_history_response_instance.to_dict()
# create an instance of ReportHistoryResponse from a dict
report_history_response_from_dict = ReportHistoryResponse.from_dict(report_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


