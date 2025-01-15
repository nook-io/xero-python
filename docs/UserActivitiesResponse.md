# UserActivitiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organisation_id** | **str** | The requested Organisation to which the data pertains | [optional] 
**data_month** | **str** | The month of the report | [optional] 
**users** | [**List[UserResponse]**](UserResponse.md) |  | [optional] 

## Example

```python
from xero_python.models.user_activities_response import UserActivitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivitiesResponse from a JSON string
user_activities_response_instance = UserActivitiesResponse.from_json(json)
# print the JSON string representation of the object
print UserActivitiesResponse.to_json()

# convert the object into a dict
user_activities_response_dict = user_activities_response_instance.to_dict()
# create an instance of UserActivitiesResponse from a dict
user_activities_response_from_dict = UserActivitiesResponse.from_dict(user_activities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


