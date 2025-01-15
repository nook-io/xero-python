# TrialBalanceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date of the report | [optional] 
**end_date** | **date** | End date of the report | [optional] 
**accounts** | [**List[TrialBalanceAccount]**](TrialBalanceAccount.md) | Refer to the accounts section below | [optional] 

## Example

```python
from xero_python.models.trial_balance_response import TrialBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceResponse from a JSON string
trial_balance_response_instance = TrialBalanceResponse.from_json(json)
# print the JSON string representation of the object
print TrialBalanceResponse.to_json()

# convert the object into a dict
trial_balance_response_dict = trial_balance_response_instance.to_dict()
# create an instance of TrialBalanceResponse from a dict
trial_balance_response_from_dict = TrialBalanceResponse.from_dict(trial_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


