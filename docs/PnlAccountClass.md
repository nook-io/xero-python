# PnlAccountClass


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | Total revenue/expense value | [optional] 
**account_types** | [**List[PnlAccountType]**](PnlAccountType.md) | Contains trading income and other income for revenue section / operating expenses and direct cost for expense section if the data is available for each section. Refer to the account type element below | [optional] 

## Example

```python
from xero_python.models.pnl_account_class import PnlAccountClass

# TODO update the JSON string below
json = "{}"
# create an instance of PnlAccountClass from a JSON string
pnl_account_class_instance = PnlAccountClass.from_json(json)
# print the JSON string representation of the object
print PnlAccountClass.to_json()

# convert the object into a dict
pnl_account_class_dict = pnl_account_class_instance.to_dict()
# create an instance of PnlAccountClass from a dict
pnl_account_class_from_dict = PnlAccountClass.from_dict(pnl_account_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


