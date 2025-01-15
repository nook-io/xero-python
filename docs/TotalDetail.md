# TotalDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_paid** | **float** | Total paid invoice and cash value within the period. | [optional] 
**total_outstanding** | **float** | Total outstanding invoice value within the period. | [optional] 
**total_credited_un_applied** | **float** | Total unapplied credited value within the period. | [optional] 

## Example

```python
from xero_python.models.total_detail import TotalDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TotalDetail from a JSON string
total_detail_instance = TotalDetail.from_json(json)
# print the JSON string representation of the object
print TotalDetail.to_json()

# convert the object into a dict
total_detail_dict = total_detail_instance.to_dict()
# create an instance of TotalDetail from a dict
total_detail_from_dict = TotalDetail.from_dict(total_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


