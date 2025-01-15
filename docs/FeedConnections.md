# FeedConnections


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination3**](Pagination3.md) |  | [optional] 
**items** | [**List[FeedConnection]**](FeedConnection.md) |  | [optional] 

## Example

```python
from xero_python.models.feed_connections import FeedConnections

# TODO update the JSON string below
json = "{}"
# create an instance of FeedConnections from a JSON string
feed_connections_instance = FeedConnections.from_json(json)
# print the JSON string representation of the object
print FeedConnections.to_json()

# convert the object into a dict
feed_connections_dict = feed_connections_instance.to_dict()
# create an instance of FeedConnections from a dict
feed_connections_from_dict = FeedConnections.from_dict(feed_connections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


