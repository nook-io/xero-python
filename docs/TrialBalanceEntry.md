# TrialBalanceEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Net movement or net balance in the account | [optional] 
**entry_type** | **str** | Sign (Debit/Credit) of the movement of balance in the account | [optional] 

## Example

```python
from xero_python.models.trial_balance_entry import TrialBalanceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceEntry from a JSON string
trial_balance_entry_instance = TrialBalanceEntry.from_json(json)
# print the JSON string representation of the object
print TrialBalanceEntry.to_json()

# convert the object into a dict
trial_balance_entry_dict = trial_balance_entry_instance.to_dict()
# create an instance of TrialBalanceEntry from a dict
trial_balance_entry_from_dict = TrialBalanceEntry.from_dict(trial_balance_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


