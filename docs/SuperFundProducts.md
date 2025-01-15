# SuperFundProducts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**super_fund_products** | [**List[SuperFundProduct]**](SuperFundProduct.md) |  | [optional] 

## Example

```python
from xero_python.models.super_fund_products import SuperFundProducts

# TODO update the JSON string below
json = "{}"
# create an instance of SuperFundProducts from a JSON string
super_fund_products_instance = SuperFundProducts.from_json(json)
# print the JSON string representation of the object
print SuperFundProducts.to_json()

# convert the object into a dict
super_fund_products_dict = super_fund_products_instance.to_dict()
# create an instance of SuperFundProducts from a dict
super_fund_products_from_dict = SuperFundProducts.from_dict(super_fund_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


