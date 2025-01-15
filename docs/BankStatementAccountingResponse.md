# BankStatementAccountingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_account_id** | **str** | Xero Identifier of bank account | [optional] 
**bank_account_name** | **str** | Name of bank account | [optional] 
**bank_account_currency_code** | **str** | Currency code of the bank account | [optional] 
**statements** | [**List[StatementResponse]**](StatementResponse.md) | List of bank statements and linked accounting data for the requested period | [optional] 

## Example

```python
from xero_python.models.bank_statement_accounting_response import BankStatementAccountingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BankStatementAccountingResponse from a JSON string
bank_statement_accounting_response_instance = BankStatementAccountingResponse.from_json(json)
# print the JSON string representation of the object
print BankStatementAccountingResponse.to_json()

# convert the object into a dict
bank_statement_accounting_response_dict = bank_statement_accounting_response_instance.to_dict()
# create an instance of BankStatementAccountingResponse from a dict
bank_statement_accounting_response_from_dict = BankStatementAccountingResponse.from_dict(bank_statement_accounting_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


