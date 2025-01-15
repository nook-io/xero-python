# IncomeByContactResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date of the report | [optional] 
**end_date** | **date** | End date of the report | [optional] 
**total** | **float** | Total value | [optional] 
**total_detail** | [**TotalDetail**](TotalDetail.md) |  | [optional] 
**total_other** | [**TotalOther**](TotalOther.md) |  | [optional] 
**contacts** | [**List[ContactDetail]**](ContactDetail.md) |  | [optional] 
**manual_journals** | [**ManualJournalTotal**](ManualJournalTotal.md) |  | [optional] 

## Example

```python
from xero_python.models.income_by_contact_response import IncomeByContactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IncomeByContactResponse from a JSON string
income_by_contact_response_instance = IncomeByContactResponse.from_json(json)
# print the JSON string representation of the object
print IncomeByContactResponse.to_json()

# convert the object into a dict
income_by_contact_response_dict = income_by_contact_response_instance.to_dict()
# create an instance of IncomeByContactResponse from a dict
income_by_contact_response_from_dict = IncomeByContactResponse.from_dict(income_by_contact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


