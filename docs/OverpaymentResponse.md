# OverpaymentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overpayment_id** | **str** | Xero Identifier of overpayment | [optional] 
**contact** | [**ContactResponse**](ContactResponse.md) |  | [optional] 
**total** | **float** | Total of Invoice tax inclusive (i.e. SubTotal + TotalTax); Not included in summary mode | [optional] 
**line_items** | [**List[LineItemResponse]**](LineItemResponse.md) | Not included in summary mode | [optional] 

## Example

```python
from xero_python.models.overpayment_response import OverpaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OverpaymentResponse from a JSON string
overpayment_response_instance = OverpaymentResponse.from_json(json)
# print the JSON string representation of the object
print OverpaymentResponse.to_json()

# convert the object into a dict
overpayment_response_dict = overpayment_response_instance.to_dict()
# create an instance of OverpaymentResponse from a dict
overpayment_response_from_dict = OverpaymentResponse.from_dict(overpayment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


