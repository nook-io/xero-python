# LeaveApplications


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leave_applications** | [**List[LeaveApplication]**](LeaveApplication.md) |  | [optional] 

## Example

```python
from xero_python.models.leave_applications import LeaveApplications

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveApplications from a JSON string
leave_applications_instance = LeaveApplications.from_json(json)
# print the JSON string representation of the object
print LeaveApplications.to_json()

# convert the object into a dict
leave_applications_dict = leave_applications_instance.to_dict()
# create an instance of LeaveApplications from a dict
leave_applications_from_dict = LeaveApplications.from_dict(leave_applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


