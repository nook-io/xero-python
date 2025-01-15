# RequestEmpty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Need at least one field to create an empty JSON payload | [optional] 

## Example

```python
from xero_python.models.request_empty import RequestEmpty

# TODO update the JSON string below
json = "{}"
# create an instance of RequestEmpty from a JSON string
request_empty_instance = RequestEmpty.from_json(json)
# print the JSON string representation of the object
print RequestEmpty.to_json()

# convert the object into a dict
request_empty_dict = request_empty_instance.to_dict()
# create an instance of RequestEmpty from a dict
request_empty_from_dict = RequestEmpty.from_dict(request_empty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


