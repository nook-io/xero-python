# UserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The Xero identifier for the user | [optional] 
**user_created_date_utc** | **datetime** | Timestamp of user creation. | [optional] 
**last_login_date_utc** | **datetime** | Timestamp of user last login | [optional] 
**is_external_partner** | **bool** | User is external partner. | [optional] 
**has_accountant_role** | **bool** | User has Accountant role. | [optional] 
**month_period** | **str** | Month period in format  yyyy-MM. | [optional] 
**number_of_logins** | **int** | Number of times the user has logged in. | [optional] 
**number_of_documents_created** | **int** | Number of documents created. | [optional] 
**net_value_documents_created** | **float** | Net value of documents created. | [optional] 
**absolute_value_documents_created** | **float** | Absolute value of documents created. | [optional] 
**attached_practices** | [**List[PracticeResponse]**](PracticeResponse.md) |  | [optional] 
**history_records** | [**List[HistoryRecordResponse]**](HistoryRecordResponse.md) |  | [optional] 

## Example

```python
from xero_python.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print UserResponse.to_json()

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_from_dict = UserResponse.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


