# Currency


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**description** | **str** | Name of Currency | [optional] 

## Example

```python
from xero_python.models.currency import Currency

# TODO update the JSON string below
json = "{}"
# create an instance of Currency from a JSON string
currency_instance = Currency.from_json(json)
# print the JSON string representation of the object
print Currency.to_json()

# convert the object into a dict
currency_dict = currency_instance.to_dict()
# create an instance of Currency from a dict
currency_from_dict = Currency.from_dict(currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


