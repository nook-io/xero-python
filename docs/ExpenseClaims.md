# ExpenseClaims


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expense_claims** | [**List[ExpenseClaim]**](ExpenseClaim.md) |  | [optional] 

## Example

```python
from xero_python.models.expense_claims import ExpenseClaims

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseClaims from a JSON string
expense_claims_instance = ExpenseClaims.from_json(json)
# print the JSON string representation of the object
print ExpenseClaims.to_json()

# convert the object into a dict
expense_claims_dict = expense_claims_instance.to_dict()
# create an instance of ExpenseClaims from a dict
expense_claims_from_dict = ExpenseClaims.from_dict(expense_claims_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


