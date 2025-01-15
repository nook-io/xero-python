# Timesheets


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**timesheets** | [**List[Timesheet]**](Timesheet.md) |  | [optional] 

## Example

```python
from xero_python.models.timesheets import Timesheets

# TODO update the JSON string below
json = "{}"
# create an instance of Timesheets from a JSON string
timesheets_instance = Timesheets.from_json(json)
# print the JSON string representation of the object
print Timesheets.to_json()

# convert the object into a dict
timesheets_dict = timesheets_instance.to_dict()
# create an instance of Timesheets from a dict
timesheets_from_dict = Timesheets.from_dict(timesheets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


