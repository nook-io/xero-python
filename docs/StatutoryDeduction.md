# StatutoryDeduction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Xero identifier for earnings order | [optional] 
**name** | **str** | Name of the earnings order | [optional] 
**statutory_deduction_category** | [**StatutoryDeductionCategory**](StatutoryDeductionCategory.md) |  | [optional] 
**liability_account_id** | **str** | Xero identifier for Liability Account | [optional] 
**current_record** | **bool** | Identifier of a record is active or not. | [optional] 

## Example

```python
from xero_python.models.statutory_deduction import StatutoryDeduction

# TODO update the JSON string below
json = "{}"
# create an instance of StatutoryDeduction from a JSON string
statutory_deduction_instance = StatutoryDeduction.from_json(json)
# print the JSON string representation of the object
print StatutoryDeduction.to_json()

# convert the object into a dict
statutory_deduction_dict = statutory_deduction_instance.to_dict()
# create an instance of StatutoryDeduction from a dict
statutory_deduction_from_dict = StatutoryDeduction.from_dict(statutory_deduction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


