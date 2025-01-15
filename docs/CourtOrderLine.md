# CourtOrderLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court_order_type_id** | **str** | Xero identifier for payroll court order type | [optional] 
**amount** | **float** | Amount | [optional] 

## Example

```python
from xero_python.models.court_order_line import CourtOrderLine

# TODO update the JSON string below
json = "{}"
# create an instance of CourtOrderLine from a JSON string
court_order_line_instance = CourtOrderLine.from_json(json)
# print the JSON string representation of the object
print CourtOrderLine.to_json()

# convert the object into a dict
court_order_line_dict = court_order_line_instance.to_dict()
# create an instance of CourtOrderLine from a dict
court_order_line_from_dict = CourtOrderLine.from_dict(court_order_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


