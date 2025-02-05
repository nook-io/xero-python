# Benefit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | unique identifier in Xero | [optional] 
**name** | **str** | Name of the employer pension | 
**category** | **str** | Category type of the employer pension | 
**liability_account_id** | **str** | Xero identifier for Liability Account | 
**expense_account_id** | **str** | Xero identifier for Expense Account | 
**standard_amount** | **float** | Standard amount of the employer pension | [optional] 
**percentage** | **float** | Percentage of gross of the employer pension | 
**calculation_type** | **str** | Calculation Type of the employer pension (FixedAmount or PercentageOfGross). | 
**current_record** | **bool** | Identifier of a record is active or not. | [optional] 
**subject_to_nic** | **bool** | Identifier of subject To NIC | [optional] 
**subject_to_pension** | **bool** | Identifier of subject To pension | [optional] 
**subject_to_tax** | **bool** | Identifier of subject To Tax | [optional] 
**is_calculating_on_qualifying_earnings** | **bool** | Identifier of calculating on qualifying earnings | [optional] 
**show_balance_to_employee** | **bool** | display the balance to employee | [optional] 

## Example

```python
from xero_python.models.benefit import Benefit

# TODO update the JSON string below
json = "{}"
# create an instance of Benefit from a JSON string
benefit_instance = Benefit.from_json(json)
# print the JSON string representation of the object
print Benefit.to_json()

# convert the object into a dict
benefit_dict = benefit_instance.to_dict()
# create an instance of Benefit from a dict
benefit_from_dict = Benefit.from_dict(benefit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


