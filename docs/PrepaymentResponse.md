# PrepaymentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prepayment_id** | **str** | Xero Identifier of prepayment | [optional] 
**contact** | [**ContactResponse**](ContactResponse.md) |  | [optional] 
**total** | **float** | Total of Invoice tax inclusive (i.e. SubTotal + TotalTax); Not included in summary mode | [optional] 
**line_items** | [**List[LineItemResponse]**](LineItemResponse.md) | Not included in summary mode | [optional] 

## Example

```python
from xero_python.models.prepayment_response import PrepaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrepaymentResponse from a JSON string
prepayment_response_instance = PrepaymentResponse.from_json(json)
# print the JSON string representation of the object
print PrepaymentResponse.to_json()

# convert the object into a dict
prepayment_response_dict = prepayment_response_instance.to_dict()
# create an instance of PrepaymentResponse from a dict
prepayment_response_from_dict = PrepaymentResponse.from_dict(prepayment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


