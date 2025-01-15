# Bill


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** | Day of Month (0-31) | [optional] 
**type** | [**PaymentTermType**](PaymentTermType.md) |  | [optional] 

## Example

```python
from xero_python.models.bill import Bill

# TODO update the JSON string below
json = "{}"
# create an instance of Bill from a JSON string
bill_instance = Bill.from_json(json)
# print the JSON string representation of the object
print Bill.to_json()

# convert the object into a dict
bill_dict = bill_instance.to_dict()
# create an instance of Bill from a dict
bill_from_dict = Bill.from_dict(bill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


