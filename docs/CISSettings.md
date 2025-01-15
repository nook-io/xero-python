# CISSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cis_settings** | [**List[CISSetting]**](CISSetting.md) |  | [optional] 

## Example

```python
from xero_python.models.cis_settings import CISSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CISSettings from a JSON string
cis_settings_instance = CISSettings.from_json(json)
# print the JSON string representation of the object
print CISSettings.to_json()

# convert the object into a dict
cis_settings_dict = cis_settings_instance.to_dict()
# create an instance of CISSettings from a dict
cis_settings_from_dict = CISSettings.from_dict(cis_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


