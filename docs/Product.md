# Product


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the product | [optional] 
**name** | **str** | The name of the product | [optional] 
**seat_unit** | **str** | The unit of the per seat product. e.g. \&quot;user\&quot;, \&quot;organisation\&quot;, \&quot;SMS\&quot;, etc | [optional] 
**type** | **str** | The pricing model of the product: * FIXED: Customers are charged a fixed amount for each billing period * PER_SEAT: Customers are charged based on the number of units they purchase * METERED: Customers are charged per use of this product  | [optional] 
**usage_unit** | **str** | The unit of the usage product. e.g. \&quot;user\&quot;, \&quot;minutes\&quot;, \&quot;SMS\&quot;, etc | [optional] 

## Example

```python
from xero_python.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print Product.to_json()

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_from_dict = Product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


