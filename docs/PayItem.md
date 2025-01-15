# PayItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earnings_rates** | [**List[EarningsRate1]**](EarningsRate1.md) |  | [optional] 
**deduction_types** | [**List[DeductionType]**](DeductionType.md) |  | [optional] 
**leave_types** | [**List[LeaveType]**](LeaveType.md) |  | [optional] 
**reimbursement_types** | [**List[ReimbursementType]**](ReimbursementType.md) |  | [optional] 

## Example

```python
from xero_python.models.pay_item import PayItem

# TODO update the JSON string below
json = "{}"
# create an instance of PayItem from a JSON string
pay_item_instance = PayItem.from_json(json)
# print the JSON string representation of the object
print PayItem.to_json()

# convert the object into a dict
pay_item_dict = pay_item_instance.to_dict()
# create an instance of PayItem from a dict
pay_item_from_dict = PayItem.from_dict(pay_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


