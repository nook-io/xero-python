# StatementBalanceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Total closing balance of the account. This includes both reconciled and unreconciled bank statement lines. The closing balance will always be represented as a positive number, with it’s debit/credit status defined in the statementBalanceDebitCredit field. | [optional] 
**type** | **str** | The DEBIT or CREDIT status of the account. Cash accounts in credit have a negative balance. | [optional] 

## Example

```python
from xero_python.models.statement_balance_response import StatementBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatementBalanceResponse from a JSON string
statement_balance_response_instance = StatementBalanceResponse.from_json(json)
# print the JSON string representation of the object
print StatementBalanceResponse.to_json()

# convert the object into a dict
statement_balance_response_dict = statement_balance_response_instance.to_dict()
# create an instance of StatementBalanceResponse from a dict
statement_balance_response_from_dict = StatementBalanceResponse.from_dict(statement_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


