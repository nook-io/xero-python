# TaxRate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of tax rate | [optional] 
**tax_type** | **str** | The tax type | [optional] 
**tax_components** | [**List[TaxComponent]**](TaxComponent.md) | See TaxComponents | [optional] 
**status** | **str** | See Status Codes | [optional] 
**report_tax_type** | **str** | See ReportTaxTypes | [optional] 
**can_apply_to_assets** | **bool** | Boolean to describe if tax rate can be used for asset accounts i.e.  true,false | [optional] [readonly] 
**can_apply_to_equity** | **bool** | Boolean to describe if tax rate can be used for equity accounts i.e true,false | [optional] [readonly] 
**can_apply_to_expenses** | **bool** | Boolean to describe if tax rate can be used for expense accounts  i.e. true,false | [optional] [readonly] 
**can_apply_to_liabilities** | **bool** | Boolean to describe if tax rate can be used for liability accounts  i.e. true,false | [optional] [readonly] 
**can_apply_to_revenue** | **bool** | Boolean to describe if tax rate can be used for revenue accounts i.e. true,false | [optional] [readonly] 
**display_tax_rate** | **float** | Tax Rate (decimal to 4dp) e.g 12.5000 | [optional] [readonly] 
**effective_rate** | **float** | Effective Tax Rate (decimal to 4dp) e.g 12.5000 | [optional] [readonly] 

## Example

```python
from xero_python.models.tax_rate import TaxRate

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRate from a JSON string
tax_rate_instance = TaxRate.from_json(json)
# print the JSON string representation of the object
print TaxRate.to_json()

# convert the object into a dict
tax_rate_dict = tax_rate_instance.to_dict()
# create an instance of TaxRate from a dict
tax_rate_from_dict = TaxRate.from_dict(tax_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


