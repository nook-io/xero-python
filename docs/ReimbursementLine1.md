# ReimbursementLine1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reimbursement_type_id** | **str** | Xero reimbursement type identifier | [optional] 
**amount** | **float** | Reimbursement type amount | [optional] 
**description** | **str** | Reimbursement lines description (max length 50) | [optional] 
**expense_account** | **str** | Reimbursement expense account. For posted pay run you should be able to see expense account code. | [optional] 

## Example

```python
from xero_python.models.reimbursement_line1 import ReimbursementLine1

# TODO update the JSON string below
json = "{}"
# create an instance of ReimbursementLine1 from a JSON string
reimbursement_line1_instance = ReimbursementLine1.from_json(json)
# print the JSON string representation of the object
print ReimbursementLine1.to_json()

# convert the object into a dict
reimbursement_line1_dict = reimbursement_line1_instance.to_dict()
# create an instance of ReimbursementLine1 from a dict
reimbursement_line1_from_dict = ReimbursementLine1.from_dict(reimbursement_line1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


