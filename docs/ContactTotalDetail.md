# ContactTotalDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_paid** | **float** | Total paid invoice and cash value for the contact within the period. | [optional] 
**total_outstanding** | **float** | Total outstanding invoice value for the contact within the period. | [optional] 
**total_credited_un_applied** | **float** | Total unapplied credited value for the contact within the period. | [optional] 

## Example

```python
from xero_python.models.contact_total_detail import ContactTotalDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ContactTotalDetail from a JSON string
contact_total_detail_instance = ContactTotalDetail.from_json(json)
# print the JSON string representation of the object
print ContactTotalDetail.to_json()

# convert the object into a dict
contact_total_detail_dict = contact_total_detail_instance.to_dict()
# create an instance of ContactTotalDetail from a dict
contact_total_detail_from_dict = ContactTotalDetail.from_dict(contact_total_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


