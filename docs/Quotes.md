# Quotes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotes** | [**List[Quote]**](Quote.md) |  | [optional] 

## Example

```python
from xero_python.models.quotes import Quotes

# TODO update the JSON string below
json = "{}"
# create an instance of Quotes from a JSON string
quotes_instance = Quotes.from_json(json)
# print the JSON string representation of the object
print Quotes.to_json()

# convert the object into a dict
quotes_dict = quotes_instance.to_dict()
# create an instance of Quotes from a dict
quotes_from_dict = Quotes.from_dict(quotes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


