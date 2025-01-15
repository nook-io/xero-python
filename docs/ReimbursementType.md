# ReimbursementType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the earnings rate (max length &#x3D; 100) | [optional] 
**account_code** | **str** | See Accounts | [optional] 
**reimbursement_type_id** | **str** | Xero identifier | [optional] 
**updated_date_utc** | **str** | Last modified timestamp | [optional] [readonly] 
**current_record** | **bool** | Is the current record | [optional] 

## Example

```python
from xero_python.models.reimbursement_type import ReimbursementType

# TODO update the JSON string below
json = "{}"
# create an instance of ReimbursementType from a JSON string
reimbursement_type_instance = ReimbursementType.from_json(json)
# print the JSON string representation of the object
print ReimbursementType.to_json()

# convert the object into a dict
reimbursement_type_dict = reimbursement_type_instance.to_dict()
# create an instance of ReimbursementType from a dict
reimbursement_type_from_dict = ReimbursementType.from_dict(reimbursement_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


