# UsageRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The quantity recorded | 
**subscription_id** | **str** | The unique identifier of the Subscription. | 
**subscription_item_id** | **str** | The unique identifier of the SubscriptionItem. | 
**test_mode** | **bool** | If the subscription is a test subscription | 
**recorded_at** | **datetime** | The time when this usage was recorded in UTC | 
**usage_record_id** | **str** | The unique identifier of the usageRecord. | 
**price_per_unit** | **float** | The price per unit | 
**product_id** | **str** | The unique identifier of the linked Product | 

## Example

```python
from xero_python.models.usage_record import UsageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRecord from a JSON string
usage_record_instance = UsageRecord.from_json(json)
# print the JSON string representation of the object
print UsageRecord.to_json()

# convert the object into a dict
usage_record_dict = usage_record_instance.to_dict()
# create an instance of UsageRecord from a dict
usage_record_from_dict = UsageRecord.from_dict(usage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


