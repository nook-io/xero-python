# CashflowAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account | [optional] 
**account_type** | **str** | The type of the account. See &lt;a href&#x3D;&#39;https://developer.xero.com/documentation/api/types#AccountTypes&#39;&gt;Account Types&lt;/a&gt; | [optional] 
**account_class** | **str** | The class of the account. See &lt;a href&#x3D;&#39;https://developer.xero.com/documentation/api/types#AccountClassTypes&#39;&gt;Account Class Types&lt;/a&gt; | [optional] 
**code** | **str** | Account code | [optional] 
**name** | **str** | Account name | [optional] 
**reporting_code** | **str** | Reporting code used for cash flow classification | [optional] 
**total** | **float** | Total amount for the account | [optional] 

## Example

```python
from xero_python.models.cashflow_account import CashflowAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowAccount from a JSON string
cashflow_account_instance = CashflowAccount.from_json(json)
# print the JSON string representation of the object
print CashflowAccount.to_json()

# convert the object into a dict
cashflow_account_dict = cashflow_account_instance.to_dict()
# create an instance of CashflowAccount from a dict
cashflow_account_from_dict = CashflowAccount.from_dict(cashflow_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


