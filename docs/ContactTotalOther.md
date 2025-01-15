# ContactTotalOther


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_outstanding_aged** | **float** | Total outstanding invoice value for the contact within the period where the invoices are more than 90 days old | [optional] 
**total_voided** | **float** | Total voided value for the contact. | [optional] 
**total_credited** | **float** | Total credited value for the contact. | [optional] 
**transaction_count** | **int** | Number of transactions for the contact. | [optional] 

## Example

```python
from xero_python.models.contact_total_other import ContactTotalOther

# TODO update the JSON string below
json = "{}"
# create an instance of ContactTotalOther from a JSON string
contact_total_other_instance = ContactTotalOther.from_json(json)
# print the JSON string representation of the object
print ContactTotalOther.to_json()

# convert the object into a dict
contact_total_other_dict = contact_total_other_instance.to_dict()
# create an instance of ContactTotalOther from a dict
contact_total_other_from_dict = ContactTotalOther.from_dict(contact_total_other_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


