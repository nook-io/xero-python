# CashValidationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The Xero identifier for an account | [optional] 
**statement_balance** | [**StatementBalanceResponse**](StatementBalanceResponse.md) |  | [optional] 
**statement_balance_date** | **date** | UTC Date when the last bank statement item was entered into Xero. This date is represented in ISO 8601 format. | [optional] 
**bank_statement** | [**BankStatementResponse**](BankStatementResponse.md) |  | [optional] 
**cash_account** | [**CashAccountResponse**](CashAccountResponse.md) |  | [optional] 

## Example

```python
from xero_python.models.cash_validation_response import CashValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashValidationResponse from a JSON string
cash_validation_response_instance = CashValidationResponse.from_json(json)
# print the JSON string representation of the object
print CashValidationResponse.to_json()

# convert the object into a dict
cash_validation_response_dict = cash_validation_response_instance.to_dict()
# create an instance of CashValidationResponse from a dict
cash_validation_response_from_dict = CashValidationResponse.from_dict(cash_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


