# Reimbursement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reimbursement_id** | **str** | Xero unique identifier for a reimbursement | [optional] 
**name** | **str** | Name of the reimbursement | 
**account_id** | **str** | Xero unique identifier for the account used for the reimbursement | 
**current_record** | **bool** | Indicates that whether the reimbursement is active | [optional] 

## Example

```python
from xero_python.models.reimbursement import Reimbursement

# TODO update the JSON string below
json = "{}"
# create an instance of Reimbursement from a JSON string
reimbursement_instance = Reimbursement.from_json(json)
# print the JSON string representation of the object
print Reimbursement.to_json()

# convert the object into a dict
reimbursement_dict = reimbursement_instance.to_dict()
# create an instance of Reimbursement from a dict
reimbursement_from_dict = Reimbursement.from_dict(reimbursement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


