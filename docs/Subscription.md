# Subscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_period_end** | **datetime** | End of the current period that the subscription has been invoiced for.  | 
**end_date** | **datetime** | If the subscription has been canceled, this is the date when the subscription ends. If null, the subscription is active and has not been cancelled | [optional] 
**id** | **str** | The unique identifier of the subscription | 
**organisation_id** | **str** | The Xero generated unique identifier for the organisation | 
**plans** | [**List[Plan]**](Plan.md) | List of plans for the subscription. | 
**start_date** | **datetime** | Date when the subscription was first created. | 
**status** | **str** | Status of the subscription. Available statuses are ACTIVE, CANCELED, and PAST_DUE. | 
**test_mode** | **bool** | Boolean used to indicate if the subscription is in test mode | [optional] 

## Example

```python
from xero_python.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print Subscription.to_json()

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


