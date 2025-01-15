# LeaveAccrualLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leave_type_id** | **str** | Xero identifier for the Leave type | [optional] 
**number_of_units** | **float** | Leave accrual number of units | [optional] 

## Example

```python
from xero_python.models.leave_accrual_line import LeaveAccrualLine

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveAccrualLine from a JSON string
leave_accrual_line_instance = LeaveAccrualLine.from_json(json)
# print the JSON string representation of the object
print LeaveAccrualLine.to_json()

# convert the object into a dict
leave_accrual_line_dict = leave_accrual_line_instance.to_dict()
# create an instance of LeaveAccrualLine from a dict
leave_accrual_line_from_dict = LeaveAccrualLine.from_dict(leave_accrual_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


