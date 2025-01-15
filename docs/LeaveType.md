# LeaveType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the earnings rate (max length &#x3D; 100) | [optional] 
**type_of_units** | **str** | The type of units by which leave entitlements are normally tracked. These are typically the same as the type of units used for the employee’s ordinary earnings rate | [optional] 
**leave_type_id** | **str** | Xero identifier | [optional] 
**normal_entitlement** | **float** | The number of units the employee is entitled to each year | [optional] 
**leave_loading_rate** | **float** | Enter an amount here if your organisation pays an additional percentage on top of ordinary earnings when your employees take leave (typically 17.5%) | [optional] 
**updated_date_utc** | **str** | Last modified timestamp | [optional] [readonly] 
**is_paid_leave** | **bool** | Set this to indicate that an employee will be paid when taking this type of leave | [optional] 
**show_on_payslip** | **bool** | Set this if you want a balance for this leave type to be shown on your employee’s payslips | [optional] 
**current_record** | **bool** | Is the current record | [optional] 
**leave_category_code** | [**LeaveCategoryCode**](LeaveCategoryCode.md) |  | [optional] 
**sgc_exempt** | **bool** | Set this to indicate that the leave type is exempt from superannuation guarantee contribution | [optional] 

## Example

```python
from xero_python.models.leave_type import LeaveType

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveType from a JSON string
leave_type_instance = LeaveType.from_json(json)
# print the JSON string representation of the object
print LeaveType.to_json()

# convert the object into a dict
leave_type_dict = leave_type_instance.to_dict()
# create an instance of LeaveType from a dict
leave_type_from_dict = LeaveType.from_dict(leave_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


