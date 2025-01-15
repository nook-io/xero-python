# CISOrgSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cis_settings** | [**List[CISOrgSetting]**](CISOrgSetting.md) |  | [optional] 

## Example

```python
from xero_python.models.cis_org_settings import CISOrgSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CISOrgSettings from a JSON string
cis_org_settings_instance = CISOrgSettings.from_json(json)
# print the JSON string representation of the object
print CISOrgSettings.to_json()

# convert the object into a dict
cis_org_settings_dict = cis_org_settings_instance.to_dict()
# create an instance of CISOrgSettings from a dict
cis_org_settings_from_dict = CISOrgSettings.from_dict(cis_org_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


