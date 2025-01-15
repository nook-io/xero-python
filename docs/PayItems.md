# PayItems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_items** | [**PayItem**](PayItem.md) |  | [optional] 

## Example

```python
from xero_python.models.pay_items import PayItems

# TODO update the JSON string below
json = "{}"
# create an instance of PayItems from a JSON string
pay_items_instance = PayItems.from_json(json)
# print the JSON string representation of the object
print PayItems.to_json()

# convert the object into a dict
pay_items_dict = pay_items_instance.to_dict()
# create an instance of PayItems from a dict
pay_items_from_dict = PayItems.from_dict(pay_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


