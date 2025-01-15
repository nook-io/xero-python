# LeavePeriod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_units** | **float** | The Number of Units for the leave | [optional] 
**pay_period_end_date** | **str** | The Pay Period End Date (YYYY-MM-DD) | [optional] 
**pay_period_start_date** | **str** | The Pay Period Start Date (YYYY-MM-DD) | [optional] 
**leave_period_status** | [**LeavePeriodStatus**](LeavePeriodStatus.md) |  | [optional] 

## Example

```python
from xero_python.models.leave_period import LeavePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of LeavePeriod from a JSON string
leave_period_instance = LeavePeriod.from_json(json)
# print the JSON string representation of the object
print LeavePeriod.to_json()

# convert the object into a dict
leave_period_dict = leave_period_instance.to_dict()
# create an instance of LeavePeriod from a dict
leave_period_from_dict = LeavePeriod.from_dict(leave_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


