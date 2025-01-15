# PurchaseOrders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination1**](Pagination1.md) |  | [optional] 
**warnings** | [**List[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 
**purchase_orders** | [**List[PurchaseOrder]**](PurchaseOrder.md) |  | [optional] 

## Example

```python
from xero_python.models.purchase_orders import PurchaseOrders

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrders from a JSON string
purchase_orders_instance = PurchaseOrders.from_json(json)
# print the JSON string representation of the object
print PurchaseOrders.to_json()

# convert the object into a dict
purchase_orders_dict = purchase_orders_instance.to_dict()
# create an instance of PurchaseOrders from a dict
purchase_orders_from_dict = PurchaseOrders.from_dict(purchase_orders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


