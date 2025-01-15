# ReimbursementLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reimbursement_type_id** | **str** | Xero identifier for payroll reimbursement | [optional] 
**description** | **str** | Reimbursement line description | [optional] 
**amount** | **float** | Reimbursement amount | [optional] 

## Example

```python
from xero_python.models.reimbursement_line import ReimbursementLine

# TODO update the JSON string below
json = "{}"
# create an instance of ReimbursementLine from a JSON string
reimbursement_line_instance = ReimbursementLine.from_json(json)
# print the JSON string representation of the object
print ReimbursementLine.to_json()

# convert the object into a dict
reimbursement_line_dict = reimbursement_line_instance.to_dict()
# create an instance of ReimbursementLine from a dict
reimbursement_line_from_dict = ReimbursementLine.from_dict(reimbursement_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


