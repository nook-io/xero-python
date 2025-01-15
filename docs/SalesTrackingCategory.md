# SalesTrackingCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_category_name** | **str** | The default sales tracking category name for contacts | [optional] 
**tracking_option_name** | **str** | The default purchase tracking category name for contacts | [optional] 

## Example

```python
from xero_python.models.sales_tracking_category import SalesTrackingCategory

# TODO update the JSON string below
json = "{}"
# create an instance of SalesTrackingCategory from a JSON string
sales_tracking_category_instance = SalesTrackingCategory.from_json(json)
# print the JSON string representation of the object
print SalesTrackingCategory.to_json()

# convert the object into a dict
sales_tracking_category_dict = sales_tracking_category_instance.to_dict()
# create an instance of SalesTrackingCategory from a dict
sales_tracking_category_from_dict = SalesTrackingCategory.from_dict(sales_tracking_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


