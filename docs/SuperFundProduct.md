# SuperFundProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abn** | **str** | The ABN of the Regulated SuperFund | [optional] 
**usi** | **str** | The USI of the Regulated SuperFund | [optional] 
**spin** | **str** | The SPIN of the Regulated SuperFund. This field has been deprecated. New superfunds will not have a SPIN value. The USI field should be used instead of SPIN | [optional] 
**product_name** | **str** | The name of the Regulated SuperFund | [optional] 

## Example

```python
from xero_python.models.super_fund_product import SuperFundProduct

# TODO update the JSON string below
json = "{}"
# create an instance of SuperFundProduct from a JSON string
super_fund_product_instance = SuperFundProduct.from_json(json)
# print the JSON string representation of the object
print SuperFundProduct.to_json()

# convert the object into a dict
super_fund_product_dict = super_fund_product_instance.to_dict()
# create an instance of SuperFundProduct from a dict
super_fund_product_from_dict = SuperFundProduct.from_dict(super_fund_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


