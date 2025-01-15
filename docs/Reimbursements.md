# Reimbursements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**problem** | [**Problem**](Problem.md) |  | [optional] 
**reimbursements** | [**List[Reimbursement]**](Reimbursement.md) |  | [optional] 

## Example

```python
from xero_python.models.reimbursements import Reimbursements

# TODO update the JSON string below
json = "{}"
# create an instance of Reimbursements from a JSON string
reimbursements_instance = Reimbursements.from_json(json)
# print the JSON string representation of the object
print Reimbursements.to_json()

# convert the object into a dict
reimbursements_dict = reimbursements_instance.to_dict()
# create an instance of Reimbursements from a dict
reimbursements_from_dict = Reimbursements.from_dict(reimbursements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


