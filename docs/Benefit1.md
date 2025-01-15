# Benefit1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Xero identifier for superannuation | [optional] 
**name** | **str** | Name of the superannuations | 
**category** | **str** | Superannuations Category type | 
**liability_account_id** | **str** | Xero identifier for Liability Account | 
**expense_account_id** | **str** | Xero identifier for Expense Account | 
**calculation_type_nz** | **str** | Calculation Type of the superannuation either FixedAmount or PercentageOfTaxableEarnings | [optional] 
**standard_amount** | **float** | Standard amount of the superannuation | [optional] 
**percentage** | **float** | Percentage of Taxable Earnings of the superannuation | [optional] 
**company_max** | **float** | Company Maximum amount of the superannuation | [optional] 
**current_record** | **bool** | Identifier of a record is active or not. | [optional] 

## Example

```python
from xero_python.models.benefit1 import Benefit1

# TODO update the JSON string below
json = "{}"
# create an instance of Benefit1 from a JSON string
benefit1_instance = Benefit1.from_json(json)
# print the JSON string representation of the object
print Benefit1.to_json()

# convert the object into a dict
benefit1_dict = benefit1_instance.to_dict()
# create an instance of Benefit1 from a dict
benefit1_from_dict = Benefit1.from_dict(benefit1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


