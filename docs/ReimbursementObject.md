# ReimbursementObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**reimbursement** | [**Reimbursement**](Reimbursement.md) |  | [optional] 

## Example

```python
from xero_python.models.reimbursement_object import ReimbursementObject

# TODO update the JSON string below
json = "{}"
# create an instance of ReimbursementObject from a JSON string
reimbursement_object_instance = ReimbursementObject.from_json(json)
# print the JSON string representation of the object
print ReimbursementObject.to_json()

# convert the object into a dict
reimbursement_object_dict = reimbursement_object_instance.to_dict()
# create an instance of ReimbursementObject from a dict
reimbursement_object_from_dict = ReimbursementObject.from_dict(reimbursement_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


