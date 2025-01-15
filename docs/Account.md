# Account


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Customer defined alpha numeric account code e.g 200 or SALES (max length &#x3D; 10) | [optional] 
**name** | **str** | Name of account (max length &#x3D; 150) | [optional] 
**account_id** | **str** | The Xero identifier for an account – specified as a string following  the endpoint name   e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9 | [optional] 
**type** | [**AccountType**](AccountType.md) |  | [optional] 
**bank_account_number** | **str** | For bank accounts only (Account Type BANK) | [optional] 
**status** | **str** | Accounts with a status of ACTIVE can be updated to ARCHIVED. See Account Status Codes | [optional] 
**description** | **str** | Description of the Account. Valid for all types of accounts except bank accounts (max length &#x3D; 4000) | [optional] 
**bank_account_type** | **str** | For bank accounts only. See Bank Account types | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**tax_type** | **str** | The tax type from taxRates | [optional] 
**enable_payments_to_account** | **bool** | Boolean – describes whether account can have payments applied to it | [optional] 
**show_in_expense_claims** | **bool** | Boolean – describes whether account code is available for use with expense claims | [optional] 
**var_class** | **str** | See Account Class Types | [optional] [readonly] 
**system_account** | **str** | If this is a system account then this element is returned. See System Account types. Note that non-system accounts may have this element set as either “” or null. | [optional] [readonly] 
**reporting_code** | **str** | Shown if set | [optional] 
**reporting_code_name** | **str** | Shown if set | [optional] [readonly] 
**has_attachments** | **bool** | boolean to indicate if an account has an attachment (read only) | [optional] [readonly] [default to False]
**updated_date_utc** | **str** | Last modified date UTC format | [optional] [readonly] 
**add_to_watchlist** | **bool** | Boolean – describes whether the account is shown in the watchlist widget on the dashboard | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

## Example

```python
from xero_python.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print Account.to_json()

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


