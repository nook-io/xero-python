# Purchase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_price** | **float** | Unit Price of the item. By default UnitPrice is rounded to two decimal places. You can use 4 decimal places by adding the unitdp&#x3D;4 querystring parameter to your request. | [optional] 
**account_code** | **str** | Default account code to be used for purchased/sale. Not applicable to the purchase details of tracked items | [optional] 
**cogs_account_code** | **str** | Cost of goods sold account. Only applicable to the purchase details of tracked items. | [optional] 
**tax_type** | **str** | The tax type from TaxRates | [optional] 

## Example

```python
from xero_python.models.purchase import Purchase

# TODO update the JSON string below
json = "{}"
# create an instance of Purchase from a JSON string
purchase_instance = Purchase.from_json(json)
# print the JSON string representation of the object
print Purchase.to_json()

# convert the object into a dict
purchase_dict = purchase_instance.to_dict()
# create an instance of Purchase from a dict
purchase_from_dict = Purchase.from_dict(purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


