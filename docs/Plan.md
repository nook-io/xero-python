# Plan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the plan | 
**name** | **str** | The name of the plan. It is used in the invoice line item description.  | 
**status** | **str** | Status of the plan. Available statuses are ACTIVE, CANCELED, and PENDING_ACTIVATION.  | 
**subscription_items** | [**List[SubscriptionItem]**](SubscriptionItem.md) | List of the subscription items belonging to the plan. It does not include cancelled subscription items.  | 

## Example

```python
from xero_python.models.plan import Plan

# TODO update the JSON string below
json = "{}"
# create an instance of Plan from a JSON string
plan_instance = Plan.from_json(json)
# print the JSON string representation of the object
print Plan.to_json()

# convert the object into a dict
plan_dict = plan_instance.to_dict()
# create an instance of Plan from a dict
plan_from_dict = Plan.from_dict(plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


