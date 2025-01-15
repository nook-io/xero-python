# TimesheetObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**timesheet** | [**Timesheet**](Timesheet.md) |  | [optional] 

## Example

```python
from xero_python.models.timesheet_object import TimesheetObject

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetObject from a JSON string
timesheet_object_instance = TimesheetObject.from_json(json)
# print the JSON string representation of the object
print TimesheetObject.to_json()

# convert the object into a dict
timesheet_object_dict = timesheet_object_instance.to_dict()
# create an instance of TimesheetObject from a dict
timesheet_object_from_dict = TimesheetObject.from_dict(timesheet_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


