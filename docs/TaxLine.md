# TaxLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_line_id** | **str** | Xero identifier for payroll tax line | [optional] 
**description** | **str** | Tax line description | [optional] 
**is_employer_tax** | **bool** | Identifies if the amount is paid for by the employee or employer. True if employer pays the tax | [optional] 
**amount** | **float** | The amount of the tax line | [optional] 
**global_tax_type_id** | **str** | Tax type ID | [optional] 
**manual_adjustment** | **bool** | Identifies if the tax line is a manual adjustment | [optional] 

## Example

```python
from xero_python.models.tax_line import TaxLine

# TODO update the JSON string below
json = "{}"
# create an instance of TaxLine from a JSON string
tax_line_instance = TaxLine.from_json(json)
# print the JSON string representation of the object
print TaxLine.to_json()

# convert the object into a dict
tax_line_dict = tax_line_instance.to_dict()
# create an instance of TaxLine from a dict
tax_line_from_dict = TaxLine.from_dict(tax_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


