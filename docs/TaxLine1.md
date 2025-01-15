# TaxLine1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payslip_tax_line_id** | **str** | Xero identifier for payslip tax line ID. | [optional] 
**amount** | **float** | The tax line amount | [optional] 
**tax_type_name** | **str** | Name of the tax type. | [optional] 
**description** | **str** | Description of the tax line. | [optional] 
**manual_tax_type** | [**ManualTaxType**](ManualTaxType.md) |  | [optional] 
**liability_account** | **str** | The tax line liability account code. For posted pay run you should be able to see liability account code | [optional] 

## Example

```python
from xero_python.models.tax_line1 import TaxLine1

# TODO update the JSON string below
json = "{}"
# create an instance of TaxLine1 from a JSON string
tax_line1_instance = TaxLine1.from_json(json)
# print the JSON string representation of the object
print TaxLine1.to_json()

# convert the object into a dict
tax_line1_dict = tax_line1_instance.to_dict()
# create an instance of TaxLine1 from a dict
tax_line1_from_dict = TaxLine1.from_dict(tax_line1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


