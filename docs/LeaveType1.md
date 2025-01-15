# LeaveType1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leave_id** | **str** | Xero unique identifier for the leave | [optional] 
**leave_type_id** | **str** | Xero unique identifier for the leave type | [optional] 
**name** | **str** | Name of the leave type | 
**is_paid_leave** | **bool** | Indicate that an employee will be paid when taking this type of leave | 
**show_on_payslip** | **bool** | Indicate that a balance for this leave type to be shown on the employee’s payslips | 
**updated_date_utc** | **datetime** | UTC timestamp of last update to the leave type note | [optional] 
**is_active** | **bool** | Shows whether the leave type is active or not | [optional] 
**is_statutory_leave** | **bool** | Shows whether the leave type is a statutory leave type or not | [optional] 

## Example

```python
from xero_python.models.leave_type1 import LeaveType1

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveType1 from a JSON string
leave_type1_instance = LeaveType1.from_json(json)
# print the JSON string representation of the object
print LeaveType1.to_json()

# convert the object into a dict
leave_type1_dict = leave_type1_instance.to_dict()
# create an instance of LeaveType1 from a dict
leave_type1_from_dict = LeaveType1.from_dict(leave_type1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


