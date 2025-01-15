# PnlAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account | [optional] 
**account_type** | **str** | The type of the account. See &lt;a href&#x3D;&#39;https://developer.xero.com/documentation/api/types#AccountTypes&#39;&gt;Account Types&lt;/a&gt; | [optional] 
**code** | **str** | Account code | [optional] 
**name** | **str** | Account name | [optional] 
**reporting_code** | **str** | Reporting code (Shown if set) | [optional] 
**total** | **float** | Total movement on this account | [optional] 

## Example

```python
from xero_python.models.pnl_account import PnlAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PnlAccount from a JSON string
pnl_account_instance = PnlAccount.from_json(json)
# print the JSON string representation of the object
print PnlAccount.to_json()

# convert the object into a dict
pnl_account_dict = pnl_account_instance.to_dict()
# create an instance of PnlAccount from a dict
pnl_account_from_dict = PnlAccount.from_dict(pnl_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


