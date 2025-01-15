# AccountUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **str** | The month this usage item contains data for | [optional] 
**account_id** | **str** | The account this usage item contains data for | [optional] 
**currency_code** | **str** | The currency code this usage item contains data for | [optional] 
**total_received** | **float** | Total received | [optional] 
**count_received** | **int** | Count of received | [optional] 
**total_paid** | **float** | Total paid | [optional] 
**count_paid** | **int** | Count of paid | [optional] 
**total_manual_journal** | **float** | Total value of manual journals | [optional] 
**count_manual_journal** | **int** | Count of manual journals | [optional] 
**account_name** | **str** | The name of the account | [optional] 
**reporting_code** | **str** | Shown if set | [optional] 
**reporting_code_name** | **str** | Shown if set | [optional] 
**report_code_updated_date_utc** | **datetime** | Last modified date UTC format | [optional] 

## Example

```python
from xero_python.models.account_usage import AccountUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUsage from a JSON string
account_usage_instance = AccountUsage.from_json(json)
# print the JSON string representation of the object
print AccountUsage.to_json()

# convert the object into a dict
account_usage_dict = account_usage_instance.to_dict()
# create an instance of AccountUsage from a dict
account_usage_from_dict = AccountUsage.from_dict(account_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


