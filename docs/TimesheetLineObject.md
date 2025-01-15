# TimesheetLineObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**timesheet_line** | [**TimesheetLine**](TimesheetLine.md) |  | [optional] 

## Example

```python
from xero_python.models.timesheet_line_object import TimesheetLineObject

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetLineObject from a JSON string
timesheet_line_object_instance = TimesheetLineObject.from_json(json)
# print the JSON string representation of the object
print TimesheetLineObject.to_json()

# convert the object into a dict
timesheet_line_object_dict = timesheet_line_object_instance.to_dict()
# create an instance of TimesheetLineObject from a dict
timesheet_line_object_from_dict = TimesheetLineObject.from_dict(timesheet_line_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


