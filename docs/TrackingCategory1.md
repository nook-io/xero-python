# TrackingCategory1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_groups_tracking_category_id** | **str** | The Xero identifier for Employee groups tracking category. | [optional] 
**timesheet_tracking_category_id** | **str** | The Xero identifier for Timesheet tracking category. | [optional] 

## Example

```python
from xero_python.models.tracking_category1 import TrackingCategory1

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingCategory1 from a JSON string
tracking_category1_instance = TrackingCategory1.from_json(json)
# print the JSON string representation of the object
print TrackingCategory1.to_json()

# convert the object into a dict
tracking_category1_dict = tracking_category1_instance.to_dict()
# create an instance of TrackingCategory1 from a dict
tracking_category1_from_dict = TrackingCategory1.from_dict(tracking_category1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


