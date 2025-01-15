# TrialBalanceMovement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debits** | **float** | Debit amount | [optional] 
**credits** | **float** | Credit amount | [optional] 
**movement** | [**TrialBalanceEntry**](TrialBalanceEntry.md) |  | [optional] 
**signed_movement** | **float** | Value of movement. Expense and Asset accounts code debits as positive. Revenue, Liability, and Equity accounts code debits as negative | [optional] 

## Example

```python
from xero_python.models.trial_balance_movement import TrialBalanceMovement

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceMovement from a JSON string
trial_balance_movement_instance = TrialBalanceMovement.from_json(json)
# print the JSON string representation of the object
print TrialBalanceMovement.to_json()

# convert the object into a dict
trial_balance_movement_dict = trial_balance_movement_instance.to_dict()
# create an instance of TrialBalanceMovement from a dict
trial_balance_movement_from_dict = TrialBalanceMovement.from_dict(trial_balance_movement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


