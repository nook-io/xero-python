# Pagination3


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Page number which specifies the set of records to retrieve. Example - https://api.xero.com/bankfeeds.xro/1.0/Statements?page&#x3D;2 to get the second set of the records. When page value is not a number or a negative number, by default, the first set of records is returned. | [optional] 
**page_size** | **int** | Page size which specifies how many records per page will be returned (default 50). Example - https://api.xero.com/bankfeeds.xro/1.0/Statements?pageSize&#x3D;100 to specify page size of 100. | [optional] 
**page_count** | **int** | Number of pages available | [optional] 
**item_count** | **int** | Number of items returned | [optional] 

## Example

```python
from xero_python.models.pagination3 import Pagination3

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination3 from a JSON string
pagination3_instance = Pagination3.from_json(json)
# print the JSON string representation of the object
print Pagination3.to_json()

# convert the object into a dict
pagination3_dict = pagination3_instance.to_dict()
# create an instance of Pagination3 from a dict
pagination3_from_dict = Pagination3.from_dict(pagination3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


