# WorkingWeek


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monday** | **float** | The number of hours worked on a Monday | 
**tuesday** | **float** | The number of hours worked on a Tuesday | 
**wednesday** | **float** | The number of hours worked on a Wednesday | 
**thursday** | **float** | The number of hours worked on a Thursday | 
**friday** | **float** | The number of hours worked on a Friday | 
**saturday** | **float** | The number of hours worked on a Saturday | 
**sunday** | **float** | The number of hours worked on a Sunday | 

## Example

```python
from xero_python.models.working_week import WorkingWeek

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingWeek from a JSON string
working_week_instance = WorkingWeek.from_json(json)
# print the JSON string representation of the object
print WorkingWeek.to_json()

# convert the object into a dict
working_week_dict = working_week_instance.to_dict()
# create an instance of WorkingWeek from a dict
working_week_from_dict = WorkingWeek.from_dict(working_week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


