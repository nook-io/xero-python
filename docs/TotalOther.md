# TotalOther


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_outstanding_aged** | **float** | Total outstanding invoice value within the period where the invoices are more than 90 days old | [optional] 
**total_voided** | **float** | Total voided value. | [optional] 
**total_credited** | **float** | Total credited value. | [optional] 

## Example

```python
from xero_python.models.total_other import TotalOther

# TODO update the JSON string below
json = "{}"
# create an instance of TotalOther from a JSON string
total_other_instance = TotalOther.from_json(json)
# print the JSON string representation of the object
print TotalOther.to_json()

# convert the object into a dict
total_other_dict = total_other_instance.to_dict()
# create an instance of TotalOther from a dict
total_other_from_dict = TotalOther.from_dict(total_other_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


