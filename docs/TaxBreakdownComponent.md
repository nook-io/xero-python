# TaxBreakdownComponent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_component_id** | **str** | The unique ID number of this component | [optional] 
**type** | **str** | The type of the jurisdiction | [optional] 
**name** | **str** | The name of the jurisdiction | [optional] 
**tax_percentage** | **float** | The percentage of the tax | [optional] 
**tax_amount** | **float** | The amount of the tax | [optional] 
**taxable_amount** | **float** | The amount that is taxable | [optional] 
**non_taxable_amount** | **float** | The amount that is not taxable | [optional] 
**exempt_amount** | **float** | The amount that is exempt | [optional] 
**state_assigned_no** | **str** | The state assigned number of the jurisdiction | [optional] 
**jurisdiction_region** | **str** | Name identifying the region within the country | [optional] 

## Example

```python
from xero_python.models.tax_breakdown_component import TaxBreakdownComponent

# TODO update the JSON string below
json = "{}"
# create an instance of TaxBreakdownComponent from a JSON string
tax_breakdown_component_instance = TaxBreakdownComponent.from_json(json)
# print the JSON string representation of the object
print TaxBreakdownComponent.to_json()

# convert the object into a dict
tax_breakdown_component_dict = tax_breakdown_component_instance.to_dict()
# create an instance of TaxBreakdownComponent from a dict
tax_breakdown_component_from_dict = TaxBreakdownComponent.from_dict(tax_breakdown_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


