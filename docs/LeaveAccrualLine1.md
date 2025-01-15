# LeaveAccrualLine1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leave_type_id** | **str** | Xero identifier for the Leave type. | [optional] 
**number_of_units** | **float** | Leave Accrual number of units | [optional] 
**auto_calculate** | **bool** | If you want to auto calculate leave. | [optional] 

## Example

```python
from xero_python.models.leave_accrual_line1 import LeaveAccrualLine1

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveAccrualLine1 from a JSON string
leave_accrual_line1_instance = LeaveAccrualLine1.from_json(json)
# print the JSON string representation of the object
print LeaveAccrualLine1.to_json()

# convert the object into a dict
leave_accrual_line1_dict = leave_accrual_line1_instance.to_dict()
# create an instance of LeaveAccrualLine1 from a dict
leave_accrual_line1_from_dict = LeaveAccrualLine1.from_dict(leave_accrual_line1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


