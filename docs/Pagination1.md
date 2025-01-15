# Pagination1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_count** | **int** |  | [optional] 
**item_count** | **int** |  | [optional] 

## Example

```python
from xero_python.models.pagination1 import Pagination1

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination1 from a JSON string
pagination1_instance = Pagination1.from_json(json)
# print the JSON string representation of the object
print Pagination1.to_json()

# convert the object into a dict
pagination1_dict = pagination1_instance.to_dict()
# create an instance of Pagination1 from a dict
pagination1_from_dict = Pagination1.from_dict(pagination1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


