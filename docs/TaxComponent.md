# TaxComponent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Tax Component | [optional] 
**rate** | **float** | Tax Rate (up to 4dp) | [optional] 
**is_compound** | **bool** | Boolean to describe if Tax rate is compounded. | [optional] 
**is_non_recoverable** | **bool** | Boolean to describe if tax rate is non-recoverable. Non-recoverable rates are only applicable to Canadian organisations | [optional] 

## Example

```python
from xero_python.models.tax_component import TaxComponent

# TODO update the JSON string below
json = "{}"
# create an instance of TaxComponent from a JSON string
tax_component_instance = TaxComponent.from_json(json)
# print the JSON string representation of the object
print TaxComponent.to_json()

# convert the object into a dict
tax_component_dict = tax_component_instance.to_dict()
# create an instance of TaxComponent from a dict
tax_component_from_dict = TaxComponent.from_dict(tax_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


