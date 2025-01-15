# Connection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Xero identifier | [optional] 
**tenant_id** | **str** | Xero identifier of organisation | [optional] 
**auth_event_id** | **str** | Identifier shared across connections authorised at the same time | [optional] 
**tenant_type** | **str** | Xero tenant type (i.e. ORGANISATION, PRACTICE) | [optional] 
**tenant_name** | **str** | Xero tenant name | [optional] 
**created_date_utc** | **datetime** | The date when the user connected this tenant to your app | [optional] 
**updated_date_utc** | **datetime** | The date when the user most recently connected this tenant to your app. May differ to the created date if the user has disconnected and subsequently reconnected this tenant to your app. | [optional] 

## Example

```python
from xero_python.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print Connection.to_json()

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_from_dict = Connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


