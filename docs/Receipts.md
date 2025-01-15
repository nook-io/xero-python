# Receipts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receipts** | [**List[Receipt]**](Receipt.md) |  | [optional] 

## Example

```python
from xero_python.models.receipts import Receipts

# TODO update the JSON string below
json = "{}"
# create an instance of Receipts from a JSON string
receipts_instance = Receipts.from_json(json)
# print the JSON string representation of the object
print Receipts.to_json()

# convert the object into a dict
receipts_dict = receipts_instance.to_dict()
# create an instance of Receipts from a dict
receipts_from_dict = Receipts.from_dict(receipts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


