# Error2

On error, the API consumer will receive an HTTP response with a HTTP Status Code of 4xx or 5xx and a Content-Type of application/problem+json.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Human readable high level error description. | [optional] 
**status** | **int** | The numeric HTTP Status Code, e.g. 404 | [optional] 
**detail** | **str** | Human readable detailed error description. | [optional] 
**type** | **str** | Identifies the type of error. | [optional] 

## Example

```python
from xero_python.models.error2 import Error2

# TODO update the JSON string below
json = "{}"
# create an instance of Error2 from a JSON string
error2_instance = Error2.from_json(json)
# print the JSON string representation of the object
print Error2.to_json()

# convert the object into a dict
error2_dict = error2_instance.to_dict()
# create an instance of Error2 from a dict
error2_from_dict = Error2.from_dict(error2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


