# APIException

The object returned for a bad request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_number** | **float** | The error number | [optional] 
**type** | **str** | The type of error | [optional] 
**message** | **str** | The message describing the error | [optional] 

## Example

```python
from xero_python.models.api_exception import APIException

# TODO update the JSON string below
json = "{}"
# create an instance of APIException from a JSON string
api_exception_instance = APIException.from_json(json)
# print the JSON string representation of the object
print APIException.to_json()

# convert the object into a dict
api_exception_dict = api_exception_instance.to_dict()
# create an instance of APIException from a dict
api_exception_from_dict = APIException.from_dict(api_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


