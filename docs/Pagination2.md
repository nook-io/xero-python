# Pagination2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0. | [optional] 
**page_size** | **int** | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | [optional] 
**page_count** | **int** | Number of pages available | [optional] 
**item_count** | **int** | Number of items returned | [optional] 

## Example

```python
from xero_python.models.pagination2 import Pagination2

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination2 from a JSON string
pagination2_instance = Pagination2.from_json(json)
# print the JSON string representation of the object
print Pagination2.to_json()

# convert the object into a dict
pagination2_dict = pagination2_instance.to_dict()
# create an instance of Pagination2 from a dict
pagination2_from_dict = Pagination2.from_dict(pagination2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


