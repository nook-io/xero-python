# ConversionDate

The date when the organisation starts using Xero

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | The month the organisation starts using Xero. Value is an integer between 1 and 12 | [optional] 
**year** | **int** | The year the organisation starts using Xero. Value is an integer greater than 2006 | [optional] 

## Example

```python
from xero_python.models.conversion_date import ConversionDate

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionDate from a JSON string
conversion_date_instance = ConversionDate.from_json(json)
# print the JSON string representation of the object
print ConversionDate.to_json()

# convert the object into a dict
conversion_date_dict = conversion_date_instance.to_dict()
# create an instance of ConversionDate from a dict
conversion_date_from_dict = ConversionDate.from_dict(conversion_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


