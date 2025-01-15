# CashflowResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date of the report | [optional] 
**end_date** | **date** | End date of the report | [optional] 
**cash_balance** | [**CashBalance**](CashBalance.md) |  | [optional] 
**cashflow_activities** | [**List[CashflowActivity]**](CashflowActivity.md) | Break down of cash and cash equivalents for the period | [optional] 

## Example

```python
from xero_python.models.cashflow_response import CashflowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowResponse from a JSON string
cashflow_response_instance = CashflowResponse.from_json(json)
# print the JSON string representation of the object
print CashflowResponse.to_json()

# convert the object into a dict
cashflow_response_dict = cashflow_response_instance.to_dict()
# create an instance of CashflowResponse from a dict
cashflow_response_from_dict = CashflowResponse.from_dict(cashflow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


