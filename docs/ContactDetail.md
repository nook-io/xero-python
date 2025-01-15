# ContactDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | ID of the contact associated with the transactions.    Transactions with no contact will be grouped under the special ID: 86793108-198C-46D8-90A3-43C1D12686CE.    Transactions that are receive or spend bank transfers will be grouped under the special ID: 207322B3-6A58-4BE7-80F1-430123914AD6 | [optional] 
**name** | **str** | Name of the contact associated with the transactions.    If no contact is associated with the transactions this will appear as “None Provided”,    For receive or spend bank transfer transactions, this will appear as “Bank Transfer”. | [optional] 
**total** | **float** | Total value for the contact | [optional] 
**total_detail** | [**ContactTotalDetail**](ContactTotalDetail.md) |  | [optional] 
**total_other** | [**ContactTotalOther**](ContactTotalOther.md) |  | [optional] 
**account_codes** | **List[str]** | A list of account codes involved in transactions. | [optional] 

## Example

```python
from xero_python.models.contact_detail import ContactDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetail from a JSON string
contact_detail_instance = ContactDetail.from_json(json)
# print the JSON string representation of the object
print ContactDetail.to_json()

# convert the object into a dict
contact_detail_dict = contact_detail_instance.to_dict()
# create an instance of ContactDetail from a dict
contact_detail_from_dict = ContactDetail.from_dict(contact_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


