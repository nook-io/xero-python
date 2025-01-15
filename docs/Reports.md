# Reports


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[Report]**](Report.md) |  | [optional] 

## Example

```python
from xero_python.models.reports import Reports

# TODO update the JSON string below
json = "{}"
# create an instance of Reports from a JSON string
reports_instance = Reports.from_json(json)
# print the JSON string representation of the object
print Reports.to_json()

# convert the object into a dict
reports_dict = reports_instance.to_dict()
# create an instance of Reports from a dict
reports_from_dict = Reports.from_dict(reports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


