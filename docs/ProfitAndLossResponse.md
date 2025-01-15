# ProfitAndLossResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date of the report | [optional] 
**end_date** | **date** | End date of the report | [optional] 
**net_profit_loss** | **float** | Net profit loss value | [optional] 
**revenue** | [**PnlAccountClass**](PnlAccountClass.md) |  | [optional] 
**expense** | [**PnlAccountClass**](PnlAccountClass.md) |  | [optional] 

## Example

```python
from xero_python.models.profit_and_loss_response import ProfitAndLossResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProfitAndLossResponse from a JSON string
profit_and_loss_response_instance = ProfitAndLossResponse.from_json(json)
# print the JSON string representation of the object
print ProfitAndLossResponse.to_json()

# convert the object into a dict
profit_and_loss_response_dict = profit_and_loss_response_instance.to_dict()
# create an instance of ProfitAndLossResponse from a dict
profit_and_loss_response_from_dict = ProfitAndLossResponse.from_dict(profit_and_loss_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


