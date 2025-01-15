# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Xero identifier | [optional] 
**email_address** | **str** | Email address of user | [optional] 
**first_name** | **str** | First name of user | [optional] 
**last_name** | **str** | Last name of user | [optional] 
**updated_date_utc** | **str** | Timestamp of last change to user | [optional] [readonly] 
**is_subscriber** | **bool** | Boolean to indicate if user is the subscriber | [optional] 
**organisation_role** | **str** | User role that defines permissions in Xero and via API (READONLY, INVOICEONLY, STANDARD, FINANCIALADVISER, etc) | [optional] 

## Example

```python
from xero_python.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


