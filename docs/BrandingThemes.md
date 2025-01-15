# BrandingThemes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branding_themes** | [**List[BrandingTheme]**](BrandingTheme.md) |  | [optional] 

## Example

```python
from xero_python.models.branding_themes import BrandingThemes

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingThemes from a JSON string
branding_themes_instance = BrandingThemes.from_json(json)
# print the JSON string representation of the object
print BrandingThemes.to_json()

# convert the object into a dict
branding_themes_dict = branding_themes_instance.to_dict()
# create an instance of BrandingThemes from a dict
branding_themes_from_dict = BrandingThemes.from_dict(branding_themes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


