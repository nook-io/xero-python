# LeavePeriod1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start_date** | **date** | The Pay Period Start Date (YYYY-MM-DD) | [optional] 
**period_end_date** | **date** | The Pay Period End Date (YYYY-MM-DD) | [optional] 
**number_of_units** | **float** | The Number of Units for the leave | [optional] 
**period_status** | **str** | Period Status | [optional] 

## Example

```python
from xero_python.models.leave_period1 import LeavePeriod1

# TODO update the JSON string below
json = "{}"
# create an instance of LeavePeriod1 from a JSON string
leave_period1_instance = LeavePeriod1.from_json(json)
# print the JSON string representation of the object
print LeavePeriod1.to_json()

# convert the object into a dict
leave_period1_dict = leave_period1_instance.to_dict()
# create an instance of LeavePeriod1 from a dict
leave_period1_from_dict = LeavePeriod1.from_dict(leave_period1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


