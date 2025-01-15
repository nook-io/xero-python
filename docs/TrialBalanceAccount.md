# TrialBalanceAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account | [optional] 
**account_type** | **str** | The type of the account. See &lt;a href&#x3D;&#39;https://developer.xero.com/documentation/api/types#AccountTypes&#39;&gt;Account Types&lt;/a&gt; | [optional] 
**account_code** | **str** | Customer defined alpha numeric account code e.g 200 or SALES | [optional] 
**account_class** | **str** | The class of the account. See &lt;a href&#x3D;&#39;https://developer.xero.com/documentation/api/types#AccountClassTypes&#39;&gt;Account Class Types&lt;/a&gt; | [optional] 
**status** | **str** | Accounts with a status of ACTIVE can be updated to ARCHIVED. See &lt;a href&#x3D;&#39;https://developer.xero.com/documentation/api/types#AccountStatusCodes&#39;&gt;Account Status Codes&lt;/a&gt; | [optional] 
**reporting_code** | **str** | Reporting code (Shown if set) | [optional] 
**account_name** | **str** | Name of the account | [optional] 
**balance** | [**TrialBalanceEntry**](TrialBalanceEntry.md) |  | [optional] 
**signed_balance** | **float** | Value of balance. Expense and Asset accounts code debits as positive. Revenue, Liability, and Equity accounts code debits as negative | [optional] 
**account_movement** | [**TrialBalanceMovement**](TrialBalanceMovement.md) |  | [optional] 

## Example

```python
from xero_python.models.trial_balance_account import TrialBalanceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceAccount from a JSON string
trial_balance_account_instance = TrialBalanceAccount.from_json(json)
# print the JSON string representation of the object
print TrialBalanceAccount.to_json()

# convert the object into a dict
trial_balance_account_dict = trial_balance_account_instance.to_dict()
# create an instance of TrialBalanceAccount from a dict
trial_balance_account_from_dict = TrialBalanceAccount.from_dict(trial_balance_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


