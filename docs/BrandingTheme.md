# BrandingTheme


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branding_theme_id** | **str** | Xero identifier | [optional] 
**name** | **str** | Name of branding theme | [optional] 
**logo_url** | **str** | The location of the image file used as the logo on this branding theme | [optional] 
**type** | **str** | Always INVOICE | [optional] 
**sort_order** | **int** | Integer – ranked order of branding theme. The default branding theme has a value of 0 | [optional] 
**created_date_utc** | **str** | UTC timestamp of creation date of branding theme | [optional] [readonly] 

## Example

```python
from xero_python.models.branding_theme import BrandingTheme

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingTheme from a JSON string
branding_theme_instance = BrandingTheme.from_json(json)
# print the JSON string representation of the object
print BrandingTheme.to_json()

# convert the object into a dict
branding_theme_dict = branding_theme_instance.to_dict()
# create an instance of BrandingTheme from a dict
branding_theme_from_dict = BrandingTheme.from_dict(branding_theme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


