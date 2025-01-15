# SubscriptionItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** | Date when the subscription to this product will end | [optional] 
**id** | **str** | The unique identifier of the subscription item. | 
**price** | [**Price**](Price.md) |  | 
**product** | [**Product**](Product.md) |  | 
**quantity** | **int** | The quantity of the item. For a fixed product, it is 1. For a per-seat product, it is a positive integer. For metered products, it is always null. | [optional] 
**start_date** | **datetime** | Date the subscription started, or will start. Note: this could be in the future for downgrades or reduced number of seats that haven&#39;t taken effect yet.  | 
**status** | **str** | Status of the subscription item. Available statuses are ACTIVE, CANCELED, and PENDING_ACTIVATION.  | 
**test_mode** | **bool** | If the subscription is a test subscription | [optional] 

## Example

```python
from xero_python.models.subscription_item import SubscriptionItem

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionItem from a JSON string
subscription_item_instance = SubscriptionItem.from_json(json)
# print the JSON string representation of the object
print SubscriptionItem.to_json()

# convert the object into a dict
subscription_item_dict = subscription_item_instance.to_dict()
# create an instance of SubscriptionItem from a dict
subscription_item_from_dict = SubscriptionItem.from_dict(subscription_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


