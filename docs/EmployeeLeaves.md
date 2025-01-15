# EmployeeLeaves


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**leave** | [**List[EmployeeLeave1]**](EmployeeLeave1.md) |  | [optional] 

## Example

```python
from xero_python.models.employee_leaves import EmployeeLeaves

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeLeaves from a JSON string
employee_leaves_instance = EmployeeLeaves.from_json(json)
# print the JSON string representation of the object
print EmployeeLeaves.to_json()

# convert the object into a dict
employee_leaves_dict = employee_leaves_instance.to_dict()
# create an instance of EmployeeLeaves from a dict
employee_leaves_from_dict = EmployeeLeaves.from_dict(employee_leaves_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


